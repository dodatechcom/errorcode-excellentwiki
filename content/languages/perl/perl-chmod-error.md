---
title: "[Solution] Perl Chmod Error"
description: "Fix Perl chmod errors when changing file permissions including numeric mode mistakes and permission denied issues."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Chmod errors occur when Perl chmod is called with incorrect numeric modes or when the process lacks permission to change file modes.

## Common Causes

- Octal mode not prefixed with 0
- chmod on files owned by another user
- Numeric mode calculation error
- Not checking chmod return value

## How to Fix

### 1. Use proper octal mode

```perl
# WRONG: Decimal mode
chmod 755, $file;  # decimal 755 = 01363

# CORRECT: Octal mode with 0 prefix
chmod 0755, $file;  # rwxr-xr-x
chmod 0644, $file;  # rw-r--r--
```

### 2. Check return value

```perl
chmod(0644, $file) or warn "Cannot chmod $file: $!";
```

## Examples

```perl
use strict;
use warnings;
use Fcntl;

my $file = 'test.txt';
open(my $fh, '>', $file) or die "Cannot open: $!";
print $fh "test data\n";
close $fh;

chmod(0644, $file) or warn "chmod failed: $!";
my $mode = (stat $file)[2] & 07777;
printf "File mode: %04o\n", $mode;
```

## Related Errors

- [Permission denied](/languages/perl/perl-permission-denied)
- [File not found](/languages/perl/perl-file-not-found)
- [Runtime error](/languages/perl/perl-runtime-error)
