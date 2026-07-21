---
title: "[Solution] Groovy SQL Error"
description: "Groovy SQL operations errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy SQL Error

Groovy SQL operations errors.

### Common Causes
Wrong connection; SQL syntax; resource leak

### How to Fix
```groovy
import groovy.sql.Sql
def sql = Sql.newInstance('jdbc:h2:mem:test', 'sa', '')
sql.execute('CREATE TABLE test (id INT, name VARCHAR)')
```

### Examples
```groovy
sql.eachRow('SELECT * FROM test') { row ->
    println row.name
}
sql.close()
```
