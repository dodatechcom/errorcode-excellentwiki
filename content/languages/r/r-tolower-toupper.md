---
title: "[Solution] R tolower/toupper Error"
description: "Case conversion encoding errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R tolower/toupper Error

Case conversion encoding errors.

### Common Causes
Encoding mismatch; locale issues

### How to Fix
```r
tolower("HELLO")
toupper("hello")
```

### Examples
```r
tolower("Hello World")
toupper("Hello World")
```
