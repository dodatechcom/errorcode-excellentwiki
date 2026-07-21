---
title: "Regex compilation error in Erlang re module"
description: "Fix Erlang regex compilation errors when using the re module with invalid regular expression patterns."
languages: ["erlang"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A regex compilation error is returned by the `re` module when the provided regular expression pattern is syntactically invalid. The error typically includes the position in the pattern where parsing failed.

## Common Causes

- Unmatched parentheses or brackets in the pattern
- Using unsupported regex syntax for the PCRE engine
- Escaped characters that are not special (e.g., `\[` without need)
- Invalid quantifier syntax like `*{2,5}` instead of `{2,5}`
- Forgetting to escape special characters in string literals

## How to Fix

```erlang
%% WRONG: Unmatched parenthesis
{ok, Re} = re:compile("(hello world").
%% error: missing closing parenthesis

%% CORRECT: Balance parentheses
{ok, Re} = re:compile("(hello world)").
```

```erlang
%% WRONG: Invalid quantifier
{ok, Re} = re:compile("a*+").
%% error: nothing to repeat

%% CORRECT: Use proper possessive quantifier syntax
{ok, Re} = re:compile("a++").
```

## Examples

```erlang
%% Example 1: Compile and match
{ok, Re} = re:compile("^[a-z]+@[a-z]+\\.com$"),
{match, _} = re:run("alice@example.com", Re).

%% Example 2: Inline flags
{ok, Re} = re:compile("hello\\s+world", [caseless]),
{match, _} = re:run("Hello World", Re).

%% Example 3: Using replace
{ok, Re} = re:compile("\\d+"),
Result = re:replace("abc123def456", Re, "NUM", [{return, list}]).
```

## Related Errors

- [String error](erl-string-error) -- related string processing issues
- [IO error](erl-io-error) -- output formatting problems
