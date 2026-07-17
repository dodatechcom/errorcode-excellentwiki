---
title: "[Solution] Linux EBADF (errno 9) — Bad File Descriptor Fix"
description: "Fix Linux EBADF (errno 9) Bad File Descriptor error. Resolve invalid fd issues, double-close bugs, and file descriptor misuse."
platforms: ["linux"]
severities: ["error"]
error_types: ["runtime"]
weight: 90
---

# Linux EBADF (errno 9) — Bad File Descriptor

EBADF (errno 9) means you passed a file descriptor to a system call that is not valid. The descriptor may have never been opened, already been closed, or never existed at all. This error appears with calls like `read()`, `write()`, `close()`, `dup()`, `fcntl()`, `ioctl()`, `mmap()`, and `send()`/`recv()`. It often signals a bug in resource management within your code.

## Common Causes

- Closing a file descriptor twice (double-close bug)
- Using a file descriptor after calling `close()` on it
- Passing -1 or an uninitialized variable as a file descriptor
- Attempting to read/write on a descriptor that was never successfully opened
- A failed `open()`, `socket()`, or `pipe()` was not checked before use
- File descriptor table overflow causing `open()` to return -1

## How to Fix EBADF

### 1. Check Return Values Before Using File Descriptors

Always verify that `open()`, `socket()`, `pipe()`, or `dup()` succeeded:

```c
int fd = open("/path/to/file", O_RDWR);
if (fd == -1) {
    perror("open failed");
    exit(EXIT_FAILURE);
}
// Now safe to use fd
```

### 2. Avoid Double-Close Bugs

Never close the same file descriptor twice. Set it to -1 after closing:

```c
close(fd);
fd = -1; // Prevent accidental double-close

// In a long function, guard against stale usage:
if (fd != -1) {
    close(fd);
    fd = -1;
}
```

### 3. Initialize File Descriptors

Always initialize fd variables to -1 or a known invalid value:

```c
int fd = -1;     // Not 0, not any valid descriptor
int sock_fd = -1;

// Now you can safely check before closing
if (fd != -1) close(fd);
```

### 4. Use valgrind to Detect Double-Close and Use-After-Close

```bash
# Run with valgrind to find file descriptor bugs
valgrind --track-fds=yes ./my_program

# Check for invalid reads/writes related to fd
valgrind --track-fds=yes --leak-check=full ./my_program
```

Valgrind will report which descriptors were opened, closed, and used after close.

### 5. Check /proc for Open File Descriptors

On Linux, inspect the file descriptors of a running process:

```bash
# List open file descriptors for a process
ls -la /proc/<pid>/fd

# Count open file descriptors
ls /proc/<pid>/fd | wc -l

# Check the maximum allowed
cat /proc/<pid>/limits | grep "open files"
```

### 6. Use fcntl to Validate File Descriptors

You can check if a file descriptor is valid before using it:

```c
#include <fcntl.h>

int is_fd_valid(int fd) {
    return fcntl(fd, F_GETFD) != -1 || errno != EBADF;
}

// Usage
if (is_fd_valid(fd)) {
    read(fd, buf, sizeof(buf));
} else {
    fprintf(stderr, "Invalid file descriptor %d\n", fd);
}
```

### 7. Guard Against Failed pipe() or socketpair()

These calls can fail, leaving you with invalid descriptors:

```c
int pipefd[2];
if (pipe(pipefd) == -1) {
    perror("pipe");
    exit(EXIT_FAILURE);
}
// pipefd[0] and pipefd[1] are now valid

// Similarly for socketpair
int sv[2];
if (socketpair(AF_UNIX, SOCK_STREAM, 0, sv) == -1) {
    perror("socketpair");
    exit(EXIT_FAILURE);
}
```

### 8. Track File Descriptors in Complex Programs

For large programs with many open files, maintain a descriptor table:

```c
#include <stdbool.h>

#define MAX_FDS 1024
bool fd_used[MAX_FDS] = {false};

bool fd_open(int fd) {
    if (fd < 0 || fd >= MAX_FDS) return false;
    return fd_used[fd];
}

// Set fd_used[fd] = true after open, false after close
```

### 9. Common Shell Scenario

EBADF can appear in shell scripts when redirecting from a closed descriptor:

```bash
# This produces EBADF if fd 3 was never opened
echo "data" >&3

# Check if fd is open first
exec 3>/tmp/myfile
echo "data" >&3
exec 3>&-  # Close fd 3
```

## Debugging Checklist

1. Confirm the fd was obtained from a successful `open()`, `socket()`, or `pipe()`
2. Check for double-close by searching all `close(fd)` calls in your code
3. Verify the fd has not been closed in a different code path
4. Use `valgrind --track-fds=yes` to trace all fd operations
5. Check `/proc/<pid>/fd` if the issue is in a running process

## Related Error Codes

- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
- [EMFILE (errno 24)](/os/linux/errno-24/) — Too many open files
- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
