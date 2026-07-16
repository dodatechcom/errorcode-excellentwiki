---
title: "Glob failed"
description: "A glob error occurs when pattern matching for filenames fails due to permission issues or invalid patterns."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["glob", "pattern", "file", "perl"]
weight: 5
---

## What This Error Means

A `Glob failed` error occurs when Perl's glob function or `<*>` operator fails to expand a filename pattern. This can happen due to permission issues, invalid patterns, or system-level errors.

## Common Causes

- Permission denied on directory
- Invalid glob pattern syntax
- System resource limitations
- Directory doesn't exist

## How to Fix

```perl
# WRONG: Glob without checking
my @files = <*.{txt,log}>;  # Glob failed if permission denied

# CORRECT: Use eval to handle errors
my @files = eval { <*.txt> };
if ($@) {
    warn "Glob failed: $@";
}
```

```perl
# WRONG: Glob on non-existent directory
my @files = </nonexistent/*.txt>;  # Glob failed

# CORRECT: Check directory first
my $dir = "/nonexistent";
if (-d $dir) {
    my @files = <$dir/*.txt>;
} else {
    warn "Directory not found: $dir";
}
```

## Examples

```perl
# Example 1: Permission denied
chmod 0000, '/tmp/restricted';
my @files = </tmp/restricted/*>;  # Glob failed

# Example 2: Invalid pattern
my @files = <[invalid>;  # Glob failed

# Example 3: Resource limit
my @files = </very/large/directory/*>;  # may fail on large dirs
```

## Related Errors

- [No such file or directory](/languages/perl/file-not-found3)
- [die error](/languages/perl/die-error)
