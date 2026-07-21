---
title: "[Solution] R xml2 Parsing Error"
description: "xml2 XML parsing errors."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R xml2 Parsing Error

xml2 XML parsing errors.

### Common Causes
Malformed XML; encoding; namespace

### How to Fix
```r
library(xml2)
doc <- read_xml("file.xml")
xml_find_all(doc, "//item")
```

### Examples
```r
xml_text(xml_find_first(doc, "//title"))
```
