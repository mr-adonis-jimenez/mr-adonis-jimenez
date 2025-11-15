"""Dataset and data loading utilities for HDF5 files."""

from pathlib import Path
from typing import Optional, Union
import h5py
import yaml


def convert_tuples_to_lists(obj):
    """Recursively convert tuples to lists in nested data structures.

    This is necessary because YAML dumps tuples as !!python/tuple which
    is not ideal for portability and readability.

    Args:
        obj: Any object (dict, list, tuple, or primitive)

    Returns:
        Object with all tuples converted to lists
    """
    if isinstance(obj, dict):
        return {k: convert_tuples_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert_tuples_to_lists(item) for item in obj]
    else:
        return obj


def search_file_tree(
    folder_path: Union[str, Path],
    key: Optional[str] = None,
    hdf5_key_for_length: Optional[str] = None,
    redo: bool = False,
    write: bool = True,
    read_only: bool = False,
) -> dict:
    """Search HDF5 files in a folder and collect metadata.

    Args:
        folder_path: Path to folder containing HDF5 files
        key: Primary key to use for validation (required unless redo=True and write=False)
        hdf5_key_for_length: Specific key to use for determining file shapes.
            If None, will collect shapes for all available keys.
        redo: If True, regenerate metadata even if dataset_info.yaml exists
        write: If True, write the metadata to dataset_info.yaml
        read_only: If True, skip writing dataset_info.yaml (overrides write=True)

    Returns:
        Dictionary containing metadata about the HDF5 files

    Raises:
        ValueError: If key is None and not in redo+no-write mode
    """
    folder_path = Path(folder_path)
    dataset_info_path = folder_path / "dataset_info.yaml"

    # Validate key requirement
    if key is None and ((not redo) or write):
        raise ValueError(
            "The 'key' argument is required unless you pass redo=True and write=False. "
            "This key is needed for validation and determining file structure."
        )

    # Check if we should use existing metadata
    if not redo and dataset_info_path.exists():
        with open(dataset_info_path, 'r') as f:
            return yaml.safe_load(f)

    # Collect metadata from HDF5 files
    metadata = {
        'folder_path': str(folder_path),
        'primary_key': key,
        'files': [],
        'file_shapes': {},  # Changed to dict to support multiple keys
    }

    hdf5_files = sorted(folder_path.glob("*.h5")) + sorted(folder_path.glob("*.hdf5"))

    for file_path in hdf5_files:
        try:
            with h5py.File(file_path, 'r') as f:
                file_info = {
                    'path': str(file_path),
                    'name': file_path.name,
                }

                # Collect shapes for specified key or all keys
                if hdf5_key_for_length:
                    # Use specific key for length
                    if hdf5_key_for_length in f:
                        shape = f[hdf5_key_for_length].shape
                        if hdf5_key_for_length not in metadata['file_shapes']:
                            metadata['file_shapes'][hdf5_key_for_length] = []
                        metadata['file_shapes'][hdf5_key_for_length].append(shape)
                else:
                    # Collect shapes for all keys
                    for key_name in f.keys():
                        if hasattr(f[key_name], 'shape'):
                            shape = f[key_name].shape
                            if key_name not in metadata['file_shapes']:
                                metadata['file_shapes'][key_name] = []
                            metadata['file_shapes'][key_name].append(shape)

                # Validate primary key exists if specified
                if key and key not in f:
                    file_info['warning'] = f"Primary key '{key}' not found in file"

                metadata['files'].append(file_info)

        except Exception as e:
            metadata['files'].append({
                'path': str(file_path),
                'name': file_path.name,
                'error': str(e),
            })

    # Convert tuples to lists before writing to YAML
    metadata = convert_tuples_to_lists(metadata)

    # Write metadata to file if requested and not read-only
    if write and not read_only:
        with open(dataset_info_path, 'w') as f:
            yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)

    return metadata


