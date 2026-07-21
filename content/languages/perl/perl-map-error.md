---
title: "[Solution] Perl Map Error"
description: "Fix Perl map function errors when transforming lists incorrectly or producing unintended side effects."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Map errors occur when the map function returns unexpected results due to incorrect block syntax, missing return values, or side effects.

## Common Causes

- Map block not returning a value
- Using map for side effects instead of foreach
- Map in scalar context losing list results
- Forgetting map returns a flat list from nested structures

## How to Fix

### 1. Ensure block returns a value

```perl
# WRONG: No explicit return
my @squares = map { $_ * } @nums;

# CORRECT: Explicit return
my @squares = map { $_ * $_ } @nums;
```

### 2. Use foreach for side effects

```perl
# WRONG: Using map for side effects
map { print "$_\n" } @list;

# CORRECT: Use foreach
foreach my $item (@list) {
    print "$item\n";
}
```

## Examples

```perl
use strict;
use warnings;

my @words = qw(hello world);
my @upper = map { uc($_) } @words;
print "Uppercase: @upper\n";  # HELLO WORLD

my @lengths = map { length($_) } @words;
print "Lengths: @lengths\n";  # 5 5
```

## Related Errors

- [List error](/languages/perl/perl-list-error)
- [Grep error](/languages/perl/perl-grep-error)
- [Undefined value](/languages/perl/undefined-value)
