---
title: "[Solution] SQLite FTS content_rowid missing"
description: "An FTS table configured with content= requires a content_rowid= that was not provided."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite FTS content_rowid missing

SQLite FTS raises **FTS content_rowid missing** when an fts table configured with content= requires a content_rowid= that was not provided. Full-text search is a powerful extension but requires correct configuration.

## Common Causes

- The content_rowid= parameter is missing.
- The content_rowid column does not exist in the content table.
- The content_rowid type is incompatible.

## How to Fix

### Provide content_rowid when using content=

```sql
CREATE VIRTUAL TABLE docs USING fts5(title, body, content=my_table, content_rowid=id);
```

### Ensure the content_rowid column exists in the content table

```sql
PRAGMA table_info(my_table);
```

### Use rowid if no explicit ID column exists

```sql
CREATE VIRTUAL TABLE docs USING fts5(title, body, content=my_table, content_rowid=rowid);
```

## Examples

```sql
CREATE VIRTUAL TABLE docs USING fts5(title, content=my_table);
-- Error: content_rowid required when content= is specified
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
