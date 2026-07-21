---
title: "[Solution] Spring Multipart Upload Error"
description: "File upload failing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

File upload failing.

## Common Causes

Wrong config.

## How to Fix

Configure multipart.

## Example

```properties
spring.servlet.multipart.max-file-size=10MB
spring.servlet.multipart.max-request-size=10MB
```
