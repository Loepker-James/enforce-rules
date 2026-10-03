## Changelog
All notable changes to this project are documented in this file.
This file should not be updated by contributors.

For migration instructions, see [MIGRATION](docs/migration.md).
If you are upgrading, read the migration guide fully.

---

## 1.0.0 — Created on 2026‑08‑22

### Added
- validate() function
- Original keywords (see [README](README.md))

### Documentation
- Added full keyword reference table to [README](README.md)
- Clarified behavior of must_be_true
- Added examples for all keywords
- Updated installation instructions
- Added Versioning Policy section to [README](README.md)

---

## 1.0.1 — Created on 2026‑08‑29

### Refactored
- Type hints now use object instead of Any
- Fixed inconsistency in [README](README.md)

---

## 1.0.2 — Created on 2026‑08‑29

### Documentation
- Improved newline visibility for [README on PyPI](pypi.org/project/enforce-rules)

---

## 1.0.3 — Created on 2026‑08‑29

### Fixed
- Version numbering in README

---

## 1.1.0 — Created on 2026‑08‑29

### Changed
- "regex" keyword now uses re.search instead of re.fullmatch

### Migration
- See:
  - [Guidelines For Upgrading To](docs/migration.md#upgrading-from-11--to-11)
  - [Guidelines For Downgrading From](docs/migration.md#downgrading-from-11-to-11-)

---

## 1.1.1 — Created on 2026‑08‑29

### Fixed
- Version numbering in [README](README.md)

---

## 1.1.2 — Created on 2026‑08‑29

### Added
- Internal type hint for regex

---

## 1.1.3 — Created on 2026‑08‑29

### Documentation
- Made changelog visible on sources other than GitHub

---

## 1.1.4 — Created on 2026‑08‑30

### Documentation
- Improved newline visibility in README

---

## 2.0.0 — Created on 2026‑08‑30

### Added
- "before_date"
- "after_date"

  (See [Datetime Issue #6](https://github.com/Loepker-James/enforce-rules/issues/6))

---

## 2.0.1 — Created on 2026‑08‑30

### Fixed
- Bugs preventing "regex_flags" from working  
  (Any version before this does not support "regex_flags")

---

## 2.0.2 — Created on 2026‑08‑30

### Documentation
- Fixed README

---

## 2.0.3 — Created on 2026‑08‑30

### Refactored
- Improved internal type hints

---

## 2.0.4 — Created on 2026‑08‑30

### Fixed
- Version number in README

---

## 3.0.0 — Created on 2026‑08‑30

### Added
- New chess‑themed keywords (see Chess Issue #7)

### Documentation
- Improved type hints

---

## 3.0.1 — Created on 2026‑08‑30

### Fixed
- Updated README to version 3.0.1

---

## 3.0.2 — Created on 2026‑08‑30

### Fixed
- README

---

## 3.1.0 — Created on 2026‑09‑02

### Added
- "is_password" (see Password Issue #1)

### Refactored
- Used collections.abc for certain type hints

---

## 3.1.1 — Created on 2026‑09‑04

### Fixed
- Bug in [README](README.md)

---

## 3.1.2 — Created on 2026‑09‑04

### Documentation
- Fixed version number in [README](README.md)

---

## 3.1.3 — Created on 2026‑09‑05

### Documentation
- Added links to docs/ in README

---

## 3.1.4 — Created on 2026‑09‑05

### Added
- Re‑added credits (accidentally removed in 3.1.1)

### Note
- Any [README](README.md) in versions 3.1.1–3.1.4 (except 3.1.4) will not show credits.

---

## 3.1.5 — Created on 2026‑09‑07
**Note: This version is broken.**

### Refactored
- Used typing.Final in validate() for type hinting

---

## 3.1.6 — Created on 2026‑09‑07

### Changed
- Replaced typing.Final with a comment  
- Fixes broken 3.1.5

---

## 3.2.0 — Created on 2026‑09‑08

### Added
- is_valid()

---

## 3.2.1 — Created on 2026‑09‑11

### Refactored
- Added internal type hint in validate()

---

## 3.2.2 — Created on 2026‑09‑11

### Refactored
- Added internal type hint in is_valid()

---

## 3.2.3 — Created on 2026‑09‑12

### Refactored
- Refined type hints

---

## 3.2.4 — Created on 2026‑09‑12

### Refactored
- Used r"\" instead of "\\"

---

## 3.2.5 — Created on 2026‑09‑12

### Documentation
- Added headers in [README](README.md)

---

## 3.2.6 — Created on 2026‑09‑12

### Documentation
- Added header in [README](README.md)

---

## 3.2.7 — Created on 2026‑09‑12

### Refactored
- Added internal type hint

---

## 3.2.8 — Created on 2026‑09‑13

### Refactored
- Added internal type hint

---

## 3.2.9 — Created on 2026‑09‑13

### Refactored
- Added internal type hint

---

## 3.2.10 — Created on 2026‑09‑25

### Fixed
- Raw string bug introduced in [3.2.4](CHANGELOG.md#324--created-on-20260912)

---

## 3.2.11 — Created on 2026‑09‑26

### Added
- validate_call decorator

---

## 3.2.12 — Created on 2026‑09‑27

### Refactored
- Used Field instead of PositiveInt for LengthType type hint

## 3.12.13 — Created on 2026-10-02

### Fixed
- Added requirements.txt in tarball (failed)

## 3.12.14 — Created on 2026-10-02

### Fixed
- Added dependencies in [pyproject.toml](pyproject.toml)

## 3.12.15 — Created on 2026-10-02
Nothing. I wanted to add something but it turns out I didn't add it.

## 3.12.16 — Created on 2026-10-03

### Added
- Claude in Credits
- Dependency Line In [README](README.md)

## 3.2.17 — Created on 2026-10-03
### Added
- [py.typed](src/enforce_rules/py.typed)

## 3.2.18 — Created on 2026-10-03
### Fixed
- Required python version number in [pyproject.toml](pyproject.toml)

## 3.2.19 — Created on 2026-10-03
### Fixed
- Issues that prevent Python 3.10 from working

### Changed
- Required python version number in [pyproject.toml](pyproject.toml)

## 3.2.20 — Created on 2026-10-03
### Fixed
- [Tests](tests/)
