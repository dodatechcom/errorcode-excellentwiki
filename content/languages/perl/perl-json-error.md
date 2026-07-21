---
title: "[Solution] Perl JSON Error"
description: "Fix Perl JSON encode/decode errors including malformed JSON strings and invalid character handling."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

JSON errors occur when Perl JSON modules fail to decode malformed JSON strings or when encoding data containing unsupported types.

## Common Causes

- Malformed JSON string (trailing commas, unquoted keys)
- JSON string with invalid UTF-8 characters
- Encoding Perl data structures with code references
- JSON boolean values not handled correctly

## How to Fix

### 1. Validate JSON before decoding

```perl
use JSON;

# WRONG: Not handling errors
my $data = decode_json($json_string);

# CORRECT: Use eval
eval {
    my $data = decode_json($json_string);
};
if ($@) {
    warn "JSON decode error: $@";
}
```

### 2. Handle boolean values

```perl
use JSON;
my $json = JSON->new->utf8->canonical;
my $data = { active => JSON::true, count => 5 };
my $text = $json->encode($data);
```

## Examples

```perl
use strict;
use warnings;
use JSON;

my $json_text = '{"name":"Alice","age":30,"active":true}';
my $data = eval { decode_json($json_text) };
if ($@) {
    warn "JSON error: $@";
} else {
    print "Name: $data->{name}\n";
    print "Age: $data->{age}\n";
}
```

## Related Errors

- [Encoding error](/languages/perl/perl-encoding-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [Module not found](/languages/perl/perl-module-not-found)
