import unittest
from unittest.mock import patch

from .config import create_options


class TestOptions(unittest.TestCase):
    def test_create_options_valid(self):
        script_name = "script_name"
        product_id = "product_id"
        client_id = "client_id"
        api_key = "api_key"
        file_path = "/path/to/addon.zip"
        notes = "Release notes"
        debug = "true"
        retry_count = "3"
        sleep_seconds = "5"

        test_args = [
            script_name,
            product_id,
            client_id,
            api_key,
            file_path,
            notes,
            debug,
            retry_count,
            sleep_seconds,
        ]
        with patch("sys.argv", test_args):
            options = create_options()
            self.assertEqual(options.product_id, product_id)
            self.assertEqual(options.client_id, client_id)
            self.assertEqual(options.api_key, api_key)
            self.assertEqual(options.file_path, file_path)
            self.assertEqual(options.notes, notes)
            self.assertTrue(options.debug)
            self.assertEqual(options.retry_count, int(retry_count))
            self.assertEqual(options.sleep_seconds, int(sleep_seconds))

    def test_create_options_debug_false(self):
        script_name = "script_name"
        product_id = "product_id"
        client_id = "client_id"
        api_key = "api_key"
        file_path = "/path/to/addon.zip"
        notes = "Release notes"
        debug = "false"
        retry_count = "3"
        sleep_seconds = "5"

        test_args = [
            script_name,
            product_id,
            client_id,
            api_key,
            file_path,
            notes,
            debug,
            retry_count,
            sleep_seconds,
        ]
        with patch("sys.argv", test_args):
            options = create_options()
            self.assertEqual(options.product_id, product_id)
            self.assertEqual(options.client_id, client_id)
            self.assertEqual(options.api_key, api_key)
            self.assertEqual(options.file_path, file_path)
            self.assertEqual(options.notes, notes)
            self.assertFalse(options.debug)
            self.assertEqual(options.retry_count, int(retry_count))
            self.assertEqual(options.sleep_seconds, int(sleep_seconds))

    def test_options_to_edge_options(self):
        script_name = "script_name"
        product_id = "product_id"
        client_id = "client_id"
        api_key = "api_key"
        file_path = "/path/to/addon.zip"
        notes = "Release notes"
        debug = "true"
        retry_count = "3"
        sleep_seconds = "5"

        test_args = [
            script_name,
            product_id,
            client_id,
            api_key,
            file_path,
            notes,
            debug,
            retry_count,
            sleep_seconds,
        ]
        with patch("sys.argv", test_args):
            options = create_options()
            edge_options = options.to_edge_options()
            self.assertEqual(edge_options.product_id, product_id)
            self.assertEqual(edge_options.client_id, client_id)
            self.assertEqual(edge_options.api_key, api_key)
            self.assertEqual(edge_options.retry_count, int(retry_count))
            self.assertEqual(edge_options.sleep_seconds, int(sleep_seconds))

    def test_create_options_invalid_number_args(self):
        test_args = ["script_name", "product_id"]
        with patch("sys.argv", test_args):
            with self.assertRaises(SystemExit):
                create_options()
