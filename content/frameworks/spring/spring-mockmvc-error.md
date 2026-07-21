---
title: "[Solution] Spring MockMvc Error"
description: "MockMvc not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

MockMvc not working.

## Common Causes

Wrong setup.

## How to Fix

Setup correctly.

## Example

```java
@Autowired private MockMvc mvc;
@Test void t() throws Exception { mvc.perform(get("/api")).andExpect(ok()); }
```
