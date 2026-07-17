---
title: "[Solution] Perl Socket Error Connection Refused"
description: "Fix Perl socket errors when connections are refused. Handle network timeouts, DNS failures, and connection issues."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A socket error in Perl occurs when TCP/IP connections fail. Common errors include connection refused, timeout, and DNS resolution failure.

## Common Causes

- Server not running on target port
- Wrong host or port number
- Firewall blocking connection
- DNS resolution failure
- Too many concurrent connections

## How to Fix

```perl
# WRONG: No error handling
use IO::Socket::INET;
my $sock = IO::Socket::INET->new(
    PeerAddr => 'localhost',
    PeerPort => 8080,
    Proto    => 'tcp',
);  # May return undef on failure

# CORRECT: Check connection
use IO::Socket::INET;
use Socket qw(:crlf);

my $sock = IO::Socket::INET->new(
    PeerAddr => 'localhost',
    PeerPort => 8080,
    Proto    => 'tcp',
    Timeout  => 10,
) or die "Cannot connect: $@";
```

```perl
# WRONG: No timeout
my $sock = IO::Socket::INET->new(
    PeerAddr => 'remote.server.com',
    PeerPort => 9090,
    Proto    => 'tcp',
);  # May hang forever

# CORRECT: Set timeout
my $sock = IO::Socket::INET->new(
    PeerAddr => 'remote.server.com',
    PeerPort => 9090,
    Proto    => 'tcp',
    Timeout  => 30,
) or die "Connection failed or timed out: $@";
```

```perl
# WRONG: Not retrying on failure
send_request();  # Fails once

# CORRECT: Retry with backoff
sub send_with_retry {
    my ($max_retries) = @_;
    for my $i (0 .. $max_retries - 1) {
        eval { send_request(); return; };
        warn "Attempt $i failed: $@" if $@;
        sleep(2 ** $i);  # Exponential backoff
    }
    die "All retry attempts failed";
}
```

## Examples

```perl
# Example 1: Simple HTTP client with error handling
use IO::Socket::INET;

sub http_get {
    my ($host, $port, $path) = @_;
    
    my $sock = IO::Socket::INET->new(
        PeerAddr => $host,
        PeerPort => $port,
        Proto    => 'tcp',
        Timeout  => 10,
    ) or return undef;
    
    print $sock "GET $path HTTP/1.0\r\nHost: $host\r\n\r\n";
    my @response = <$sock>;
    close($sock);
    
    return join('', @response);
}

# Example 2: Non-blocking connect
use IO::Select;
my $sock = IO::Socket::INET->new(PeerAddr => 'host', PeerPort => 80);
my $sel = IO::Select->new($sock);
if ($sel->can_write(5)) {
    # Connected
} else {
    die "Connection timed out";
}

# Example 3: Check if port is open
sub is_port_open {
    my ($host, $port, $timeout) = @_;
    my $sock = eval {
        IO::Socket::INET->new(
            PeerAddr => $host, PeerPort => $port,
            Proto => 'tcp', Timeout => $timeout || 5,
        );
    };
    return defined $sock;
}
```

## Related Errors

- [perl-file-not-found]({{< relref "/languages/perl/perl-file-not-found" >}}) — file not found
- [perl-dbi-error]({{< relref "/languages/perl/perl-dbi-error" >}}) — database error
- [perl-runtime-error]({{< relref "/languages/perl/perl-runtime-error" >}}) — runtime error
