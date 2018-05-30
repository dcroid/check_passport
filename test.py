import datetime
import unittest

from main import check_passport, calculate_age


class TestStringMethods(unittest.TestCase):

    def test_calculate_age(self):
        date_tmp = '%Y-%m-%d'

        date = datetime.datetime.strptime('1988-05-27', date_tmp).date()
        date2 = datetime.datetime.strptime('2018-05-29', date_tmp).date()
        date3 = datetime.datetime.strptime('2019-05-29', date_tmp).date()
        self.assertEqual(30, calculate_age(date))
        self.assertEqual(0, calculate_age(date2))
        self.assertEqual(-1, calculate_age(date3))

    def test_check_passport_rais_exception(self):
        dob = '1988-05-27'
        get_passport = '2002-05-27'

        self.assertRaises(Exception, check_passport)
        self.assertRaises(Exception, check_passport, dob=dob)
        self.assertRaises(Exception, check_passport, get_passport=get_passport)
        self.assertRaises(Exception, check_passport, get_passport=get_passport.replace("-", "/"), dob=dob)
        self.assertRaises(Exception, check_passport, get_passport=get_passport, dob=dob.replace("-", "/"))
        self.assertRaises(Exception, check_passport, get_passport=get_passport, dob='2018-01-01')

    def test_check_passport_false(self):
        get_passport_list = '{}-05-26'.format(2018), \
                            '{}-06-28'.format(2018)

        for get_passport in get_passport_list:
            self.assertFalse(check_passport(get_passport=get_passport, dob='{}-05-27'.format(2004)))

    def test_check_passport_true(self):
        get_passport_list = '{}-05-28'.format(2018), \
                            '{}-06-01'.format(2018), \
                            '{}-06-26'.format(2018), \
                            '{}-06-27'.format(2018)

        for get_passport in get_passport_list:
            self.assertTrue(check_passport(get_passport=get_passport, dob='{}-05-27'.format(2004)))
            self.assertTrue(check_passport(get_passport=get_passport, dob='{}-05-27'.format(2004 - 6)))
            self.assertTrue(check_passport(get_passport=get_passport, dob='{}-05-27'.format(2004 - 31)))
