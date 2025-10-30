"""Example usage of the dataset module with all the fixes applied."""

from zea.zea.data.datasets import Folder, Dataset, search_file_tree

# Example 1: Using search_file_tree with tuple-to-list conversion
# This will automatically convert tuples to lists in the YAML output
def example_search_file_tree():
    """Demonstrates the fixed tuple-to-list conversion."""
    metadata = search_file_tree(
        folder_path="path/to/data",
        key="image",
        hdf5_key_for_length="image",  # Specify which key to use for shapes
        redo=False,
        write=True,  # Will write dataset_info.yaml with lists instead of tuples
    )
    # The resulting YAML will have:
    # file_shapes:
    #   image:
    #     - [124, 500, 686]
    # instead of:
    # file_shapes:
    #   - !!python/tuple
    #     - 124
    #     - 500
    #     - 686


# Example 2: Handling multiple keys with different shapes
def example_multiple_keys():
    """Demonstrates handling of multiple keys with different shapes."""
    # When hdf5_key_for_length is None, all keys are collected
    # The resulting YAML will have:
    # file_shapes:
    #   image: [[124, 500, 686], [124, 500, 686], ...]
    #   image_sc: [[64, 250, 343], [64, 250, 343], ...]
    #   label: [[124], [124], ...]

    # Or specify a particular key:
    metadata = search_file_tree(
        folder_path="path/to/data",
        key="image",
        hdf5_key_for_length="image_sc",  # Only collect shapes for image_sc
        write=True,
    )


# Example 3: Folder with required key argument
def example_folder_with_key():
    """Demonstrates that key is now required for Folder."""
    # This will work - key is provided
    folder = Folder(
        folder_path="path/to/data",
        key="image",  # Now required!
        hdf5_key_for_length="image",
    )

    # This will raise ValueError - key is missing


# Example 4: Avoiding bugs with redo=True and write=False
def example_avoid_bugs():
    """Demonstrates how to avoid bugs as mentioned in docs."""
    # Use search_file_tree_kwargs to pass redo and write
    folder = Folder(
        folder_path="path/to/data",
        key="image",
        search_file_tree_kwargs={
            'redo': True,
            'write': False,
        }
    )
    # This will regenerate metadata but not write to disk


# Example 5: Read-only folders
def example_read_only():
    """Demonstrates read-only folder support."""
    # Create a read-only folder that won't write dataset_info.yaml
    folder = Folder(
        folder_path="path/to/read_only_data",
        key="image",
        read_only=True,  # Skip writing dataset_info.yaml
    )

    # Also works with Dataset class
    dataset = Dataset(
        folder_path="path/to/read_only_data",
        key="image",
        read_only=True,
    )

    # Or use search_file_tree directly
    metadata = search_file_tree(
        folder_path="path/to/read_only_data",
        key="image",
        read_only=True,  # Overrides write=True
    )


# Example 6: Complete workflow
def example_complete_workflow():
    """Demonstrates a complete workflow with all fixes."""
    # Create a dataset with proper configuration
    dataset = Dataset(
        folder_path=["path/to/train", "path/to/val"],
        key="image",  # Required!
        hdf5_key_for_length=None,  # Collect shapes for all keys
        search_file_tree_kwargs={
            'redo': False,  # Use existing metadata if available
            'write': True,  # Write to dataset_info.yaml
        },
        read_only=False,  # Allow writing
    )

    # Validate the dataset
    if dataset.validate():
        print("Dataset is valid!")
        shapes = dataset.get_shapes()
        print(f"Available shapes: {shapes}")
        # Example output:
        # Available shapes: {
        #     'image': (124, 500, 686),
        #     'image_sc': (64, 250, 343),
        #     'label': (124,)
        # }
    else:
        print("Dataset validation failed!")


if __name__ == "__main__":
    print("See function docstrings for usage examples")
