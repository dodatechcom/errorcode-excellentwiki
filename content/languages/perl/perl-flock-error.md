---
title: "[Solution] Perl Flock Error"
description: "Fix Perl flock errors when acquiring or releasing file locks including deadlock and timeout scenarios."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Flock errors occur when Perl flock() cannot acquire a lock due to existing locks, timeout, or operating system limitations.

## Common Causes

- Non-blocking flock fails when lock held by another process
- flock on NFS-mounted file system
- Lock not released after error
- Blocking flock hangs indefinitely

## How to Fix

### 1. Handle flock failure

```perl
# WRONG: Assuming flock always succeeds
flock($fh, LOCK_EX);

# CORRECT: Check return value
use Fcntl qw(:flock);
flock($fh, LOCK_EX) or warn "Cannot lock: $!";
```

### 2. Always unlock in error path

```perl
eval {
    flock($fh, LOCK_EX) or die "Cannot lock";
    # critical section
};
if ($@) {
    flock($fh, LOCK_UN);
    die $@;
}
```

## Examples

```perl
use strict;
use warnings;
use Fcntl qw(:flock);

open(my $fh, '>', 'locked.txt') or die "Cannot open: $!";
if (flock($fh, LOCK_EX | LOCK_NB)) {
    print $fh "Exclusive lock acquired\n";
    flock($fh, LOCK_UN);
} else {
    warn "Cannot acquire lock: $!";
}
```

## Related Errors

- [File not found](/languages/perl/perl-file-not-found)
- [Permission denied](/languages/perl/perl-permission-denied)
- [Runtime error](/languages/perl/perl-runtime-error)
