# Migration

Changes that break backwards compatibility go here, so you can update your code before you download it.

Syntax deprecations are [here](https://github.com/Loepker-James/enforce-rules/blob/main/docs/deprecations.md).

## Upgrading from 1.1- to 1.1+

Version 1.1 changes how rule patterns are matched. Previously, patterns used re.fullmatch, which required the entire string to match the rule. Starting in 1.1, patterns use re.search, which allows partial matches.

What changed
Old behavior: The entire value had to match the pattern.
New behavior: The pattern only needs to appear somewhere inside the value.

Why this matters
If your rules relied on full‑string matching, they may now match more values than before.

### Old vs New Examples

Old (fullmatch):
Only matches "abc" exactly.
```python
validate("abc", {"regex": "abc"}) #matches
validate("xabc", {"regex": "abc"}) #does not match
```

New (search):
Matches if "abc" appears anywhere.
```python
validate("abc", {"regex": "abc"}) #matches
validate("xabc", {"regex": "abc"}) #matches
```

What you may need to change
If you want to keep the old full‑match behavior, update your patterns to anchor them using ^ and $.

Example: pattern = "^abc$"

This behaves like the old fullmatch.

Summary:

Most users do not need to change anything. But if you depended on strict full‑string matching, you should update your patterns to include ^ and $.
