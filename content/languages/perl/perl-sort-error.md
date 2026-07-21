---
title: "[Solution] Perl Sort Error"
description: "Fix Perl sort function errors when comparison functions are incorrectly implemented or produce unstable results."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Sort errors occur when the Perl sort function receives incorrect comparison block return values or when the default sort uses unexpected string ordering.

## Common Causes

- Sort comparison block not returning -1, 0, or 1
- Default sort using string instead of numeric comparison
- Modifying $a or $b inside sort block
- Sort comparison not transitive

## How to Fix

### 1. Return correct comparison values

```perl
# WRONG: Not returning proper values
my @sorted = sort { $a - $b } @nums;

# CORRECT: Use spaceship operator
my @sorted = sort { $a <=> $b } @nums;   # numeric
my @sorted = sort { $a cmp $b } @words;  # string
```

### 2. Do not modify $a or $b

```perl
# WRONG: Modifying $a or $b
my @sorted = sort { lc($a) cmp lc($b) } @words;

# CORRECT: Use a transform
my @sorted = sort { lc($a) cmp lc($b) } @words;
# Actually this is fine - lc does not modify $a
```

## Examples

```perl
use strict;
use warnings;

my @numbers = (5, 2, 8, 1, 9);
my @sorted = sort { $a <=> $b } @numbers;
print "Sorted: @sorted\n";  # 1 2 5 8 9

my @words = qw(cherry apple banana);
my @alpha = sort { $a cmp $b } @words;
print "Alpha: @alpha\n";  # apple banana cherry
```

## Related Errors

- [List error](/languages/perl/perl-list-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [Comparison error](/languages/perl/perl-locale-error)
