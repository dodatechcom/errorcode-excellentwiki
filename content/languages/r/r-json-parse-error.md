---
title: "[Solution] R JSON Parse Error"
description: "JSON content cannot be parsed by jsonlite."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R JSON Parse Error

JSON content cannot be parsed by jsonlite.

### Common Causes
Malformed JSON; single quotes; trailing commas

### How to Fix
```r
library(jsonlite)
data <- fromJSON("data.json")
validate(json_string)
```

### Examples
```r
json <- '{"name": "John"}'
data <- fromJSON(json)
```
