---
title: "[Solution] R testthat Test Error"
description: "testthat test failures."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R testthat Test Error

testthat test failures.

### Common Causes
Test data changed; expected output wrong

### How to Fix
```r
library(testthat)
test_dir("tests/testthat")
```

### Examples
```r
test_that("math works", {
  expect_equal(2 + 2, 4)
})
```
