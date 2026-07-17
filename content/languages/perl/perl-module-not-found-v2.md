---
title: "[Solution] Perl Can't Locate Module in @INC"
description: "Fix Perl 'Can't locate module in @INC' error when required modules are missing. Install, configure paths, and handle missing dependencies."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The error `Can't locate Module.pm in @INC` occurs when Perl cannot find a required module. The `@INC` array contains the directories Perl searches for modules.

## Common Causes

- Module not installed
- Module name typo
- Module installed in non-standard location
- Wrong Perl version
- Missing dependencies

## How to Fix

```perl
# WRONG: Module not installed
use NonExistent::Module;  # Error: Can't locate

# CORRECT: Install module first
# From command line:
# cpan install NonExistent::Module
# Or: cpanm NonExistent::Module
```

```perl
# WRONG: Typo in module name
use LWP::Usefull;  # Should be LWP::UserAgent

# CORRECT: Check module name
# perldoc -l LWP::UserAgent  # Shows install path
use LWP::UserAgent;
```

```perl
# WRONG: Module in non-standard location
use MyCustom::Module;  # Not in @INC

# CORRECT: Add path to @INC
BEGIN {
    push @INC, '/opt/perl/lib';
}
use MyCustom::Module;
# Or use lib pragma:
use lib '/opt/perl/lib';
use MyCustom::Module;
```

## Examples

```perl
# Example 1: Check @INC
perl -e 'print join "\n", @INC'

# Example 2: Install module from CPAN
# cpan App::cpanminus
# cpanm Module::Name

# Example 3: Use local::lib for user install
# eval "$(perl -Mlocal::lib=~/perl5)"
# cpanm Module::Name

# Example 4: List installed modules
# perl -MExtUtils::Installed -e 'print join "\n", installed_modules()'
```

## Related Errors

- [perl-compilation-error]({{< relref "/languages/perl/perl-compilation-error" >}}) — syntax error
- [perl-runtime-error]({{< relref "/languages/perl/perl-runtime-error" >}}) — runtime error
- [perl-file-not-found]({{< relref "/languages/perl/perl-file-not-found" >}}) — file not found
