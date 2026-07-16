---
title: "[Solution] Linux ELIBBAD (errno 59) — Accessing Corrupted Shared Library Fix"
description: "Fix Linux ELIBBAD (errno 59) Accessing a corrupted shared library error. Solutions for shared library corruption issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
tags: ["elibbad", "shared-library", "errno-59", "corrupt", "integrity"]
weight: 5
---

# Linux ELIBBAD (errno 59) — Accessing a Corrupted Shared Library

ELIBBAD (errno 59) means the shared library being accessed is corrupted or invalid. This error occurs when the dynamic linker detects that a shared library file is damaged, has an invalid ELF header, or failed integrity checks. It is distinct from ELIBACC (errno 58) because ELIBBAD indicates the library exists but is corrupted, not that it is missing.

## Common Causes

- Shared library file was truncated during installation or update
- Disk corruption damaged the library file
- Incomplete download or transfer of the library
- Binary compatibility issue between library and architecture

## How to Fix ELIBBAD

### 1. Verify Library Integrity

Check if the shared library has a valid ELF header:

```bash
file /usr/lib/libname.so
readelf -h /usr/lib/libname.so
```

### 2. Reinstall the Library Package

Reinstall the package that provides the corrupted library:

```bash
sudo apt install --reinstall libname-dev    # Debian/Ubuntu
sudo dnf reinstall libname-devel            # RHEL/Fedora
sudo pacman -S libname                      # Arch
```

### 3. Check for Disk Corruption

Run a filesystem check on the partition containing the library:

```bash
sudo fsck -f /dev/sda1
```

### 4. Verify Package Integrity

Check for corrupted packages:

```bash
sudo debsums libname    # Debian/Ubuntu
rpm -V libname          # RHEL/Fedora
```

### 5. Check for Architecture Mismatch

Ensure the library matches your system architecture:

```bash
uname -m
file /usr/lib/libname.so
readelf -h /usr/lib/libname.so | grep Machine
```

## Verification

After reinstalling, confirm the library is valid:

```bash
ldd /path/to/program
ldconfig -p | grep libname
```

## Related Error Codes

- [ELIBACC (errno 58)](/os/linux/errno-58/) — Can't access needed shared library
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
- [ENOEXEC (errno 8)](/os/linux/errno-8/) — Executable format error
