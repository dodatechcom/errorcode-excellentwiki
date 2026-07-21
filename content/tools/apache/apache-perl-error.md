---
title: "[Solution] Apache mod_perl Error"
description: "Fix Apache mod_perl errors when Perl scripts fail to load or execute within the Apache process."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

# Apache mod_perl Error

Apache mod_perl fails to compile or execute Perl scripts within the server process.

```
Can't locate object method "handler" via package "MyApache::Handler"
```

## Common Causes

- mod_perl module not installed
- Perl module path not configured
- Perl syntax errors in handler script
- Apache::Registry not loaded
- Version mismatch between mod_perl and Perl

## How to Fix

### Install mod_perl

```bash
# Debian/Ubuntu
apt install libapache2-mod-perl2

# RHEL/CentOS
yum install mod_perl

a2enmod perl
systemctl restart apache2
```

### Configure Perl Switches

```apache
<IfModule mod_perl.c>
    PerlSwitches -I/home/app/lib
    PerlRequire /etc/apache2/startup.pl
</IfModule>
```

### Fix Handler Configuration

```apache
<Location /perl>
    SetHandler perl-script
    PerlResponseHandler MyApache::Handler
</Location>
```

### Debug Perl Errors

```bash
# Check Perl module syntax
perl -c /etc/apache2/startup.pl

# Check Apache error log
tail -f /var/log/apache2/error.log
```

### Use Apache::Registry for Scripts

```apache
<Location /scripts>
    SetHandler perl-script
    PerlHandler Apache::Registry
    Options +ExecCGI
</Location>
```

## Examples

```perl
# /etc/apache2/startup.pl
package MyApache::Handler;
use strict;
use warnings;
use Apache2::RequestRec ();
use Apache2::Response ();

sub handler {
    my $r = shift;
    $r->content_type('text/html');
    $r->print("<h1>Hello from mod_perl</h1>");
    return Apache2::Const::OK;
}
1;
```
