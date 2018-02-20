import json
import unittest
import pyperclip
from src.com.jalasoft.search_files.utils.copy_2_clipboard import Copy2ClipBoard


class Copy2ClipBoardTest(unittest.TestCase):
    """
    Test the Copy2ClipBoard class functions
    """

    def test_convert_dictionary_to_json_is_returning_a_json_when_a_dictionary_is_provided(self):
        dictionary = {
            "1": "Basic Search",
            "2": "Advanced Search",
            "0": "Exit"
        }
        json_expected = json.dumps(dictionary, ensure_ascii=False)
        copy2clipboard = Copy2ClipBoard()
        json_result = copy2clipboard.convert_dictionary_to_json(dictionary)
        self.assertEqual(json_result, json_expected)

    def test_convert_dictionary_to_json_is_returning_a_json_when_a_void_dictionary_is_provided(self):
        dictionary = {}
        json_expected = json.dumps(dictionary, ensure_ascii=False)
        copy2clipboard = Copy2ClipBoard()
        json_result = copy2clipboard.convert_dictionary_to_json(dictionary)
        self.assertEqual(json_result, json_expected)

    def test_copy_to_clip_is_copying_the_json_structure_generated_from_a_dictionary_in_memory(self):
        dictionary = {
            "1": "Basic Search",
            "2": "Advanced Search",
            "0": "Exit"
        }
        json_expected = json.dumps(dictionary, ensure_ascii=False)
        copy2clipboard = Copy2ClipBoard()
        copy2clipboard.copy_to_clip(dictionary)
        self.assertEqual(pyperclip.paste(), json_expected)

    def test_copy_to_clip_is_copying_the_json_structure_generated_from_a_void_dictionary_in_memory(self):
        dictionary = {}
        json_expected = json.dumps(dictionary, ensure_ascii=False)
        copy2clipboard = Copy2ClipBoard()
        copy2clipboard.copy_to_clip(dictionary)
        self.assertEqual(pyperclip.paste(), json_expected)

