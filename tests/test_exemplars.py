import pytest
import json
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock

import exemplars


@pytest.fixture
def valid_data():
    """
    Fixture providing valid JSON data for testing.
    """
    return {
        "icu_version": "67.1",
        "locales": {
            "en_US": {
                "main": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "auxiliary": {"single_chars": ["x", "y"], "sequences": None},
                "punctuation": ["!", "?"],
                "case_insensitive": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "case_mapping": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "numbers": {
                    "decimal": ".",
                    "group": ",",
                    "percent": "%",
                    "zero_digit": "0",
                    "digit": "#",
                    "pattern_digit": ";",
                    "plus_sign": "+",
                    "minus_sign": "-",
                    "exponential": "E",
                    "per_mille": "‰",
                    "infinity": "∞",
                    "nan": "NaN",
                    "digits": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                },
                "currency": "$",
            }
        },
        "display_names": {"en_US": "English (United States)"},
    }


@pytest.fixture
def invalid_data_missing_field():
    """
    Fixture providing invalid JSON data for testing.

    This data is considered invalid because it is missing the 'decimal' field
    in the 'numbers' object
    """
    return {
        "icu_version": "67.1",
        "locales": {
            "en_US": {
                "main": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "auxiliary": {"single_chars": ["x", "y"], "sequences": None},
                "punctuation": ["!", "?"],
                "case_insensitive": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "case_mapping": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "numbers": {
                    "group": ",",
                    "percent": "%",
                    "zero_digit": "0",
                    "digit": "#",
                    "pattern_digit": ";",
                    "plus_sign": "+",
                    "minus_sign": "-",
                    "exponential": "E",
                    "per_mille": "‰",
                    "infinity": "∞",
                    "nan": "NaN",
                    "digits": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                },
                "currency": "$",
            }
        },
        "display_names": {"en_US": "English (United States)"},
    }


@pytest.fixture
def invalid_data_type_mismatch():
    """
    Fixture providing JSON data with a type mismatch for testing.
    """
    return {
        "icu_version": "67.1",
        "locales": {
            "en_US": {
                "main": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "auxiliary": {"single_chars": ["x", "y"], "sequences": None},
                "punctuation": ["!", "?"],
                "case_insensitive": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "case_mapping": {"single_chars": ["a", "b"], "sequences": ["abc"]},
                "numbers": {
                    "decimal": ".",
                    "group": ",",
                    "percent": "%",
                    "zero_digit": "0",
                    "digit": "#",
                    "pattern_digit": ";",
                    "plus_sign": "+",
                    "minus_sign": "-",
                    "exponential": "E",
                    "per_mille": "‰",
                    "infinity": "∞",
                    "nan": "NaN",
                    "digits": "0123456789",  # Should be a list, not a string
                },
                "currency": "$",
            }
        },
        "display_names": {"en_US": "English (United States)"},
    }


def test_normalize_locale_id():
    """
    Test the normalize_locale_id function with various locale IDs.
    """
    assert exemplars.normalize_locale_id("en") == "en"
    assert exemplars.normalize_locale_id("fr-CA") == "fr_CA"
    assert exemplars.normalize_locale_id("bs-Cyrl-BA") == "bs_Cyrl_BA"
    assert exemplars.normalize_locale_id("fr_CA") == "fr_CA"
    assert exemplars.normalize_locale_id("bs_Cyrl_BA") == "bs_Cyrl_BA"


def test_get_exemplars_main():
    """
    Test the get_exemplars function for the 'main' type.
    """
    ex = exemplars.get_exemplars("en", "main")
    assert isinstance(ex, list)
    assert len(ex) > 0
    assert all(isinstance(char, str) for char in ex)


def test_get_exemplars_auxiliary():
    """
    Test the get_exemplars function for the 'auxiliary' type.
    """
    ex = exemplars.get_exemplars("en", "auxiliary")
    assert isinstance(ex, list)
    assert all(isinstance(char, str) for char in ex)


def test_get_exemplars_invalid_locale():
    """
    Test the get_exemplars function with an invalid locale.
    """
    with pytest.raises(ValueError):
        exemplars.get_exemplars("invalid-locale", "main")


