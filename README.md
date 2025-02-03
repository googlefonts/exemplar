# Exemplar

![API version](https://img.shields.io/badge/API%20version-v1-blue)
![GitHub Release](https://img.shields.io/github/v/release/googlefonts/exemplar)
![ICU version](https://img.shields.io/badge/dynamic/json?url=https://cdn.jsdelivr.net/gh/googlefonts/exemplar@1/api/data.json&query=%24.icu_version&label=ICU%20version)

## About

The Exemplar API project JSON endpoints include Unicode CLDR (Common Locale Data Repository) exemplar encoding data by [Unicode locale](https://unicode-org.github.io/icu/userguide/locale/#the-locale-concept). The goal of this project is to provide simple GET client access to localized exemplar encoding data in a public, widely-supported JSON format endpoint.

This project leverages the [ICU (International Components for Unicode) library](https://unicode-org.github.io/icu/) to distribute software internationalization data that are consistent with the latest Unicode data standards.

## Exemplar Data Categories

The following data are categorized by [Unicode locale](https://unicode-org.github.io/icu/userguide/locale/#the-locale-concept) tag:

- **Main Exemplars** [main]
  - Minimum base set of characters used in the language. Note: only includes lowercase for languages that support different case forms. [CLDR documentation](https://cldr.unicode.org/translation/core-data/exemplars#exemplar-characters)
  - Example [Engish (United States)]: abcdefghijklmnopqrstuvwxyz
  - Example [Vietnamese (Vietnam)]: aáàăắằẵẳâấầẫẩãảạặậbcdđeéèêếềễểẽẻẹệghiíìĩỉịklmnoóòôốồỗổõỏơớờỡởợọộpqrstuúùũủưứừữửựụvxyýỳỹỷỵ
  - Example [Hindi (India)]:  ़ँंःॐअआइईउऊऋऌऍएऐऑओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहऽािीुूृॅेैॉोौ्
- **Auxiliary Exemplars** [auxiliary]
  - Foreign borrowings and specialized usage exemplars in the language. [CLDR documentation](https://cldr.unicode.org/translation/core-data/exemplars#exemplar-characters)
  - Example [Engish (United States)]: áàăâåäãāæçéèĕêëēíìĭîïīñóòŏôöøōœúùŭûüūÿ
  - Example [Vietnamese (Vietnam)]: fjwz
  - Example [Hindi (India)]: ‌‍ॄ
- **Case-insensitive Exemplars** [case_insensitive]
  - Defines exemplar equivalence, irrespective of case, in the language.
  - Example [Engish (United States)]: aAbBcCdDeEfFgGhHiIjJkKKlLmMnNoOpPqQrRsSſtTuUvVwWxXyYzZ
  - Example [Vietnamese (Vietnam)]: aAáÁàÀăĂắẮằẰẵẴẳẲâÂấẤầẦẫẪẩẨãÃảẢạẠặẶậẬbBcCdDđĐeEéÉèÈêÊếẾềỀễỄểỂẽẼẻẺẹẸệỆgGhHiIíÍìÌĩĨỉỈịỊkKKlLmMnNoOóÓòÒôÔốỐồỒỗỖổỔõÕỏỎơƠớỚờỜỡỠởỞợỢọỌộỘpPqQrRsSſtTuUúÚùÙũŨủỦưƯứỨừỪữỮửỬựỰụỤvVxXyYýÝỳỲỹỸỷỶỵỴ
  - Example [Hindi (India)]:  ़ँंःॐअआइईउऊऋऌऍएऐऑओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहऽािीुूृॅेैॉोौ्
- **Case-mapped Exemplars** [case_mapping]
  - Defines the relationship between uppercase, lowercase and title case exemplars in the language for ICU case mapping. [ICU documentation](https://unicode-org.github.io/icu/userguide/transforms/casemappings.html)
  - Example [Engish (United States)]: aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ
  - Example [Vietnamese (Vietnam)]: aAáÁàÀăĂắẮằẰẵẴẳẲâÂấẤầẦẫẪẩẨãÃảẢạẠặẶậẬbBcCdDđĐeEéÉèÈêÊếẾềỀễỄểỂẽẼẻẺẹẸệỆgGhHiIíÍìÌĩĨỉỈịỊkKlLmMnNoOóÓòÒôÔốỐồỒỗỖổỔõÕỏỎơƠớỚờỜỡỠởỞợỢọỌộỘpPqQrRsStTuUúÚùÙũŨủỦưƯứỨừỪữỮửỬựỰụỤvVxXyYýÝỳỲỹỸỷỶỵỴ
  - Example [Hindi (India)]:  ़ँंःॐअआइईउऊऋऌऍएऐऑओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसहऽािीुूृॅेैॉोौ्
- **Punctuation Exemplars** [punctuation]
  - Punctuation customarily used with the language. [CLDR documentation](https://cldr.unicode.org/translation/core-data/exemplars#exemplar-characters)
  - Example [Engish (United States)]: -‐‑–—,;:!?.…'‘’"“”()[]§@*/&#†‡′″
  - Example [Vietnamese (Vietnam)]: -‐‑–—,;:!?.…'‘’"“”()[]§@*/&#†‡′″
  - Example [Hindi (India)]: -‐‑–—,;:!?.…।॥'‘’"“”()[]§@*/#†‡′″॰
- **Numbers Exemplars** [numbers]
  - The number digits used in the locale.
  - Example [Engish (United States)]: 0123456789
  - Example [Vietnamese (Vietnam)]: 0123456789
  - Example [Hindi (India)]: 0123456789
  - Example [Arabic (Egypt)]: ٠١٢٣٤٥٦٧٨٩
- **Currency Exemplars** [currency]
  - The currency symbol used for formatting currency numbers in the locale.
  - Example [Engish (United States)]: $
  - Example [Vietnamese (Vietnam)]: ₫
  - Example [Hindi (India)]: ₹

Additional data including locale tag display names and ICU library definition version are available.

### Endpoints

![jsDelivr Major Version Release Status](https://img.shields.io/website?url=https://cdn.jsdelivr.net/gh/googlefonts/exemplar@1/api/data.json&style=for-the-badge&logo=jsdelivr&label=v1%20Major%20API)
![jsDelivr Current Release Status](https://img.shields.io/website?url=https://cdn.jsdelivr.net/gh/googlefonts/exemplar@1.0.0/api/data.json&style=for-the-badge&logo=jsdelivr&label=v1.0.0%20API)

#### Latest Release

```
https://cdn.jsdelivr.net/gh/googlefonts/exemplar@1/api/data.json
```

#### Endpoint Versioning

The Exemplar API follows [semantic versioning](https://semver.org/) principles. Backwards compatibility is assured within major version releases. For example, all `v1` endpoints will remain backwards compatible with any changes or additions made across the `v1.x.x` releases.

The root endpoint is:

```
https://cdn.jsdelivr.net
```

Versioned endpoint construction uses the following syntax:

```
/gh/googlefonts/exemplar@[VERSION]/api/data.json
```

where `[VERSION]` represents a repository semantic version release number git tag, or git commit hash.

#### Major Version Tracking Release

Automatically update to new point releases across a major release cycle by using the major release number only:

```
/gh/googlefonts/exemplar@1/api/data.json
```

#### Pinned Version Release

Define a pinned point release with a full release version number in `MAJOR.MINOR.PATCH` syntax:

```
/gh/googlefonts/exemplar@1.0.0/api/data.json
```

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
      "punctuation": ["punct1", "punct2"],
      "case_insensitive": {
        "single_chars": ["char1", "char2"],
        "sequences": ["seq1", "seq2"]
      },
      "case_mapping": {
        "single_chars": ["char1", "char2"],
        "sequences": ["seq1", "seq2"]
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
      "currency": "currency_symbol"
    }
  },
  "display_names": {
    "locale_id": "Locale Display Name"
  }
}
```

**Note:** The following fields can have null values when data do not exist or are not available:
- `punctuation`
- `case_insensitive.single_chars`
- `case_insensitive.sequences`
- `case_mapping.single_chars`
- `case_mapping.sequences`
- `currency`

## Example Usage

There are demo scripts in the [`examples` directory](examples/) that demonstrate how to use the Exemplar project JSON data. These examples include:

- [**currency.py**](examples/currency.py): Demonstrates how to extract and print localized currency symbols and their Unicode codepoints from the JSON data.
- [**locsets.py**](examples/locsets.py): Demonstrates how to extract and print locale-specific exemplar character sets from the JSON data. This script takes a locale ID as a command-line argument and reports the main, auxiliary, case-insensitive, case-mapping, numbers, punctuation, and currency exemplars for the specified locale.

## Development

The JSON data are generated with the [`exemplars.py`](exemplars.py) script in the root of the repository.  The [schema.json](schema.json) file defines the JSON structure for validation testing at runtime.  The Python dependencies are defined in the [requirements.txt](requirements.txt) file.

The JSON data can be generated with the following command:

```
$ python exemplars.py
```

JSON files write to the `api` sub-directory.

## Changelog

Please see the [CHANGELOG.md](CHANGELOG.md) file in the root of the repository.

## Licenses

The source code in this repository is licensed under [the Apache License, Version 2.0](LICENSE.md).

The CLDR data are redistributed under [the Unicode License v3](https://www.unicode.org/license.txt).