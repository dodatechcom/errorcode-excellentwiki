---
title: "[Solution] R Shiny Server Error"
description: "Shiny server function errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Shiny Server Error

Shiny server function errors.

### Common Causes
Missing output; wrong input ref

### How to Fix
```r
server <- function(input, output, session) {
  output$text <- renderText({ paste("Hello", input$name) })
}
```

### Examples
```r
server <- function(input, output) {
  output$result <- renderText({ input$x * 2 })
}
```
