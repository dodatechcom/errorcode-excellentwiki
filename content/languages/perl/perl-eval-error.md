---
title: "[Solution] Perl Eval Error"
description: "Fix Perl eval block errors including eval STRING vs eval BLOCK confusion and error capture issues."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Eval errors occur when eval is used incorrectly, when eval STRING executes invalid code, or when errors are not properly captured after eval.

## Common Causes

- eval STRING with syntax errors not caught
- eval BLOCK not returning proper values
- $@ not checked immediately after eval
- die inside eval modifying $_ unexpectedly

## How to Fix

### 1. Check $@ immediately after eval

```perl
# WRONG: Not checking immediately
eval { risky_operation() };
process_data();  # may alter $@
warn $@ if $@;

# CORRECT: Check immediately
eval { risky_operation() };
my $error = $@;
if ($error) {
    warn "Failed: $error";
}
```

### 2. Use eval STRING carefully

```perl
# WRONG: User input in eval STRING
eval $user_input;  # code injection risk

# CORRECT: Use eval BLOCK for code
eval { do_something($input) };
```

## Examples

```perl
use strict;
use warnings;

my $code = q{ 2 + 2 };
my $result = eval $code;
if ($@) {
    warn "Eval error: $@";
} else {
    print "Result: $result\n";
}
```

## Related Errors

- [Die error](/languages/perl/die-error)
- [Compilation error](/languages/perl/perl-compilation-error)
- [Runtime error](/languages/perl/perl-runtime-error)
