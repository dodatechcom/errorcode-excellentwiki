---
title: "[Solution] Perl Exporter Symbol Export Error Fix"
description: "Fix Perl Exporter errors when exporting symbols between modules."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1039
---

## What This Error Means

An Exporter error occurs when using the Exporter module to export symbols (functions, variables) from one package to another. Common issues include exporting undefined symbols, tag name conflicts, or missing export lists.

## Common Causes

- Exporting symbols that don't exist in the package
- Using @EXPORT instead of @EXPORT_OK (exporting everything by default)
- Conflicting symbol names between modules
- Forgetting to use our for exported package variables
- Circular dependencies between modules

## How to Fix

```perl
# WRONG: Exporting undefined symbol
package MyModule;
use Exporter 'import';
our @EXPORT = qw(undefined_func);  # Doesn't exist in this package

# CORRECT: Only export existing symbols
package MyModule;
use Exporter 'import';
our @EXPORT_OK = qw(greet farewell);
sub greet    { print "Hello\n" }
sub farewell { print "Goodbye\n" }
1;
```

```perl
# WRONG: Using @EXPORT when @EXPORT_OK is better
our @EXPORT = qw(helper);  # Forces helper() on all users

# CORRECT: Use @EXPORT_OK for optional exports
our @EXPORT_OK = qw(helper);  # User must request it
our @EXPORT    = qw(main_func);  # Only essential ones
```

```perl
# WRONG: Exporting without package variable declaration
use Exporter 'import';
@EXPORT_OK = qw($VERSION);  # Uses global $main::EXPORT_OK

# CORRECT: Declare with our
package MyModule;
use Exporter 'import';
our @EXPORT_OK = qw($VERSION);
our $VERSION = '1.0';
1;
```

```perl
# Using export tags
package MyModule;
use Exporter 'import';
our @EXPORT_OK = qw(red green blue
                    apple orange banana);
our %EXPORT_TAGS = (
    colors => [qw(red green blue)],
    fruits => [qw(apple orange banana)],
    all    => [@EXPORT_OK],
);
1;

# Usage:
# use MyModule ':colors';  # Import red, green, blue
# use MyModule ':fruits';  # Import apple, orange, banana
```

## Examples

```perl
package My::Math;
use Exporter 'import';
our @EXPORT_OK = qw(add subtract multiply divide);
our %EXPORT_TAGS = (all => [qw(add subtract multiply divide)]);

sub add      { $_[0] + $_[1] }
sub subtract { $_[0] - $_[1] }
sub multiply { $_[0] * $_[1] }
sub divide   { $_[0] / $_[1] }
1;

package main;
use My::Math ':all';
print add(5, 3);  # 8
```

## Related Errors

- [Perl module not found](perl-module-not-found) - module not found
- [Perl compilation error](perl-compilation-error) - compilation issue
- [Perl undefined sub](undefined-sub) - undefined sub
