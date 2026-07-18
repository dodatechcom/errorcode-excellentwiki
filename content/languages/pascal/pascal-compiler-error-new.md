---
title: "[Solution] Pascal: compile error identifier expected"
description: "Fix Pascal compile errors by correcting syntax, adding missing semicolons, and fixing identifiers."
languages: ["pascal"]
error-types: ["compile-time-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A Pascal compile error indicating `identifier expected` means the compiler encountered a token where it expected a valid identifier (variable name, type name, function name, or keyword). This is a syntax error that prevents compilation. The error typically points to a specific location in the source code where the compiler's parser found an unexpected symbol. Common triggers include missing or extra keywords, misplaced operators, incorrect syntax in declarations, and malformed expressions.

## Why It Happens

Compile errors with `identifier expected` occur from several syntax mistakes. Placing an expression where a variable name is expected, such as using a number in a declaration without an assignment operator, triggers this error. Missing semicolons between statements can cause the parser to interpret tokens incorrectly. Extra or missing keywords like `begin`, `end`, `var`, `type`, or `procedure` produce cascading errors. Using reserved words as identifiers (such as `program`, `begin`, `end`, `var` as variable names) is not allowed. Incorrect use of the assignment operator `:=` versus the comparison operator `=` in boolean contexts confuses the parser. Malformed type declarations, such as using a colon instead of an equals sign in type definitions, also cause this error.

## How to Fix It

**Check for missing or extra keywords:**

```pascal
{ WRONG: missing 'begin' }
program BadSyntax;
var
  x: Integer;
  x := 5;  { Identifier expected - parser confused }
end.

{ CORRECT }
program GoodSyntax;
var
  x: Integer;
begin
  x := 5;
end.
```

**Fix declaration syntax:**

```pascal
program Declarations;
var
  { WRONG: using = instead of : }
  { x = Integer; }

  { CORRECT: use colon for variable declarations }
  x: Integer;

  { WRONG: using : instead of = for type declarations }
  { type MyInt : Integer; }

  { CORRECT: use = for type declarations }
type
  MyInt = Integer;
begin
  x := 42;
end.
```

**Correct assignment vs comparison operators:**

```pascal
program Operators;
var
  x, y: Integer;
  flag: Boolean;
begin
  x := 5;
  y := 10;

  { WRONG: using = for assignment }
  { x = 5; }  { identifier expected }

  { CORRECT: use := for assignment }
  x := 5;

  { CORRECT: use = for comparison in if statements }
  if x = y then
    WriteLn('Equal')
  else
    WriteLn('Not equal');
end.
```

**Avoid using reserved words as identifiers:**

```pascal
{ WRONG: using reserved words }
{ var begin: Integer; }
{ var end: Integer; }
{ program = 5; }

{ CORRECT: use valid identifiers }
program ValidIdentifiers;
var
  beginVal: Integer;
  endVal: Integer;
begin
  beginVal := 1;
  endVal := 10;
  WriteLn(beginVal, ' to ', endVal);
end.
```

**Check for typos in standard function names:**

```pascal
program StandardFunctions;
var
  s: string;
  i: Integer;
begin
  s := 'Hello';

  { WRONG: typo in Length }
  { i := Lenght(s); }

  { CORRECT }
  i := Length(s);
  WriteLn('Length: ', i);
end.


## Common Mistakes

- Confusing `:=` (assignment) with `=` (comparison or type definition)
- Using reserved Pascal keywords as variable or function names
- Missing semicolons between declarations or statements
- Forgetting that Pascal requires `begin` and `end` to delimit compound statements
- Not matching parentheses in complex expressions

## Related Pages

- [Parse error in Pascal](/languages/pascal/pascal-runtime-error-new)
- [Type mismatch in Pascal](/languages/pascal/pascal-type-mismatch-v2)
- [File not found in Pascal](/languages/pascal/pascal-file-not-found-v2)
- [Runtime error in Pascal](/languages/pascal/pascal-runtime-error-v2)
