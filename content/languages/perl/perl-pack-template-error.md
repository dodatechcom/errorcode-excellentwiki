---
title: "[Solution] Perl Pack Template Error"
description: "Fix Perl pack/unpack template errors when converting between binary data and Perl values."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Pack template errors occur when pack or unpack templates do not match the data format, causing incorrect binary representations.

## Common Causes

- Template letter does not match data type
- Wrong template count for array packing
- Missing template characters for alignment
- Unpack template does not match packed data

## How to Fix

### 1. Match template to data

```perl
# WRONG: Using wrong template
my $packed = pack("C", 1000);  # C is unsigned char (0-255)

# CORRECT: Use appropriate template
my $packed = pack("N", 1000);  # N is 32-bit big-endian unsigned
```

### 2. Document template alignment

```perl
# WRONG: Alignment issues
my $packed = pack("CC", 1, 2);
my $val = unpack("S", $packed);  # may read wrong bytes

# CORRECT: Explicit alignment
my $packed = pack("CC", 1, 2);
my @vals = unpack("CC", $packed);  # gets both bytes
```

## Examples

```perl
use strict;
use warnings;

# Pack a 32-bit integer
my $num = 42;
my $packed = pack("N", $num);
my $unpacked = unpack("N", $packed);
print "Original: $num, Unpacked: $unpacked\n";

# Pack a string
my $str = "Hello";
my $pstr = pack("A5", $str);
my $ustr = unpack("A5", $pstr);
print "String: $ustr\n";
```

## Related Errors

- [Runtime error](/languages/perl/perl-runtime-error)
- [Encoding error](/languages/perl/perl-encoding-error)
- [Compilation error](/languages/perl/perl-compilation-error)
