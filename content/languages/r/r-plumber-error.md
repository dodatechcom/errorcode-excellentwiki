---
title: "[Solution] R plumber API Error"
description: "Fix plumber API errors including endpoint failures, request parsing issues, and deployment problems in plumber APIs."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["plumber", "api", "rest", "endpoint", "web-service", "r"]
weight: 5
---

## What This Error Means

Plumber API errors occur when a plumber-defined REST API fails during request handling. This can happen due to endpoint configuration issues, request parsing failures, or runtime errors in the API code.

## Common Causes

- Endpoint function throws an error
- Invalid request body or query parameters
- Missing or incorrect Content-Type header
- Serialization issues with response objects
- CORS configuration problems

## How to Fix

```r
# WRONG: Endpoint function throws error
#* @get /data
function(req) {
  data <- read.csv(req$query$file)  # Error if file missing
}

# CORRECT: Validate inputs
#* @get /data
function(req) {
  if (is.null(req$query$file)) {
    stop("Missing 'file' parameter")
  }
  if (!file.exists(req$query$file)) {
    stop("File not found: ", req=query$file)
  }
  read.csv(req$query$file)
}
```

```r
# WRONG: Not handling serialization
#* @serializer json
#* @get /summary
function() {
  list(mean = mean(1:10), sd = sd(1:10))
}

# CORRECT: Ensure serializable output
#* @serializer json
#* @get /summary
function() {
  result <- tryCatch(
    list(mean = mean(1:10), sd = sd(1:10)),
    error = function(e) list(error = e$message)
  )
  result
}
```

```r
# WRONG: No error handling
#* @post /process
function(body) {
  process_data(body)  # May throw unhandled error
}

# CORRECT: Wrap in tryCatch
#* @post /process
function(body) {
  tryCatch(
    {
      result <- process_data(body)
      list(status = "success", data = result)
    },
    error = function(e) {
      plumber::list_error(
        message = e$message,
        status = 400
      )
    }
  )
}
```

## Examples

```r
# Example 1: Basic plumber setup with error handling
# plumber.R
#* @apiTitle Data API
#* @apiDescription A simple data API with error handling

#* Echo the message
#* @param msg The message to echo
#* @get /echo
function(msg = "no message") {
  list(message = msg)
}

# Example 2: Run plumber API
library(plumber)
pr <- plumber::plumb("plumber.R")
pr$run(port = 8000)

# Example 3: Test endpoint with error handling
tryCatch(
  httr::GET("http://localhost:8000/echo?msg=hello"),
  error = function(e) cat("Connection failed:", e$message, "\n")
)
```

## Related Errors

- [error-in-source]({{< relref "/languages/r/error-in-source" >}}) — sourcing R scripts
- [error-in-read.csv]({{< relref "/languages/r/error-in-read.csv" >}}) — CSV reading errors
- [error-in-eval]({{< relref "/languages/r/error-in-eval" >}}) — evaluation errors
