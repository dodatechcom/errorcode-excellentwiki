---
title: "[Solution] Spring Controller Advice Error"
description: "Global handler not catching."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Global handler not catching.

## Common Causes

Wrong type.

## How to Fix

Handle correct type.

## Example

```java
@RestControllerAdvice
public class EH {
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<String> h(ResourceNotFoundException e) {}
}
```
