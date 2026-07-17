---
title: "[Solution] Perl List Util Error Fix"
description: "Fix Perl List::Util errors. Learn why List::Util functions fail and how to use them properly."
languages: ["perl"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A List::Util error occurs when functions from the List::Util module fail. This can happen due to empty lists, wrong arguments, or module not loaded.

## Common Causes

- Empty list passed to function
- Wrong number of arguments
- Module not loaded
- Non-list argument

## How to Fix

```perl
# WRONG: Empty list
use List::Util qw(sum);
my $total = sum();  # Returns undef

# CORRECT: Check for empty list
use List::Util qw(sum);
my @numbers = (1, 2, 3);
my $total = sum(@numbers) // 0;
```

```perl
# WRONG: Wrong arguments
use List::Util qw(first);
my $item = first { $_ > 5 } (1, 2, 3);  # Returns undef

# CORRECT: Check result
use List::Util qw(first);
my $item = first { $_ > 5 } (1, 2, 3, 10);
if (defined $item) {
    print "Found: $item\n";
}
```

## Examples

```perl
# Example 1: Basic List::Util
use List::Util qw(sum min max first reduce);

my @nums = (1, 2, 3, 4, 5);
print sum(@nums);   # 15
print min(@nums);   # 1
print max(@nums);   # 5

# Example 2: first with condition
my $even = first { $_ % 2 == 0 } @nums;

# Example 3: reduce for complex operations
my $product = reduce { $a * $b } 1, @nums;
```

## Related Errors

- [Perl undefined value](perl-undefined-value) - undefined value
- [Perl runtime error](perl-runtime-error) - runtime issue
- [Perl hash error](perl-hash-error) - hash error
