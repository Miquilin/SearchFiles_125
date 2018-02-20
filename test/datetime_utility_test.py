import unittest
from src.com.jalasoft.search_files.utils.datetime_utility import DateTimeUtility


class DateTimeUtilityTest(unittest.TestCase):
    """
    Test the DateTimeUtility class functions
    """
    def test_convert_string_to_datetime_returns_a_date_from_a_string(self):
        str_date = "2018-01-01 08:00:00"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), str_date)

    def test_convert_string_to_date_time_returns_the_right_date_when_time_is_in_24h_format(self):
        str_date = "2018-01-01 22:00:00"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), str_date)

    def test_convert_string_to_date_time_returns_the_right_date_when_time_is_in_24h_format(self):
        str_date = "2018-01-01 22:00:00"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), str_date)

    def test_convert_string_to_date_time_returns_a_void_date_when_time_provided_is_any_string_char(self):
        str_date = "my_date"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), "")

    def test_convert_string_to_date_time_returns_a_void_date_when_time_provided_is_a_number(self):
        str_date = 1234567890
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), "")

    def test_convert_string_to_date_time_returns_a_void_date_when_time_provided_is_an_special_character(self):
        str_date = "#!$%&/()=?¡"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), "")

    def test_convert_string_to_date_time_returns_a_void_date_when_time_only_contains_date_part(self):
        str_date = "2018-01-01"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), "")

    def test_convert_string_to_date_time_returns_a_void_date_when_time_only_contains_time_part(self):
        str_date = "08:00:00"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), "")

    def test_convert_string_to_date_time_returns_a_void_date_when_time_provided_does_not_have_a_proper_format(self):
        str_date = "08:00:00 2018-01-01"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), "")

    def test_convert_string_to_date_time_returns_a_void_date_when_time_provided_does_not_have_a_proper_separators(self):
        str_date = "2018/01/01 08:00:00"
        date_time = DateTimeUtility()
        date_returned = date_time.convert_string_to_datetime(str_date)
        self.assertEqual(str(date_returned), "")