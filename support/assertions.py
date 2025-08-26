from support.error_messages import AssertionErrors
import urllib.parse

class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, f'Expected:{expected}, {actual}'
