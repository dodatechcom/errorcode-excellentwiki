---
title: "[Solution] R renderTable() Error"
description: "renderTable() fails in Shiny."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R renderTable() Error

renderTable() fails in Shiny.

### Common Causes
Data NULL; column issues

### How to Fix
```r
output$table <- renderTable({
  req(data())
  data()
})
```

### Examples
```r
output$table <- renderTable({
  head(mtcars)
})
```
