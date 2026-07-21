---
title: "[Solution] R crayon Color Error"
description: "crayon color output errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R crayon Color Error

crayon color output errors.

### Common Causes
No terminal colors; wrong style

### How to Fix
```r
library(crayon)
cat(red("Error"), "message\n")
cat(bold(blue("Info")), "message\n")
```

### Examples
```r
if (crayon::has_color()) {
  cat(red("Error") + ": something wrong\n")
}
```
