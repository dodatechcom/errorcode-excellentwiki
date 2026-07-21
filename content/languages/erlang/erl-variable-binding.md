---
title: "[Solution] Erlang Variable Binding"
description: "Variable already bound or not bound."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Variable Binding

Variable already bound or not bound.

### Common Causes
Pattern match failure; reassignment

### How to Fix
```erlang
X = 5,
X = 10.  % Error - already bound
```

### Examples
```erlang
X = 5,
Y = X + 1.  % OK
```
