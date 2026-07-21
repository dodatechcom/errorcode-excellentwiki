---
title: "Macro undefined error in Erlang preprocessor"
description: "Resolve Erlang undefined macro errors caused by missing include files or typos in macro names."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

When the Erlang preprocessor encounters a macro call with `-define(MACRO, ...)` or `?MACRO` and the macro has not been defined (either in the current file or via an included header file), the compiler reports an undefined macro error.

## Common Causes

- Typo in the macro name when calling `?MacroName`
- Forgetting to include the header file that defines the macro
- Circular include dependencies that prevent the macro from being seen
- Using `-undef(MACRO)` and then trying to reference it later
- Conditional macros inside `-ifdef` blocks that were never defined

## How to Fix

```erlang
%% WRONG: Macro name typo
-define(MAX_RETRIES, 3).
io:format("~p~n", [?MAX_RERTIES]).
%% error: undefined macro 'MAX_RERTIES'

%% CORRECT: Match the exact macro name
io:format("~p~n", [?MAX_RETRIES]).
```

```erlang
%% WRONG: Missing include
-module(my_module).
-export([start/0]).
start() -> ?APP_NAME.
%% error: undefined macro 'APP_NAME'

%% CORRECT: Include the header
-module(my_module).
-include("app_config.hrl").
-export([start/0]).
start() -> ?APP_NAME.
```

## Examples

```erlang
%% Example 1: Macro defined in another file
%% config.hrl: -define(DB_HOST, "localhost").
-module(db).
%% Missing: -include("config.hrl").
connect() -> ?DB_HOST.  %% undefined macro error

%% Example 2: Conditional macro
-ifdef(TEST_MODE).
-define(LOG(Msg), io:format(Msg)).
-endif.
%% If TEST_MODE is not defined and you call ?LOG, it fails

%% Example 3: Macro defined after use
-define(VERSION, "1.0").
io:format(?VERSION).     %% this works
-define(VERSION, "2.0"). %% redefining is a warning, not error
```

## Related Errors

- [Preprocessor error](erl-preprocessor) -- other preprocessor directive problems
- [Include error](erl-macro-error) -- issues with header file inclusion
