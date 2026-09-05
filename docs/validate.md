```validate()``` checks a value against a set of rules.

Rule dictionaries work by writing a keyword, then a rule value attached to it. For more information look in [api.md](https://github.com/Loepker-James/enforce-rules/blob/main/docs/api.md).

The validator does these steps for each rule.

1. Puts your key in a match/case loop.
2. Calls the corresponding helper with rule value and the value to be validated
3. The helper may raise an error.
4. If none of the helpers raise errors, return the value.

length:
Suceeds if value's length is equal to rule value.

min_length:
Suceeds if value's length is greater than or equal to rule value.

max_length:
