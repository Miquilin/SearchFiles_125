from src.com.jalasoft.search_files.menu.cli_menu_basic_flow import CLIMenuBasicFlow
from src.com.jalasoft.search_files.menu.cli_menu_advanced_flow import CLIMenuAdvancedFlow
from src.com.jalasoft.search_files.utils.copy_2_clipboard import Copy2ClipBoard


class SearchFile(object):

    def main():
        basic_menu = CLIMenuBasicFlow()
        advanced_menu = CLIMenuAdvancedFlow()
        copy_to_clip = Copy2ClipBoard()
        while True:
            go_to_search_for = False
            go_to_search_criteria = True
            go_to_search_in_path = True
            go_to_summary_option = True
            go_to_search_results = True
            go_to_new_search = True
            go_to_search_for_name_criteria = True
            go_to_search_for_extension = True
            go_to_search_for_size = True
            go_to_search_for_size_criteria = True
            go_to_search_for_owner_criteria = True
            go_to_search_for_date_criteria = True
            go_to_search_for_date_operator = True
            go_to_search_for_date_text_criteria = True
            go_to_search_for_content_criteria = True
            go_to_search_in_menu = True
            go_to_search_in_path_criteria = True
            go_to_summary = True
            go_to_adv_search_results = True
            go_to_adv_new_search = True
            choice = basic_menu.show_menu(1)

            # Main menu [menu 1]
            while go_to_search_for == False:
                if choice == 0:
                    basic_menu.show_menu(0)
                if basic_menu.main_menu_validation(choice):
                    if choice == "1":
                        go_to_search_criteria = False
                        go_to_search_for = True
                        choice = basic_menu.show_menu(2)
                        continue
                    if choice == "2":
                        go_to_search_for_name_criteria = False
                        go_to_search_for = True
                        choice = advanced_menu.show_menu(2)
                else:
                    choice = basic_menu.show_menu(1)
            # Basic Search - Search For [menu 2]
            while go_to_search_criteria == False:
                if choice == "0":
                    basic_menu.show_menu(0)
                if basic_menu.basic_search_for_option_validation(choice):
                    basic_menu.set_summary_data_items("search_for_option", basic_menu.get_search_for_menu_item(choice))
                    go_to_search_criteria = True
                    go_to_search_in_path = False
                    choice = basic_menu.show_menu(3)
                else:
                    choice = basic_menu.show_menu(2)
            # Basic Search - Search For Criteria [menu 3]
            while go_to_search_in_path == False:
                if choice == "0":
                    basic_menu.show_menu(0)
                if basic_menu.basic_search_for_criteria_validation(choice):
                    basic_menu.set_summary_data_items("search_for_criteria", choice)
                    go_to_search_in_path = True
                    go_to_summary_option = False
                    choice = basic_menu.show_menu(4)
                else:
                    choice = basic_menu.show_menu(3)
            # Basic Search - Search in path [menu 4]
            while go_to_summary_option == False:
                if basic_menu.basic_search_in_path_validation(choice):
                    basic_menu.set_summary_data_items("search_in_path", choice)
                    go_to_summary_option = True
                    go_to_search_results = False
                    choice = basic_menu.show_menu(5)
                else:
                    choice = basic_menu.show_menu(4)
            # Basic Search Summary - Menu 5
            while go_to_search_results == False:
                if choice == "0":
                    basic_menu.show_menu(0)
                if basic_menu.basic_summary_option_validation(choice):
                    if choice == "1":
                        basic_menu.start_search_process()
                        go_to_search_results = True
                        go_to_new_search = False
                        choice = basic_menu.show_menu(6)
                    if choice == "2":
                        go_to_new_search = True
                        break
                else:
                    choice = basic_menu.show_menu(5)
            # Result - Menu 6
            while go_to_new_search == False:
                if choice == "0":
                    basic_menu.show_menu(0)
                if basic_menu.basic_result_option_validation(choice):
                    if choice == "1":
                        copy_to_clip.copy_to_clip(basic_menu.get_results_dictionary())
                        choice = basic_menu.show_menu(6)
                    if choice == "2":
                        break

            # Advanced Search - Search For Name [menu 2]
            while go_to_search_for_name_criteria == False:
                if choice == "0":
                    advanced_menu.show_menu(0)
                if advanced_menu.advanced_search_for_name_menu_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_name",
                                                                  advanced_menu.get_advanced_search_for_name_menu_items(
                                                                      choice))
                    if choice == "3":
                        go_to_search_for_name_criteria = True
                        go_to_search_for_size = False
                        choice = advanced_menu.show_menu(4)
                    else:
                        go_to_search_for_name_criteria = True
                        go_to_search_for_extension = False
                        choice = advanced_menu.show_menu(3)
                else:
                    choice = advanced_menu.show_menu(2)
            # Advanced Search - Search For Name Criteria [menu 3]
            while go_to_search_for_extension == False:
                if advanced_menu.advanced_search_for_name_criteria_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_name_criteria", choice)
                    go_to_search_for_extension = True
                    go_to_search_for_size = False
                    choice = advanced_menu.show_menu(4)
                else:
                    choice = advanced_menu.show_menu(3)
            # Advanced Search - Search For Extension Criteria [menu 4]
            while go_to_search_for_size == False:
                if advanced_menu.advanced_search_for_extension_criteria_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_extension_criteria", choice)
                    go_to_search_for_size = True
                    go_to_search_for_size_criteria = False
                    choice = advanced_menu.show_menu(5)
                else:
                    choice = advanced_menu.show_menu(4)
            # Advanced Search - Search For Size [menu 5]
            while go_to_search_for_size_criteria == False:
                if choice == "0":
                    advanced_menu.show_menu(0)
                if advanced_menu.advanced_search_for_size_menu_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_size",
                                                                  advanced_menu.get_advanced_search_for_size_menu_items(
                                                                      choice))
                    if choice == "3":
                        go_to_search_for_size_criteria = True
                        go_to_search_for_date = False
                        choice = advanced_menu.show_menu(7)
                    else:
                        go_to_search_for_size_criteria = True
                        go_to_search_for_owner_criteria = False
                        choice = advanced_menu.show_menu(6)
                else:
                    choice = advanced_menu.show_menu(5)
            # Advanced Search - Search For Size Criteria [menu 6]
            while go_to_search_for_owner_criteria == False:
                if advanced_menu.advanced_search_for_size_criteria_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_size_criteria", choice)
                    go_to_search_for_owner_criteria = True
                    go_to_search_for_date = False
                    choice = advanced_menu.show_menu(7)
                else:
                    choice = advanced_menu.show_menu(6)
            # Advanced Search - Search For Owner Criteria [menu 7]
            while go_to_search_for_date == False:
                if advanced_menu.advanced_search_for_owner_criteria_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_owner_criteria", choice)
                    go_to_search_for_date = True
                    go_to_search_for_date_criteria = False
                    choice = advanced_menu.show_menu(8)
                else:
                    choice = advanced_menu.show_menu(7)
                # Advanced Search - Search For Date Operator menu [menu 8]
                while go_to_search_for_date_criteria == False:
                    if choice == "0":
                        advanced_menu.show_menu(0)
                    if advanced_menu.advanced_search_for_date_criteria_menu_validation(choice):
                        advanced_menu.set_advanced_summary_data_items("search_for_date_criteria",
                                                                      advanced_menu.get_advanced_search_for_date_criteria_menu_items(
                                                                          choice))
                        if choice == "3":
                            go_to_search_for_date_criteria = True
                            go_to_search_in_menu = False
                            choice = advanced_menu.show_menu(11)
                        else:
                            go_to_search_for_date_criteria = True
                            go_to_search_for_date_operator = False
                            choice = advanced_menu.show_menu(9)
                    else:
                        choice = advanced_menu.show_menu(8)
            # Advanced Search - Search For Date Operator menu [menu 9]
            while go_to_search_for_date_operator == False:
                if choice == "0":
                    advanced_menu.show_menu(0)
                if advanced_menu.advanced_search_for_date_criteria_menu_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_date_operation_criteria",
                                                                  advanced_menu.get_advanced_search_for_date_operator_menu_items(
                                                                      choice))
                    go_to_search_for_date_operator = True
                    go_to_search_for_content_criteria = False
                    choice = advanced_menu.show_menu(10)
                else:
                    choice = advanced_menu.show_menu(9)
            # Advanced Search - Search For Date Criteria [menu 10]
            while go_to_search_for_content_criteria == False:
                if advanced_menu.advanced_search_for_owner_criteria_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_date_text_criteria", choice)
                    go_to_search_for_content_criteria = True
                    go_to_search_in_menu = False
                    choice = advanced_menu.show_menu(11)
                else:
                    choice = advanced_menu.show_menu(10)
            # Advanced Search - Search For Content Criteria [menu 11]
            while go_to_search_in_menu == False:
                if advanced_menu.advanced_search_for_content_criteria_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_for_content_criteria", choice)
                    go_to_search_in_menu = True
                    go_to_search_in_path_criteria = False
                    choice = advanced_menu.show_menu(12)
                else:
                    choice = advanced_menu.show_menu(11)
            # Advanced Search - Search In Menu [menu 12]
            while go_to_search_in_path_criteria == False:
                if choice == "0":
                    advanced_menu.show_menu(0)
                if advanced_menu.advanced_search_in_menu_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_in",
                                                                  advanced_menu.get_advanced_search_in_items(choice))
                    go_to_search_in_path_criteria = True
                    go_to_summary = False
                    choice = advanced_menu.show_menu(13)
                else:
                    choice = advanced_menu.show_menu(12)
            # Advanced Search - Search In Path  Criteria [menu 13]
            while go_to_summary == False:
                if advanced_menu.advanced_search_in_path_criteria_validation(choice):
                    advanced_menu.set_advanced_summary_data_items("search_in_criteria", choice)
                    go_to_summary = True
                    go_to_adv_search_results = False
                    choice = advanced_menu.show_menu(14)
                else:
                    choice = advanced_menu.show_menu(13)
            # Advanced Search - Summary Search [menu 14]
            while go_to_adv_search_results == False:
                if choice == "0":
                    advanced_menu.show_menu(0)
                if advanced_menu.advanced_summary_menu_validation(choice):
                    if choice == "1":
                        advanced_menu.start_search_process()
                        go_to_adv_search_results = True
                        go_to_adv_new_search = False
                        choice = advanced_menu.show_menu(15)
                    if choice == "2":
                        go_to_new_search = True
                        break
                else:
                    choice = basic_menu.show_menu(5)
            # Advanced Search Result [menu 15]
            while go_to_adv_new_search == False:
                if choice == "0":
                    advanced_menu.show_menu(0)
                if advanced_menu.advanced_summary_menu_validation(choice):
                    if choice == "1":
                        copy_to_clip.copy_to_clip(advanced_menu.get_results_dictionary())
                        choice = advanced_menu.show_menu(15)
                    if choice == "2":
                        advanced_menu.clean_advanced_summary_items()
                        break

    if __name__ == "__main__":
        main()
