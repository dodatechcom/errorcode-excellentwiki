---
title: "syntax error at line X"
description: "A syntax error occurs when Perl encounters code that violates the language's syntax rules during parsing."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `syntax error` is raised when Perl's parser encounters code that doesn't conform to the language's syntax rules. This is a compile-time error that prevents the script from running.

## Common Causes

- Missing or mismatched parentheses, brackets, or braces
- Missing semicolons
- Invalid operator usage
- Unclosed quotes or heredocs

## How to Fix

```perl
# WRONG: Missing semicolon
my $x = 10
my $y = 20   # syntax error at line 2

# CORRECT: Add semicolons
my $x = 10;
my $y = 20;
```

```perl
# WRONG: Unclosed parenthesis
my @arr = (1, 2, 3;
# syntax error

# CORRECT: Balance parentheses
my @arr = (1, 2, 3);
```

## Examples

```perl
# Example 1: Missing closing brace
sub greet {
    print "hello";
# syntax error

# Example 2: Invalid string interpolation
my $name = "World";
my $msg = "Hello, ${name";  # syntax error

# Example 3: Wrong operator
my $x = 5 +* 3;  # syntax error
```

## Related Errors

- [Bareword not allowed](/languages/perl/bareword)
- [Undefined subroutine](/languages/perl/undefined-sub)
