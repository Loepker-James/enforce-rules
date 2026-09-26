# Migration

Changes that break backwards compatibility and bugged versions go here, so you can update your code before you download it.

Syntax deprecations are [here](https://github.com/Loepker-James/enforce-rules/blob/main/docs/deprecations.md).

## Upgrading from 1.1- to 1.1+

Version 1.1 changes how rule patterns are matched. Previously, patterns used ```re.fullmatch```, which required the entire string to match the rule. Starting in 1.1, patterns use ```re.search```, which allows partial matches.

### What changed

Old behavior (1.1-): The entire value had to match the pattern.

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

#### 1.1+ (search):
```python
validate("xabc", {"regex": "abc"}) #matches in 1.1+
```

#### 1.1- (fullmatch):
```python
validate("xabc", {"regex": "abc"}) #does not match in 1.1-
```

### What you may need to change
If your rules depend on partial substring matching, do not downgrade.  
The 1.1‑ series only supports full‑match behavior, so any rule relying on search‑style matching must explicitly use `.*` or `.*?` around the pattern (for example: `.*abc.*`).  
Without these wrappers, the older validator will treat the pattern as a full‑match and your partial‑match rule will stop working.

If your rules depend on full‑string matching, you must remove any ^ and $ anchors you added for 1.1+.  
The older 1.1‑ validator already performs full‑match checks, so anchored patterns are unnecessary and you should use plain patterns (e.g., `abc` instead of `^abc$`).

### Example (downgrade‑safe)
pattern = "abc"

This restores the original 1.1‑ full‑match behavior without relying on 1.1+ anchors or search‑style wrappers.

### Summary
If your rules rely on partial matching, wrap your pattern with ```.*``` or ```.*?``` as needed, because 1.1‑ only supports full‑match semantics.  
If your rules rely on full‑match semantics, remove ^ and $ anchors so you're using proper 1.1‑ API behavior.


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
Skip this version and downgrade directly from a stable 3.1.x release to the next working version.


## Raw String Ending With Single Backslash (3.2.4 → 3.2.9) — DONT

A mistake was introduced in **3.2.4** where a raw string was written ending with a single backslash:

```
r"\"
```

This is not valid Python syntax.  
Raw strings cannot end with a single backslash because the backslash escapes the closing quote, causing Python to raise a syntax error before the module can load.

### What went wrong
* A raw string was incorrectly written with a trailing backslash.  
* Python treated the final backslash as escaping the closing quote.  
* The module failed during import because the file could not be parsed.  
* Any tool or rule depending on this file never executed because Python stopped before reaching user code.

### Why this matters
Since the module cannot import, this mistake causes:
* immediate syntax errors,
* broken configuration files,
* failed initialization,
* and any rule or validator depending on the file to never run.

### Affected versions
* **Broken:** 3.2.4 → 3.2.9  
* **Fixed:** 3.2.10 and later  
  (The mistake was removed and the file now contains valid syntax.)

### Required user actions
* Avoid using versions **3.2.4 through 3.2.9**.  
* If your project is in this line, please upgrade to **3.2.10+**.  
* No rule changes are required — the issue was **external**, caused by an invalid raw‑string literal.  
* After upgrading, the module will import normally again.

### Summary
An invalid raw‑string literal ending with a single backslash was introduced in **3.2.4**, causing Python to raise a syntax error.  
This mistake persisted through **3.2.9** and was removed in **3.2.10**.  
Upgrade to a fixed version if your project relies on this module.

 
