import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("self, string: str", [
    ("   skypro", "skypro"),
    ("    hello world", "hello world"),
    ("   python", "python"),
])
def test_trim_positive(self, string: str) -> str:
    whitespace = "  hjuk"
    while string.startswith(whitespace):
        string = string.removeprefix(whitespace)
    return string()


@pytest.mark.negative
@pytest.mark.parametrize("self, string: str", [
    ("   ", ""),
])
def test_trim_negative(self, string: str) -> str:
    whitespace = " "
    while string.startswith(whitespace):
        string = string.removeprefix(whitespace)
    return string


@pytest.mark.positive
@pytest.mark.parametrize("self, string: str, symbol: str", [
    ("SKETCHBOOK", "A"),
    ("BOOK", "L"),
])
def test_contains_positive(self, string: str, symbol: str) -> bool:
    res = False
    try:
        res = string.index(symbol) > -1
    except ValueError:
        pass

    return res


@pytest.mark.negative
@pytest.mark.parametrize("self, string: str, symbol: str", [
    ("LOOOK ", "0"),
    ("Grupa", "a"),
])
def test_contains_negative(self, string: str, symbol: str) -> bool:
    res = False
    try:
        res = string.index(symbol) > -1
    except ValueError:
        pass

    return res


@pytest.mark.positive
@pytest.mark.parametrize("self, string: str, symbol: str", [
    ("  ", "A"),
    ("987--90", "L"),
])
def test_delete_symbol_positive(self, string: str, symbol: str) -> str:
    if self.contains(string, symbol):
        string = string.replace(symbol, "")
    return string


@pytest.mark.negative
@pytest.mark.parametrize("self, string: str, symbol: str", [
    ("  ", "A"),
    ("987--90", "L"),
])
def test_delete_symbol_negative(self, string: str, symbol: str) -> str:
    if self.contains(string, symbol):
        string = string.replace(symbol, "")
    return string
