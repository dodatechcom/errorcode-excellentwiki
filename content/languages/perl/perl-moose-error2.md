---
title: "[Solution] Perl Moose Error"
description: "Fix Perl Moose object system errors including attribute conflicts, method modifiers, and type constraint failures."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Moose errors occur when object attributes conflict, type constraints fail, or method modifiers are incorrectly applied.

## Common Causes

- Attribute name conflict in role composition
- Type constraint violation on attribute assignment
- Missing required attribute in constructor
- Method modifier on non-existent method

## How to Fix

### 1. Resolve attribute conflicts

```perl
# WRONG: Conflicting attributes in roles
# Role A has 'name', Role B has 'name'

# CORRECT: Use -excludes or rename
with 'RoleA' => { -excludes => ['name'] };
```

### 2. Handle required attributes

```perl
# WRONG: Missing required attribute
has 'id' => (is => 'ro', isa => 'Int', required => 1);
my $obj = My::Class->new();  # dies: id is required

# CORRECT: Provide required attributes
my $obj = My::Class->new(id => 42);
```

## Examples

```perl
use strict;
use warnings;
use Moose;

package Person;
has name => (is => 'ro', isa => 'Str', required => 1);
has age  => (is => 'rw', isa => 'Int');
__PACKAGE__->meta->make_immutable;

my $p = Person->new(name => 'Alice', age => 30);
print $p->name, "\n";
```

## Related Errors

- [Runtime error](/languages/perl/perl-runtime-error)
- [Module not found](/languages/perl/perl-module-not-found)
- [Compilation error](/languages/perl/perl-compilation-error)
