---
title: "[Solution] Erlang Parse Tools"
description: "Parse tools (leex/yacc) errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Parse Tools

Parse tools (leex/yacc) errors.

### Common Causes
Wrong rule; token issues

### How to Fix
```erlang
% In lexer.xrl
Digit = [0-9]
{Digit}+ -> {token, {integer, list_to_integer(TokenChars)}}.
```

### Examples
```erlang
% In parser.yrl
expr -> integer : {value, $1}.
```
