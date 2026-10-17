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

By participating in this project, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md). To report unacceptable behavior, see the [reporting section](CODE_OF_CONDUCT.md#5-reporting).

---

## How to Propose Changes

Before writing code, please open an Issue describing:

- the problem  
- the proposed solution  
- any new keywords  
- expected behavior  

This ensures alignment with PER’s design philosophy.

---

## What's in the release tarball (3.2.26+)

The PyPI tarball (.tar.gz) contains (excluding build metadata) the [source (src/)](src/), [tests (tests/)](tests/), [README.md](README.md), [LICENSE](LICENSE), [.gitignore](.gitignore), and [requirements.txt](requirements.txt). Tests, CI config, and other repo files are on GitHub only.

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

You should **only** bump a version **if** you are changing one of these files:

- [`README.md`](README.md)  
- [`LICENSE`](LICENSE) (which you should never change)
- [`requirements.txt`](requirements.txt) (which you should never change)
- [`MANIFEST.in`](MANIFEST.in) (which you should never change)
- [`.gitignore`](.gitignore) (which you should never change)
- [`pyproject.toml`](pyproject.toml)
- [`src/enforce_rules/**`](/src/enforce_rules/)
  
Pull requests that add `__version__`, `--version` flags, or any version-exposing code won't be accepted.  
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
This is because I am using syntax CodeQL does not yet understand.

GitHub is still displaying this banner. Although this banner is being displayed, the project is fully functional, and contributors do not need to take any action regarding this notice.

In short: the banner is harmless. Everything is working correctly.  


---

## What happens to an issue

Every issue is either open or closed. A closed issue has one of two reasons, and GitHub shows it next to the title.

### Closed as completed
The work is done. The bug is fixed, the feature is added, or the question is answered.

### Closed as not planned
The issue will not be worked on. This does not mean the report was unwelcome. It means one of these:

* **It cannot be fixed.** The cause is outside this project, such as a bug in another library, or the problem cannot be reproduced with the information given.
* **It will not be fixed.** The change doesn't fit the project. For example, it would change what an existing keyword does without explicit permission, which this project doesn't do (see the versioning policy in the [README](README.md)).
* **It is invalid.** A required field in the issue form was empty or didn't answer the question, so there wasn't enough to act on.
* **It is a duplicate.** The same problem is already reported. The closing comment links to the original issue, and you are welcome to add what you know there.

The closing comment always says which one applies. If you think the decision was wrong, add a comment on the closed issue saying why, and it will be read. Please do not reopen it without changing something, since a reopened issue with no new information is closed again. See [§3.12 of the Code of Conduct](CODE_OF_CONDUCT.md#312-closing-and-reopening-issues).

### Left open
A problem that is real but cannot be fixed right now stays open, usually with the `help wanted` label. This means a fix from you would be welcome.

---

## Issue templates
Please fill in every required field. A required field that is empty or answered with text like "n/a" will be closed as invalid, and you are welcome to open a new issue with the details. See [§3.12 of the Code of Conduct](CODE_OF_CONDUCT.md#312-reopening-closed-issues) about reopening a closed issue.

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

Following the guidelines in this document is required under [§2.3 of the Code of Conduct (Follow Project Rules)](CODE_OF_CONDUCT.md#23-follow-project-rules).

---

## P.S.

I do not create releases when writing new code; I publish directly to `main`.  
For release history, see the [CHANGELOG](CHANGELOG.md).
