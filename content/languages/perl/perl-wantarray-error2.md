---
title: "[Solution] Perl Wantarray Error"
description: "Fix Perl wantarray errors when subroutines need to return different values based on calling context."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Wantarray errors occur when a subroutine does not properly distinguish between list and scalar calling context.

## Common Causes

- Subroutine returns list when scalar expected
- Using wantarray without checking for undef
- Not handling void context
- Inconsistent return values across contexts

## How to Fix

### 1. Handle all contexts properly

```perl
sub get_data {
    my @data = (1, 2, 3);
    if (!defined wantarray) {
        # void context
        return;
    } elsif (wantarray) {
        return @data;
    } else {
        return scalar @data;
    }
}
```

### 2. Always return something in scalar context

```perl
# WRONG: Returns empty in scalar context
sub get_value { return () if wantarray; }

# CORRECT: Return meaningful scalar
sub get_value { return wantarray ? () : 0; }
```

## Examples

```perl
use strict;
use warnings;

sub context_aware {
    my @items = qw(a b c);
    return wantarray ? @items : scalar @items;
}

my @list = context_aware();
my $count = context_aware();
print "List: @list, Count: $count\n";
```

## Related Errors

- [Undefined value](/languages/perl/undefined-value)
- [Return value error](/languages/perl/perl-runtime-error)
- [Compilation error](/languages/perl/perl-compilation-error)