class Folder:
    """Group of HDF5 files in a folder that can be validated.

    Mostly used internally, you might want to use the Dataset class instead.
    """

    def __init__(
        self,
        folder_path: Union[list[str], list[Path], str, Path],
        key: str,  # Now required - removed default None
        hdf5_key_for_length: Optional[str] = None,
        search_file_tree_kwargs: Optional[dict] = None,
        read_only: bool = False,
    ):
        """Initialize a Folder.

        Args:
            folder_path: Path(s) to folder(s) containing HDF5 files
            key: Primary key for validation (REQUIRED)
            hdf5_key_for_length: Specific key to use for file shapes.
                If None, shapes will be collected for all keys.
            search_file_tree_kwargs: Additional kwargs to pass to search_file_tree.
                Can include 'redo' and 'write' to avoid bugs mentioned in docs.
            read_only: If True, skip writing dataset_info.yaml files

        Raises:
            ValueError: If key is not provided
        """
        if key is None:
            raise ValueError(
                "The 'key' argument is required for Folder initialization. "
                "This is needed for proper validation and file structure determination."
            )

        # Handle single path or list of paths
        if isinstance(folder_path, (str, Path)):
            folder_path = [folder_path]

        self.folder_paths = [Path(p) for p in folder_path]
        self.key = key
        self.hdf5_key_for_length = hdf5_key_for_length
        self.read_only = read_only

        # Prepare search_file_tree kwargs
        search_kwargs = {
            'key': key,
            'hdf5_key_for_length': hdf5_key_for_length,
            'read_only': read_only,
        }
        if search_file_tree_kwargs:
            search_kwargs.update(search_file_tree_kwargs)

        # Search all folders
        self.metadata = []
        for folder in self.folder_paths:
            metadata = search_file_tree(folder, **search_kwargs)
            self.metadata.append(metadata)

    def validate(self) -> bool:
        """Validate that all files in the folder have consistent structure.

        Returns:
            True if validation passes, False otherwise
        """
        for metadata in self.metadata:
            # Check for errors in files
            for file_info in metadata.get('files', []):
                if 'error' in file_info or 'warning' in file_info:
                    return False

            # Check that shapes are consistent per key
            for key_name, shapes in metadata.get('file_shapes', {}).items():
                if shapes and len(set(tuple(s) for s in shapes)) > 1:
                    print(f"Warning: Inconsistent shapes for key '{key_name}': {set(tuple(s) for s in shapes)}")
                    return False

        return True

    def get_shapes(self) -> dict[str, tuple]:
        """Get the shapes for each key across all folders.

        Returns:
            Dictionary mapping key names to their shapes
        """
        all_shapes = {}
        for metadata in self.metadata:
            for key_name, shapes in metadata.get('file_shapes', {}).items():
                if shapes:
                    # Take the first shape (they should all be consistent if validated)
                    all_shapes[key_name] = tuple(shapes[0])
        return all_shapes


class Dataset:
    """Dataset class for working with HDF5 files.

    This class provides a high-level interface for working with collections
    of HDF5 files organized in folders.
    """

    def __init__(
        self,
        folder_path: Union[list[str], list[Path], str, Path],
        key: str,
        hdf5_key_for_length: Optional[str] = None,
        search_file_tree_kwargs: Optional[dict] = None,
        read_only: bool = False,
    ):
        """Initialize a Dataset.

        Args:
            folder_path: Path(s) to folder(s) containing HDF5 files
            key: Primary key for validation (REQUIRED)
            hdf5_key_for_length: Specific key to use for file shapes
            search_file_tree_kwargs: Additional kwargs to pass to search_file_tree
            read_only: If True, skip writing dataset_info.yaml files
        """
        self.folder = Folder(
            folder_path=folder_path,
            key=key,
            hdf5_key_for_length=hdf5_key_for_length,
            search_file_tree_kwargs=search_file_tree_kwargs,
            read_only=read_only,
        )
        self.key = key

    def validate(self) -> bool:
        """Validate the dataset.

        Returns:
            True if validation passes, False otherwise
        """
        return self.folder.validate()

    def get_shapes(self) -> dict[str, tuple]:
        """Get the shapes for each key in the dataset.

        Returns:
            Dictionary mapping key names to their shapes
        """
        return self.folder.get_shapes()
