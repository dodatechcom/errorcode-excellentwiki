---
title: "[Solution] Erlang Debug Trace"
description: "Debug tracing errors"
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Debug Trace

Debug tracing errors

### Common Causes
Wrong trace; too many traces

### How to Fix
```erlang
 dbg:tracer().
 dbg:p(all, c).
 dbg:tpl(my_module, my_func, x).
```

### Examples
```erlang
 dbg:stop().
```
