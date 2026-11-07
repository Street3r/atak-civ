# Finnish localization (fi)

Finnish translation of the ATAK-CIV user interface and MIL-STD-2525 symbol names. The target users are Finnish Defence Forces (Puolustusvoimat, PV) conscripts and reservists, so military terms follow PV publications where they exist (see [GLOSSARY.md](GLOSSARY.md) and [Sources](#sources)).

## Files

| Path | Content |
|---|---|
| `atak/ATAK/app/src/main/res/values-fi/strings.xml` | 5652 of 5819 translatable strings (ATAK-CIV 5.5.1.10) |
| `atak/ATAK/app/src/main/res/values-fi/arrays.xml` | 13 string arrays whose items are literal text |
| `localization/fi/GLOSSARY.md` | Terminology with sources |
| `localization/fi/tools/l10n_fi.py` | Helper: `dump`, `build`, `check` |

The values-fi files are the result. They can be edited directly. Run the check afterwards.

## Checking

```bash
python3 localization/fi/tools/l10n_fi.py check
```

The check compares `values-fi` with the English source and reports:

- unknown keys
- format placeholders that differ (`%s`, `%1$d` …)
- escaping errors (`'`, `"`, `@`, `?`, `&`)
- line breaks (`\n`) or escaped leading and trailing spaces (` `) that differ from the English
- XML errors
- string arrays whose item count differs

## What is left in English, and why

- **Product, protocol and format names.** For example ATAK, TAK Server, CoT, KML, DTED, MISB.
- **CAS 9-line / 5-line readouts and brevity codes.** These are used verbatim in procedures.
- **Strings that the code uses as data.** The Java code compares, parses or stores the displayed text, so translating these strings would break a feature:
  - role names (`team_member` … `k9`)
  - MEDEVAC line 5 (`litter_x`, `ambulance_x`)
  - `preferences_text102`
  - `go_caps`

  They are listed at the end of the translator's keep list and can be translated after the code stores fixed values instead of display text.
- **MEDEVAC line 4, 7 and 9 choices.** The code parses these by their English first letter and by the word "Other". The Finnish labels keep that letter (for example "N – Ei mitään") and the text "Other (Specify)".
- **METOC symbols.**

## Decisions

- Overlays = *Karttatasot*.
- Hostile = *vihollinen*.
- Mils are labelled *Piirut (6400)*. ATAK uses the NATO 6400 circle, and PV is moving to the same standard.
- Size classes follow the PV bar rule (SML, item 22) for tanks and weapons: Light / Medium / Heavy = *kevyt / raskas / järeä*. Mortars, machine guns, grenade launchers and AD missiles keep the NATO scale *kevyt / keskiraskas / raskas* (see the glossary).
- Where two PV sources disagree, the newer one is used. Open questions are marked *open* in the glossary.

## Known limitations (upstream code)

Some text cannot be fully localized without code changes:

- **Hard-coded English.** Examples:
  - " meters." in the LRF message
  - "Begin" / "Process" in the product information wizard
  - plural "s" appended to counts
  - MEDEVAC dialog titles
  - `NorthReference.getName()` inserted into sentences
- **Sentences split across keys or completed in Java.** For example, one half of a quotation mark pair comes from the Java code.
- **Display text used as data** (see above).
- **One key used for two meanings.** For example, `start` is both a button and a label, and `dismiss` is both "acknowledge" and "close".

## Sources

The glossary abbreviations refer to these public publications.

**PV publications**

- Sotilasmerkistö ja -lyhenteet (2005)
- Taistelijan opas (2013)
- Sotilaan käsikirja (2024 and 2026 editions)
- Johtajan käsikirja (2022)
- Jääkärijoukkueen ja -ryhmän käsikirja (2018)
- Merisotilaan käsikirja (2010)
- Suojelutoiminnan käsikirja (2022)
- Suojaamisen käsikirja (2021)
- Suojanedistämisen käsikirja (2021)
- Mittaustoiminnan käsikirja (2015)
- Ilmatorjunnan ampumaopin käsikirja (2017)
- Huoltojoukkueen käsikirja (2017)
- Viestimies 4/2017
- Talvikoulutusopas (2004)
- Yleinen ase- ja asejärjestelmäopas (2001)
- Taisteluensiapu-opetuspaketti (2019, Pääesikunta)
- Ohje R-alueelle lentämisestä (Pääesikunta)
- AJP-01 Naton yhteinen doktriini (Finnish edition)

**Other publications**

- Kybertaistelu 2020 (Maanpuolustuskorkeakoulu, 2014)
- Hyytiäinen: Sotilaallisten maastoanalyysien metamalli (Maanpuolustuskorkeakoulu, 2003)

**Glossaries**

- Nato-sanasto (Valtioneuvosto, 2025)
- Kyberturvallisuuden sanasto (2018)
- Kokonaisturvallisuuden sanasto (2017)
- Pelastusalan sanasto (2026)
- Geoinformatiikan sanasto (4th ed.)
- Microsoft terminology (fi-FI)

## Testing

1. Build the app as usual.
2. Set the device language to Finnish (suomi).
3. Check in particular:
   - the 2525 symbol palette names
   - MEDEVAC 9-line save, reopen and readout
   - the narrow fields: polar coordinate spinners, the track history sort header, and the Data Package date column
