---
title: "[Solution] Perl Seek/Tell Error"
description: "Fix Perl seek and tell errors when repositioning file handles or querying current file position."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Seek/tell errors occur when Perl seek() is called with invalid offsets or when tell() returns -1 indicating an unseekable handle.

## Common Causes

- seek() on pipe or terminal (non-seekable)
- Offset beyond file boundaries
- Not checking tell() return value
- Mixing buffered and unbuffered seeks

## How to Fix

### 1. Check if handle is seekable

```perl
# WRONG: Seeking on pipe
seek(STDIN, 0, 0);

# CORRECT: Check first
if (seek($fh, 0, 1)) {
    # handle is seekable
} else {
    warn "Cannot seek: $!";
}
```

### 2. Use correct whence values

```perl
seek($fh, 0, 0);   # beginning (SEEK_SET)
seek($fh, 0, 1);   # current (SEEK_CUR)
seek($fh, 0, 2);   # end (SEEK_END)
```

## Examples

```perl
use strict;
use warnings;

open(my $fh, '<', 'data.txt') or die "Cannot open: $!";
my $pos = tell($fh);
print "Initial position: $pos\n";
seek($fh, 0, 2);  # go to end
my $size = tell($fh);
print "File size: $size\n";
close $fh;
```

## Related Errors

- [File not found](/languages/perl/perl-file-not-found)
- [File test error](/languages/perl/perl-file-test-error)
- [Runtime error](/languages/perl/perl-runtime-error)
