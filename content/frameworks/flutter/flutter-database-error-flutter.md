---
title: "[Solution] flutter Database Error Flutter"
description: "SQLite not working."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

SQLite not working.

## Common Causes

Wrong path.

## How to Fix

Check path.

## Example

```dart
final db = await openDatabase('my.db', version: 1,
  onCreate: (db, v) => db.execute('CREATE TABLE t (id INTEGER PRIMARY KEY)'));
```
