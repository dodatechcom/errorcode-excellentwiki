---
title: "[Solution] Erlang Application Structure"
description: "Application structure errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Application Structure

Application structure errors.

### Common Causes
Missing .app.src; wrong modules

### How to Fix
```erlang
{application, my_app, [
    {description, "My App"},
    {vsn, "0.1.0"},
    {modules, []},
    {applications, [kernel, stdlib]},
    {mod, {my_app, []}}
]}.
```

### Examples
```erlang
% In my_app.erl
-behaviour(application).
start(_StartType, _StartArgs) -> my_sup:start_link().
stop(_State) -> ok.
```
