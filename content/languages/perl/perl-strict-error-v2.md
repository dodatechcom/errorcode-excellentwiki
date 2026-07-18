---
title: "[Solution] Perl Global Symbol Requires Explicit Package Fix"
description: "Fix Perl 'Global symbol requires explicit package name' strict errors. Learn why strict mode catches undeclared variables and how to fix them."
languages: ["perl"]
severities: ["error"]
error-types: ["compile-error"]
weight: 5
---

## What This Error Means

The Perl `Global symbol requires explicit package name` error is raised by `use strict 'vars'` when a variable is used without being declared with `my`, `our`, or `state`. This is one of the most common Perl errors and indicates that a variable name was not properly scoped.

## Why It Happens

- A variable is used without `my`, `our`, or `state` declaration
- A typo in a variable name creates an undeclared global
- A variable declared in one scope is used in a different scope
- Using `$_` or other special variables without enabling `use strict`
- Copy-pasting code that assumes strict is not enabled
- A variable was accidentally deleted during refactoring
- Package variables are used without fully qualifying the name

## How to Fix It

### Declare all variables with my

```perl
# WRONG: Variable not declared
use strict;
print $name;  # Global symbol requires explicit package name

# CORRECT: Declare with my
use strict;
my $name = "Alice";
print $name;
```

### Fix variable name typos

```perl
# WRONG: Typo creates undeclared variable
use strict;
my $username = "admin";
print $usernmae;  # typo: Global symbol error

# CORRECT: Ensure correct spelling
use strict;
my $username = "admin";
print $username;
```

### Use our for package variables

```perl
# WRONG: Package variable without declaration
use strict;
print $main::config;  # needs 'our' declaration

# CORRECT: Use 'our' for package variables
use strict;
our $config = { debug => 1 };
print $main::config;
```

### Fix scope-related errors

```perl
# WRONG: Variable declared in inner scope
use strict;
if (1) {
    my $temp = 42;
}
print $temp;  # error: $temp is out of scope

# CORRECT: Declare in the correct scope
use strict;
my $temp;
if (1) {
    $temp = 42;
}
print $temp;
```

### Use perltidy to find undeclared variables

```perl
# CORRECT: Run syntax check
# perl -c script.pl
# Or use perltidy to auto-format and spot issues
# perltidy script.pl -b
```

### Handle special variables under strict

```perl
# CORRECT: Special variables are exempt from strict
use strict;
use warnings;

# These work without declaration
while (<>) { print; }
for (@_) { print; }
```

## Common Mistakes

- Not using `use strict` and `use warnings` in every Perl script
- Forgetting that `my` creates lexically scoped variables
- Assuming that `local` creates a new variable (it does not; it temporarily overrides)
- Not realizing that loop variables declared with `my` are scoped to the loop
- Using bareword filehandles instead of lexical filehandle variables

## Related Pages

- [Perl Uninitialized Warning](perl-uninitialized-warning) - undef value
- [Perl Compilation Error](perl-compilation-error) - compile error
- [Perl Syntax Error V2](perl-syntax-error-v2) - syntax error
- [Perl Strict Error](perl-strict-error) - related strict issue
