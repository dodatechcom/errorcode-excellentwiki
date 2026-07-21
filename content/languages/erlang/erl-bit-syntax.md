---
title: "[Solution] Erlang Bit Syntax"
description: "Bit syntax errors."
languages: ["erlang"]
error-types: ["language-error"]
severities: ["error"]
---

# Erlang Bit Syntax

Bit syntax errors.

### Common Causes
Wrong size; signed/unsigned; unit

### How to Fix
```erlang
<<X:4, Y:4>> = <<0xAB>>.
```

### Examples
```erlang
<<Len:32/big-unsigned-integer, Data:Len/binary>> = Packet.
```
