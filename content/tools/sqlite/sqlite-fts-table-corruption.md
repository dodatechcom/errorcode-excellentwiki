---
title: "[Solution] SQLite FTS table corruption"
description: "An FTS index has become corrupted and search results may be incorrect or queries may fail."
tools: ["sqlite"]
error-types: ["corruption-error"]
severities: ["error"]
---


# [Solution] SQLite FTS table corruption

SQLite FTS raises **FTS table corruption** when an fts index has become corrupted and search results may be incorrect or queries may fail. Full-text search is a powerful extension but requires correct configuration.

## Common Causes

- The FTS segment files are damaged.
- A crash during FTS update corrupted the index.
- The underlying content table was modified outside of FTS.

## How to Fix

### Rebuild the FTS index

```sql
INSERT INTO docs(docs) VALUES('rebuild');
```

### Drop and recreate the FTS table

```sql
DROP TABLE IF EXISTS docs;
CREATE VIRTUAL TABLE docs USING fts5(title, body);
-- Re-populate from content table
```

### Use contentless-auto-delete for simpler rebuilds

```sql
CREATE VIRTUAL TABLE docs USING fts5(title, body, contentless_delete=1);
```

## Examples

```sql
INSERT INTO docs(docs) VALUES('rebuild');
-- Rebuilds the FTS index from the content table
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
