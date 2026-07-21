---
title: "Record include file error in Erlang module"
description: "Fix Erlang record include file errors when .hrl files are missing or have incorrect paths."
languages: ["erlang"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

This error occurs when an `-include` or `-include_lib` directive references a header file that the compiler cannot find, or when the header file contains syntax errors that prevent record definitions from being parsed.

## Common Causes

- Header file path is incorrect or relative to the wrong directory
- Using `-include` instead of `-include_lib` for library dependencies
- The .hrl file contains syntax errors
- Missing the application directory prefix when using `-include_lib`
- Circular include dependencies between header files

## How to Fix

```erlang
%% WRONG: Incorrect relative path
-include("records.hrl").  %% file is in ../include/

%% CORRECT: Use proper relative path
-include("../include/records.hrl").
```

```erlang
%% WRONG: Using -include for a library
-include("mnesia/include/mnesia.hrl").

%% CORRECT: Use -include_lib for OTP libraries
-include_lib("mnesia/include/mnesia.hrl").
```

## Examples

```erlang
%% Example 1: Standard OTP header inclusion
-module(my_server).
-include_lib("stdlib/include/qlc.hrl").
-include_lib("kernel/include/file.hrl").
-export([start/0]).

%% Example 2: Project-specific header
-record(config, {host, port, timeout}).
-include("config.hrl").

%% Example 3: Conditional include
-ifndef(LOG_HRL).
-define(LOG_HRL, true).
-include("log.hrl").
-endif.
```

## Related Errors

- [Macro undef error](erl-macro-undef) -- macros defined in missing header files
- [Preprocessor error](erl-preprocessor) -- other preprocessor issues
