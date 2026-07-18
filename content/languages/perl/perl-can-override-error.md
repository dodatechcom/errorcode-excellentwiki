---
title: "[Solution] Perl Cannot Modify Non-Lvalue Subroutine Fix"
description: "Fix Perl 'Can't modify non-lvalue subroutine' errors. Learn why lvalue restrictions exist and how to return modifiable values from subs."
languages: ["perl"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

The Perl `Can't modify non-lvalue subroutine call` error occurs when you try to assign a value to the return value of a subroutine that is not declared as an lvalue subroutine. In Perl, only lvalue subroutines can appear on the left side of an assignment operator.

## Why It Happens

- Trying to assign to the return value of a regular subroutine
- A subroutine was called in a context that expects a modifiable value
- The subroutine is not declared with the `:lvalue` attribute
- Chained assignments involving non-lvalue subroutine returns
- Using `substr` or `vec` on a value returned by a non-lvalue sub
- Attempting to modify a string returned by a function

## How to Fix It

### Declare subroutine as lvalue

```perl
# WRONG: Regular sub cannot be assigned to
sub get_name {
    return $name;
}
get_name() = "Alice";  # error: Can't modify non-lvalue subroutine

# CORRECT: Declare as lvalue sub
sub get_name :lvalue {
    return $name;
}
get_name() = "Alice";  # works
```

### Create an lvalue accessor for a hash field

```perl
# WRONG: Direct assignment to accessor
sub field {
    my $self = shift;
    return $self->{field};
}
field($obj) = "new value";  # error

# CORRECT: Use lvalue attribute
sub field :lvalue {
    my $self = shift;
    $self->{field};
}
field($obj) = "new value";  # works
```

### Use temporary variable for modification

```perl
# WRONG: Cannot modify return of substr directly
sub get_string {
    return "hello world";
}
substr(get_string(), 0, 5) = "goodbye";  # error

# CORRECT: Store in variable first
my $str = get_string();
substr($str, 0, 5) = "goodbye";
print $str;  # "goodbye world"
```

### Use lvalue for conditional returns

```perl
# CORRECT: Lvalue sub with conditional logic
sub config_value :lvalue {
    my ($self, $key) = @_;
    if (exists $self->{config}{$key}) {
        $self->{config}{$key};
    } else {
        $self->{defaults}{$key};  # may not work for assignment
    }
}

# Simpler: always modify the hash directly
$self->{config}{$key} = $new_value;
```

### Avoid lvalue subs for complex return values

```perl
# CORRECT: For complex objects, use method instead of lvalue
sub set_name {
    my ($self, $name) = @_;
    die "Name required" unless defined $name;
    $self->{name} = $name;
    return $self;
}

$obj->set_name("Alice");
```

## Common Mistakes

- Not realizing that lvalue subs bypass any validation logic in the sub
- Using lvalue subs when a setter method would be more appropriate
- Forgetting that lvalue subs return aliases, not copies
- Using `:lvalue` on subs that return temporary values
- Not understanding that lvalue attribute is not supported in all Perl versions equally

## Related Pages

- [Perl Compilation Error](perl-compilation-error) - compile error
- [Perl Runtime Error](perl-runtime-error) - runtime issue
- [Perl Moo Error](perl-moo-error) - OO framework error
- [Perl Strict Error](perl-strict-error) - strict mode violation
