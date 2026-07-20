---
title: "[Solution] Perl CPAN Module Install Error Fix"
description: "Fix Perl CPAN installation errors when installing modules from CPAN."
languages: ["perl"]
error-types: ["build-error"]
severities: ["error"]
weight: 1019
---

## What This Error Means

A CPAN installation error occurs when using `cpan` or `cpanm` (cpanminus) to install Perl modules from CPAN. These errors can result from network issues, missing development tools, test failures, or dependency problems.

## Common Causes

- Missing C compiler (gcc, make) for XS modules
- Network/proxy issues preventing download from CPAN mirrors
- Failed tests causing install to abort
- Circular or missing dependencies
- Permission denied when writing to system Perl directories

## How to Fix

```bash
# WRONG: Installing without required build tools
# Error: "make: command not found" or "gcc: command not found"

# CORRECT: Install build tools first
# Debian/Ubuntu:
sudo apt-get install build-essential

# RedHat/CentOS:
sudo yum groupinstall "Development Tools"

# macOS:
xcode-select --install
```

```bash
# WRONG: Installing to system directories without sudo
cpan Some::Module  # Fails with permission denied

# CORRECT: Use local::lib for user installs
# Set up local::lib first
cpan local::lib
eval $(perl -I ~/perl5/lib/perl5 -Mlocal::lib)

# Then install modules
cpan Some::Module
```

```bash
# WRONG: Test failures aborting install
cpan Some::Module
# Tests fail -> install stops

# CORRECT: Force install despite test failures
cpan -f Some::Module
# Or with cpanm:
cpanm --force Some::Module
```

```bash
# WRONG: Installing with outdated CPAN configuration
# Error: "Could not fetch authors/id/..."

# CORRECT: Update CPAN configuration
cpan
# At the CPAN shell:
# o conf init
# reload cpan
# o conf commit
# quit

# Or reinitialize:
rm -rf ~/.cpan
cpan
```

## Examples

```bash
# Using cpanminus for easier installs
# Install cpanminus first
cpan App::cpanminus

# Then install modules easily
cpanm Moose
cpanm Dancer2
cpanm --installdeps .

# Install a specific version
cpanm Plack@1.0047

# Install from local distribution file
cpanm ./Some-Module-1.0.tar.gz
```

```perl
# Check installed module versions
perl -MCPAN -e 'CPAN::Shell->install("Module::Name")'
```

## Related Errors

- [Perl module not found](perl-module-not-found) - module not found
- [Perl Module::Build error](perl-module-build-error) - build issue
- [Perl compilation error](perl-compilation-error) - compilation issue
