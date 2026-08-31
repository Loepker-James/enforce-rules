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

Be respectful, constructive, and kind.  

No harassment, discrimination, or hostile behavior will be tolerated.



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



git clone <repo>

cd enforce-rules

python -m pip install -e .

python -m unittest discover -s tests





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


Pull requests that add __version__, --version flags, or any version-exposing code
will not be accepted. This project uses metadata-based versioning only.



---



## Backwards Compatibility

PER guarantees full backwards compatibility.  

Existing rule dictionaries, keyword meanings, and validator behaviors must never change.



---



## Adding New Keywords

New keywords must:



- be additive  

- not modify existing keyword behavior (unless it is the point of the keyword; e.g. min_exclusive and max_exclusive. For more clarification, please ask me in an issue. If you would ever like to contact me, put it in an issue and we will get it sorted out.)

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


## Maintainer Notes

This section documents internal decisions and guidelines for future maintainers.

### Design Principles
- PER must remain fully backwards compatible.
- All keywords must be additive; never modify existing keyword behavior. (Unless it is one of the exceptions seen earlier)
- Error messages must be explicit and never silent.

### Roadmap
For roadmaps, you can usually look in issues. There I put everything I would want (and/or I think you would) there.

### Review Guidelines
- Reject PRs that introduce silent failures.
- Reject PRs that change existing keyword semantics.
- Require full test coverage for all new keywords.
- Require documentation updates for all new features.

### Internal Decisions
- validate() uses match/case dispatch for clarity and maintainability.
- Keyword names follow snake_case and must be descriptive.

