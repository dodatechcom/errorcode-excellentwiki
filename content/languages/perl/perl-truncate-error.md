---
title: "[Solution] Perl Truncate Error"
description: "Fix Perl truncate errors when attempting to shorten files to a specified length."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Truncate errors occur when Perl truncate() is called on non-file-handle objects, on read-only files, or with invalid length arguments.

## Common Causes

- truncate on read-only file
- Length argument larger than current file size
- truncate on pipe or socket
- Not checking truncate return value

## How to Fix

### 1. Verify file is writable

```perl
# WRONG: Not checking permissions
truncate($file, 100);

# CORRECT: Check and handle errors
truncate($file, 100) or warn "Cannot truncate $file: $!";
```

### 2. Use file handle, not filename

```perl
# WRONG: Using filename
truncate('data.txt', 0);

# CORRECT: Use file handle
open(my $fh, '+<', 'data.txt') or die "Cannot open: $!";
truncate($fh, 0);
```

## Examples

```perl
use strict;
use warnings;

open(my $fh, '>', 'temp.txt') or die "Cannot open: $!";
print $fh "Line one\nLine two\nLine three\n";
truncate($fh, 0);
print $fh "Truncated content only\n";
close $fh;

my $size = -s 'temp.txt';
print "File size after truncate: $size bytes\n";
```

## Related Errors

- [File not found](/languages/perl/perl-file-not-found)
- [Permission denied](/languages/perl/perl-permission-denied)
- [Runtime error](/languages/perl/perl-runtime-error)
