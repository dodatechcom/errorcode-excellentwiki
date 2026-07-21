---
title: "[Solution] R writeLines() Error"
description: "writeLines() file writing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R writeLines() Error

writeLines() file writing errors.

### Common Causes
Path missing; encoding; connection issues

### How to Fix
```r
writeLines(lines, con = "output.txt")
writeLines(lines, con = "output.txt", useBytes = TRUE)
```

### Examples
```r
writeLines(c("line1", "line2"), con = "output.txt")
```