def test_get_exemplars_invalid_type():
    """
    Test the get_exemplars function with an invalid type.
    """
    ex = exemplars.get_exemplars("en", "invalid-type")
    assert isinstance(ex, list)
    assert len(ex) > 0
    assert all(isinstance(char, str) for char in ex)


def test_get_exemplars_invalid_option():
    """
    Test the get_exemplars function with an invalid option.
    """
    ex = exemplars.get_exemplars("en", "main", 999)
    assert isinstance(ex, list)
    assert len(ex) > 0
    assert all(isinstance(char, str) for char in ex)


def test_get_icu_version():
    """
    Test the get_icu_version function.
    """
    version = exemplars.get_icu_version()
    assert isinstance(version, str)
    assert len(version) > 0


def test_get_locale_name():
    """
    Test the get_locale_name function with various locale IDs.
    """
    assert exemplars.get_locale_name("en") == "English"
    assert exemplars.get_locale_name("fr-CA") == "French (Canada)"
    assert exemplars.get_locale_name("zh-Hans") == "Chinese (Simplified)"
    assert exemplars.get_locale_name("es-ES") == "Spanish (Spain)"
    assert (
        exemplars.get_locale_name("bs-Cyrl-BA")
        == "Bosnian (Cyrillic, Bosnia & Herzegovina)"
    )


def test_get_number_symbols():
    """
    Test the get_number_symbols function with various locales.
    """
    symbols = exemplars.get_number_symbols("en")
    assert isinstance(symbols, dict)
    assert symbols["decimal"] == "."
    assert symbols["group"] == ","
    assert symbols["percent"] == "%"
    assert symbols["zero_digit"] == "0"
    assert symbols["digit"] == "#"
    assert symbols["pattern_digit"] == ";"
    assert symbols["plus_sign"] == "+"
    assert symbols["minus_sign"] == "-"
    assert symbols["exponential"] == "E"
    assert symbols["per_mille"] == "‰"
    assert symbols["infinity"] == "∞"
    assert symbols["nan"] == "NaN"
    assert symbols["digits"] == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols_ar = exemplars.get_number_symbols("ar")
    assert isinstance(symbols_ar, dict)
    assert symbols_ar["decimal"] == "."
    assert symbols_ar["group"] == ","
    assert symbols_ar["percent"] == "‎%‎"
    assert symbols_ar["zero_digit"] == "0"
    assert symbols_ar["digit"] == "#"
    assert symbols_ar["pattern_digit"] == ";"
    assert symbols_ar["plus_sign"] == "‎+"
    assert symbols_ar["minus_sign"] == "‎-"
    assert symbols_ar["exponential"] == "E"
    assert symbols_ar["per_mille"] == "‰"
    assert symbols_ar["infinity"] == "∞"
    assert symbols_ar["nan"] == "ليس رقمًا"
    assert symbols_ar["digits"] == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def test_get_currency():
    """
    Test the get_currency function with various locales.
    """
    assert exemplars.get_currency("en_US") == "$"
    assert exemplars.get_currency("fr_FR") == "€"
    assert exemplars.get_currency("ja_JP") == "￥"
    assert exemplars.get_currency("en_GB") == "£"


def test_get_currency_no_territory():
    """
    Test the get_currency function with a locale that has no territory.
    """
    assert exemplars.get_currency("en") is None


def test_get_currency_exception():
    """
    Test the get_currency function when an exception is raised.
    """
    with patch("exemplars.icu.Locale", side_effect=Exception("Test Exception")):
        assert exemplars.get_currency("en_US") is None


def test_get_currency_invalid():
    """
    Test the get_currency function with an invalid locale.
    """
    assert exemplars.get_currency("un_KN_OWN") is None


def test_categorize_exemplars_with_sequences():
    """
    Test the categorize_exemplars function with a mix of single characters and sequences.
    """
    exemplars_list = ["a", "b", "abc", "def"]
    result = exemplars.categorize_exemplars(exemplars_list)
    assert result["single_chars"] == ["a", "b"]
    assert result["sequences"] == ["abc", "def"]


