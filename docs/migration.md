# Migration

Changes that break backwards compatibility and bugged versions go here, so you can update your code before you download it.

Syntax deprecations are [here](https://github.com/Loepker-James/enforce-rules/blob/main/docs/deprecations.md).

## Upgrading from 1.1- to 1.1+

Version 1.1 changes how rule patterns are matched. Previously, patterns used ```re.fullmatch```, which required the entire string to match the rule. Starting in 1.1, patterns use ```re.search```, which allows partial matches.

### What changed

Old behavior (1-1).: The entire value had to match the pattern.

New behavior (1.1+): The pattern only needs to appear somewhere inside the value.

### Why this matters

If your rules relied on full‑string matching, they may now match more values than before.

### Old vs New Examples

#### Old (fullmatch):

Only matches "abc" exactly.
```python
validate("abc", {"regex": "abc"}) #matches
validate("xabc", {"regex": "abc"}) #does not match
```

#### New (search):

Matches if "abc" appears anywhere.
```python
validate("abc", {"regex": "abc"}) #matches
validate("xabc", {"regex": "abc"}) #matches
```

### What you may need to change

If you want to keep the old full‑match behavior, update your patterns to anchor them using ^ and $.

Example: pattern = "^abc$"

This behaves like the old fullmatch.

Summary:

Most users do not need to change anything. But if you depended on strict full‑string matching, you should update your patterns to include ^ and $.

## Downgrading from 1.1+ to 1.1-

Version 1.1+ introduced a change to how rule patterns are matched.  
If you need to return to the 1.1- series, you must revert any patterns that rely on the newer partial‑match behavior.

### What changed

Old behavior (1.1-): The entire value must match the pattern.

New behavior (1.1+): The pattern only needs to appear somewhere inside the value.

### Why this matters

If you wrote rules expecting partial matches, they will behave differently — or fail — when running under 1.1-.  
The older validator only supports full‑string matching.

### Examples of what to revert

1.1+ (search):
```python
validate("xabc", {"regex": "abc"}) #matches in 1.1+
```

1.1- (fullmatch):
```python
validate("xabc", {"regex": "abc"}) #does not match in 1.1-
```

### What you may need to change
If your rules depend on partial substring matching, do not downgrade.  
The 1.1- series only supports full‑match behavior, so any rule relying on search‑style matching will stop working.

If your rules depend on full‑string matching, you must remove any ^ and $ anchors you added for 1.1+.  
The older 1.1- validator already performs full‑match checks, so anchored patterns are unnecessary.

### Example (downgrade‑safe)
pattern = "abc"

This restores the original 1.1‑ full‑match behavior without relying on 1.1+ anchors.

### Summary
If your rules rely on partial matching, you should not downgrade to 1.1-.  
If your rules rely on full‑match semantics, remove ^ and $ anchors so you're using proper 1.1- api.

## Upgrading/Downgrading to 3.1.5 --- DONT
Version 3.1.5 should be skipped.
This release shipped with a missing internal import, which causes the validator to raise an error immediately on startup. Because the module cannot fully load, no rules validate at all.

### What went wrong
* A required internal import was accidentally removed.
* The validator fails during initialization.
* Any call to ```validate()``` never occurs because Python raises an error before the function is reached.
* No rules are parsed or executed.

### Why this matters
Since the validator cannot start, 3.1.5 is unusable.
Users upgrading to this version will encounter immediate crashes, making migration impossible.

### Required user actions
* Do not install 3.1.5.
* If you already installed it, downgrade immediately to **any stable version in the 3.1.x line**, specifically **3.1.0 through 3.1.4**.  
  These versions all share the same working validator code.
* No rule changes are required — the issue is internal, not user-facing.
* After downgrading to a stable 3.1.x version, validation will work normally again.

### Summary
3.1.5 contains a missing import that prevents the validator from running.
Skip this version and upgrade directly from a stable 3.1.x release to the next working version.


