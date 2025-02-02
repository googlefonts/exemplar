import json
import sys
from pathlib import Path


def fetch_locale_data() -> dict:
    """
    Fetches the locale data from the local JSON file.

    Returns:
        dict: The data from the JSON file, or an empty dictionary if an error occurs.
    """
    file_path = Path(__file__).resolve().parent.parent / "api" / "data.json"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON")
        return {}


def report_locale_data(locale_id: str, data: dict):
    """
    Reports the locale-specific data for the given locale ID.

    Args:
        locale_id (str): The locale identifier.
        data (dict): The data from the JSON file.

    Prints the locale-specific data in separate sections for main, auxiliary,
    case-insensitive, case-mapping, numbers, punctuation, and currency exemplars.
    """
    locale_data = data.get("locales", {}).get(locale_id, {})
    display_name = data.get("display_names", {}).get(locale_id, "Unknown Locale")

    if not locale_data:
        print(f"No data available for locale ID: {locale_id}")
        return

    main_data = locale_data.get("main", {}).get("single_chars", [])
    aux_data = locale_data.get("auxiliary", {}).get("single_chars", [])
    ci_data = locale_data.get("case_insensitive", {}).get("single_chars", [])
    cm_data = locale_data.get("case_mapping", {}).get("single_chars", [])
    digit_data = locale_data.get("numbers", {}).get("digits", [])
    punc_data = locale_data.get("punctuation", [])
    currency_data = locale_data.get("currency", "")

    print(f"{locale_id}: {display_name}\n")
    print("--- Main Exemplars ---")
    print("".join(map(str, main_data)))
    print("\n--- Auxiliary Exemplars ---")
    print("".join(map(str, aux_data)))
    print("\n--- Case-Insensitive Exemplars ---")
    print("".join(map(str, ci_data)))
    print("\n--- Case-Mapping Exemplars ---")
    print("".join(map(str, cm_data)))
    print("\n--- Number Exemplars ---")
    print("".join(map(str, digit_data)))
    print("\n--- Punctuation Exemplars ---")
    print("".join(map(str, punc_data)))
    print("\n--- Currency Exemplars ---")
    print(currency_data if currency_data else "")


def main():
    """
    Main function to execute the script. Takes a locale ID as a command-line argument
    and reports the locale-specific data.
    """
    if len(sys.argv) != 2:
        print("Usage: python locsets.py <locale_id>")
        sys.exit(1)

    locale_id = sys.argv[1]
    data = fetch_locale_data()

    report_locale_data(locale_id, data)


if __name__ == "__main__":
    main()
