---
title: "[Solution] Perl Syswrite Error"
description: "Fix Perl syswrite errors when writing raw data to file handles including partial write handling."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Syswrite errors occur when syswrite returns fewer bytes than requested or fails due to disk full or broken pipe conditions.

## Common Causes

- Disk full or quota exceeded
- Broken pipe on network socket
- Not handling partial writes
- Mixing syswrite with buffered print

## How to Fix

### 1. Handle partial writes

```perl
# WRONG: Assuming complete write
syswrite($fh, $data, length($data));

# CORRECT: Loop until complete
my $written = 0;
my $total = length($data);
while ($written < $total) {
    my $bytes = syswrite($fh, $data, $total - $written, $written);
    die "syswrite failed: $!" unless defined $bytes;
    $written += $bytes;
}
```

### 2. Check for errors

```perl
my $bytes = syswrite($fh, $data);
unless (defined $bytes) {
    die "Write error: $!";
}
```

## Examples

```perl
use strict;
use warnings;

open(my $fh, '>:raw', 'output.bin') or die "Cannot open: $!";
my $data = "Hello, binary world!\n";
my $written = syswrite($fh, $data);
if (defined $written) {
    print "Wrote $written bytes\n";
} else {
    warn "syswrite failed: $!";
}
close $fh;
```

## Related Errors

- [File not found](/languages/perl/perl-file-not-found)
- [IO error](/languages/perl/perl-dbi-error)
- [Runtime error](/languages/perl/perl-runtime-error)
