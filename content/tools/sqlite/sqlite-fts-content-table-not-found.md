---
title: "[Solution] SQLite FTS content table not found"
description: "An FTS table references a content table that does not exist."
tools: ["sqlite"]
error-types: ["query-error"]
severities: ["error"]
---


# [Solution] SQLite FTS content table not found

SQLite FTS raises **FTS content table not found** when an fts table references a content table that does not exist. Full-text search is a powerful extension but requires correct configuration.

## Common Causes

- The content table was dropped.
- The content= parameter references a non-existent table.
- A typo in the content table name.

## How to Fix

### Verify the content table exists

```sql
SELECT name FROM sqlite_master WHERE type='table' AND name='my_content';
```

### Create the content table

```sql
CREATE TABLE my_content (id INTEGER PRIMARY KEY, title TEXT, body TEXT);
```

### Use contentless FTS if no content table is needed

```sql
CREATE VIRTUAL TABLE docs USING fts5(content='');
```

## Examples

```sql
CREATE VIRTUAL TABLE docs USING fts5(title, body, content=my_nonexistent);
-- Error: no such table: my_nonexistent
```

## Related Errors

- [SQLite Documentation](https://www.sqlite.org/c3ref/c_abort.html) — Official result code reference
