# Copyright 2025 Google, LLC

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import icu
import json
import sys
import jsonschema
import gzip
from pathlib import Path
from typing import List, Dict, Any

# API version constant
API_VERSION = "v1"

# Mapping of exemplar types to their corresponding integer values used by ICU
EXEMPLAR_TYPES: Dict[str, int] = {
    "main": 0,
    "auxiliary": 1,
    "index": 2,
    "punctuation": 3,
}

# List of valid options for exemplar sets
OPTIONS: List[int] = [0, 2, 4]


def normalize_locale_id(localeID: str) -> str:
    """
    Normalize the locale ID by replacing '-' with '_'.

    Parameters:
    localeID (str): The locale identifier.

    Returns:
    str: Normalized locale identifier.
    """
    return localeID.replace("-", "_")


def get_exemplars(localeID: str, extype: str = "main", option: int = 0) -> List[str]:
    """
    Retrieve exemplars for a given locale and type.

    Parameters:
    localeID (str): The locale identifier.
    extype (str): The type of exemplars to retrieve (main, auxiliary, index, punctuation).
    option (int): The option for exemplar set.

    Returns:
    list: Sorted list of exemplars.
    """
    option = option if option in OPTIONS else 0
    extype = extype.lower() if extype.lower() in EXEMPLAR_TYPES else None
    localeID = normalize_locale_id(localeID)
    if localeID in icu.Collator.getAvailableLocales():
        collator = icu.Collator.createInstance(icu.Locale(localeID))
    else:
        collator = icu.Collator.createInstance(icu.Locale.getRoot())
    type = EXEMPLAR_TYPES[extype]
    if localeID not in icu.Locale.getAvailableLocales():
        raise ValueError(
            f"Specified Locale {localeID} not available in icu4c {get_icu_version()}"
        )
    try:
        return sorted(
            icu.LocaleData(localeID).getExemplarSet(option, type),
            key=collator.getSortKey,
        )
    except icu.ICUError as e:
        # Note: logs and returns an empty list when ICUError encountered
        sys.stderr.write(f"{e}")
        return []
    except Exception as e:
        sys.stderr.write(f"{e}")
        sys.exit(1)


def get_icu_version() -> str:
    """
    Retrieve the ICU version.

    Returns:
    str: ICU version.
    """
    return icu.ICU_VERSION


def get_locale_name(localeID: str) -> str:
    """
    Retrieve the display name for a given locale.

    Parameters:
    localeID (str): The locale identifier.

    Returns:
    str: Display name of the locale.
    """
    return icu.Locale(localeID).getDisplayName()


def get_number_symbols(localeID: str) -> Dict[str, Any]:
    """
    Retrieve number symbols for a given locale.

    Parameters:
    localeID (str): The locale identifier.

    Returns:
    dict: Dictionary of number symbols.
    """
    locale = icu.Locale(localeID)
    number_format = icu.NumberFormat.createInstance(locale)
    symbols = number_format.getDecimalFormatSymbols()

    # Format numbers 0-9 and extract digits
    digits: List[str] = []
    for i in range(10):
        formatted_number = number_format.format(i)
        for char in formatted_number:
            if char.isdigit():
                digits.append(char)
                break

    return {
        "decimal": symbols.getSymbol(icu.DecimalFormatSymbols.kDecimalSeparatorSymbol),
        "group": symbols.getSymbol(icu.DecimalFormatSymbols.kGroupingSeparatorSymbol),
        "percent": symbols.getSymbol(icu.DecimalFormatSymbols.kPercentSymbol),
        "zero_digit": symbols.getSymbol(icu.DecimalFormatSymbols.kZeroDigitSymbol),
        "digit": symbols.getSymbol(icu.DecimalFormatSymbols.kDigitSymbol),
        "pattern_digit": symbols.getSymbol(
            icu.DecimalFormatSymbols.kPatternSeparatorSymbol
        ),
        "plus_sign": symbols.getSymbol(icu.DecimalFormatSymbols.kPlusSignSymbol),
        "minus_sign": symbols.getSymbol(icu.DecimalFormatSymbols.kMinusSignSymbol),
        "exponential": symbols.getSymbol(icu.DecimalFormatSymbols.kExponentialSymbol),
        "per_mille": symbols.getSymbol(icu.DecimalFormatSymbols.kPerMillSymbol),
        "infinity": symbols.getSymbol(icu.DecimalFormatSymbols.kInfinitySymbol),
        "nan": symbols.getSymbol(icu.DecimalFormatSymbols.kNaNSymbol),
        "digits": digits,
    }


def categorize_exemplars(exemplars: List[str]) -> Dict[str, List[str]]:
    """
    Categorize exemplars into single characters and sequences.

    Parameters:
    exemplars (list): List of exemplars.

    Returns:
    dict: Dictionary with single characters and sequences.
    """
    single_chars = [char for char in exemplars if len(char) == 1]
    sequences = [char for char in exemplars if len(char) > 1]
    return {"single_chars": single_chars, "sequences": sequences}


def generate_locale_data() -> Dict[str, Any]:
    """
    Generate locale data for all available locales.

    Returns:
    dict: Dictionary containing locale data.
    """
    data = {"icu_version": get_icu_version(), "locales": {}, "display_names": {}}
    for localeID in icu.Locale.getAvailableLocales():
        localeID = normalize_locale_id(localeID)
        data["locales"][localeID] = {
            "main": categorize_exemplars(get_exemplars(localeID, "main")),
            "auxiliary": categorize_exemplars(get_exemplars(localeID, "auxiliary")),
            "punctuation": get_exemplars(localeID, "punctuation"),
            "case_insensitive": categorize_exemplars(
                get_exemplars(localeID, "main", 2)
            ),
            "case_mapping": categorize_exemplars(get_exemplars(localeID, "main", 4)),
            "numbers": get_number_symbols(localeID),
        }
        data["display_names"][localeID] = get_locale_name(localeID)
    return data


def validate_json_data(data: Dict[str, Any]) -> None:
    """
    Validate JSON data against the schema.

    Parameters:
    data (dict): JSON data to validate.
    """
    try:
        # Load the JSON schema from a separate file
        with open("schema.json", "r") as f:
            schema = json.load(f)
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        sys.stderr.write(f"JSON data validation error: {e.message}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: {e.message}\n")
        sys.exit(1)


def write_json_files(data: Dict[str, Any], output_dir: str) -> None:
    """
    Write JSON data to files.

    Parameters:
    data (dict): JSON data to write.
    output_dir (str): Directory to write the files to.
    """
    json_dir = Path(output_dir) / API_VERSION
    json_dir.mkdir(parents=True, exist_ok=True)
    minified_data = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    with (json_dir / "icu_exemplars.json").open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    with (json_dir / "icu_exemplars-min.json").open("w", encoding="utf-8") as f:
        f.write(minified_data)
    with gzip.open(json_dir / "icu_exemplars-min.json.gz", "wb", compresslevel=9) as f:
        f.write(minified_data.encode("utf-8"))


def create_json_dump(output_dir: str = "docs") -> None:
    """
    Create a JSON dump of locale data.

    Parameters:
    output_dir (str): Directory to write the files to.
    """
    data = generate_locale_data()
    validate_json_data(data)
    write_json_files(data, output_dir)


if __name__ == "__main__":
    create_json_dump()
