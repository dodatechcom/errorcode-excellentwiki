---
title: "[Solution] R Shiny Reactive Error"
description: "Fix Shiny reactive errors including reactive expression failures, observer errors, and invalidation issues in Shiny applications."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Shiny reactive errors occur when reactive expressions, observers, or render functions fail. These errors often appear in the Shiny app console or as error messages in the UI.

## Common Causes

- Reactive expression referencing non-existent inputs
- Observer depending on a reactive value that hasn't been initialized
- Circular dependencies between reactives
- Render function failing due to invalid data

## How to Fix

```r
# WRONG: Accessing non-existent input
server <- function(input, output, session) {
  output$plot <- renderPlot({
    plot(input$missing_input)  # Error: input$missing_input not found
  })
}

# CORRECT: Check if input exists
server <- function(input, output, session) {
  output$plot <- renderPlot({
    req(input$existing_input)  # req() silently validates
    plot(input$existing_input)
  })
}
```

```r
# WRONG: Reactive expression with side effects
my_reactive <- reactive({
  data <- read.csv("data.csv")
  # This runs every time, even if data hasn't changed
})

# CORRECT: Use eventReactive for explicit triggers
my_data <- eventReactive(input$load_btn, {
  read.csv("data.csv")
})
```

```r
# WRONG: Circular dependency
a <- reactive({ b() + 1 })
b <- reactive({ a() + 1 })  # Infinite loop!

# CORRECT: Break the cycle
a <- reactive({ input$x + 1 })
b <- reactive({ input$y + 1 })
```

## Examples

```r
# Example 1: Safe reactive wrapper
safe_reactive <- function(expr) {
  reactive({
    tryCatch(
      expr,
      error = function(e) {
        showNotification(paste("Error:", e$message), type = "error")
        NULL
      }
    )
  })
}

# Example 2: Using req() and validate()
server <- function(input, output, session) {
  output$summary <- renderPrint({
    req(input$file)  # Stop if no file uploaded
    validate(need(
      input$file$datapath,
      "No data available"
    ))
    summary(read.csv(input$file$datapath))
  })
}

# Example 3: Observe with error handling
observe({
  req(input$action)
  tryCatch({
    perform_action(input$action)
  }, error = function(e) {
    showNotification(paste("Failed:", e$message), type = "error")
  })
})
```

## Related Errors

- [object-not-found]({{< relref "/languages/r/object-not-found" >}}) — object not found
- [error-in-eval]({{< relref "/languages/r/error-in-eval" >}}) — evaluation errors
- [error-in-source]({{< relref "/languages/r/error-in-source" >}}) — sourcing errors
