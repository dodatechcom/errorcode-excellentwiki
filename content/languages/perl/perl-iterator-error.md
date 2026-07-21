---
title: "[Solution] Perl Iterator Error"
description: "Fix Perl iterator errors when generator functions or iterator objects produce unexpected or exhausted values."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Iterator errors occur when Perl iterator functions return undefined values, are called after exhaustion, or have incorrect closure behavior.

## Common Causes

- Iterator exhausted without checking for undef
- Closure variable modified between iterations
- Iterator returning references instead of values
- Nested iterator calls conflicting

## How to Fix

### 1. Check for undef before using

```perl
# WRONG: Not checking iterator end
while (my $item = $iterator->next) { ... }

# CORRECT: Properly check
while (defined(my $item = $iterator->next)) {
    last unless defined $item;
    process($item);
}
```

### 2. Use closures correctly

```perl
# WRONG: Closure captures loop variable
my @iters;
for my $i (1..3) {
    push @iters, sub { return $i };
}

# CORRECT: Capture current value
for my $i (1..3) {
    my $val = $i;
    push @iters, sub { return $val };
}
```

## Examples

```perl
use strict;
use warnings;

sub make_counter {
    my $count = 0;
    return sub { return $count++ };
}

my $counter = make_counter();
print $counter->(), "\n";  # 0
print $counter->(), "\n";  # 1
print $counter->(), "\n";  # 2
```

## Related Errors

- [Undefined value](/languages/perl/undefined-value)
- [Reference error](/languages/perl/reference-error)
- [Runtime error](/languages/perl/perl-runtime-error)
