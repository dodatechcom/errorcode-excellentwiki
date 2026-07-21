---
title: "[Solution] Erlang Try/Catch"
description: "try-catch expression errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Try/Catch

try-catch expression errors.

### Common Causes
Missing of; wrong exception class

### How to Fix
```erlang
try risky_function()
catch
    error:Reason -> {error, Reason};
    exit:Reason -> {exit, Reason};
    throw:Value -> {thrown, Value}
end.
```

### Examples
```erlang
try
    list:nth(10, ShortList)
catch
    error:badarg -> {error, "bad index"};
    _:_ -> {error, "unknown"}
end.
```
