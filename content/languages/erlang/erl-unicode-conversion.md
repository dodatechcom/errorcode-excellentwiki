---
title: "Unicode conversion error in Erlang string handling"
description: "Fix Erlang unicode_to_binary and unicode_to_list errors when converting strings with invalid byte sequences."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A unicode conversion error is raised when calling functions like `unicode:characters_to_binary/2` or `unicode:characters_to_list/2` on input containing invalid byte sequences for the target encoding. The conversion returns `{error, ...}` instead of the expected result.

## Common Causes

- Passing raw Latin-1 bytes to a UTF-8 conversion function
- Input containing truncated multi-byte UTF-8 sequences
- Mixing binaries with different encodings in a single list
- Using `latin1` encoding on data that contains code points above 255
- Incorrect encoding specification in the conversion function

## How to Fix

```erlang
%% WRONG: Assuming binary is valid UTF-8
Bad = <<16#FF, 16#FE>>,  %% invalid UTF-8 bytes
Result = unicode:characters_to_binary(Bad, utf8, utf8).
%% returns {error, ...}

%% CORRECT: Validate before converting
Bin = <<228, 189, 160>>,  %% valid UTF-8 for Chinese character
Result = unicode:characters_to_binary(Bin, utf8, utf8).
%% returns <<"你">> or similar valid result
```

```erlang
%% WRONG: Missing encoding argument
List = unicode:characters_to_list(<<228, 189, 160>>).
%% may return wrong result without explicit encoding

%% CORRECT: Specify source encoding
List = unicode:characters_to_list(<<228, 189, 160>>, utf8).
```

## Examples

```erlang
%% Example 1: Convert valid UTF-8 to Latin-1
Utf8 = <<"héllo">>,  %% note: é is two bytes in UTF-8
Latin = unicode:characters_to_binary(Utf8, utf8, latin1).

%% Example 2: List conversion with replacement
Input = [72, 101, 108, 108, 111],  %% "Hello" in ASCII
Output = unicode:characters_to_list(Input, latin1).

%% Example 3: Mixed encoding list causes error
Mixed = [<<"hello">>, <<228, 189, 160>>],
Result = unicode:characters_to_binary(Mixed, utf8, utf8).
```

## Related Errors

- [Unicode error](erl-unicode-error) -- other unicode handling issues
- [String error](erl-string-error) -- general string processing errors
