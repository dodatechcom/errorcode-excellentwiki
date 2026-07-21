---
title: "[Solution] Spring RestController Error"
description: "Endpoint not responding."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Endpoint not responding.

## Common Causes

Wrong annotation.

## How to Fix

Use @RestController.

## Example

```java
@RestController
@RequestMapping("/api")
public class AC {}
```
