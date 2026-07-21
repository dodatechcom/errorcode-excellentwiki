---
title: "[Solution] R knitr Chunk Error"
description: "knitr code chunk processing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R knitr Chunk Error

knitr code chunk processing errors.

### Common Causes
Syntax error; missing package; output too large

### How to Fix
```r
library(knitr)
knit("document.Rmd")
```

### Examples
```r
# In Rmd chunk:
# ```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
# ```
```
