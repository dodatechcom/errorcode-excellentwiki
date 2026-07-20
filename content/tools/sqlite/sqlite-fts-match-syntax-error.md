---
title: "[Solution] SQLite FTS MATCH syntax error"
description: "An FTS MATCH query contains a syntax error."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite FTS MATCH syntax error

SQLite FTS raises **FTS MATCH syntax error** when an fts match query contains a syntax error. Full-text search is a powerful extension but requires correct configuration.

## Common Causes

- Invalid characters in the MATCH expression.
- Incorrect use of FTS operators.
- A phrase is not properly quoted.

## How to Fix

### Use correct FTS MATCH syntax

```sql
SELECT * FROM docs WHERE docs MATCH 'search term';
```

### Quote phrases with double quotes

```sql
SELECT * FROM docs WHERE docs MATCH '"exact phrase"';
```

### Use column filters

```sql
SELECT * FROM docs WHERE docs MATCH 'title:search OR body:term';
```

## Examples

```sql
SELECT * FROM docs WHERE docs MATCH '"unclosed phrase;
-- Error: FTS5 syntax error near "unclosed
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
