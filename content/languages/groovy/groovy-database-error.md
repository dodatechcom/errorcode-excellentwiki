---
title: "[Solution] Groovy Database Error"
description: "Database operations errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy Database Error

Database operations errors.

### Common Causes
Wrong driver; connection pool issues

### How to Fix
```groovy
import groovy.sql.Sql
def sql = Sql.newInstance(url, user, pass, driver)
```

### Examples
```groovy
sql.withInstance(url, user, pass, driver) {
    it.executeInsert('INSERT INTO test VALUES (1, ?)', ['value'])
}
```
