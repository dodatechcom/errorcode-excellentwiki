---
title: "[Solution] Perl OO Tutorial Inheritance Error Fix"
description: "Fix Perl object-oriented programming errors. Learn proper inheritance, method resolution, and OO patterns."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1021
---

## What This Error Means

An OO error in Perl occurs when working with object-oriented programming constructs. Common issues include incorrect `@ISA` setup, method resolution order problems, and calling parent constructors incorrectly.

## Common Causes

- Setting up `@ISA` incorrectly for inheritance
- Forgetting to call `SUPER::` methods in overridden methods
- Method resolution order (MRO) confusion with multiple inheritance
- Using `bless` incorrectly in constructors
- Not using `$class->new` or `package->new` correctly

## How to Fix

```perl
# WRONG: Incorrect @ISA setup
package Dog;
@ISA = ('Animal');  # Should be our or use vars
sub speak { print "Woof\n"; }

# CORRECT: Use our for package variables
package Dog;
use parent 'Animal';  # Modern way
sub speak { print "Woof\n"; }
```

```perl
# WRONG: Calling parent method incorrectly
package Dog;
use parent 'Animal';

sub speak {
    my $self = shift;
    SUPER::speak($self);  # Wrong syntax
    print "Woof\n";
}

# CORRECT: Use SUPER:: in method call
sub speak {
    my $self = shift;
    $self->SUPER::speak(@_);
    print "Woof\n";
}
```

```perl
# WRONG: Method resolution order with multiple inheritance
package FlyingFish;
@ISA = ('Fish', 'Bird');  # Fish methods take precedence

# CORRECT: Use mro pragma to control resolution
package FlyingFish;
use parent 'Fish', 'Bird';
use mro 'c3';  # C3 linearization
# Now Bird methods come before Fish
```

```perl
# WRONG: Constructor that doesn't support inheritance
package Base;
sub new {
    bless {}, 'Base';  # Hardcoded class name
}

package Derived;
use parent 'Base';
my $obj = Derived->new();  # Blessed into 'Base', not 'Derived'

# CORRECT: Use the class parameter
package Base;
sub new {
    my $class = shift;
    bless {}, $class;  # Uses actual calling class
}
```

## Examples

```perl
package Animal;
sub new {
    my $class = shift;
    my $self = { name => shift // 'unknown' };
    return bless $self, $class;
}
sub speak { my $self = shift; print "$self->{name} makes noise\n" }

package Dog;
use parent 'Animal';
sub speak {
    my $self = shift;
    $self->SUPER::speak;
    print "$self->{name} barks\n";
}

my $dog = Dog->new("Rex");
$dog->speak;  # Rex makes noise \n Rex barks
```

## Related Errors

- [Perl can override error](perl-can-override-error) - can() issue
- [Perl autoloader error](perl-autoloader-error) - autoloader issue
- [Perl blessing error](bareword) - blessing issue
