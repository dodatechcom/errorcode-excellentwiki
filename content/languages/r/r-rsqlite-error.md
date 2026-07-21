---
title: "[Solution] R RSQLite Error"
description: "RSQLite database errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R RSQLite Error

RSQLite database errors.

### Common Causes
Wrong file path; SQL syntax

### How to Fix
```r
library(DBI)
library(RSQLite)
con <- dbConnect(SQLite(), "mydb.sqlite")
dbListTables(con)
```

### Examples
```r
dbWriteTable(con, "mtcars", mtcars)
dbGetQuery(con, "SELECT * FROM mtcars WHERE mpg > 25")
```
