---
title: "[Solution] Perl Deadlock Error"
description: "Fix Perl deadlock errors that occur when threads or processes wait indefinitely for each other's resources."
languages: ["perl"]
error-types: ["runtime-error"]
severities: ["error"]
---

Deadlock errors occur when multiple threads or processes hold locks that the others need, causing all to wait indefinitely.

## Common Causes

- Two threads locking resources in opposite order
- Nested locks without timeout
- Lock held during blocking I/O
- Missing lock release in error path

## How to Fix

### 1. Always lock resources in the same order

```perl
# WRONG: Different lock order in threads
# Thread 1: lock A then lock B
# Thread 2: lock B then lock A

# CORRECT: Both threads lock A first, then B
use threads;
use threads::shared;

my $lock_a :shared;
my $lock_b :shared;

lock($lock_a);
lock($lock_b);
```

### 2. Use lock timeouts

```perl
use threads;
use Thread::Queue;

eval {
    local $SIG{ALRM} = sub { die "timeout\n" };
    alarm(5);
    lock($shared_resource);
    alarm(0);
};
if ($@ =~ /timeout/) {
    warn "Could not acquire lock";
}
```

## Examples

```perl
use strict;
use warnings;
use threads;

my $resource1 :shared;
my $resource2 :shared;

my $t1 = threads->create(sub {
    lock($resource1);
    sleep 1;
    lock($resource2);
    return "Thread 1 done";
});

my $t2 = threads->create(sub {
    lock($resource2);
    sleep 1;
    lock($resource1);
    return "Thread 2 done";
});
```

## Related Errors

- [Thread related error](/languages/perl/perl-perlthrtut-error)
- [Socket error](/languages/perl/perl-socket-error)
- [Signal handler error](/languages/perl/perl-signal-handler-error)
