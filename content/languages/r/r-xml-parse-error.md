---
title: "[Solution] R XML Parse Error"
description: "XML content cannot be parsed."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R XML Parse Error

XML content cannot be parsed.

### Common Causes
Malformed XML; encoding issues; namespace problems

### How to Fix
```r
library(xml2)
doc <- read_xml("file.xml")
```

### Examples
```r
xml <- "<root><item>text</item></root>"
doc <- read_xml(xml)
```
