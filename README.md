# Exemplar

![API version](https://img.shields.io/badge/API%20version-v1-blue)
![GitHub Release](https://img.shields.io/github/v/release/googlefonts/exemplar)
![ICU version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgooglefonts.github.io%2Fexemplar%2Fv1%2Fdata.json&query=%24.icu_version&label=ICU%20version)

## About

The Exemplar API project JSON endpoints include Unicode CLDR (Common Locale Data Repository) exemplar, number, punctuation and currency encoding data by BCP 47 locale tag. The goal of this project is to provide easy client access to localized encoding data in a widely supported JSON format.

This project leverages the ICU (International Components for Unicode) library to generate localization data that are consistent with the latest Unicode data standards.

## Data

The JSON API endpoints include the following data:
- **ICU Version**: the ICU library version used to generate the data.
- **Exemplar Characters**: Localized exemplar encoding sets, categorized into main, auxiliary, case-insensitive, & case-mapped types. Separate fields are defined for single characters and sequences, where sequences are defined as strings of multiple exemplar encodings as defined by the ICU library.
- **Number and Number Symbols**: Localized numbers and number symbols used for formatting numbers in various locales, including decimal separators, grouping separators, percent signs, and more.
- **Punctuation**: Localized punctuation marks.
- **Currency Symbols**: Localized currency symbols or currency strings
- **Locale Tag Display Names**: Human-friendly locale names by locale tag.

### Versioning

The current Exemplar API version is `v1`.

The Exemplar API follows [semantic versioning](https://semver.org/) principles. Backwards compatibility is assured within major version releases. For example, all `v1` endpoints will remain backwards compatible with any changes or additions made within the `v1` version.

The API version is defined in the endpoint URL with the following syntax:

```
https://googlefonts.github.io/exemplar/[VERSION]/data.json
```

### Endpoints

The JSON data can be accessed by GET request to one of the following endpoints:

- **GitHub CDN**: `https://googlefonts.github.io/exemplar/v1/data.json`
- **Netlify CDN**: `https://googlefonts-exemplar.netlify.app/v1/data.json` 

### Endpoints Status

![GitHub CDN Build Status](https://img.shields.io/github/actions/workflow/status/googlefonts/exemplar/pages%2Fpages-build-deployment?branch=main&style=for-the-badge&logo=github&label=GitHub%20Build)
![GitHub API Status](https://img.shields.io/website?url=https%3A%2F%2Fgooglefonts.github.io%2Fexemplar%2Fv1%2Fdata.json&style=for-the-badge&logo=github&label=GitHub%20API%20Status)


![Netlify CDN Build Status](https://img.shields.io/netlify/dfd069d4-e4c6-42c3-aee5-d4115fd2bd37?logo=netlify&style=for-the-badge&label=Netlify%20Build)
![Netlify API Status](https://img.shields.io/website?url=https%3A%2F%2Fgooglefonts-exemplar.netlify.app%2Fv1%2Fdata.json&style=for-the-badge&logo=netlify&label=Netlify%20API%20Status)


### Data Structure

The JSON data follow a [repository-defined schema](schema.json). Below is an overview of the structure:

#### Exemplar JSON

```json
{
  "icu_version": "version_string",
  "locales": {
    "locale_id": {
      "main": {
        "single_chars": ["char1", "char2"],
        "sequences": ["seq1", "seq2"]
      },
      "auxiliary": {
        "single_chars": ["char1", "char2"],
        "sequences": ["seq1", "seq2"]
      },
      "punctuation": ["punct1", "punct2"],  // might be null
      "case_insensitive": {
        "single_chars": ["char1", "char2"],  // might be null
        "sequences": ["seq1", "seq2"]  // might be null
      },
      "case_mapping": {
        "single_chars": ["char1", "char2"],  // might be null
        "sequences": ["seq1", "seq2"]  // might be null
      },
      "numbers": {
        "decimal": "decimal_char",
        "group": "group_char",
        "percent": "percent_char",
        "zero_digit": "zero_digit_char",
        "digit": "digit_char",
        "pattern_digit": "pattern_digit_char",
        "plus_sign": "plus_sign_char",
        "minus_sign": "minus_sign_char",
        "exponential": "exponential_char",
        "per_mille": "per_mille_char",
        "infinity": "infinity_char",
        "nan": "nan_char",
        "digits": ["digit1", "digit2"]
      },
      "currency": "currency_symbol"  // might be null
    }
  },
  "display_names": {
    "locale_id": "Locale Display Name"
  }
}
```

## Example Usage

### Python

Here is an example of fetching the JSON with the requests library in Python:

```python
import requests

url = 'https://googlefonts.github.io/exemplar/v1/data.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error fetching exemplar characters: {response.status_code}")
```

## Examples

There are demo scripts in the [`examples` directory](examples/) that demonstrate how to use the Exemplar project JSON data. These examples include:

- [**currency.py**](examples/currency.py): Demonstrates how to extract and print localized currency symbols and their Unicode codepoints from the JSON data.

## Development

The JSON data are generated with the [`exemplars.py`](exemplars.py) script in the root of the repository.  The [schema.json](schema.json) file defines the JSON structure for validation testing at runtime.  The Python dependencies are defined in the [requirements.txt](requirements.txt) file.

The JSON data can be generated with the following command:

```
$ python exemplars.py
```

JSON files write to the `docs` sub-directory. The output directory name is required by GitHub Pages and should not be changed.

## Changelog

Please see the [CHANGELOG.md](CHANGELOG.md) file in the root of the repository.

## Licenses

The source code in this repository is licensed under [the Apache License, Version 2.0](LICENSE.md).

The CLDR data are redistributed under [the Unicode License v3](https://www.unicode.org/license.txt).