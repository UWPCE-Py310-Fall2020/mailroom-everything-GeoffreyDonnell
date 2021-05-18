"""
A series of unit sets to ensure the logic of the mailroom program
is working properly using pytest.
"""

from mailroom import generate_donor_list
from mailroom import current_donor
from mailroom import add_new_donor_to_database
from mailroom import generate_report_data


def test_generate_donor_list():
    """
    This test is to ensure that the donor list generated is correct.
    There is no input variable for this function as it relies on values declared globally.
    """
    expected = ['Tony Stark',
                'Steven Rogers',
                'Bruce Wayne',
                'Clark Kent',
                'Geoffrey Donnell']
    assert generate_donor_list() == expected


def test_current_donor():
    """
    This test is to ensure that the current donor used will have their
    donation history appended.
    """
    expected = [('Tony Stark', [10, 1200]),
                ('Steven Rogers', [10, 20]),
                ('Bruce Wayne', [20, 30, 40]),
                ('Clark Kent', [50]),
                ('Geoffrey Donnell', [60, 70])]

    assert current_donor('Tony Stark', 1200) == expected


def test_add_new_donor_to_database():
    """
    This test is to ensure that the new donor and gift is added to the list.
    """
    expected = [('Tony Stark', [10, 1200]),
                ('Steven Rogers', [10, 20]),
                ('Bruce Wayne', [20, 30, 40]),
                ('Clark Kent', [50]),
                ('Geoffrey Donnell', [60, 70]),
                ('Iron Man', [200])]
    assert add_new_donor_to_database('Iron Man', 200) == expected


def test_donation_total():
    """
    The generate_report_data() calculates multiple values used.
    This test is to check that the correct donation total is calculated
    """
    results = generate_report_data()
    assert results[1] == [1210, 30, 90, 50, 130, 200]


def test_donation_freq():
    """
    The generate_report_data() calculate multiple values used.
    This test is to check that the correct donation freq. is calculated
    """
    results = generate_report_data()
    assert results[2] == [2, 2, 3, 1, 2, 1]


def test_donation_average():
    """
    The generate_report_data() calculate multiple values used.
    This test is to check that the correct donation freq. is calculated
    """
    results = generate_report_data()
    assert results[3] == [605.00, 15.00, 30.00, 50.00, 65.00, 200.00]
