---
title: "[Solution] Perl Circular Reference Error"
description: "Fix Perl circular reference errors causing memory leaks when objects reference each other in reference chains."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Circular reference errors occur when two or more data structures reference each other, preventing the garbage collector from freeing memory.

## Common Causes

- Parent object holds reference to child that references parent
- Linked list node pointing back to a previous node
- Closure capturing a reference to itself
- Hash containing self-referential key-value pair

## How to Fix

### 1. Use weak references

```perl
# WRONG: Circular reference
use strict;
my $parent = { name => 'parent' };
my $child  = { parent => $parent };
$parent->{child} = $child;  # circular reference

# CORRECT: Use Scalar::Util weaken
use strict;
use Scalar::Util qw(weaken);
my $parent = { name => 'parent' };
my $child  = { parent => $parent };
weaken($child->{parent});
$parent->{child} = $child;
```

### 2. Break cycles explicitly

```perl
# Break circular reference when done
undef $parent->{child};
undef $child->{parent};
```

## Examples

```perl
# Example 1: Circular hash references
use strict;
use Scalar::Util qw(weaken);

my %people;
$people{alice} = { name => 'Alice' };
$people{bob}   = { name => 'Bob' };
$people{alice}{friend} = $people{bob};
$people{bob}{friend}   = $people{alice};  # circular
weaken($people{alice}{friend});
```

## Related Errors

- [Reference error](/languages/perl/reference-error)
- [Undefined value](/languages/perl/undefined-value)
- [Memory related runtime error](/languages/perl/runtime-error)
