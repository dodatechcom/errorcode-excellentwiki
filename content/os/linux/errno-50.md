---
title: "[Solution] Linux ENOPKG (errno 50) — No Package Found Fix"
description: "Fix Linux ENOPKG (errno 50) No package found error. Solutions for package management and library issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENOPKG (errno 50) — No Package Found

ENOPKG (errno 50) means the requested package or library cannot be found. This error occurs when a system call or library function tries to load a dynamic library or package that does not exist on the system. It is distinct from ENOENT (errno 2) because ENOPKG specifically refers to package or library resolution.

## Common Causes

- A required shared library is not installed
- The dynamic linker cannot find the specified library
- A package manager query returned no results
- The library path is misconfigured in `ld.so.conf`

## How to Fix ENOPKG

### 1. Search for the Package

Find the package that provides the missing library:

```bash
apt search lib<name>
dnf provides */lib<name>.so
```

### 2. Install the Missing Library

Install the required package:

```bash
sudo apt install lib<name>-dev
sudo dnf install lib<name>
```

### 3. Update the Library Cache

Refresh the dynamic linker cache:

```bash
sudo ldconfig
```

### 4. Check Library Paths

Verify the library path configuration:

```bash
echo $LD_LIBRARY_PATH
cat /etc/ld.so.conf
ldconfig -p | grep lib<name>
```

Add a custom path if needed:

```bash
echo "/usr/local/lib" | sudo tee -a /etc/ld.so.conf
sudo ldconfig
```

## Verification

After installing the package, confirm the library is available:

```bash
ldconfig -p | grep lib<name>
ldd /path/to/program | grep lib<name>
```

## Related Error Codes

- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
- [ENOLIB (errno 78)](/os/linux/errno-78/) — No such library (if applicable)
- [ENOMEM (errno 12)](/os/linux/errno-12/) — Out of memory
