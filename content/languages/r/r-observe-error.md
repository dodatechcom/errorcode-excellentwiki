---
title: "[Solution] R observe() Error"
description: "observe() side-effect errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R observe() Error

observe() side-effect errors.

### Common Causes
Missing input ref; side effects outside reactive

### How to Fix
```r
observe({
  req(input$go)
  print(input$go)
})
```

### Examples
```r
observe({
  cat("Value:", input$slider, "\n")
})
```
