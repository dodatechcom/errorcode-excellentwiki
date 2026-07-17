---
title: "[Solution] Perl Module Not Found Fix"
description: "Fix Perl module not found errors. Learn why Perl modules fail to load and how to install missing modules."
languages: ["perl"]
severities: ["error"]
error-types: ["load-error"]
weight: 5
---

## What This Error Means

A Perl module not found error occurs when the Perl interpreter cannot locate a required module. This can happen due to missing installation or wrong @INC path.

## Common Causes

- Module not installed
- Wrong module name
- @INC path not configured
- Version mismatch

## How to Fix

```perl
# WRONG: Module not installed
use NonExistent::Module;

# CORRECT: Install module first
# cpan install Module::Name
# Or use cpanm
# cpanm Module::Name
```

```perl
# WRONG: Wrong module name
use LWP::UserAgnet;  # Typo

# CORRECT: Verify module name
perldoc -l LWP::UserAgent
```

## Examples

```perl
# Example 1: Check installed modules
perl -MLWP::UserAgent -e1

# Example 2: Add to INC
use lib '/path/to/modules';
use MyModule;

# Example 3: Install with cpanm
# cpanm Module::Name
```

## Related Errors

- [Perl compilation error](perl-compilation-error) - compilation issue
- [Perl runtime error](perl-runtime-error) - runtime issue
- [Perl file not found](perl-file-not-found) - file not found
