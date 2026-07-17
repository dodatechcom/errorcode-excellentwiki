---
title: "[Solution] Perl CGI Malformed Header Error"
description: "Fix Perl CGI malformed header errors. Ensure proper HTTP headers, avoid premature output, and handle CGI correctly."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `malformed header` error in Perl CGI occurs when the web server receives output that doesn't start with a valid HTTP header. The CGI protocol requires headers before the body, separated by a blank line.

## Common Causes

- Premature output before headers (print before use CGI)
- Missing Content-Type header
- Extra whitespace or newlines before header
- Using warn/die that outputs before header
- Missing CGI module

## How to Fix

```perl
# WRONG: Printing before CGI header
print "Hello, World!\n";  # Error: no header

# CORRECT: Use CGI module for headers
use CGI;
print CGI::header('text/html');
print "<html><body>Hello, World!</body></html>\n";
```

```perl
# WRONG: Using warn before header
use CGI;
warn "Debug info";  # May output before header
print CGI::header();

# CORRECT: Capture warnings
use CGI;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
print CGI::header();
```

```perl
# WRONG: Missing newline after header
print "Content-Type: text/html\r\n";
print "<html>...</html>";  # Missing blank line after header

# CORRECT: Include blank line
print "Content-Type: text/html\r\n\r\n";
print "<html>...</html>";
```

## Examples

```perl
# Example 1: Basic CGI script
#!/usr/bin/perl
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
print $cgi->header('text/html');
print <<HTML;
<!DOCTYPE html>
<html>
<head><title>CGI Test</title></head>
<body>
<h1>Hello from CGI!</h1>
</body>
</html>
HTML

# Example 2: JSON response
#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use JSON;

my $cgi = CGI->new;
print $cgi->header('application/json');
print encode_json({ message => "Hello", status => "ok" });

# Example 3: Handle errors in CGI
use CGI::Carp qw(fatalsToBrowser);
eval {
    # Your CGI code here
};
if ($@) {
    print CGI::header('text/plain', '500 Server Error');
    print "Error: $@";
}
```

## Related Errors

- [perl-compilation-error]({{< relref "/languages/perl/perl-compilation-error" >}}) — syntax error
- [perl-runtime-error]({{< relref "/languages/perl/perl-runtime-error" >}}) — runtime error
- [perl-file-not-found]({{< relref "/languages/perl/perl-file-not-found" >}}) — file not found
