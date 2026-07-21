---
title: "[Solution] Perl Umask Error"
description: "Fix Perl umask errors when setting file creation masks that result in incorrect permissions."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Umask errors occur when the umask value is set incorrectly, causing newly created files to have overly restrictive or overly permissive permissions.

## Common Causes

- umask not restored after temporary change
- Incorrect umask calculation (subtractive, not additive)
- umask set to 0 allowing world-writable files
- Not accounting for umask when creating files

## How to Fix

### 1. Save and restore umask

```perl
# WRONG: Not restoring umask
umask(022);
# files created here have new umask

# CORRECT: Local umask
my $old_umask = umask(022);
# files created here with 022
umask($old_umask);
# restored
```

### 2. Understand umask is subtractive

```perl
# umask 022 means:
# 0666 & ~0222 = 0644 (rw-r--r--)
umask(022);
open(my $fh, '>', 'file.txt');
# file.txt permissions = 0644
```

## Examples

```perl
use strict;
use warnings;

my $original = umask();
printf "Current umask: %04o\n", $original;

umask(027);  # no access for group/other
open(my $fh, '>', 'secure.txt') or die "Cannot create: $!";
print $fh "secure data\n";
close $fh;

printf "secure.txt mode: %04o\n", (stat('secure.txt')[2] & 07777);
umask($original);
```

## Related Errors

- [Chmod error](/languages/perl/perl-chmod-error)
- [Permission denied](/languages/perl/perl-permission-denied)
- [File not found](/languages/perl/perl-file-not-found)
