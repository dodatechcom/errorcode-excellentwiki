---
title: "[Solution] SQLite REGEXP not defined"
description: "The REGEXP operator is used but no REGEXP function has been registered."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite REGEXP not defined

SQLite produces **REGEXP not defined** when the regexp operator is used but no regexp function has been registered. This error can occur in various contexts and requires understanding the specific trigger.

## Common Causes

- SQLite does not include REGEXP by default.
- A custom REGEXP function was not loaded.
- The regexp extension was not compiled in.

## How to Fix

### Load the regexp extension

```sql
-- In application code:
import re
conn.create_function('regexp', 2, lambda pattern, string: 1 if re.search(pattern, string) else 0)
```

### Use LIKE or GLOB instead of REGEXP

```sql
SELECT * FROM t WHERE name LIKE '%error%';
SELECT * FROM t WHERE name GLOB '*error*';
```

### Install a regexp extension

```bash
# Compile SQLite with regexp support or load a shared library
```

## Examples

```sql
SELECT * FROM t WHERE name REGEXP '^[A-Z]';
-- Error: no such function: regexp
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
