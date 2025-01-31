import json
import sys
from pathlib import Path
from typing import Dict, List


def get_currency_symbols(filepath: str) -> Dict[str, Dict[str, List[str]]]:
    """
    Retrieve currency symbols from the exemplars JSON file.

    This function reads a JSON file containing locale data and extracts the currency symbols
    for each locale. It also converts the currency strings to their corresponding Unicode codepoints.

    Parameters:
    filepath (str): The path to the JSON file.

    Returns:
    Dict[str, Dict[str, List[str]]]: A dictionary of localized currency symbols.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)
    except json.JSONDecodeError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)

    currency_symbols = {}
    for locale, locale_data in data["locales"].items():
        if locale_data.get("currency"):
            display_name = data["display_names"].get(locale, locale)
            symbol = locale_data["currency"]
            unicode_codepoints = [f"U+{ord(char):04X}" for char in symbol]
            currency_symbols[locale] = {
                "symbol": symbol,
                "unicode_codepoints": unicode_codepoints,
                "display_name": display_name,
            }
    return currency_symbols


def print_currency_symbols(currency_symbols: Dict[str, Dict[str, List[str]]]) -> None:
    """
    Print the currency symbols with their Unicode codepoints and display names.

    Parameters:
    currency_symbols (Dict[str, Dict[str, List[str]]]): The dictionary of currency symbols to print.
    """
    print(f"{'Locale':<10} {'Display Name':<30} {'Symbol':<10} {'Unicode Codepoints'}")
    print("=" * 70)
    for locale, locale_data in currency_symbols.items():
        codepoints_str = " ".join(locale_data["unicode_codepoints"])
        print(
            f"{locale:<10} {locale_data['display_name']:<30} {locale_data['symbol']:<10} {codepoints_str}"
        )


if __name__ == "__main__":
    filepath = Path(__file__).parent.parent / "docs" / "v1" / "icu_exemplars-min.json"
    currency_symbols = get_currency_symbols(str(filepath))
    print_currency_symbols(currency_symbols)
