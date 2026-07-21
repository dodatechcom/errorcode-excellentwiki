---
title: "[Solution] R scan() Error"
description: "scan() input reading errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R scan() Error

scan() input reading errors.

### Common Causes
Type mismatch; unexpected EOF

### How to Fix
```r
values <- scan("data.txt", what = numeric())
values <- scan(text = "1 2 3 4 5", what = numeric())
```

### Examples
```r
values <- scan(text = "1 2 3 4 5", what = numeric())
```
