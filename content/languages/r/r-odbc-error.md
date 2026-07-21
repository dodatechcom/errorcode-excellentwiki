---
title: "[Solution] R ODBC Database Error"
description: "ODBC connection errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ODBC Database Error

ODBC connection errors.

### Common Causes
Driver missing; connection string wrong

### How to Fix
```r
library(DBI)
library(odbc)
con <- dbConnect(odbc::odbc(), driver = "SQL Server", server = "server", database = "db")
```

### Examples
```r
dbListTables(con)
dbGetQuery(con, "SELECT TOP 10 * FROM table")
```
