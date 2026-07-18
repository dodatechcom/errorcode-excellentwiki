---
title: "[Solution] C alarm / timer Error — How to Fix"
description: "Fix C alarm() and timer-related errors including missed alarms and race conditions."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C alarm / timer Error — How to Fix

alarm() schedules SIGALRM delivery. Common errors include not handling SIGALRM, race conditions between alarm firing and activity check, and using alarm with sleep creating unpredictable behavior.

## Common Error Messages

- `SIGALRM not handled — program terminated`
- `Race condition between alarm and activity check`
- `alarm(0) cancels alarm unexpectedly`
- `Nested alarm calls interfere with each other`

## How to Fix It

### Set up SIGALRM handler properly

```c
#include <signal.h>
#include <unistd.h>
#include <stdio.h>

volatile sig_atomic_t timed_out = 0;

void alarm_handler(int sig) {
    timed_out = 1;
}

int main(void) {
    struct sigaction sa = { .sa_handler = alarm_handler };
    sigemptyset(&sa.sa_mask);
    sigaction(SIGALRM, &sa, NULL);
    alarm(5);  // 5 second timeout
    while (!timed_out) {
        // do work
    }
    printf("Timed out!\n");
    return 0;
}
```

### Use alarm with select/poll for timeout

```c
#include <signal.h>
#include <unistd.h>
#include <sys/select.h>

volatile sig_atomic_t timeout_flag = 0;
void alarm_handler(int sig) { timeout_flag = 1; }

int read_with_timeout(int fd, void *buf, size_t len, int secs) {
    struct sigaction sa = { .sa_handler = alarm_handler };
    sigemptyset(&sa.sa_mask);
    sigaction(SIGALRM, &sa, NULL);
    alarm(secs);
    fd_set fds;
    FD_ZERO(&fds);
    FD_SET(fd, &fds);
    int ret = select(fd + 1, &fds, NULL, NULL, NULL);
    alarm(0);
    if (timeout_flag) return -2;
    return ret > 0 ? read(fd, buf, len) : -1;
}
```

### Use timer_create for POSIX timers

```c
#include <signal.h>
#include <time.h>
#include <stdio.h>

void timer_handler(union sigval sv) {
    printf("Timer expired!\n");
}

int main(void) {
    timer_t timerid;
    struct sigevent sev = {
        .sigev_notify = SIGEV_THREAD,
        .sigev_notify_function = timer_handler
    };
    timer_create(CLOCK_REALTIME, &sev, &timerid);
    struct itimerspec its = { .it_value = { .tv_sec = 5 } };
    timer_settime(timerid, 0, &its, NULL);
    pause();
    return 0;
}
```

### Use setitimer for interval timers

```c
#include <sys/time.h>
#include <signal.h>
#include <stdio.h>

volatile sig_atomic_t tick_count = 0;
void tick(int sig) { tick_count++; }

int main(void) {
    signal(SIGALRM, tick);
    struct itimerval val = {
        .it_interval = { .tv_usec = 500000 },
        .it_value = { .tv_usec = 500000 }
    };
    setitimer(ITIMER_REAL, &val, NULL);
    while (tick_count < 10) {}
    printf("Got %d ticks\n", tick_count);
    return 0;
}
```

## Common Scenarios

### Scenario 1: SIGALRM not handled causing default termination

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Race condition between alarm check and activity

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using alarm with sleep causing unpredictable timing

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always install SIGALRM handler before calling alarm()
- **Tip 2:** Use sigaction instead of signal for reliable behavior
- **Tip 3:** Consider POSIX timers (timer_create) for more control
