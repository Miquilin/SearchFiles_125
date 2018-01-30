from src.com.jalasoft.search_files.menu.CLIMenuFlow import CLIMenuFlow


class SearchFile(object):

    def main():
        menu = CLIMenuFlow()
        while True:
            go_to_search_criteria = False
            choice = menu.show_menu(1)
            # Search For - menu 1
            while (go_to_search_criteria == False):
                if choice == "0":
                    menu.show_menu(0)
                if menu.search_for_option_validation(choice):
                    menu.set_summary_data_items("search_for_option", menu.get_search_for_items(choice))
                    go_to_search_criteria = True
                    go_to_search_in_menu = False
                    choice = menu.show_menu(2)
                else:
                    choice = menu.show_menu(1)
            # Search For Criteria - Menu 2
            while (go_to_search_in_menu == False):
                if menu.search_for_criteria_validation(choice):
                    menu.set_summary_data_items("search_for_criteria", choice)
                    go_to_search_in_menu = True
                    go_to_search_in_path = False
                    choice = menu.show_menu(3)
                else:
                    choice = menu.show_menu(2)
            # Search In - Menu 3
            while (go_to_search_in_path == False):
                if choice == "0":
                    menu.show_menu(0)
                if menu.search_in_option_validation(choice):
                    menu.set_summary_data_items("search_in_option", menu.get_search_in_items(choice))
                    go_to_search_in_path = True
                    go_to_summary_option = False
                    choice = menu.show_menu(4)
                else:
                    choice = menu.show_menu(3)
            # Searh in path - Menu 4
            while (go_to_summary_option == False):
                if menu.search_in_path_validation(choice):
                    menu.set_summary_data_items("search_in_path", choice)
                    go_to_summary_option = True
                    go_to_search_results = False
                    choice = menu.show_menu(5)
                else:
                    choice = menu.show_menu(4)
            # Summary - Menu 5
            while (go_to_search_results == False):
                if choice == "0":
                    menu.show_menu(0)
                if menu.summary_option_validation(choice):
                    if choice == "1":
                        print("doing the search")
                        # here add the search method
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
                if menu.result_option_validation(choice):
                    if choice == "1":
                        print(choice, " doing the copy to clipboard")
                        ## Here the code related to Clipboard
                        choice = menu.show_menu(6)
                    if choice == "2":
                        print(choice, " doing a new search")
                        break

    if __name__ == "__main__":
        # menu = CLIMenu()
        # menu.search_for_menu()
        main()
