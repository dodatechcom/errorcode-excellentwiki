---
title: "No such file or directory"
description: "A file not found error occurs when attempting to open a file that doesn't exist at the specified path."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `No such file or directory` error is raised when Perl tries to open a file that doesn't exist at the specified path. This is a system-level error that occurs during file I/O operations.

## Common Causes

- File doesn't exist at specified path
- Wrong file path or directory
- Typo in filename
- Incorrect working directory

## How to Fix

```perl
# WRONG: Not checking if file exists
open(my $fh, '<', 'data.txt') or die "Cannot open: $!";

# CORRECT: Check file exists first
use File::Basename;
if (-e 'data.txt') {
    open(my $fh, '<', 'data.txt') or die "Cannot open: $!";
} else {
    die "File not found: data.txt";
}
```

```perl
# WRONG: Wrong path
open(my $fh, '<', 'data.txt') or die "Cannot open: $!";

# CORRECT: Use absolute path or verify relative path
use Cwd 'abs_path';
my $path = abs_path('data.txt');
if (defined $path) {
    open(my $fh, '<', $path) or die "Cannot open: $!";
} else {
    die "File not found";
}
```

## Examples

```perl
# Example 1: Non-existent file
open(my $fh, '<', 'nonexistent.txt') or die "Cannot open: $!";
# No such file or directory

# Example 2: Wrong directory
open(my $fh, '<', '../data/file.txt') or die "Cannot open: $!";

# Example 3: Typo in filename
open(my $fh, '<', 'configuartion.txt') or die "Cannot open: $!";
```

## Related Errors

- [syntax error at line X](/languages/perl/syntax-error6)
- [Glob failed](/languages/perl/glob-error)
