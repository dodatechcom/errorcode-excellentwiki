---
title: "Syntax error"
description: "A syntax error occurs when the Pascal compiler encounters code that violates the language's syntax rules."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["syntax", "compiler", "compilation", "pascal"]
weight: 5
---

## What This Error Means

A `Syntax error` in Pascal occurs when the compiler encounters code that doesn't conform to the language's syntax rules. This is a compile-time error that prevents the program from being built.

## Common Causes

- Missing semicolons
- Mismatched begin/end
- Invalid identifier usage
- Wrong operator syntax

## How to Fix

```pascal
program SyntaxErrorDemo;

begin
  WriteLn('Hello')   // Missing semicolon
  WriteLn('World');
end.
```

```pascal
program SyntaxFix;

begin
  WriteLn('Hello');
  WriteLn('World');
end.
```

```pascal
program MismatchedBeginEnd;

begin
  WriteLn('Hello');
  WriteLn('World');
end;  // Extra end
```

## Examples

```pascal
program SyntaxExample;

begin
  // Example 1: Missing semicolon
  WriteLn('Hello')
  WriteLn('World')  // syntax error

  // Example 2: Mismatched begin/end
  begin
    WriteLn('Hello');
  end;
end;  // syntax error (extra end)

  // Example 3: Invalid character
  x := 5 +& 3;  // syntax error
```

## Related Errors

- [I/O error](/languages/pascal/io-error)
- [Invalid pointer operation](/languages/pascal/invalid-pointer)
