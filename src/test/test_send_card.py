import unittest
import pathlib

from controller.get_card_controller import GetCardController


class TestSendCardService(unittest.TestCase):
    def setUp(self) -> None:
        self.get_card_controller = GetCardController()

    def test_get_raw_cards_folder(self):
        mock_folder = self.get_card_controller._get_root_folder()
        parent_path = pathlib.Path(__file__).parent.parent.parent.resolve()

        self.assertEqual(mock_folder, parent_path)

    def test_get_file_list(self):
        expected_file_format = 'md'

        files = self.get_card_controller._get_files_list()
        random_file = files[0]
        actual_files_format = random_file.split('/')[-1].split('.')[-1]  # ['file_name', 'md']

        self.assertEqual(actual_files_format, expected_file_format)
