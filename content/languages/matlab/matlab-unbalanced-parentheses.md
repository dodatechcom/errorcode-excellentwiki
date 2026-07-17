---
title: "[Solution] MATLAB Unbalanced Parentheses or Brackets"
description: "Fix MATLAB errors from unbalanced parentheses, brackets, or braces in expressions."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["parentheses", "brackets", "braces", "syntax", "matlab"]
weight: 5
---

## What This Error Means

MATLAB parses expressions for matching delimiters. Unbalanced parentheses, square brackets, or curly braces prevent the code from running.

## Common Causes

- Missing closing parenthesis
- Extra closing parenthesis
- Mismatched bracket types
- String containing unmatched delimiters

## How to Fix

```matlab
% WRONG: Missing closing paren
result = (1 + 2 * 3;   % Syntax error

% CORRECT: Balanced parens
result = (1 + 2) * 3;   % 9
```

```matlab
% WRONG: Mismatched brackets
a = [1, 2, 3);
b = [1, 2, 3];

% CORRECT: Use matching brackets
a = [1, 2, 3];
b = {1, 2, 3};   % cell array uses curly braces
```

## Examples

```matlab
x = sin(pi/2;          % Missing closing paren
y = [1 2 3];           % Correct
z = {1, 2, 3};         % Correct cell array
```

## Related Errors

- [Invalid Function Handle](matlab-invalid-function-handle) - handle syntax errors
- [Undefined Function](matlab-undefined-function) - function errors