def test_categorize_exemplars_empty():
    """
    Test the categorize_exemplars function with an empty list.
    """
    exemplars_list = []
    result = exemplars.categorize_exemplars(exemplars_list)
    assert result["single_chars"] is None
    assert result["sequences"] is None


def test_categorize_exemplars_only_sequences():
    """
    Test the categorize_exemplars function with only sequences.
    """
    exemplars_list = ["abc", "def"]
    result = exemplars.categorize_exemplars(exemplars_list)
    assert result["single_chars"] is None
    assert result["sequences"] == ["abc", "def"]


def test_categorize_exemplars_only_single_chars():
    """
    Test the categorize_exemplars function with only single characters.
    """
    exemplars_list = ["a", "b", "c"]
    result = exemplars.categorize_exemplars(exemplars_list)
    assert result["single_chars"] == ["a", "b", "c"]
    assert result["sequences"] is None


def test_generate_locale_data():
    """
    Test the generate_locale_data function.
    """
    data = exemplars.generate_locale_data()

    # Check that the ICU version is included
    assert "icu_version" in data

    # Check that locales and display names are dictionaries
    assert isinstance(data["locales"], dict)
    assert isinstance(data["display_names"], dict)

    # Spot check that some known locales are included
    assert "en_US" in data["locales"]
    assert "fr_FR" in data["locales"]

    # Check the structure of the data for a known locale
    en_us_data = data["locales"]["en_US"]
    assert "main" in en_us_data
    assert "auxiliary" in en_us_data
    assert "punctuation" in en_us_data
    assert "case_insensitive" in en_us_data
    assert "case_mapping" in en_us_data
    assert "numbers" in en_us_data
    assert "currency" in en_us_data

    # Spot check that display names are correct
    assert data["display_names"]["en_US"] == "English (United States)"
    assert data["display_names"]["fr_FR"] == "French (France)"


def test_validate_json_data_valid(valid_data):
    """
    Test the validate_json_data function with valid data.
    """
    # Read the actual schema.json file
    schema_path = Path(__file__).parent.parent / "schema.json"
    with schema_path.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    # This should not raise any exceptions
    exemplars.validate_json_data(valid_data)


def test_validate_json_data_missing_fields(invalid_data_missing_field):
    """
    Test the validate_json_data function with data missing required fields.
    """
    # Read the actual schema.json file
    schema_path = Path(__file__).parent.parent / "schema.json"
    with schema_path.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    with pytest.raises(SystemExit):
        exemplars.validate_json_data(invalid_data_missing_field)


def test_validate_json_data_type_mismatch(invalid_data_type_mismatch):
    """
    Test the validate_json_data function with data having type mismatches.
    """
    # Read the actual schema.json file
    schema_path = Path(__file__).parent.parent / "schema.json"
    with schema_path.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    with pytest.raises(SystemExit):
        exemplars.validate_json_data(invalid_data_type_mismatch)


def test_validate_json_data_missing_schema():
    """
    Test the validate_json_data function when the schema file is missing.
    """
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(SystemExit):
            exemplars.validate_json_data({})


def test_validate_json_data_general_exception():
    """
    Test the validate_json_data function when a general exception occurs.
    """
    with patch("builtins.open", side_effect=Exception("Test Exception")):
        with pytest.raises(SystemExit):
            exemplars.validate_json_data({})


def test_write_json_files():
    """
    Test the write_json_files function for successful file writing.
    """
    data = {"test": "data"}
    output_dir = "test_output"
    with patch("pathlib.Path.mkdir") as mock_mkdir, patch(
        "pathlib.Path.open", mock_open()
    ) as mock_file, patch("gzip.GzipFile", mock_open()) as mock_gzip:
        exemplars.write_json_files(data, output_dir)
        mock_mkdir.assert_called_once()
        assert mock_file.call_count == 2
        assert mock_gzip.call_count == 1


def test_write_json_files_exception():
    """
    Test the write_json_files function when an exception occurs during file writing.
    """
    data = {"test": "data"}
    output_dir = "test_output"
    with patch("pathlib.Path.mkdir", side_effect=Exception("Test Exception")):
        with pytest.raises(Exception):
            exemplars.write_json_files(data, output_dir)
