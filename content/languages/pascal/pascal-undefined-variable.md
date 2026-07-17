---
title: "Undefined variable in Pascal"
description: "Undefined variable errors in Pascal occur when using a variable that hasn't been declared in the current scope."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Pascal requires all variables to be declared before use in a `var` section or as part of a type definition. Using an undeclared variable is a compile-time error.

## Common Causes

- Typo in variable name
- Variable declared in different scope/procedure
- Missing var declaration block
- Variable declared after first use

## How to Fix

```pascal
program UndefinedVarDemo;

// WRONG: Using undeclared variable
begin
  x := 10;   // Error: x not declared
end.
```

```pascal
// CORRECT: Declare before use
program DefinedVarDemo;

var
  x: Integer;

begin
  x := 10;
  WriteLn(x);
end.
```

```pascal
// CORRECT: Declare in each procedure that uses it
program ScopedVarDemo;

procedure DoSomething;
var
  localVar: Integer;
begin
  localVar := 42;
  WriteLn(localVar);
end;

begin
  DoSomething;
end.
```

## Examples

```pascal
program Example;
begin
  writeln(unknownVar);   // Error: undeclared identifier
end.
```

## Related Errors

- [Type Mismatch](/languages/pascal/pascal-type-mismatch) - type errors
- [Runtime Error](/languages/pascal/pascal-runtime-error) - general errors
