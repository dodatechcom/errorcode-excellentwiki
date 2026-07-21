---
title: "[Solution] R Shiny UI Error"
description: "Shiny UI definition errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Shiny UI Error

Shiny UI definition errors.

### Common Causes
Mismatched braces; invalid IDs

### How to Fix
```r
ui <- fluidPage(
  titlePanel("App"),
  sidebarLayout(
    sidebarPanel(sliderInput("n", "N:", 1, 100, 50)),
    mainPanel(plotOutput("plot"))
  )
)
```

### Examples
```r
ui <- fluidPage(
  titlePanel("App"),
  mainPanel(textOutput("text"))
)
```
