---
title: "[Solution] Perl Signal Error"
description: "Fix Perl signal handling errors including incorrect handler setup, reentrancy, and signal-safe operations."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Signal handling errors occur when Perl signal handlers use non-signal-safe operations, or when signals interrupt critical sections.

## Common Causes

- Using die or exit inside signal handler
- Not re-setting signal handler after delivery
- Signal arriving during non-reentrant operation
- Handler accessing global state without locking

## How to Fix

### 1. Use minimal signal handlers

```perl
# WRONG: Complex operations in handler
$SIG{INT} = sub { die "interrupted"; };

# CORRECT: Set flag only
my $interrupted = 0;
$SIG{INT} = sub { $interrupted = 1; };

# Check flag in main loop
while (!$interrupted) {
    do_work();
}
```

### 2. Reset handler after delivery if needed

```perl
local $SIG{HUP} = sub {
    $SIGHUP_RECEIVED = 1;
    $SIG{HUP} = \&handle_hup;  # re-arm
};
```

## Examples

```perl
use strict;
use warnings;

my $running = 1;
$SIG{INT} = sub { $running = 0 };

print "Running (Ctrl+C to stop)...\n";
while ($running) {
    sleep 1;
    print "tick\n";
}
print "Stopped.\n";
```

## Related Errors

- [Die error](/languages/perl/die-error)
- [Runtime error](/languages/perl/perl-runtime-error)
- [Thread related error](/languages/perl/perl-perlthrtut-error)
