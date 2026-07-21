---
title: "[Solution] Perl Getopt Error"
description: "Fix Perl Getopt errors when processing command-line options including parsing failures and unknown option warnings."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Getopt errors occur when Perl Getopt modules receive invalid option syntax, unknown flags, or missing required arguments.

## Common Causes

- Unknown option passed on command line
- Required option not provided
- Option expecting value but none given
- GetOptions called after @ARGV modified

## How to Fix

### 1. Handle unknown options gracefully

```perl
# WRONG: Fails on unknown option
GetOptions("verbose" => \$verbose);

# CORRECT: Use passthrough or error handling
GetOptions("verbose" => \$verbose, "<>" => \&handle_arg);
# or
GetOptions("verbose" => \$verbose) or die "Usage: $0 [--verbose]\n";
```

### 2. Provide defaults for optional args

```perl
my $count = 1;  # default
GetOptions("count=i" => \$count);
```

## Examples

```perl
use strict;
use warnings;
use Getopt::Long;

my $verbose = 0;
my $output  = 'default.txt';

GetOptions(
    "verbose"  => \$verbose,
    "output=s" => \$output,
) or die "Usage: $0 [--verbose] [--output=file]\n";

print "Verbose: $verbose, Output: $output\n";
```

## Related Errors

- [Compilation error](/languages/perl/perl-compilation-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [Undefined value](/languages/perl/undefined-value)
