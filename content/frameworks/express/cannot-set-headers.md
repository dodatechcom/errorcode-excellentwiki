---
title: "Error: Cannot set headers after they are sent"
description: "Express throws this error when you attempt to set response headers after the response has already been flushed to the client."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["http", "response", "headers", "node"]
weight: 5
---

This error occurs in Express (and Node.js HTTP in general) when you try to call `res.setHeader()`, `res.redirect()`, or `res.send()` more than once on the same request. Once the response is sent, headers become immutable.

## Common Causes

- Calling `res.send()` or `res.json()` twice in the same route handler
- Calling `res.redirect()` and then not returning or throwing, so execution continues to another `res.send()`
- Nested async callbacks each trying to send a response
- Missing `return` statement after sending a response

## How to Fix

Always `return` after sending a response to stop further execution:

```javascript
app.get("/user", (req, res) => {
  if (!req.user) {
    return res.redirect("/login"); // return stops execution
  }
  res.json(req.user);
});
```

Use a guard to prevent double-sends:

```javascript
app.get("/data", (req, res) => {
  if (res.headersSent) return;
  res.json({ ok: true });
});
```

## Example

```javascript
app.get("/order", (req, res) => {
  res.send("First response");
  res.send("Second response"); // Error: Cannot set headers after they are sent
});
```

## Related Errors

- [TypeError: X is not a function]({{< relref "/frameworks/express/middleware-error" >}})
