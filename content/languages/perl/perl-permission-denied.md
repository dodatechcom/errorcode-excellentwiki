---
title: "[Solution] Perl Permission Denied Fix"
description: "Fix Perl permission denied errors. Learn why file permission errors occur and how to handle them."
languages: ["perl"]
severities: ["error"]
error-types: ["io-error"]
weight: 5
---

## What This Error Means

A Perl permission denied error occurs when Perl tries to access a file or resource without sufficient permissions. This is a common error in scripts that read or write files.

## Common Causes

- File not readable by current user
- Directory not writable
- Script not executable
- Wrong file ownership

## How to Fix

```perl
# WRONG: Not handling permission errors
open(my $fh, '<', '/etc/shadow') or die "Cannot open: $!";

# CORRECT: Check permissions first
if (-r '/etc/shadow') {
    open(my $fh, '<', '/etc/shadow') or die "Cannot open: $!";
} else {
    warn "No read permission";
}
```

```perl
# WRONG: Script not executable
# ./script.pl  # Permission denied

# CORRECT: Make script executable
# chmod +x script.pl
# Or run with perl interpreter
# perl script.pl
```

## Examples

```perl
# Example 1: Check file permissions
print "Readable: " . (-r 'file.txt' ? 'yes' : 'no') . "\n";
print "Writable: " . (-w 'file.txt' ? 'yes' : 'no') . "\n";

# Example 2: Change permissions
chmod 0755, 'script.pl';

# Example 3: Use eval for error handling
eval {
    open(my $fh, '<', '/restricted/file') or die $!;
};
if ($@) {
    warn "Permission denied: $@";
}
```

## Related Errors

- [Perl file not found](perl-file-not-found) - file not found
- [Perl IO error] - IO operation failed
- [Perl runtime error](perl-runtime-error) - runtime issue
