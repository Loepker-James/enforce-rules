### regex (Changed in 1.1.0)
The regex rule originally used ```re.fullmatch```, requiring the pattern to match the entire string. 
Since we (me and Copilot, mostly copilot) wrote 1.1.0, the rule uses ```re.search``` instead, allowing the pattern to appear anywhere in the value. To migrate to this change, click [Here](https://github.com/Loepker-James/enforce-rules/blob/main/docs/migration.md#upgrading-from-11--to-11)
