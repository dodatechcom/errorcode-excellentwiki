---
title: "[Solution] Perl Runtime Error - Subroutine Not Found"
description: "Fix Perl runtime errors when subroutines are not found or called incorrectly. Handle undefined functions and calling conventions."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["runtime", "subroutine", "undefined", "call", "perl"]
weight: 5
---

## What This Error Means

A Perl runtime error occurs when the script fails during execution. Common runtime errors include calling undefined subroutines, using undefined values, and file operation failures.

## Common Causes

- Calling a subroutine that doesn't exist
- Missing module with function
- Wrong number of arguments to subroutine
- Using undefined variable as function argument
- Typo in subroutine name

## How to Fix

```perl
# WRONG: Calling undefined subroutine
use strict;
use warnings;
my_greeting();  # Error: Undefined subroutine

# CORRECT: Define subroutine first
sub my_greeting {
    print "Hello!\n";
}
my_greeting();
```

```perl
# WRONG: Missing module import
use strict;
use warnings;
my $csv = Text::CSV->new();  # Error if Text::CSV not loaded

# CORRECT: Use module first
use Text::CSV;
my $csv = Text::CSV->new({ binary => 1 });
```

```perl
# WRONG: Wrong argument count
sub add($$) {
    my ($a, $b) = @_;
    return $a + $b;
}
add(1, 2, 3);  # Warning with signatures

# CORRECT: Use proper signatures
sub add {
    my ($a, $b) = @_;
    return $a + $b;
}
add(1, 2);
```

## Examples

```perl
# Example 1: Autoload for lazy loading
sub AUTOLOAD {
    my $method = $AUTOLOAD;
    $method =~ s/.*:://;
    print "Calling method: $method\n";
}

# Example 2: Check if subroutine exists
if (defined &my_function) {
    my_function();
} else {
    die "Function not defined";
}

# Example 3: Safe subroutine call
sub safe_call {
    my ($subref, @args) = @_;
    if (ref($subref) eq 'CODE') {
        return $subref->(@args);
    }
    die "Not a code reference";
}
```

## Related Errors

- [perl-undefined-value]({{< relref "/languages/perl/perl-undefined-value" >}}) — undefined value
- [perl-compilation-error]({{< relref "/languages/perl/perl-compilation-error" >}}) — syntax error
- [perl-file-not-found]({{< relref "/languages/perl/perl-file-not-found" >}}) — file not found
