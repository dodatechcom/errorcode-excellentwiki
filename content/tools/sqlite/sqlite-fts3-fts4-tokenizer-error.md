---
title: "[Solution] SQLite FTS3/FTS4 tokenizer error"
description: "The FTS3 or FTS4 full-text search engine encountered an error with its tokenizer configuration."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite FTS3/FTS4 tokenizer error

SQLite FTS raises **FTS3/FTS4 tokenizer error** when the fts3 or fts4 full-text search engine encountered an error with its tokenizer configuration. Full-text search is a powerful extension but requires correct configuration.

## Common Causes

- An invalid tokenizer was specified during table creation.
- A custom tokenizer module failed to initialize.
- The tokenizer does not support the required Unicode features.

## How to Fix

### Use a built-in tokenizer

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='porter unicode61');
```

### Verify available tokenizers

```sql
-- Available: simple, porter, unicode61, ascii
```

### Check tokenizer parameters

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='unicode61 remove_diacritics 2');
```

## Examples

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='invalid_tokenizer');
-- Error: no such tokenizer: invalid_tokenizer
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
