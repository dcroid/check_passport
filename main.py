#!/usr/bin/python
# -*- coding: UTF-8 -*-
__project__ = 'passport'
__date__ = ''
__author__ = 'andreyteterevkov'

import datetime
import dateutil.relativedelta


def calculate_age(born):
    """
    Get Age from date

    :param born: datetime.date object
    :return: int

    """
    today = datetime.date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        # raised when birth date is February 29
        # and the current year is not a leap year.
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


def check_passport(dob=None, get_passport=None):
    """Check overdue passport.

    :param dob: date of birth (Format '%Y-%m-%d')
    :param get_passport: date get passport (Format '%Y-%m-%d')
    :return: bool (True/False)

    """

    date_tmp = '%Y-%m-%d'

    # Cheking parameters
    if not dob or not get_passport:
        if not dob:
            raise Exception('No param "dob"')
        else:
            raise Exception('No param "get_passport"')

    try:
        date_dob = datetime.datetime.strptime(dob, date_tmp).date()
    except ValueError:
        raise Exception('Wrong format param "dob"')

    try:
        date_passport = datetime.datetime.strptime(get_passport, date_tmp).date()
    except ValueError:
        raise Exception('Wrong format param "get_passport"')

    age = calculate_age(date_dob)
    if age < 14:
        raise Exception('Expected age is 14+')

    if 14 <= age < 20:
        years = 14
    elif 20 <= age < 45:
        years = 20
    elif age >= 45:
        years = 45
    else:
        raise Exception('WOW! Craizy param! Bro, Check dob and calculate_age fun pls')

    max_exp_date = date_dob + dateutil.relativedelta.relativedelta(years=years, months=1)
    delta = max_exp_date - date_passport

    if delta.days not in range(0, 31):
        return False

    return True


if __name__ == '__main__':
    print(
        check_passport(dob='2018-01-01', get_passport='2002-07-22')
    )
