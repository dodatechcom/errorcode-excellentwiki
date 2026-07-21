---
title: "[Solution] R Shiny Input Widget Error"
description: "Shiny input widget definition errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Shiny Input Widget Error

Shiny input widget definition errors.

### Common Causes
ID mismatch; wrong widget type

### How to Fix
```r
sliderInput("n", "Number:", min = 1, max = 100, value = 50)
textInput("name", "Name:")
selectInput("choice", "Choose:", choices = c("A", "B"))
```

### Examples
```r
selectInput("color", "Color:", choices = c("red", "blue", "green"))
```
