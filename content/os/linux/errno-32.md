---
title: "[Solution] Linux EPIPE (errno 32) — Broken Pipe Fix"
description: "Fix Linux EPIPE (errno 32) Broken pipe error. Solutions for pipe and signal issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux EPIPE (errno 32) — Broken Pipe

EPIPE (errno 32) means the process tried to write to a pipe or FIFO whose read end has been closed. This error occurs when one end of a pipe is no longer reading, but the other end continues to write. The writing process typically receives a SIGPIPE signal before EPIPE is returned.

## Common Causes

- A child process exited while the parent was writing to its stdin pipe
- A pipeline command (`cmd1 | cmd2`) where `cmd2` exited before `cmd1` finished
- A network socket was closed by the remote end
- Writing to a named pipe (FIFO) with no readers

## How to Fix EPIPE

### 1. Handle SIGPIPE Signal

Ignore or handle the SIGPIPE signal to prevent process termination:

```c
signal(SIGPIPE, SIG_IGN);
```

### 2. Check for Closed Pipes

Verify if the pipe's read end is still open:

```bash
ls -la /proc/self/fd/0
```

### 3. Use write() Return Value

Check the return value of `write()` for EPIPE:

```c
ssize_t ret = write(fd, data, len);
if (ret == -1 && errno == EPIPE) {
    fprintf(stderr, "Pipe closed by reader\n");
    handle_broken_pipe();
}
```

### 4. Ensure Reader Stays Alive

In shell pipelines, make sure the downstream command does not exit prematurely:

```bash
# Use cat to keep the pipe open
cmd1 | cat
```

## Verification

After handling EPIPE properly, confirm the process does not terminate unexpectedly:

```bash
echo "test" | ./program
echo "Exit code: $?"
```

## Related Error Codes

- [ESPIPE (errno 29)](/os/linux/errno-29/) — Illegal seek
- [EAGAIN (errno 7)](/os/linux/errno-7/) — Resource temporarily unavailable
- [ECHILD (errno 10)](/os/linux/errno-10/) — No child processes
