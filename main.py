#!/usr/bin/python
# -*- coding: UTF-8 -*-
__project__ = 'passport'
__date__ = ''
__author__ = 'andreyteterevkov'

import datetime
import dateutil.relativedelta


YEAR_CHANGE_14 = 14
YEAR_CHANGE_20 = 20
YEAR_CHANGE_45 = 45

DATE_FORMAT = '%Y-%m-%d'


def age_get_passport(born):
    """
    Determine the year of replacement of the passport

    :param born:  birthday
    :return: Int
             Exception if birthday > today or old year < CHANGE_PASSPORT_14
    """
    age = calculate_age(born)

    if age < YEAR_CHANGE_14:
        raise Exception('Expected age is 14+')

    if YEAR_CHANGE_14 <= age < YEAR_CHANGE_20:
        return YEAR_CHANGE_14
    elif YEAR_CHANGE_20 <= age < YEAR_CHANGE_45:
        return YEAR_CHANGE_20
    elif age >= YEAR_CHANGE_45:
        return YEAR_CHANGE_45
    else:
        raise Exception('WOW! Craizy param! Bro, Check dob and calculate_age fun pls')


def calculate_age(born):
    """
    Get Age from date

    :param born: datetime.date object
    :return: int if years > 0
             0 if years <= 0


    """
    today = datetime.date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        # raised when birth date is February 29
        # and the current year is not a leap year.
        birthday = born.replace(year=today.year, month=born.month+1, day=1)

    if birthday.year < today.year:
        return today.year - born.year - 1
    else:
        years = today.year - born.year
        return years if years > 0 else 0


def check_passport(born, get_passport):
    """Check overdue passport.

    :param born: date of birth (Format '%Y-%m-%d')
    :param get_passport: date get passport (Format '%Y-%m-%d')
    :return: bool (True/False)
            True - Valid passport
            False - Invalid passport
    """

    try:
        birthday = datetime.datetime.strptime(born, DATE_FORMAT).date()
    except ValueError as error:
        raise ValueError(error)

    try:
        passport = datetime.datetime.strptime(get_passport, DATE_FORMAT).date()
    except ValueError as error:
        raise ValueError(error)

    max_issued_date = birthday + dateutil.relativedelta.relativedelta(years=age_get_passport(birthday), months=1)
    delta = max_issued_date - passport
    if delta.days not in range(0, 31):
        return False

    return True
