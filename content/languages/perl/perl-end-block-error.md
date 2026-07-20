---
title: "[Solution] Perl __END__ Token Error Fix"
description: "Fix Perl __END__ token errors. Learn how to use __END__ and __DATA__ sections properly."
languages: ["perl"]
error-types: ["syntax-error"]
severities: ["error"]
weight: 1015
---

## What This Error Means

A `__END__` token error occurs when Perl encounters an invalid `__END__` or `__DATA__` section. These tokens must appear on a line by themselves with nothing else on the line.

## Common Causes

- Extra characters on the same line as `__END__`
- Using `__END__` inside a string or code block
- Placing `__END__` before valid Perl code that won't be executed
- Confusing `__END__` with `__DATA__` for package data

## How to Fix

```perl
# WRONG: Extra characters after __END__
__END__some data  # Everything after __END__ must be on next lines
hello world
__END__

# CORRECT: __END__ on its own line
__END__
some data
hello world
```

```perl
# WRONG: __END__ inside a string
my $str = "__END__";  # This is fine, but:
if ($str eq "__END__") {
    # __END__ inside block - confusing but not an error
}

# CORRECT: __END__ only at file level
__END__
# After here is not compiled
```

```perl
# WRONG: __END__ before important code
__END__
sub important { print "won't run\n"; }  # Never compiled!
sub main { important(); }

# CORRECT: __END__ at end of file only
sub important { print "will run\n"; }
sub main { important(); }
main();
__END__
Data section follows
```

```perl
# Using __DATA__ for embedded data
package MyConfig;
__DATA__
username=admin
password=secret
timeout=30

# Reading from DATA handle
package main;
while (<MyConfig::DATA>) {
    chomp;
    my ($key, $val) = split /=/;
    print "$key => $val\n";
}
```

## Examples

```perl
use strict;
use warnings;

print "Program running\n";

__END__
This data is not compiled.
It can be read with the DATA filehandle.
print "This won't execute\n";
```

```perl
# Using __DATA__ for inline test data
package MyTest;
use strict;
use warnings;

sub read_data {
    my $data = <DATA>;
    chomp $data;
    return $data;
}

package main;
print MyTest::read_data();  # Prints: test data here

__DATA__
test data here
```

## Related Errors

- [Perl syntax error](perl-syntax-error-v2) - syntax issue
- [Perl compilation error](perl-compilation-error) - compilation issue
- [Perl file not found](perl-file-not-found) - file not found
