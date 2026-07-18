---
title: "[Solution] Fix undefined function Module Function Arity in Erlang"
description: "Resolve undef function errors in Erlang by verifying module exports with -export, ensuring proper compilation, and checking function arity correctness."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 8
---

## What This Error Means

An `undef` error occurs when calling a function that does not exist in the specified module, or when the module has not been compiled or loaded. This is one of the most common runtime errors in Erlang.

The error appears as:

```erlang
** error: undef
    in function  my_module:my_function/1
    in call from shell.erl
```

## Why It Happens

This error occurs due to missing or unloaded modules:

- Module is not compiled or compiled with errors
- Function does not exist with the specified arity
- Module is not loaded in the VM
- Typo in function or module name
- Missing `-export` declaration for the function
- Module not included in the application release

## How to Fix It

Verify the function exists and is exported:

```erlang
%% Check if function exists
erlang:function_exported(my_module, my_function, 1).

%% Check if module is loaded
code:which(my_module).
%% Returns beam file path if loaded, 'non_existent' otherwise
```

Compile and load the module:

```bash
erlc my_module.erl
erl -noshell -eval "code:load_file(my_module), halt()."
```

Use `-compile(export_all)` during development:

```erlang
-module(my_module).
-compile(export_all).

my_function(X) ->
    X * 2.
```

Ensure proper `-export` declarations:

```erlang
-module(my_module).
-export([my_function/1]).

my_function(X) ->
    X * 2.
```

Check function arity carefully:

```erlang
%% If my_func/1 exists but you call my_func/2
my_module:my_func(Arg1, Arg2).
%% undef error - wrong arity

%% Correct call
my_module:my_func(Arg1).
```

Verify module in the release path:

```erlang
%% In rebar3 project, ensure module is in src/
%% In mix project, ensure module is in lib/
code:add_pathz("/path/to/beam/files").
```

## Common Mistakes

- Forgetting to add `-export` for functions that need to be called externally
- Not recompiling after changing function signatures or arity
- Assuming beam files are automatically found without proper code paths
- Confusing module names (case-sensitive: `my_module` vs `my_Module`)
- Not including modules in release builds or application resource files

## Related Pages

- [badarg: bad argument in function call](/languages/erlang/badarg)
- [badmatch: no match of right hand side value](/languages/erlang/badmatch)
- [Function clause matching failed](/languages/erlang/erlang-functionclause)
