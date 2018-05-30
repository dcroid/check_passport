import datetime
import unittest

from main import check_passport, calculate_age, age_get_passport, \
    DATE_FORMAT, YEAR_CHANGE_45, YEAR_CHANGE_20, YEAR_CHANGE_14


class TestStringMethods(unittest.TestCase):

    def test_calculate_age(self):

        date = datetime.datetime.strptime('1988-05-27', DATE_FORMAT).date()
        date2 = datetime.datetime.strptime('2018-05-29', DATE_FORMAT).date()
        date3 = datetime.datetime.strptime('2019-05-29', DATE_FORMAT).date()
        self.assertEqual(30, calculate_age(date))
        self.assertEqual(0, calculate_age(date2))
        self.assertEqual(0, calculate_age(date3))

    def test_age_passport_change_get_int(self):
        date = datetime.datetime.strptime('2004-05-27', DATE_FORMAT).date()
        date2 = datetime.datetime.strptime('{}-05-27'.format(2004 - 6), DATE_FORMAT).date()
        date3 = datetime.datetime.strptime('{}-05-27'.format(2004 - 31), DATE_FORMAT).date()
        date4 = datetime.datetime.strptime('{}-05-27'.format(2004 - 50), DATE_FORMAT).date()

        self.assertEqual(YEAR_CHANGE_14, age_get_passport(date))
        self.assertEqual(YEAR_CHANGE_20, age_get_passport(date2))
        self.assertEqual(YEAR_CHANGE_45, age_get_passport(date3))
        self.assertEqual(YEAR_CHANGE_45, age_get_passport(date4))

    def test_age_passport_change_return_exception(self):
        date = datetime.datetime.strptime('2010-05-27', DATE_FORMAT).date()
        date2 = datetime.datetime.strptime('2010-05-27', DATE_FORMAT).date()
        self.assertRaises(Exception, age_get_passport, date)
        self.assertRaises(Exception, age_get_passport, date2)

    def test_check_passport_rais_exception(self):
        dob = '1988-05-27'
        get_passport = '2002-05-27'

        self.assertRaises(Exception, check_passport)
        self.assertRaises(Exception, check_passport, born=dob)
        self.assertRaises(Exception, check_passport, get_passport=get_passport)
        self.assertRaises(Exception, check_passport, get_passport=get_passport.replace("-", "/"), born=dob)
        self.assertRaises(Exception, check_passport, get_passport=get_passport, born=dob.replace("-", "/"))
        self.assertRaises(Exception, check_passport, get_passport=get_passport, born='2018-01-01')

    def test_check_passport_false(self):
        get_passport_list = '2018-05-26', '2018-06-28'

        for get_passport in get_passport_list:
            self.assertFalse(check_passport(get_passport=get_passport, born='2004-05-27'))

    def test_check_passport_true(self):
        get_passport_list = ['2018-05-28', '2018-06-01', '2018-06-26', '2018-06-27']

        for get_passport in get_passport_list:
            self.assertTrue(check_passport(get_passport=get_passport, born='2004-05-27'))
            self.assertTrue(check_passport(get_passport=get_passport, born='{}-05-27'.format(2004 - 6)))
            self.assertTrue(check_passport(get_passport=get_passport, born='{}-05-27'.format(2004 - 31)))
