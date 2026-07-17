---
title: "Undefined subroutine"
description: "An undefined subroutine error occurs when calling a subroutine that hasn't been defined."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

An `Undefined subroutine` error is raised when you try to call a subroutine that doesn't exist in the current scope. This typically happens with typos, missing imports, or calling subroutines before they're defined.

## Common Causes

- Typo in subroutine name
- Missing `use` or `require` for module
- Subroutine defined after it's called
- Wrong package namespace

## How to Fix

```perl
# WRONG: Typo in subroutine name
sub greet {
    print "Hello!\n";
}
greett();  # Undefined subroutine &main::greett

# CORRECT: Use correct name
greet();
```

```perl
# WRONG: Not loading module
use strict;
use warnings;
my $result = Data::Dumper::Dumper({a => 1});
# may need: use Data::Dumper;

# CORRECT: Import module first
use Data::Dumper;
my $result = Dumper({a => 1});
```

## Examples

```perl
# Example 1: Typo
sub calculate { return 42; }
my $val = calulate();  # Undefined subroutine

# Example 2: Missing module
my $obj = JSON::PP::encode_json({});  # needs: use JSON::PP;

# Example 3: Wrong package
package Foo;
sub bar { return 1; }
package main;
Foo::baz();  # Undefined subroutine &Foo::baz
```

## Related Errors

- [syntax error at line X](/languages/perl/syntax-error6)
- [Bareword not allowed](/languages/perl/bareword)
