---
title: "Regular expression error"
description: "A regex error occurs when a regular expression pattern is malformed or encounters an error during compilation or execution."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["regex", "regular-expression", "pattern", "perl"]
weight: 5
---

## What This Error Means

A regex error is raised when a regular expression pattern is malformed, contains invalid syntax, or encounters an error during compilation or matching. Perl's regex engine provides detailed error messages to help identify the issue.

## Common Causes

- Unclosed regex delimiters
- Invalid escape sequences
- Unbalanced parentheses in pattern
- Invalid quantifiers

## How to Fix

```perl
# WRONG: Unclosed regex
my $str = "hello";
if ($str =~ /hello/) {  # missing closing /
    print "match\n";
}

# CORRECT: Balance delimiters
my $str = "hello";
if ($str =~ /hello/) {
    print "match\n";
}
```

```perl
# WRONG: Invalid escape
my $str = "hello";
if ($str =~ /\p{L}/) {  # may need unicode support
    print "match\n";
}

# CORRECT: Use valid pattern or enable features
use utf8;
use feature 'unicode_strings';
if ($str =~ /\p{Letter}/) {
    print "match\n";
}
```

## Examples

```perl
# Example 1: Unclosed parenthesis
my $str = "hello";
$str =~ /(hello/;  # unmatched ( in regex

# Example 2: Invalid quantifier
my $str = "hello";
$str =~ /hello**/;  # *+ follows nothing in regex

# Example 3: Invalid character class
my $str = "hello";
$str =~ /[hello/;  # missing ]
```

## Related Errors

- [syntax error at line X](/languages/perl/syntax-error6)
- [Can't use string as HASH](/languages/perl/reference-error)
