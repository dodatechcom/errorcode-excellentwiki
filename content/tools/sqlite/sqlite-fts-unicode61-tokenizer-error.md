---
title: "[Solution] SQLite FTS unicode61 tokenizer error"
description: "The unicode61 tokenizer encountered an error during tokenization."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite FTS unicode61 tokenizer error

SQLite FTS raises **FTS unicode61 tokenizer error** when the unicode61 tokenizer encountered an error during tokenization. Full-text search is a powerful extension but requires correct configuration.

## Common Causes

- An invalid remove_diacritics value was specified.
- The tokenizer configuration is incorrect.
- The input text contains invalid Unicode.

## How to Fix

### Use valid remove_diacritics values (0, 1, or 2)

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 remove_diacritics 2');
```

### Use default unicode61 settings

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61');
```

### Check token separators

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 tokenchars ".-");
```

## Examples

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 remove_diacritics 5');
-- Error: invalid remove_diacritics value
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
