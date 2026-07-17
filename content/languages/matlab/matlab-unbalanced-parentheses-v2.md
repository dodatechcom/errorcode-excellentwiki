---
title: "[Solution] MATLAB: Unbalanced parentheses or brackets"
description: "Fix MATLAB syntax errors from unbalanced parentheses, brackets, or curly braces."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

MATLAB parses expressions for matching delimiters. Unbalanced parentheses, square brackets, or curly braces prevent the code from running.

## Common Causes

- Missing closing parenthesis
- Extra closing parenthesis
- Mismatched bracket types
- String containing unmatched delimiters
- Multi-line expression not properly continued

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

```matlab
% WRONG: Multi-line without continuation
result = 1 + 2
    + 3 + 4;   % Error: need ...

% CORRECT: Use continuation character
result = 1 + 2 + ...
    3 + 4;
```

```matlab
% CORRECT: Count delimiters
% Use editor highlighting to match:
% - Parentheses ()
% - Brackets []
% - Braces {}
```

```matlab
% CORRECT: Complex expressions
result = sin(pi/2) + ...
    cos(pi/4) * ...
    (1 + 2);
```

## Related Errors

- [Invalid Function Handle](matlab-invalid-function-handle-v2) - handle syntax
- [Undefined Function](matlab-undefined-function-v2) - function errors
- [Index Out of Range](matlab-index-out-of-range-v2) - array bounds
