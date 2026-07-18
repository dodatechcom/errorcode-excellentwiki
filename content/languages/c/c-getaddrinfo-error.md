---
title: "[Solution] C getaddrinfo() Error — How to Fix"
description: "Fix C getaddrinfo() errors including DNS resolution failures and memory management."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C getaddrinfo() Error — How to Fix

getaddrinfo resolves hostnames to addresses. Common errors include not freeing results with freeaddrinfo, not checking return value, and using stale hints.

## Common Error Messages

- `getaddrinfo: Name or service not known (EAI_NONAME)`
- `getaddrinfo: Temporary failure in name resolution`
- `Memory leak from not calling freeaddrinfo`
- `getaddrinfo: Invalid value for hints`

## How to Fix It

### Check return value and free results

```c
#include <netdb.h>
#include <stdio.h>

int main(void) {
    struct addrinfo hints = {0}, *result;
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    int ret = getaddrinfo("example.com", "80", &hints, &result);
    if (ret != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(ret));
        return 1;
    }
    // use result ...
    freeaddrinfo(result);
    return 0;
}
```

### Use gai_strerror for error messages

```c
#include <netdb.h>
#include <stdio.h>

void resolve(const char *host) {
    struct addrinfo hints = { .ai_family = AF_UNSPEC, .ai_socktype = SOCK_STREAM };
    struct addrinfo *res;
    int ret = getaddrinfo(host, "80", &hints, &res);
    if (ret != 0)
        fprintf(stderr, "Error: %s\n", gai_strerror(ret));
    else
        freeaddrinfo(res);
}
```

### Iterate through results list

```c
#include <netdb.h>
#include <sys/socket.h>
#include <unistd.h>
#include <stdio.h>

int connect_to_host(const char *host, const char *port) {
    struct addrinfo hints = { .ai_family = AF_UNSPEC, .ai_socktype = SOCK_STREAM };
    struct addrinfo *res, *rp;
    if (getaddrinfo(host, port, &hints, &res) != 0) return -1;
    int fd = -1;
    for (rp = res; rp; rp = rp->ai_next) {
        fd = socket(rp->ai_family, rp->ai_socktype, rp->ai_protocol);
        if (fd == -1) continue;
        if (connect(fd, rp->ai_addr, rp->ai_addrlen) == 0) break;
        close(fd); fd = -1;
    }
    freeaddrinfo(res);
    return fd;
}
```

### Use AI_ADDRCONFIG for appropriate results

```c
#include <netdb.h>
#include <stdio.h>

int main(void) {
    struct addrinfo hints = {
        .ai_family = AF_UNSPEC,
        .ai_socktype = SOCK_STREAM,
        .ai_flags = AI_ADDRCONFIG
    };
    struct addrinfo *res;
    if (getaddrinfo("example.com", "80", &hints, &res) == 0) {
        printf("Resolved!\n");
        freeaddrinfo(res);
    }
    return 0;
}
```

## Common Scenarios

### Scenario 1: Not calling freeaddrinfo causing memory leak

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: DNS resolution failure not handled

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Using stale addrinfo after modifying hints

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Always call freeaddrinfo on the result
- **Tip 2:** Check getaddrinfo return value and use gai_strerror
- **Tip 3:** Use AI_ADDRCONFIG to get only addresses available on the system
