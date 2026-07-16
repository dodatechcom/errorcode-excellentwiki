---
title: "[Solution] Linux ETXTBSY (errno 26) — Text File Busy Fix"
description: "Fix Linux ETXTBSY (errno 26) Text file busy error. Solutions for executable file conflict issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["enTXTBSY", "text", "errno-26", "executable"]
weight: 5
---

# Linux ETXTBSY (errno 26) — Text File Busy

ETXTBSY (errno 26) means the requested file is a currently executing text file (shared library or executable) and cannot be modified or opened for writing. This error occurs when you try to write to or delete a file that is currently being executed by another process. It is distinct from EBUSY (errno 16) because ETXTBSY specifically applies to executable text files.

## Common Causes

- Attempting to overwrite a running executable
- Trying to modify a shared library that is currently loaded
- Writing to a script while it is being executed
- A build process trying to replace a running binary

## How to Fix ETXTBSY

### 1. Identify the Running Process

Find which process is using the file:

```bash
lsof /path/to/file
fuser /path/to/file
```

### 2. Stop the Running Process

Stop or kill the process that is using the file:

```bash
fuser -k /path/to/file
```

### 3. Use Atomic Replacement

Instead of overwriting, write to a temporary file and rename:

```bash
cp new_binary /path/to/binary.tmp
mv /path/to/binary.tmp /path/to/binary
```

### 4. Rebuild Without Replacing In-Place

During compilation, output to a different name first:

```bash
gcc -o program_new source.c
mv program_new program
```

## Verification

After stopping the conflicting process and updating the file, verify:

```bash
lsof /path/to/file
echo "File is no longer in use"
```

## Related Error Codes

- [EBUSY (errno 16)](/os/linux/errno-16/) — Device or resource busy
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
