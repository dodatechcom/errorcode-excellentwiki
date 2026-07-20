---
title: "[Solution] SQLite FTS porter stemmer error"
description: "The Porter stemming algorithm used by FTS encountered an error during processing."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite FTS porter stemmer error

SQLite FTS raises **FTS porter stemmer error** when the porter stemming algorithm used by fts encountered an error during processing. Full-text search is a powerful extension but requires correct configuration.

## Common Causes

- The input word could not be stemmed.
- The Porter stemmer is combined with incompatible tokenizer options.
- An invalid character sequence was passed to the stemmer.

## How to Fix

### Combine porter with a valid base tokenizer

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='porter unicode61');
```

### Handle stemming errors at the application layer

```python
# FTS handles stemming internally; errors are rare
# Ensure input text is valid UTF-8
```

### Use simple tokenizer if porter causes issues

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='simple');
```

## Examples

```sql
CREATE VIRTUAL TABLE docs USING fts5(content, tokenize='porter');
-- Porter stemmer requires a secondary tokenizer like unicode61
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
