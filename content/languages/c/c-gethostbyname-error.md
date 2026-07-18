---
title: "[Solution] C gethostbyname() Error — How to Fix"
description: "Replace deprecated gethostbyname() with getaddrinfo() and fix DNS resolution issues."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C gethostbyname() Error — How to Fix

gethostbyname() is obsolete and not thread-safe. Common errors include using it instead of getaddrinfo(), not checking h_errno, and buffer overflow from return value reuse. Always prefer getaddrinfo().

## Common Error Messages

- `gethostbyname: Unknown host`
- `gethostbyname is not thread-safe`
- `gethostbyname: Memory allocation failure`
- `gethostbyname returns stale data from static buffer`

## How to Fix It

### Use getaddrinfo instead

```c
#include <netdb.h>
#include <stdio.h>
#include <arpa/inet.h>

int main(void) {
    struct addrinfo hints = { .ai_family = AF_INET, .ai_socktype = SOCK_STREAM };
    struct addrinfo *res;
    if (getaddrinfo("example.com", "80", &hints, &res) != 0) {
        fprintf(stderr, "Resolution failed\n");
        return 1;
    }
    struct sockaddr_in *addr = (struct sockaddr_in *)res->ai_addr;
    printf("IP: %s\n", inet_ntoa(addr->sin_addr));
    freeaddrinfo(res);
    return 0;
}
```

### Check h_errno if stuck with gethostbyname

```c
#include <netdb.h>
#include <stdio.h>

int main(void) {
    struct hostent *he = gethostbyname("example.com");
    if (!he) {
        fprintf(stderr, "Error: %d\n", h_errno);
        return 1;
    }
    printf("Host: %s\n", he->h_name);
    return 0;
}
```

### Use getaddrinfo_r for thread-safe resolution

```c
#define _GNU_SOURCE
#include <netdb.h>
#include <stdio.h>

int main(void) {
    struct addrinfo hints = { .ai_family = AF_UNSPEC, .ai_socktype = SOCK_STREAM };
    struct addrinfo result, *res;
    char buf[1024];
    int ret = getaddrinfo_r("example.com", "80", &hints, &result, buf, sizeof(buf), &res);
    if (ret == 0) {
        printf("Resolved!\n");
    }
    return 0;
}
```

### Save DNS result before reuse

```c
#include <netdb.h>
#include <arpa/inet.h>
#include <string.h>

int resolve(const char *host, char *ip_out, size_t ip_len) {
    struct hostent *he = gethostbyname(host);
    if (!he) return -1;
    struct in_addr addr;
    memcpy(&addr, he->h_addr_list[0], sizeof(addr));
    strncpy(ip_out, inet_ntoa(addr), ip_len - 1);
    ip_out[ip_len - 1] = 0;
    return 0;
}
```

## Common Scenarios

### Scenario 1: Using gethostbyname which is not thread-safe

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 2: Not checking h_errno for error details

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

### Scenario 3: Stale data from static buffer reuse

This situation occurs when code fails to handle the error properly. Always validate inputs and check return values before proceeding.

## Prevent It

- **Tip 1:** Replace gethostbyname with getaddrinfo for thread safety
- **Tip 2:** Always check return value and use gai_strerror
- **Tip 3:** Copy results before calling getaddrinfo again
