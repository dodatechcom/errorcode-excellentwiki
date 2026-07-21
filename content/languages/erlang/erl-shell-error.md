---
title: "[Solution] Erlang Shell Error"
description: "Interactive shell errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Shell Error

Interactive shell errors.

### Common Causes
Module not loaded; wrong command

### How to Fix
```erlang
1> c(my_module).
2> my_module:func(5).
```

### Examples
```erlang
$ erl -pa ./ebin
1> application:start(my_app).
```
