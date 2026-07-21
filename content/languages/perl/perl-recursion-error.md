---
title: "[Solution] Perl Recursion Limit Error"
description: "Fix Perl infinite recursion errors when subroutines call themselves without a proper base case."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Infinite recursion errors occur when a Perl subroutine calls itself without reaching a termination condition, exhausting the call stack.

## Common Causes

- Missing or unreachable base case in recursive function
- Recursive call with same arguments
- Data structure causing infinite traversal
- Mutual recursion without termination

## How to Fix

### 1. Ensure proper base case

```perl
# WRONG: No base case
sub factorial {
    my ($n) = @_;
    return $n * factorial($n - 1);  # infinite recursion
}

# CORRECT: Base case
sub factorial {
    my ($n) = @_;
    return 1 if $n <= 1;
    return $n * factorial($n - 1);
}
```

### 2. Add recursion depth limit

```perl
sub recursive {
    my ($depth) = @_;
    return if $depth > 100;  # guard
    recursive($depth + 1);
}
```

## Examples

```perl
use strict;
use warnings;

sub fibonacci {
    my ($n) = @_;
    return $n if $n <= 1;
    return fibonacci($n - 1) + fibonacci($n - 2);
}

print fibonacci(10), "\n";  # 55
```

## Related Errors

- [Runtime error](/languages/perl/perl-runtime-error)
- [Undefined value](/languages/perl/undefined-value)
- [Reference error](/languages/perl/reference-error)
