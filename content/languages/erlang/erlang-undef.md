---
title: "undef Function Error in Erlang"
description: "Erlang raises undef when calling a function that is not defined or not loaded"
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `undef` error occurs when calling a function that does not exist in the specified module, or when the module has not been loaded. This is a common error when modules are misspelled or not compiled.

## Common Causes

- Function does not exist in module
- Module not compiled or loaded
- Typo in function or module name
- Wrong arity in function call
- Missing include or dependency

## How to Fix

Verify function exists:

```erlang
%% Check module exports
module_loaded(my_module).
%% true if loaded

%% Check function exists
erlang:function_exported(my_module, my_function, 1).
```

Ensure module is compiled and loaded:

```bash
erlc my_module.erl
erl -noshell -eval "code:load_file(my_module), halt()."
```

Use -compile(export_all) for debugging:

```erlang
-module(my_module).
-compile(export_all).

my_function(X) -> X * 2.
```

Check function arity:

```erlang
%% If my_func/1 exists but you call my_func/2
my_module:my_func(Arg1, Arg2).
%% undef error - wrong arity
```

## Examples

```erlang
nonexistent_module:func().
%% ** error: undef
%%     in function  nonexistent_module:func/0
```

## Related Errors

- [badarg]({{< relref "/languages/erlang/badarg" >}})
- [badmatch]({{< relref "/languages/erlang/badmatch" >}})
