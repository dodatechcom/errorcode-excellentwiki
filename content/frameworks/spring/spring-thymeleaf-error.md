---
title: "[Solution] spring Thymeleaf Error"
description: "Template not rendering."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Template not rendering.

## Common Causes

Wrong syntax.

## How to Fix

Check template.

## Example

```html
<html xmlns:th="http://www.thymeleaf.org">
<body>
  <h1 th:text="${title}">Default</h1>
</body>
</html>
```
