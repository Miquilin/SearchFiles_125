import unittest
from src.com.jalasoft.search_files.menu.cli_menu import CLIMenu


class CLIMenuTest(unittest.TestCase):
    """
    Test the CLIMenu class functions
    """

    def test_set_a_value_from_search_for_menu_items_dict(self):
        menu = CLIMenu()
        menu.set_search_for_menu_items("125", "An option")
        option = menu.get_search_for_menu_items("125")

        self.assertEqual(option, "An option")

    def test_get_a_value_from_search_for_menu_items_dict(self):
        menu = CLIMenu()
        menu.set_search_for_menu_items("100", "New option")
        option = menu.get_search_for_menu_items("100")

        self.assertEqual(option, "New option")

