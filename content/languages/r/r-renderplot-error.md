---
title: "[Solution] R renderPlot() Error"
description: "renderPlot() fails in Shiny."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R renderPlot() Error

renderPlot() fails in Shiny.

### Common Causes
Plot code error; missing inputs

### How to Fix
```r
output$plot <- renderPlot({
  req(input$n)
  plot(1:input$n)
})
```

### Examples
```r
output$scatter <- renderPlot({
  plot(mtcars$wt, mtcars$mpg)
})
```
