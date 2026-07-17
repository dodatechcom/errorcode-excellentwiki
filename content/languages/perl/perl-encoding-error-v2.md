---
title: "[Solution] Perl Wide Character Encoding Error"
description: "Fix Perl 'wide character' encoding errors. Handle Unicode, UTF-8, and character encoding issues in Perl."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

The warning `Wide character in ...` occurs when Perl encounters a character outside the ASCII range (byte > 127) in a context where bytes are expected, typically during string operations or file I/O.

## Common Causes

- Reading UTF-8 file without setting encoding
- Mixing byte strings and character strings
- Not using `use open` for encoding
- Missing `use utf8` pragma in source
- Writing binary data as text

## How to Fix

```perl
# WRONG: No encoding handling
open(my $fh, '<', 'data.txt');  # May read UTF-8 as bytes
my $text = <$fh>;

# CORRECT: Set encoding layer
open(my $fh, '<:encoding(UTF-8)', 'data.txt');
my $text = <$fh>;
```

```perl
# WRONG: Printing UTF-8 without binmode
open(my $out, '>', 'output.txt');
print $out "Hello — World\n";  # May warn about wide character

# CORRECT: Set binmode for output
open(my $out, '>:encoding(UTF-8)', 'output.txt');
print $out "Hello — World\n";
close($out);
```

```perl
# WRONG: Mixing byte and character strings
use utf8;
my $str = "hello";  # byte string
my $uni = "Ünïcödé";  # character string (if use utf8)
my $combined = $str . $uni;  # May warn

# CORRECT: Be consistent with encoding
use utf8;
use Encode qw(encode decode);
my $str = "hello";
my $uni = "Ünïcödé";
my $combined = $str . $uni;  # Fine with use utf8
```

## Examples

```perl
# Example 1: Global encoding settings
use open qw(:std :encoding(UTF-8));

# Example 2: Encode/decode explicitly
use Encode;
my $bytes = encode('UTF-8', "Hello — World");
my $chars = decode('UTF-8', $bytes);

# Example 3: Check string encoding
use Encode::Guess;
my $decoded = decode('Guess', $raw_bytes);

# Example 4: PerlIO layers
use PerlIO::utf8;
open(my $fh, '<:utf8', 'data.txt');
binmode($fh, ':encoding(ISO-8859-1)');
```

## Related Errors

- [perl-compilation-error]({{< relref "/languages/perl/perl-compilation-error" >}}) — syntax error
- [perl-file-not-found]({{< relref "/languages/perl/perl-file-not-found" >}}) — file not found
- [perl-undefined-value]({{< relref "/languages/perl/perl-undefined-value" >}}) — undefined value
