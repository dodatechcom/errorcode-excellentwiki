---
title: "[Solution] R YAML Header Error"
description: "YAML header syntax errors in R Markdown."
languages: ["r"]
error-types: ["language-error"]
severities: ["error"]
---

# R YAML Header Error

YAML header syntax errors in R Markdown.

### Common Causes
Invalid syntax; wrong indentation; missing quotes

### How to Fix
```yaml
---
title: "My Document"
author: "Author"
output: html_document
---
```

### Examples
```yaml
---
title: "Report"
output:
  html_document:
    toc: true
---
```

