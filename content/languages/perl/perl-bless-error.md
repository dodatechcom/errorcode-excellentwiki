---
title: "[Solution] Perl bless Constructor Error Fix"
description: "Fix Perl bless errors when creating objects. Learn proper object construction with bless."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1013
---

## What This Error Means

A `bless` error occurs when using `bless` to turn a reference into an object. The most common issue is blessing a non-reference value or blessing into a non-existent package.

## Common Causes

- Calling `bless` on a non-reference (bare value like string or number)
- Blessing into a package name that doesn't exist
- Forgetting to use a reference as the first argument
- Blessing into an incorrect package name (typo)
- Not returning the blessed reference from the constructor

## How to Fix

```perl
# WRONG: Blessing a non-reference
my $obj = bless "hello", "MyClass";  # String is not a reference

# CORRECT: Bless a reference
my $obj = bless {}, "MyClass";  # Hash reference
my $obj = bless [], "MyClass";  # Array reference
my $obj = bless \my $scalar, "MyClass";  # Scalar reference
```

```perl
# WRONG: Constructor that doesn't return blessed ref
package MyClass;
sub new {
    my $class = shift;
    my $self = { name => shift };
    # Forgot to bless and return!
}

# CORRECT: Proper constructor
sub new {
    my $class = shift;
    my $self = { name => shift // 'default' };
    return bless $self, $class;
}
```

```perl
# WRONG: Blessing into misspelled package name
package MyClass;
sub new {
    my $class = shift;
    bless {}, "MyClas";  # Typo - not the same package
}

# CORRECT: Use the class parameter
sub new {
    my $class = shift;
    bless {}, $class;  # Uses the actual calling class
}
```

```perl
# WRONG: Blessing without initialization
sub new {
    my $class = shift;
    my $self = bless {}, $class;
    # No initialization - accessing properties will return undef
}

# CORRECT: Initialize all properties
sub new {
    my $class = shift;
    my %args = @_;
    my $self = {
        name  => $args{name}  // '',
        email => $args{email} // '',
    };
    return bless $self, $class;
}
```

## Examples

```perl
package Person;
sub new {
    my $class = shift;
    my %params = @_;
    my $self = {
        first_name => $params{first} // 'Unknown',
        last_name  => $params{last}  // 'Unknown',
    };
    return bless $self, $class;
}

sub full_name {
    my $self = shift;
    return "$self->{first_name} $self->{last_name}";
}

package main;
my $p = Person->new(first => "Alice", last => "Smith");
print $p->full_name;  # Alice Smith
```

## Related Errors

- [Perl reference error](perl-reference-error) - reference issue
- [Perl bareword error](bareword) - bareword issue
- [Perl undefined value](perl-undefined-value) - undefined value
