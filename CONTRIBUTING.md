# Contributing to PER (Project Enforce Rules)

Thank you for your interest in contributing to PER!  
This project expands Python’s type system with runtime rule dictionaries and strict validation.  
All contributions are welcome as long as they maintain full backwards compatibility.

---

## Introduction

PER enforces dictionary-based rules at runtime using `validate(value, rules)`.  
New keywords, improvements, tests, and documentation updates are encouraged.

---

## Code of Conduct

See the [Code of Conduct](https://github.com/Loepker-James/enforce-rules/blob/main/CODE_OF_CONDUCT.md).

---

## How to Propose Changes

Before writing code, please open an Issue describing:

- the problem  
- the proposed solution  
- any new keywords  
- expected behavior  

This ensures alignment with PER’s design philosophy.

---

## Development Setup

1. Clone the repository  
2. Install dependencies  
3. Run the test suite  
4. Make changes in a feature branch

Commands:

```git
git clone <repo>
```

```python
python -m pip install -e .
```

```python
python -m unittest discover -s tests
```

---

## Coding Standards

PER follows strict rules:

- Type hints required everywhere  
- `match/case` dispatch required in `validate()`  
- Clear, descriptive error messages  
- No silent failures  
- No breaking changes  
- No removal or renaming of existing keywords  
- Keep code simple and readable

---

## Testing Requirements

Every new keyword must include:

- Valid test cases  
- Invalid test cases  
- Edge-case tests  
- Tests for error messages  

All tests must pass before submitting a PR.

---

## Versioning Rules

PER uses non-breaking semantic versioning:

- **MAJOR** — new feature families  
- **MINOR** — new keywords  
- **PATCH** — bug fixes or internal improvements  

Major bumps do **not** imply breaking changes.

You should **never** bump a version **unless** you are changing one of these files:

- `README.md`  
- `LICENSE`  
- `pyproject.toml`  
- `src/enforce_rules/__init__.py`  
- `src/enforce_rules/enforce_rules.py`  

Pull requests that add `__version__`, `--version` flags, or any version-exposing code will not be accepted.  
This project uses metadata-based versioning only.

---

## Backwards Compatibility

PER guarantees full backwards compatibility.  
Existing rule dictionaries, keyword meanings, and validator behaviors must never change.

---

## Adding New Keywords

New keywords must:

- be additive  
- not modify existing keyword behavior (unless explicitly allowed)  
- include full test coverage  
- include documentation updates  
- include clear error messages  
- follow the naming conventions of existing keywords

---

## Submitting Pull Requests

1. Fork the repository  
2. Create a feature branch  
3. Make changes  
4. Add tests  
5. Update documentation  
6. Ensure all tests pass  
7. Submit a PR referencing the related Issue

---

## CodeQL Notice (Security and Quality Tab)

You may see a yellow “CodeQL is showing warnings” banner under the **Security and Quality** tab.  
This is because I was experimenting with `.github/workflows/` and fell in a pit. It is not an error, a real warning, or problem.

GitHub is still displaying this banner. Although this banner is being displayed, the project is fully functional, and contributors do not need to take any action regarding this notice.

In short: the banner is harmless. Everything is working correctly.  
The only change by maintainers is not to experiment with this directory at all — unless CodeQL explicitly approves.


---

## Maintainer Notes

This section documents internal decisions and guidelines for future maintainers.

### Design Principles
- PER must remain fully backwards compatible.  
- All keywords must be additive; never modify existing keyword behavior.  
- Error messages must be explicit and never silent.

### Naming Keyword Helpers
`_validate_keyword_name` is the proper naming pattern for keyword helper functions.

### Roadmap
Roadmaps are maintained in Issues.  
Category prefixes group related issues (like folders).  
Closed issues follow the format:

```
[Resolved] (Issue Title) {Version Number}
```

Example:  
`[Resolved] (add "is_password") {3.1+}`

### Review Guidelines
- Reject PRs that introduce silent failures.  
- Reject PRs that change existing keyword semantics.  
- Require full test coverage for all new keywords.  
- Require documentation updates for all new features.

### Internal Decisions
- `validate()` uses `match/case` dispatch for clarity and maintainability.  
- Keyword names follow snake_case and must be descriptive.

---

## Enforcement

Following the guidelines in this document is required under  
[§2.3 of the Code of Conduct (Follow Project Rules)](https://github.com/Loepker-James/enforce-rules/blob/main/CODE_OF_CONDUCT.md#23-follow-project-rules).

---

## P.S.

I do not create releases when writing new code; I publish directly to `main`.  
For release history, see the [CHANGELOG](https://github.com/Loepker-James/enforce-rules/blob/main/CHANGELOG.md).
