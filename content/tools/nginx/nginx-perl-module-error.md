---
title: "[Solution] Nginx Perl Module Error"
description: "The embedded Perl module encountered a compilation or runtime error."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

The embedded Perl module encountered a compilation or runtime error.

## Common Causes

- **Perl syntax error**
- **Missing Perl module**
- **Module not compiled in**
- **File permission issues**

## How to Fix

1. Test: `perl -c /etc/nginx/perl/handler.pl`
2. Check: `nginx -V 2>&1 | grep http_perl_module`
3. Install missing: `sudo cpan install JSON`
4. Check handler syntax

## Examples

**Handler:**
```nginx
location /hello {
    perl 'sub {
        my $r = shift;
        $r->headers_out->set("Content-Type", "text/plain");
        $r->send_http_header("200 OK");
        $r->print("Hello from Perl!
");
        return OK;
    }';
}
```