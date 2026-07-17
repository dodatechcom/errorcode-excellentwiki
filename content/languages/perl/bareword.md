---
title: "Bareword not allowed"
description: "A bareword error occurs when using an unquoted identifier that Perl interprets as a bareword string under strict mode."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `Bareword "X" not allowed while "strict subs" is in use` error occurs when you use an unquoted identifier that Perl interprets as a bareword string. This is enforced by the `strict` pragma.

## Common Causes

- Missing quotes on hash keys
- Unquoted file handle
- Typo in variable name
- Using bareword as hash key

## How to Fix

```perl
# WRONG: Bareword hash key
use strict;
my %config = (name => "Alice");
print $config{name};   # Bareword "name" not allowed

# CORRECT: Use => which autoquotes the left side
my %config = (name => "Alice");
print $config{name};
```

```perl
# WRONG: Bareword in comparison
use strict;
my $status = "ok";
if ($status == ok) {    # Bareword "ok" not allowed
    print "Valid\n";
}

# CORRECT: Quote the string
if ($status eq "ok") {
    print "Valid\n";
}
```

## Examples

```perl
# Example 1: Bareword file handle
use strict;
open(FILE, "data.txt"); # "FILE" is a bareword

# CORRECT: Use three-arg open
open(my $fh, '<', 'data.txt') or die "Cannot open: $!";

# Example 2: Bareword hash assignment
use strict;
my %hash;
$hash{key} = "value";  # Bareword "key" not allowed

# Example 3: Bareword in subroutine
use strict;
print STDOUT "hello";  # STDOUT is bareword
```

## Related Errors

- [syntax error at line X](/languages/perl/syntax-error6)
- [Undefined subroutine](/languages/perl/undefined-sub)
