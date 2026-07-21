---
title: "[Solution] Spring StreamingResponseBody Error"
description: "Streaming response not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Streaming response not working.

## Common Causes

Wrong return type.

## How to Fix

Use StreamingResponseBody.

## Example

```java
@GetMapping(value = "/dl", produces = "application/octet-stream")
public StreamingResponseBody dl() {
    return os -> Files.copy(path, os);
}
```
