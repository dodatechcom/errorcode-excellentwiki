---
title: "[Solution] R shinydashboard Error"
description: "shinydashboard layout errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R shinydashboard Error

shinydashboard layout errors.

### Common Causes
Missing CSS; wrong box structure

### How to Fix
```r
library(shinydashboard)
dashboardPage(
  dashboardHeader(),
  dashboardSidebar(),
  dashboardBody()
)
```

### Examples
```r
dashboardBody(
  fluidRow(
    box(title = "Plot", plotOutput("plot"))
  )
)
```
