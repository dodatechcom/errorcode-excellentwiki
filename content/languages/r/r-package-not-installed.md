---
title: "[Solution] R Package Not Installed"
description: "Package fails to load because it is not installed."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Package Not Installed

Package fails to load because it is not installed.

### Common Causes
Removed or corrupted; binary not available

### How to Fix
```r
install.packages("pkg", repos = "https://cran.r-project.org")
remove.packages("pkg")
install.packages("pkg", type = "source")
```

### Examples
```r
install.packages("ggplot2")
library(ggplot2)
```
