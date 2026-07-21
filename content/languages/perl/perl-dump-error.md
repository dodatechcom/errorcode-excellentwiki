---
title: "[Solution] Perl Dump/Undump Error"
description: "Fix Perl core dump errors and Data::Dumper output formatting issues when debugging data structures."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Dump errors occur when Perl Data::Dumper produces incorrect output or when core dump (Dump) is used for binary serialization incorrectly.

## Common Causes

- Data::Dumper not imported or used without module
- Circular references causing infinite recursion in Dumper
- Dumping file handles or code references
- Undump binary incompatible with current perl

## How to Fix

### 1. Handle circular references in Dumper

```perl
# WRONG: Circular reference hangs
use Data::Dumper;
my %data;
$data{self} = \%data;
print Dumper(\%data);  # hangs

# CORRECT: Use Maxdepth
print Dumper(\%data, 'Maxdepth' => 3);
```

### 2. Filter problematic references

```perl
$Data::Dumper::Terse = 1;
$Data::Dumper::Sortkeys = 1;
print Dumper(\%data);
```

## Examples

```perl
use strict;
use warnings;
use Data::Dumper;

my @users = (
    { name => 'Alice', age => 30 },
    { name => 'Bob',   age => 25 },
);
print Dumper(\@users);
```

## Related Errors

- [Reference error](/languages/perl/reference-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [Undefined value](/languages/perl/undefined-value)
