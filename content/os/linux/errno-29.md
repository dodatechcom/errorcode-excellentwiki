---
title: "[Solution] Linux ESPIPE (errno 29) — Illegal Seek Fix"
description: "Fix Linux ESPIPE (errno 29) Illegal seek error. Solutions for seek operation issues on pipes and sockets."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enSPIPE", "seek", "errno-29", "pipe"]
weight: 5
---

# Linux ESPIPE (errno 29) — Illegal Seek

ESPIPE (errno 29) means the `lseek()` system call was attempted on a file descriptor that does not support seeking, such as a pipe, socket, or FIFO. This error occurs when code tries to reposition the file offset on a stream that is inherently sequential. It is distinct from EINVAL (errno 22) because ESPIPE specifically indicates the file type does not support seeking.

## Common Causes

- Calling `lseek()` on a pipe or socket file descriptor
- Attempting to `fseek()` on a pipe or FIFO in a program
- Using `rewind()` on a non-seekable stream
- A file descriptor was replaced by a pipe (e.g., via `dup2()`)

## How to Fix ESPIPE

### 1. Check File Descriptor Type

Verify whether the file descriptor supports seeking:

```bash
ls -la /proc/self/fd/<fd_number>
```

### 2. Use isatty() and fstat() in Code

Programmatically check the file type before seeking:

```c
struct stat st;
fstat(fd, &st);
if (S_ISFIFO(st.st_mode) || S_ISSOCK(st.st_mode)) {
    fprintf(stderr, "Error: cannot seek on pipe/socket\n");
    return -1;
}
```

### 3. Use Buffered I/O with Memory

For pipes, read into memory and process sequentially:

```c
char buffer[4096];
ssize_t bytes_read;
while ((bytes_read = read(fd, buffer, sizeof(buffer))) > 0) {
    process_data(buffer, bytes_read);
}
```

### 4. Replace the File Descriptor

If you need to seek, redirect to a regular file:

```bash
command > output_file
```

## Verification

After restructuring the code to avoid seeking on pipes, confirm no ESPIPE errors:

```bash
strace -e trace=seek ./program 2>&1 | grep ESPIPE
```

## Related Error Codes

- [EINVAL (errno 22)](/os/linux/errno-22/) — Invalid argument
- [EPIPE (errno 32)](/os/linux/errno-32/) — Broken pipe
- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
