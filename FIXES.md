# Dataset Info YAML Fixes

This document describes the fixes applied to the `dataset_info.yaml` generation in the dataloader.

## Issues Fixed

### 1. Tuple to List Conversion

**Problem:** The YAML file was producing entries like:
```yaml
file_shapes:
- !!python/tuple
  - 124
  - 500
  - 686
```

**Solution:** Added `convert_tuples_to_lists()` function that recursively converts all tuples to lists before dumping to YAML. Now produces:
```yaml
file_shapes:
  image:
    - [124, 500, 686]
    - [124, 500, 686]
```

**Location:** `zea/zea/data/datasets.py:16-28` and used in `search_file_tree` at line 101

---

### 2. Multiple Keys with Different Shapes

**Problem:** The `hdf5_key_for_length` argument determined which key was used for file shapes, but not all keys have the same shape (e.g., `image_sc.shape != image.shape`). This meant only one key's shape was recorded.

**Solution:** Changed `file_shapes` from a list to a dictionary that maps key names to their shape lists:
- When `hdf5_key_for_length=None`: Collects shapes for **all** keys in the HDF5 files
- When `hdf5_key_for_length="specific_key"`: Collects shapes only for that specific key

Result:
```yaml
file_shapes:
  image: [[124, 500, 686], [124, 500, 686]]
  image_sc: [[64, 250, 343], [64, 250, 343]]
  label: [[124], [124]]
```

**Location:** `zea/zea/data/datasets.py:74-102`

---

### 3. Folder's Key Argument Now Required

**Problem:** The `Folder` class had an optional `key` argument, but the code actually needed it to run properly.

**Solution:** Made `key` a required argument (removed default `None`) and added proper error handling:
- Constructor now requires `key` parameter
- Raises `ValueError` with helpful message if `key=None` is passed
- Exception: Can skip key requirement by using `search_file_tree` with `redo=True` and `write=False`

**Location:** `zea/zea/data/datasets.py:147-160`

---

### 4. Read-Only Folder Support

**Problem:** No support for read-only folders where writing `dataset_info.yaml` should be skipped.

**Solution:** Added `read_only` parameter to:
- `search_file_tree()` function
- `Folder` class
- `Dataset` class

When `read_only=True`, the `dataset_info.yaml` file will not be written, even if `write=True`.

**Location:**
- `search_file_tree`: line 31, 40, 104
- `Folder`: line 150, 163, 174
- `Dataset`: line 225, 241, 246

---

## Usage Examples

### Basic Usage with All Fixes
```python
from zea.zea.data.datasets import Dataset

# Create dataset with all fixes applied
dataset = Dataset(
    folder_path="path/to/data",
    key="image",  # Now required!
    hdf5_key_for_length=None,  # Collect shapes for all keys
    read_only=False,  # Allow writing dataset_info.yaml
)

# Validate and get shapes
if dataset.validate():
    shapes = dataset.get_shapes()
    # Returns: {'image': (124, 500, 686), 'image_sc': (64, 250, 343)}
```

### Avoiding Bugs (as mentioned in docs)
```python
from zea.zea.data.datasets import Folder

folder = Folder(
    folder_path="path/to/data",
    key="image",
    search_file_tree_kwargs={
        'redo': True,   # Regenerate metadata
        'write': False  # Don't write to disk
    }
)
```

### Read-Only Mode
```python
from zea.zea.data.datasets import Dataset

dataset = Dataset(
    folder_path="path/to/readonly/data",
    key="image",
    read_only=True  # Skip writing dataset_info.yaml
)
```

## Files Modified

- `zea/zea/data/datasets.py` - Main implementation with all fixes
- `zea/zea/data/example_usage.py` - Comprehensive usage examples
- `FIXES.md` - This documentation

## Testing

See `zea/zea/data/example_usage.py` for detailed examples of each fix.
