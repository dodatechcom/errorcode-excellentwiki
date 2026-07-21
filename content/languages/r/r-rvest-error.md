---
title: "[Solution] R rvest Web Scraping Error"
description: "rvest scraping errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R rvest Web Scraping Error

rvest scraping errors.

### Common Causes
Page changed; anti-scraping; wrong selector

### How to Fix
```r
library(rvest)
page <- read_html(url)
titles <- page %>% html_elements("h1") %>% html_text()
```

### Examples
```r
page <- read_html("https://example.com")
page %>% html_element("title") %>% html_text()
```
