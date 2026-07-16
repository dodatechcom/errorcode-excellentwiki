---
title: "[Solution] Linux Error Codes (errno) — Complete Reference"
description: "Find solutions for Linux errno codes. Fix EPERM, ENOENT, EACCES, EIO, ENOMEM, and ENOSPC with step-by-step terminal commands."
platforms: ["linux"]
---

Linux `errno` values are the integer error codes returned by system calls and library functions. Each entry below includes the symbolic name, numeric value, typical cause, and a concrete fix with terminal commands you can copy and paste.

## Error Codes

| Error | Description | Fix |
|-------|-------------|-----|
| [EPERM (errno 1)](/os/linux/errno-1/) | Operation not permitted — missing privileges for the requested action | Use `sudo` or adjust capabilities with `setcap` |
| [ENOENT (errno 2)](/os/linux/errno-2/) | No such file or directory — the target path does not exist | Verify the file path, check for typos, and confirm symlinks resolve |
| [EIO (errno 5)](/os/linux/errno-5/) | Input/output error — hardware or filesystem corruption | Check disk health with `smartctl`, run `fsck`, and review `dmesg` logs |
| [ENOMEM (errno 12)](/os/linux/errno-12/) | Out of memory — system cannot allocate requested memory | Check usage with `free -h`, add swap, or reduce process memory footprint |
| [EACCES (errno 13)](/os/linux/errno-13/) | Permission denied — insufficient permissions for the operation | Fix with `chmod`, `chown`, or check ACLs with `getfacl` |
| [ENOSPC (errno 28)](/os/linux/errno-28/) | No space left on device — disk or inode exhaustion | Find large files with `du -sh /*`, clean up or expand the filesystem |

## Quick Lookup

To look up any `errno` code on a Linux system:

```bash
# Look up errno by number
python3 -c "import errno; print(errno.errorcode.get(2, 'Unknown'))"

# Or use perror
perror 111
```
