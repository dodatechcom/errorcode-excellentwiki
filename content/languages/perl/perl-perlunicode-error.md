---
title: "[Solution] Perl Unicode Handling Error Fix"
description: "Fix Perl Unicode handling errors. Learn how to properly handle UTF-8 and other character encodings."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1034
---

## What This Error Means

A Perl Unicode error occurs when character encoding is mishandled. Perl distinguishes between bytes and characters, and mixing them causes wide character warnings, malformed UTF-8 errors, or garbled output.

## Common Causes

- Printing Unicode strings to a non-UTF-8 filehandle
- Mixing byte strings with character strings
- Decoding UTF-8 data multiple times (double decoding)
- Not decoding input from files or the network
- Using length() on UTF-8 data expecting byte count

## How to Fix

```perl
# WRONG: Wide character warning
use utf8;
my $text = "café";
print $text;  # Wide character in print

# CORRECT: Set UTF-8 on STDOUT
use utf8;
use open ':std', ':encoding(UTF-8)';
my $text = "café";
print $text;  # Works correctly
```

```perl
# WRONG: Double decoding
use Encode;
my $bytes = "\xc3\xa9";  # UTF-8 bytes for é
my $str = decode('UTF-8', $bytes);
my $str2 = decode('UTF-8', $str);  # Double decode - malformed

# CORRECT: Decode only once
my $bytes = "\xc3\xa9";
my $str = decode('UTF-8', $bytes);
```

```perl
# WRONG: Assuming length == byte count
use utf8;
my $text = "Hello, 世界";
print length($text);  # 9 (characters), not 13 (bytes)

# CORRECT: Use bytes pragma for byte count
use bytes;
print length($text);  # 13 (bytes)
no bytes;
```

```perl
# WRONG: Reading file without decoding
open my $fh, '<', 'utf8.txt' or die $!;
my $line = <$fh>;  # Raw bytes, not characters

# CORRECT: Use encoding layer
open my $fh, '<:encoding(UTF-8)', 'utf8.txt' or die $!;
my $line = <$fh>;  # Properly decoded characters
```

## Examples

```perl
use utf8;
use open ':std', ':encoding(UTF-8)';

my $japanese = "こんにちは";
print "Length: " . length($japanese) . " chars\n";
print "$japanese\n";

# Safe encoding conversion
use Encode qw(encode decode);
my $utf8_bytes = encode('UTF-8', $japanese);
my $original   = decode('UTF-8', $utf8_bytes);
```

## Related Errors

- [Perl Unicode error](perl-unicode-error) - Unicode issue
- [Perl encoding error](perl-encoding-error) - encoding issue
- [Perl UTF8 error](perl-utf8-error-v2) - UTF-8 issue
