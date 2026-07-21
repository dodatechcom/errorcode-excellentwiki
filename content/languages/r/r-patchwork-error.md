---
title: "[Solution] R patchwork Layout Error"
description: "patchwork plot composition errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R patchwork Layout Error

patchwork plot composition errors.

### Common Causes
Incompatible plots; wrong operator

### How to Fix
```r
library(patchwork)
p1 + p2  # side by side
p1 / p2  # stacked
p1 + p2 + plot_layout(ncol = 1)
```

### Examples
```r
(p1 | p2) / p3
```
