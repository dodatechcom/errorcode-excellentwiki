---
title: "[Solution] Perl CGI param Method Error Fix"
description: "Fix Perl CGI param method errors. Learn how to properly read CGI parameters and handle missing or malformed input."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1007
---

## What This Error Means

A CGI `param` method error occurs when using `CGI.pm` to read request parameters. Common issues include calling `param` in the wrong context, missing parameters, or incompatible CGI mode.

## Common Causes

- Calling `param` as a function without importing it
- Accessing parameters before CGI object initialization
- Missing required parameters in the request
- Using `param` in list vs scalar context incorrectly
- Uploaded file handling without proper enctype

## How to Fix

```perl
# WRONG: Function-style call without import
use CGI;
my $name = param('name');  # param not imported

# CORRECT: Use object-oriented style
use CGI;
my $q = CGI->new;
my $name = $q->param('name');
```

```perl
# WRONG: Accessing params before initialization
my $name = CGI->param('name');  # Static method call issues

# CORRECT: Initialize properly
use CGI;
my $q = CGI->new;
my $name = $q->param('name') // 'default';
```

```perl
# WRONG: Not checking if parameter exists
my $q = CGI->new;
my $email = $q->param('email');  # May be undef

# CORRECT: Check existence
my $q = CGI->new;
if ($q->param('email')) {
    my $email = $q->param('email');
    print "Email: $email\n";
} else {
    print "Email is required\n";
}
```

```perl
# WRONG: Scalar vs list context confusion
my $q = CGI->new;
my @colors = $q->param('color');  # Always returns list
my $count = $q->param('color');   # Returns count in scalar

# CORRECT: Be explicit about context
my $q = CGI->new;
my @colors = $q->param('color');
my $count = scalar $q->param('color');
```

## Examples

```perl
use CGI;
use strict;
use warnings;

my $q = CGI->new;
print $q->header('text/html');

# Safe parameter access with defaults
my $username = $q->param('username') // '';
my $age      = $q->param('age')      // 0;

if ($username) {
    print "<h1>Hello, $username</h1>";
} else {
    print "<form><input name='username'></form>";
}
```

## Related Errors

- [Perl CGI error](perl-cgi-error) - CGI runtime issue
- [Perl module not found](perl-module-not-found) - module issue
- [Perl encoding error](perl-encoding-error) - encoding issue
