---
title: "[Solution] R ggsave() Error"
description: "ggsave() plot saving errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R ggsave() Error

ggsave() plot saving errors.

### Common Causes
Wrong extension; device not available

### How to Fix
```r
ggsave("plot.pdf", width = 8, height = 6)
ggsave("plot.png", dpi = 300)
```

### Examples
```r
p <- ggplot(mtcars, aes(wt, mpg)) + geom_point()
ggsave("scatter.pdf", p, width = 10, height = 8)
```
