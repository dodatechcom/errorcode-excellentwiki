---
title: "[Solution] Perl Memoize Error"
description: "Fix Perl Memoize module errors when caching function results including key collision and invalid cache issues."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Memoize errors occur when the Memoize module caches incorrect results due to side effects, impure functions, or cache key collisions.

## Common Causes

- Memoizing impure function (side effects, I/O)
- Arguments not properly stringifyable for cache key
- Cache growing unbounded for recursive functions
- Memoizing reference-returning function

## How to Fix

### 1. Only memoize pure functions

```perl
# WRONG: Memoizing impure function
sub get_time {
    return time();  # changes every call
}
memoize('get_time');  # returns stale cached time

# CORRECT: Memoize pure function
sub fibonacci {
    my ($n) = @_;
    return $n if $n <= 1;
    return fibonacci($n-1) + fibonacci($n-2);
}
memoize('fibonacci');
```

### 2. Provide normalizer for complex args

```perl
memoize('my_func', NORMALIZER => sub { join(',', @_) });
```

## Examples

```perl
use strict;
use warnings;
use Memoize;

sub expensive_calc {
    my ($n) = @_;
    my $sum = 0;
    $sum += $_ for 1..$n;
    return $sum;
}

memoize('expensive_calc');
print expensive_calc(1000), "\n";  # computed once
print expensive_calc(1000), "\n";  # cached
```

## Related Errors

- [Runtime error](/languages/perl/perl-runtime-error)
- [Recursion error](/languages/perl/perl-recursion-error)
- [Compilation error](/languages/perl/perl-compilation-error)
