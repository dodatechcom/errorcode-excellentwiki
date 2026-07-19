---
title: "[Solution] EvalError — Refused to Evaluate Script / Content Security Policy Fix"
description: "Fix EvalError when CSP blocks eval() or new Function(). Adjust Content Security Policy or refactor code."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# EvalError — Eval Blocked by CSP

```javascript
// Blocked by Content-Security-Policy: script-src 'self'
eval('console.log(1)');     // EvalError
new Function('return 1')();  // EvalError
```

## Fix

### Option 1: Adjust CSP
```http
Content-Security-Policy: script-src 'self' 'unsafe-eval';
```

### Option 2: Refactor to avoid eval
```javascript
// Instead of dynamic evaluation
const handlers = { add: (a, b) => a + b };
handlers[op](a, b); // instead of eval(op + '(' + a + ',' + b + ')')
```
