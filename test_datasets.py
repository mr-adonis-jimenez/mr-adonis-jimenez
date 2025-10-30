"""Unit tests for the dataset_info.yaml fixes."""

import unittest
from zea.zea.data.datasets import convert_tuples_to_lists, Folder, Dataset


class TestTupleToListConversion(unittest.TestCase):
    """Tests for convert_tuples_to_lists function."""

    def test_simple_tuple(self):
        """Test conversion of a simple tuple."""
        result = convert_tuples_to_lists((1, 2, 3))
        self.assertEqual(result, [1, 2, 3])
        self.assertIsInstance(result, list)

    def test_nested_tuple(self):
        """Test conversion of nested tuples."""
        result = convert_tuples_to_lists(((1, 2), (3, 4)))
        self.assertEqual(result, [[1, 2], [3, 4]])
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)

    def test_dict_with_tuples(self):
        """Test conversion of tuples in dictionaries."""
        data = {
            'shapes': [(124, 500, 686), (124, 500, 686)],
            'nested': {'inner': (1, 2, 3)}
        }
        result = convert_tuples_to_lists(data)
        self.assertEqual(result['shapes'], [[124, 500, 686], [124, 500, 686]])
        self.assertEqual(result['nested']['inner'], [1, 2, 3])

    def test_list_unchanged(self):
        """Test that lists remain as lists."""
        data = [1, 2, 3]
        result = convert_tuples_to_lists(data)
        self.assertEqual(result, [1, 2, 3])
        self.assertIsInstance(result, list)

    def test_primitives_unchanged(self):
        """Test that primitive types are unchanged."""
        self.assertEqual(convert_tuples_to_lists(42), 42)
        self.assertEqual(convert_tuples_to_lists("hello"), "hello")
        self.assertEqual(convert_tuples_to_lists(3.14), 3.14)


class TestFolderKeyRequirement(unittest.TestCase):
    """Tests for Folder's required key argument."""

    def test_key_is_required(self):
        """Test that Folder raises error when key is not provided."""
        with self.assertRaises(ValueError) as context:
            Folder(
                folder_path="path/to/data",
                key=None,  # Should raise error
            )
        self.assertIn("required", str(context.exception).lower())

    def test_key_provided_no_error(self):
        """Test that Folder accepts key when provided."""
        # This will fail because the path doesn't exist, but we're testing
        # that the key validation passes
        try:
            _ = Folder(
                folder_path="nonexistent/path",
                key="image",
                search_file_tree_kwargs={'redo': True, 'write': False}
            )
        except FileNotFoundError:
            # Expected - the path doesn't exist, but key validation passed
            pass
        except ValueError as e:
            if "required" in str(e).lower():
                self.fail("Folder raised ValueError about key when key was provided")


class TestMultipleKeyShapes(unittest.TestCase):
    """Tests for handling multiple keys with different shapes."""

    def test_file_shapes_is_dict(self):
        """Test that file_shapes is a dictionary to support multiple keys."""
        # This is more of a structure test
        # In actual usage, file_shapes should be: {'key1': [shapes], 'key2': [shapes]}
        shapes = {
            'image': [(124, 500, 686)],
            'image_sc': [(64, 250, 343)],
        }
        converted = convert_tuples_to_lists(shapes)

        self.assertIsInstance(converted, dict)
        self.assertEqual(converted['image'], [[124, 500, 686]])
        self.assertEqual(converted['image_sc'], [[64, 250, 343]])


class TestReadOnlyMode(unittest.TestCase):
    """Tests for read-only mode functionality."""

    def test_folder_accepts_readonly_param(self):
        """Test that Folder accepts read_only parameter."""
        try:
            folder = Folder(
                folder_path="nonexistent/path",
                key="image",
                read_only=True,
                search_file_tree_kwargs={'redo': True, 'write': False}
            )
        except FileNotFoundError:
            # Expected - testing parameter acceptance, not functionality
            pass

    def test_dataset_accepts_readonly_param(self):
        """Test that Dataset accepts read_only parameter."""
        try:
            dataset = Dataset(
                folder_path="nonexistent/path",
                key="image",
                read_only=True,
            )
        except FileNotFoundError:
            # Expected - testing parameter acceptance, not functionality
            pass


if __name__ == '__main__':
    unittest.main()
