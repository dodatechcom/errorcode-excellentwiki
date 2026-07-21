---
title: "[Solution] R clipr Clipboard Error"
description: "clipboard access errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R clipr Clipboard Error

clipboard access errors.

### Common Causes
No clipboard on server; wrong platform

### How to Fix
```r
library(clipr)
write_clip("hello")
read_clip()
```

### Examples
```r
if (clipr_available()) {
  write_clip(mtcars$mpg)
}
```
