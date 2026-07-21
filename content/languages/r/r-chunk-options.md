---
title: "[Solution] R Chunk Options Error"
description: "knitr chunk option configuration errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Chunk Options Error

knitr chunk option configuration errors.

### Common Causes
Unknown option; wrong value type

### How to Fix
```r
knitr::opts_chunk$set(echo = FALSE, warning = FALSE)
# Per-chunk: # ```{r, echo=TRUE, fig.width=8}
```

### Examples
````
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, fig.path = "figures/")
```
````

