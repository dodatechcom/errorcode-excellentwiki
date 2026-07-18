---
title: "[Solution] Perl Moo Moose Construction Error Fix"
description: "Fix Perl Moo/Moose object construction errors. Learn why OO attribute setup fails and how to build correct Moose and Moo classes."
languages: ["perl"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Perl Moo/Moose construction error occurs when object creation fails during attribute validation, type checking, or required attribute enforcement. Moo and Moose provide powerful OO frameworks for Perl, but strict attribute definitions can cause errors if not handled properly.

## Why It Happens

- A required attribute was not provided during construction
- A value fails a type constraint (e.g., passing a string where Int is expected)
- An unknown attribute is passed to the constructor
- A `before` or `after` method modifier throws an error
- An attribute default or builder produces an invalid value
- The class has circular dependencies with other Moo/Moose classes
- A `coerce` rule fails to convert the input value

## How to Fix It

### Provide all required attributes

```perl
# WRONG: Missing required attribute
package User;
use Moo;
has name => (is => 'ro', required => 1);
has email => (is => 'ro', required => 1);

my $user = User->new(name => "Alice");  # error: email required

# CORRECT: Provide all required attributes
my $user = User->new(name => "Alice", email => "alice@example.com");
```

### Use correct type constraints

```perl
# WRONG: Type mismatch
package Config;
use Moo;
has port => (is => 'ro', isa => 'Int');

my $config = Config->new(port => "abc");  # type error

# CORRECT: Provide correct types
my $config = Config->new(port => 8080);
```

### Handle constructor argument errors

```perl
# CORRECT: Moo/Moose validates constructor arguments
# Use 'handles' or 'init_arg' to control attribute naming
package API;
use Moo;
has api_key => (is => 'ro', init_arg => 'apiKey');
has timeout => (is => 'ro', default => sub { 30 });

# Constructor accepts 'apiKey' not 'api_key'
my $api = API->new(apiKey => "secret123");
```

### Use BUILD for custom validation

```perl
# CORRECT: Add custom validation in BUILD
package DateRange;
use Moo;
has start => (is => 'ro', required => 1);
has end => (is => 'ro', required => 1);

sub BUILD {
    my ($self, $args) = @_;
    if ($self->start > $self->end) {
        die "Start date must be before end date";
    }
}

my $range = DateRange->new(
    start => "2025-01-01",
    end => "2025-12-31"
);
```

### Use coercions for flexible input

```perl
# CORRECT: Coerce input to the correct type
package Config;
use Moo;
use Types::Standard qw(Int Str);

has port => (
    is => 'ro',
    isa => Int,
    coerce => sub { Int->coerce($_[0]) },
);

# Accepts both "8080" and 8080
my $config = Config->new(port => "8080");
```

### Handle Moo vs Moose compatibility

```perl
# CORRECT: Choose the right framework
# Moo is lightweight, Moose is full-featured
# Use Moo for speed, Moose for advanced features

# Moo (lightweight)
package SimpleClass;
use Moo;
has name => (is => 'ro');

# Moose (full-featured)
package ComplexClass;
use Moose;
has name => (is => 'ro', predicate => 'has_name');
has builder => (is => 'ro', builder => '_build_name');
sub _build_name { "default" }
```

## Common Mistakes

- Confusing Moo and Moose syntax (they are mostly compatible but not identical)
- Not using `required => 1` for attributes that must be provided
- Forgetting that Moo/Moose constructors are case-sensitive for attribute names
- Not providing default values for optional attributes that need initialization
- Using Moose features (like `extends` without parentheses) in Moo code

## Related Pages

- [Perl Runtime Error](perl-runtime-error) - general runtime issue
- [Perl Compilation Error](perl-compilation-error) - compile error
- [Perl Hash Reference Error](perl-hash-reference-error) - reference issue
- [Perl Module Not Found](perl-module-not-found-v2) - module not found
