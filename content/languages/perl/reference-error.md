---
title: "Can't use string as HASH"
description: "A reference error occurs when attempting to use a value as a reference when it's not a reference."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `Can't use string as HASH reference` error is raised when you try to dereference a scalar value as a hash reference, but the value is actually a string or other non-reference type. This commonly happens with incorrect data structures.

## Common Causes

- Treating string as hash reference
- Wrong data structure assumptions
- Missing reference creation
- Incorrect dereferencing syntax

## How to Fix

```perl
# WRONG: Using string as hash
my $str = "hello";
print $str->{key};  # Can't use string as HASH reference

# CORRECT: Create hash reference
my $hash = { key => "value" };
print $hash->{key};
```

```perl
# WRONG: Wrong dereferencing
my @arr = (1, 2, 3);
print $arr->{0};  # Can't use array as HASH

# CORRECT: Use correct dereferencing
my @arr = (1, 2, 3);
print $arr[0];
# or
print $arr->[0];
```

## Examples

```perl
# Example 1: String as hash
my $data = "not a hash";
print $data->{name};  # Can't use string as HASH reference

# Example 2: Array as hash
my @list = (1, 2, 3);
print $list->{key};  # Can't use array as HASH reference

# Example 3: Undefined reference
my $ref;
print $ref->{key};  # Can't use undefined value as HASH reference
```

## Related Errors

- [Glob failed](/languages/perl/glob-error)
- [die error](/languages/perl/die-error)
