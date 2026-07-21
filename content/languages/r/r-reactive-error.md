---
title: "[Solution] R Reactive Error"
description: "reactive expression errors in Shiny."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R Reactive Error

reactive expression errors in Shiny.

### Common Causes
Input outside reactive; circular deps

### How to Fix
```r
data <- reactive({
  req(input$file)
  read.csv(input$file)
})
```

### Examples
```r
output$plot <- renderPlot({
  x <- input$x_val
  y <- isolate(input$y_val)
  plot(x, y)
})
```
