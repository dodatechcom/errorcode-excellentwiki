---
title: "[Solution] Perl IO::Socket Error"
description: "Fix Perl IO::Socket errors when creating, connecting, or communicating with network sockets."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

IO::Socket errors occur when creating or connecting sockets with invalid parameters, unreachable hosts, or protocol mismatches.

## Common Causes

- Invalid port number (not in valid range)
- Connection refused on target host
- Timeout connecting to remote host
- Protocol mismatch (TCP vs UDP)

## How to Fix

### 1. Validate socket parameters

```perl
# WRONG: Invalid port
my $sock = IO::Socket::INET->new(
    PeerAddr => 'localhost',
    PeerPort => '99999',  # invalid port
    Proto    => 'tcp',
);

# CORRECT: Valid port range
my $sock = IO::Socket::INET->new(
    PeerAddr => 'localhost',
    PeerPort => 8080,
    Proto    => 'tcp',
    Timeout  => 10,
) or die "Cannot connect: $@";
```

### 2. Handle connection errors

```perl
my $sock = IO::Socket::INET->new(
    PeerAddr => 'example.com',
    PeerPort => 80,
    Proto    => 'tcp',
);
unless ($sock) {
    warn "Connection failed: $!";
    return;
}
```

## Examples

```perl
use strict;
use warnings;
use IO::Socket::INET;

my $sock = IO::Socket::INET->new(
    LocalAddr => '0.0.0.0',
    LocalPort => 9999,
    Proto     => 'tcp',
    Listen    => 5,
    Reuse     => 1,
) or die "Cannot create socket: $!";
print "Listening on port 9999\n";
close $sock;
```

## Related Errors

- [Socket error](/languages/perl/perl-socket-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [Module not found](/languages/perl/perl-module-not-found)
