import pyperclip
import json


class Copy2ClipBoard(object):

    def __init__(self):
        self.json_result = ""

    def convert_dictionary_to_json(self, dictionary):
        return json.dumps(dictionary, ensure_ascii=False)

    def copy_to_clip(self, dictionary):
        self.json_result = self.convert_dictionary_to_json(dictionary)
        pyperclip.copy(self.json_result)
