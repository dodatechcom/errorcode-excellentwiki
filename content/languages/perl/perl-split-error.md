---
title: "[Solution] Perl Split Error"
description: "Fix Perl split function errors when splitting strings with incorrect patterns or limit arguments."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Split errors occur when the split function is used with incorrect patterns, causing unexpected array results or including empty trailing fields.

## Common Causes

- Split on empty string creating single-element array
- Using split without limit loses trailing empty fields
- Regex pattern not properly escaped
- Split in scalar context returns count, not list

## How to Fix

### 1. Use split correctly with limit

```perl
# WRONG: Trailing empty fields lost
my @fields = split /,/, "a,b,c,";
# ('a', 'b', 'c') -- trailing empty lost

# CORRECT: Use limit to keep trailing
my @fields = split /,/, "a,b,c,", -1;
# ('a', 'b', 'c', '')
```

### 2. Use correct split syntax

```perl
# WRONG: Split on string not regex
my @words = split " ", $text;

# CORRECT: Split on whitespace regex
my @words = split /\s+/, $text;
```

## Examples

```perl
use strict;
use warnings;

my $csv = "one,two,,four,";
my @fields = split /,/, $csv, -1;
print "Fields: @fields\n";  # one two  four

my $text = "  hello   world  ";
my @words = split /\s+/, $text;
print "Words: @words\n";  # hello world
```

## Related Errors

- [String concatenation error](/languages/perl/perl-string-concat)
- [List error](/languages/perl/perl-list-error)
- [Regex error](/languages/perl/perl-regex-error)
