---
title: "[Solution] Erlang Application Error"
description: "Application start/stop errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Application Error

Application start/stop errors.

### Common Causes
Missing .app file; wrong config; dependency

### How to Fix
```erlang
{application, my_app, [
    {mod, {my_app, []}},
    {modules, [my_app]},
    {vsn, "1.0"}
]}.
```

### Examples
```erlang
application:start(my_app).
application:stop(my_app).
```
