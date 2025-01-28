# Exemplar

## About

The Exemplar project JSON endpoints redistribute Unicode CLDR (Common Locale Data Repository) exemplar, number, and punctuation encoding data by BCP 47 locale tag. The goal of this project is to provide easy client access to localized encoding requirements data for font development teams.

This project leverages the ICU (International Components for Unicode) library to generate data that are consistent with the latest Unicode data standards.

## Data

The JSON files include the following data:
- **ICU Version**: the ICU library version used to generate the data.
- **Exemplar Characters**: Localized exemplar encoding sets, categorized into main, auxiliary, case-insensitive, case-mapped types. Separate fields are defined for single characters and sequences, where sequences are defined as strings of multiple exemplar encodings as defined by the ICU library.
- **Number and Number Symbols**: Localized numbers and number symbols used for formatting numbers in various locales, including decimal separators, grouping separators, percent signs, and more.
- **Punctuation**: Localized punctuation marks.
- **Locale Tag Display Names**: 

## API

### Endpoints

The JSON data can be accessed at the following endpoints:

- **Pretty-printed JSON**: `https://googlefonts.github.io/exemplar/icu_exemplars-min.json`
- **Minified JSON**: `https://googlefonts.github.io/exemplar/icu_exemplars-min.json`
- **Minified JSON, gzip compressed**: `https://googlefonts.github.io/exemplar/icu_exemplars-min.json.gz`

The JSON endpoints above are ordered largest to smallest by file size.

### Data Structure

The JSON data follow a [repository-defined schema](schema.json). Below is an overview of the structure:

#### Exemplar JSON

```json
{
  "icu_version": "version_string",
  "locales": {
    "[locale_id]": {
      "main": {
        "single_chars": ["char1", "char2", ...],
        "sequences": ["sequence1", "sequence2", ...]
      },
      "auxiliary": {
        "single_chars": ["char1", "char2", ...],
        "sequences": ["sequence1", "sequence2", ...]
      },
      "punctuation": ["char1", "char2", ...],
      "case_insensitive": {
        "single_chars": ["char1", "char2", ...],
        "sequences": ["sequence1", "sequence2", ...]
      },
      "case_mapping": {
        "single_chars": ["char1", "char2", ...],
        "sequences": ["sequence1", "sequence2", ...]
      },
      "numbers": {
        "decimal": "char",
        "group": "char",
        "percent": "char",
        "zero_digit": "char",
        "digit": "char",
        "pattern_digit": "char",
        "plus_sign": "char",
        "minus_sign": "char",
        "exponential": "char",
        "per_mille": "char",
        "infinity": "char",
        "nan": "char",
        "digits": ["char0", "char1", ...]
      }
    }
  },
  "display_names": {
    "[locale_id]": "display_name"
  }
}
```

## Example Usage

### Python

#### Minified JSON

Here is an example of fetching the minified JSON file with the requests library in Python:

```python
import requests

url = 'https://googlefonts.github.io/exemplar/icu_exemplars-min.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error fetching exemplar characters: {response.status_code}")
```

#### gzip Compressed JSON

And here is an example of fetching the gzip compressed JSON file:


```python
import gzip
import json

import requests

url = 'https://googlefonts.github.io/exemplar/icu_exemplars-min.json.gz'
response = requests.get(url)

if response.status_code == 200:
    compressed_content = response.content
    decompressed_content = gzip.decompress(compressed_content)
    data = json.loads(decompressed_content.decode('utf-8'))
    print(data)
else:
    print(f"Error fetching compressed exemplar characters: {response.status_code}")
```

## Development

The JSON data are generated with the [`exemplars.py`](exemplars.py) script in the root of the repository.  The [schema.json](schema.json) file defines the JSON structure for validation testing at runtime.

## Changelog

Please see the [CHANGELOG.md](CHANGELOG.md) file in the root of the repository.

## Licenses

The source code in this repository is licensed under [the Apache License, Version 2.0](LICENSE.md).

The CLDR data are redistributed under [the Unicode License v3](https://www.unicode.org/license.txt).