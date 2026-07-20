---
title: "[Solution] Perl @INC Module Path Error Fix"
description: "Fix Perl @INC errors when modules are not found in the library search path."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1012
---

## What This Error Means

An @INC error occurs when Perl cannot find a module in its library search path. The `@INC` array contains the directories where Perl looks for modules, and a missing path prevents module loading.

## Common Causes

- Module not installed on the system
- Custom modules not in any @INC directory
- Using `use lib` incorrectly or too late
- Relative paths that don't resolve correctly
- Running the script from the wrong directory

## How to Fix

```perl
# WRONG: Assuming module is installed
use NonExistent::Module;

# CORRECT: Check if module exists first
BEGIN {
    eval { require NonExistent::Module; 1 } or do {
        die "Module not found. Install with: cpan NonExistent::Module\n";
    };
}
use NonExistent::Module;
```

```perl
# WRONG: Using relative path without adjusting @INC
use My::Local::Module;  # Not in @INC

# CORRECT: Add local lib path at compile time
use lib '/path/to/my/modules';
use lib './lib';  # Relative to current directory (not recommended)
use My::Local::Module;
```

```perl
# WRONG: Adding to @INC at runtime (too late for use)
my $lib = "/home/user/perl5/lib";
push @INC, $lib;  # Too late for use statements
use My::Module;   # Already compiled

# CORRECT: Use BEGIN block or use lib
BEGIN { push @INC, '/home/user/perl5/lib'; }
# or
use lib '/home/user/perl5/lib';
use My::Module;
```

```perl
# WRONG: Hardcoding paths
use lib '/home/alice/projects/lib';  # Will break for bob

# CORRECT: Use FindBin for relative paths
use FindBin qw($Bin);
use lib "$Bin/lib";  # Finds lib relative to script location
use My::Module;
```

## Examples

```perl
# Check current @INC
print "Library paths:\n";
print "  $_\n" for @INC;

# Add local module directory
use FindBin qw($Bin);
use lib "$Bin/../lib";
use lib "$ENV{HOME}/perl5/lib/perl5";

# Now use your modules
use My::Local::Module;
```

## Related Errors

- [Perl module not found](perl-module-not-found) - module not found
- [Perl compilation error](perl-compilation-error) - compilation issue
- [Perl bareword error](bareword) - bareword issue
