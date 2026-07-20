---
title: "[Solution] C SIGPIPE — Broken pipe signal"
description: "Fix and handle SIGPIPE broken pipe signals by ignoring SIGPIPE, checking write() return values, and using MSG_NOSIGNAL. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 830
---

# C SIGPIPE — Broken pipe signal

SIGPIPE is delivered when a process writes to a pipe or socket that has no readers (the reading end has closed). The default behavior is to terminate the process. This is common in network servers and piped commands.

## Common Causes

```c
// Cause 1: Writing to a pipe whose read end was closed
int pipefd[2];
pipe(pipefd);
close(pipefd[0]);  // close read end
write(pipefd[1], "hello", 5);  // SIGPIPE: no readers
```

```c
// Cause 2: Writing to a socket after peer disconnected
int sock = socket(AF_INET, SOCK_STREAM, 0);
connect(sock, ...);
// peer closes connection
write(sock, "data", 4);  // SIGPIPE if peer closed
```

```c
// Cause 3: Shell pipeline — writing to stdout when next command exits early
// shell: cmd1 | cmd2 | cmd3
// If cmd3 exits, cmd1 may get SIGPIPE when writing to pipe
```

```c
// Cause 4: send() on closed socket
int sock = connect_to_server();
close(sock);  // close locally
send(sock, "data", 4, 0);  // SIGPIPE
```

```c
// Cause 5: printf to broken pipe
#include <stdio.h>
int main(void) {
    // If stdout is piped and reader closes
    printf("lots of output\n");  // may get SIGPIPE
    return 0;
}
```

## How to Fix

### Fix 1: Ignore SIGPIPE globally

```c
#include <signal.h>

int main(void) {
    // Ignore SIGPIPE — write() will return -1 with errno = EPIPE
    signal(SIGPIPE, SIG_IGN);

    // ... program code ...
    return 0;
}
```

### Fix 2: Check write() return value for EPIPE

```c
#include <unistd.h>
#include <errno.h>
#include <stdio.h>

int write_all(int fd, const void *buf, size_t count) {
    const char *ptr = buf;
    while (count > 0) {
        ssize_t n = write(fd, ptr, count);
        if (n < 0) {
            if (errno == EPIPE) {
                // Pipe closed — handle gracefully
                fprintf(stderr, "Pipe closed, peer gone\n");
                return -1;
            }
            if (errno == EINTR) continue;  // interrupted, retry
            return -1;  // other error
        }
        ptr += n;
        count -= n;
    }
    return 0;
}
```

### Fix 3: Use MSG_NOSIGNAL flag for send() on sockets

```c
#include <sys/socket.h>
#include <errno.h>

int send_safe(int sock, const void *buf, size_t len) {
    // MSG_NOSIGNAL prevents SIGPIPE on broken socket
    ssize_t n = send(sock, buf, len, MSG_NOSIGNAL);
    if (n < 0) {
        if (errno == EPIPE || errno == ECONNRESET) {
            // Connection closed by peer
            return -1;
        }
        return -1;
    }
    return (int)n;
}
```

### Fix 4: Use per-thread signal handling with sigaction

```c
#include <signal.h>
#include <unistd.h>
#include <stdio.h>

static void sigpipe_handler(int sig) {
    (void)sig;
    // Optionally log, or just return (write() will fail with EPIPE)
}

int setup_sigpipe_handler(void) {
    struct sigaction sa;
    sa.sa_handler = sigpipe_handler;
    sa.sa_flags = 0;
    sigemptyset(&sa.sa_mask);
    return sigaction(SIGPIPE, &sa, NULL);
}
```

### Fix 5: Server pattern — handle EPIPE per connection

```c
#include <sys/socket.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>

void handle_client(int client_sock) {
    const char *response = "HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!";
    size_t len = 0;
    while (response[len]) len++;

    ssize_t sent = send(client_sock, response, len, MSG_NOSIGNAL);
    if (sent < 0) {
        if (errno == EPIPE || errno == ECONNRESET || errno == ECONNREFUSED) {
            // Client disconnected — clean up silently
            close(client_sock);
            return;
        }
        perror("send");
    }

    close(client_sock);
}
```

## Examples

```c
// Real-world: robust pipe writer
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

int main(void) {
    // Ignore SIGPIPE so we get EPIPE from write() instead
    signal(SIGPIPE, SIG_IGN);

    int pipefd[2];
    if (pipe(pipefd) < 0) {
        perror("pipe");
        return 1;
    }

    pid_t pid = fork();
    if (pid == 0) {
        // Child: reader — close write end, read briefly, then close
        close(pipefd[1]);
        char buf[32];
        read(pipefd[0], buf, sizeof(buf));
        close(pipefd[0]);  // close read end
        _exit(0);
    }

    // Parent: writer
    close(pipefd[0]);  // close read end

    // Write some data
    write(pipefd[1], "hello\n", 6);

    // Wait for child to close read end
    int status;
    waitpid(pid, &status, 0);

    // Now write to broken pipe — should get EPIPE, not SIGPIPE
    ssize_t n = write(pipefd[1], "world\n", 6);
    if (n < 0 && errno == EPIPE) {
        printf("Caught EPIPE: %s\n", strerror(errno));
    }

    close(pipefd[1]);
    return 0;
}
```

```c
// Real-world: network server with SIGPIPE handling
#include <sys/socket.h>
#include <netinet/in.h>
#include <signal.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>

int main(void) {
    // Critical for servers: ignore SIGPIPE
    signal(SIGPIPE, SIG_IGN);

    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    struct sockaddr_in addr = {
        .sin_family = AF_INET,
        .sin_port = htons(8080),
        .sin_addr.s_addr = INADDR_ANY
    };

    bind(server_fd, (struct sockaddr *)&addr, sizeof(addr));
    listen(server_fd, 128);

    while (1) {
        int client = accept(server_fd, NULL, NULL);
        if (client < 0) continue;

        const char *msg = "Hello!\n";
        ssize_t n = send(client, msg, 7, MSG_NOSIGNAL);
        if (n < 0) {
            if (errno == EPIPE) {
                // Client gone — clean up
            }
        }
        close(client);
    }

    return 0;
}
```

## Related Errors

- [C SIGSEGV](/languages/c/sigsegv-handling) — Segmentation fault handling
- [C SIGBUS](/languages/c/sigbus-handling) — Bus error
- [C USE_AFTER_FREE_C](/languages/c/use-after-free-c) — Use after free UB
