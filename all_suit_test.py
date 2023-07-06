import unittest

from unittest.loader import makeSuite

from test_cases.add_a_new_player import TestAddAPlayer
from test_cases.changing_language_before_login_in import TestChangeLanguage
from test_cases.log_out import TestLogOut
from test_cases.login_to_the_system import TestLoginPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestLogOut))
    test_suite.addTest(makeSuite(TestChangeLanguage))
    test_suite.addTest(makeSuite(TestAddAPlayer))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
