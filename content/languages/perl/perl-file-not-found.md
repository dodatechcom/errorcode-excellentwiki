---
title: "[Solution] Perl File Not Found Fix"
description: "Fix Perl file not found errors. Learn why file operations fail and how to handle missing files properly."
languages: ["perl"]
severities: ["error"]
error-types: ["io-error"]
weight: 5
---

## What This Error Means

A Perl file not found error occurs when Perl cannot locate or open a file. This commonly happens with open, require, or file test operations.

## Common Causes

- File does not exist
- Wrong file path
- Permission denied
- Typo in filename

## How to Fix

```perl
# WRONG: Not checking file existence
open(my $fh, '<', 'data.txt') or die "Cannot open: $!";

# CORRECT: Check file exists first
if (-e 'data.txt') {
    open(my $fh, '<', 'data.txt') or die "Cannot open: $!";
} else {
    warn "File not found: data.txt";
}
```

```perl
# WRONG: Wrong path
open(my $fh, '<', 'data.txt');  # File is in /etc/

# CORRECT: Use correct path
open(my $fh, '<', '/etc/data.txt') or die "Cannot open: $!";
```

## Examples

```perl
# Example 1: File test operators
-e 'file.txt'  # Exists
-f 'file.txt'  # Is a regular file
-r 'file.txt'  # Readable
-w 'file.txt'  # Writable

# Example 2: Safe file opening
my $filename = 'data.txt';
if (open(my $fh, '<', $filename)) {
    while (<$fh>) {
        print $_;
    }
    close($fh);
} else {
    warn "Cannot open $filename: $!";
}

# Example 3: Glob for multiple files
my @files = glob("*.txt");
```

## Related Errors

- [Perl permission denied](perl-permission-denied) - permission issue
- [Perl IO error] - IO operation failed
- [Perl runtime error](perl-runtime-error) - runtime issue
