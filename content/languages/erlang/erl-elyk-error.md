---
title: "[Solution] Erlang Elixir Interop"
description: "Elixir/Erlang interop errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Elixir Interop

Elixir/Erlang interop errors.

### Common Causes
Wrong module; atom differences

### How to Fix
```erlang
% Erlang calling Elixir
'Elixir.MyModule':function(args).
```

### Examples
```erlang
% Elixir calling Erlang
:erlang_module.function(args)
```
