---
title: "[Solution] Perl Operator Overload Error Fix"
description: "Fix Perl operator overloading errors. Learn how to use the overload pragma to define custom operators for objects."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1011
---

## What This Error Means

An operator overloading error occurs when using the `overload` pragma to define custom operator behavior for objects. Common issues include missing or invalid overload definitions and recursive overload calls.

## Common Causes

- Overloaded method that calls the original operator recursively
- Missing required overloads for comparison or stringification
- Invalid overload key names
- Overload returning wrong types for the operator

## How to Fix

```perl
# WRONG: Recursive overload
package MyNum;
use overload '+' => sub {
    my ($a, $b) = @_;
    return $a + $b;  # Infinite recursion!
};

# CORRECT: Unbless before operation
use overload '+' => sub {
    my ($a, $b) = @_;
    my $aval = ref($a) ? $a->{value} : $a;
    my $bval = ref($b) ? $b->{value} : $b;
    return bless { value => $aval + $bval }, ref($a) || __PACKAGE__;
};
```

```perl
# WRONG: Missing stringification overload
use overload '""' => sub { my $o = shift; return $o };  # Returns object, not string

# CORRECT: Return a string
use overload '""' => sub {
    my $o = shift;
    return "[$o->{value}]";
};
```

```perl
# WRONG: Overloading comparison without numeric
use overload 'cmp' => sub { ... };  # Need '<=>' too
use overload '<=>' => sub {
    my ($a, $b) = @_;
    ($a->{value} || 0) <=> ($b->{value} || 0);
};
```

```perl
# Complete overloaded class
package MyNumber;
use overload
    '+'  => sub { my ($a, $b) = @_; _arith($a, $b, '+') },
    '-'  => sub { my ($a, $b) = @_; _arith($a, $b, '-') },
    '*'  => sub { my ($a, $b) = @_; _arith($a, $b, '*') },
    '""' => sub { my $o = shift; "[$o->{value}]" },
    '0+' => sub { my $o = shift; $o->{value} },
    fallback => 1;

sub new { bless { value => $_[1] // 0 }, shift }
sub _arith {
    my ($a, $b, $op) = @_;
    my $va = ref($a) ? $a->{value} : $a;
    my $vb = ref($b) ? $b->{value} : $b;
    my $result = eval "$va $op $vb";
    return bless { value => $result }, ref($a) || __PACKAGE__;
}
1;

my $x = MyNumber->new(10);
my $y = MyNumber->new(5);
print $x + $y;  # [15]
```

## Examples

```perl
package MyString;
use overload
    '.'  => sub { my ($a, $b) = @_; _concat($a, $b) },
    'x'  => sub { my ($a, $b) = @_; _repeat($a, $b) },
    '""' => sub { my $o = shift; $o->{data} },
    fallback => 1;

sub new { bless { data => $_[1] // '' }, shift }
sub _concat { my ($a, $b) = @_; MyString->new($a->{data} . $b->{data}) }
sub _repeat { my ($a, $b) = @_; MyString->new($a->{data} x $b) }
1;
```

## Related Errors

- [Perl blessing error](bareword) - blessing issue
- [Perl reference error](perl-reference-error) - reference issue
- [Perl tie error](perl-tie-error) - tie binding issue
