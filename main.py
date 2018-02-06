from src.com.jalasoft.search_files.menu.cli_menu_basic_flow import CLIMenuBasicFlow
from src.com.jalasoft.search_files.menu.cli_menu import CLIMenu
from src.com.jalasoft.search_files.utils.copy_2_clipboard import Copy2ClipBoard


class SearchFile(object):

    def main():
        menu = CLIMenuBasicFlow()
        cli_menu = CLIMenu()
        copy_to_clip = Copy2ClipBoard()
        while True:
            go_to_search_for = False
            choice = menu.show_menu(1)

            # Main menu [menu 1]
            while go_to_search_for == False:
                if choice == 0:
                    menu.show_menu(0)
                if menu.main_menu_validation(choice):
                    if choice == "1":
                        go_to_search_criteria = False
                        go_to_search_for = True
                        menu.show_menu(2)
                    if choice == "2":
                        print("launch advanced menu")
                else:
                    choice = menu.show_menu(1)

            # Basic Search - Search For [menu 2]
            while go_to_search_criteria == False:
                if choice == "0":
                    menu.show_menu(0)
                if menu.basic_search_for_option_validation(choice):
                    menu.set_summary_data_items("search_for_option", menu.get_search_for_items(choice))
                    go_to_search_criteria = True
                    go_to_search_in_path = False
                    choice = menu.show_menu(3)
                else:
                    choice = menu.show_menu(2)

            # Basic Search - Search For Criteria [menu 3]
            while go_to_search_in_path == False:
                if choice == "0":
                    menu.show_menu(0)
                if menu.basic_search_for_criteria_validation(choice):
                    menu.set_summary_data_items("search_for_criteria", choice)
                    go_to_search_in_path = True
                    go_to_summary_option = False
                    choice = menu.show_menu(4)
                else:
                    choice = menu.show_menu(3)

            # Basic Search - Search in path [menu 4]
            while go_to_summary_option == False:
                if menu.basic_search_in_path_validation(choice):
                    menu.set_summary_data_items("search_in_path", choice)
                    go_to_summary_option = True
                    go_to_search_results = False
                    choice = menu.show_menu(5)
                else:
                    choice = menu.show_menu(4)
            # Summary - Menu 5
            while go_to_search_results == False:
                if choice == "0":
                    menu.show_menu(0)
                if menu.basic_summary_option_validation(choice):
                    if choice == "1":
                        menu.start_search_process()
                        go_to_search_results = True
                        go_to_new_search = False
                        choice = menu.show_menu(6)
                    if choice == "2":
                        go_to_new_search = True
                        break
                else:
                    choice = menu.show_menu(5)
            # Result - Menu 6
            while (go_to_new_search == False):
                if choice == "0":
                    menu.show_menu(0)
                if menu.basic_result_option_validation(choice):
                    if choice == "1":
                        copy_to_clip.copy_to_clip(cli_menu.results_data)
                        print("Doing the copy to Clipboard")
                        choice = menu.show_menu(6)
                    if choice == "2":
                        break

    if __name__ == "__main__":
        main()
