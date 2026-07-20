---
title: "[Solution] C CANNOT_FIND_LIBRARY — Cannot find -l"
description: "Fix C cannot find library errors by installing the library, setting LIBRARY_PATH, or using pkg-config. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["linker-error"]
weight: 803
---

# C CANNOT_FIND_LIBRARY — Cannot find -l

The linker cannot find the specified library file. The `-l` flag tells the linker to search for `lib<name>.so` or `lib<name>.a`, but the file does not exist in any of the standard or specified library paths.

## Common Causes

```bash
# Cause 1: Library is not installed
gcc main.c -lssl -lcrypto
# /usr/bin/ld: cannot find -lssl
```

```c
// Cause 2: Typo in library name
gcc main.c -lmathtool  // library is actually libmathtool.so but installed as libmathtools.so
```

```bash
# Cause 3: Library installed in non-standard location
gcc main.c -L/opt/custom/lib -lcustom  // missing -L flag
```

```bash
# Cause 4: 32-bit vs 64-bit mismatch
gcc -m32 main.c -lmylib  # looking in /usr/lib but library is in /usr/lib64
```

```bash
# Cause 5: Static library (.a) not present, only shared (.so) or vice versa
gcc -static main.c -lmylib  # only libmylib.so exists, no libmylib.a
```

## How to Fix

### Fix 1: Install the missing library

```bash
# Debian/Ubuntu
sudo apt-get install libssl-dev      # provides libssl.so and libcrypto.so

# Fedora/RHEL
sudo dnf install openssl-devel

# Arch
sudo pacman -S openssl
```

### Fix 2: Use pkg-config to get correct flags

```bash
# Find the correct compile and link flags
pkg-config --libs --cflags libssl

# Use in build command
gcc main.c $(pkg-config --libs --cflags libssl) -o app

# In CMake
find_package(PkgConfig)
pkg_check_modules(SSL REQUIRED libssl)
target_link_libraries(app ${SSL_LIBRARIES})
```

### Fix 3: Set LIBRARY_PATH or use -L

```bash
# Option A: -L flag on command line
gcc main.c -L/usr/local/lib -lmylib -o app

# Option B: Set environment variable
export LIBRARY_PATH=/usr/local/lib:$LIBRARY_PATH
gcc main.c -lmylib -o app

# Option C: For runtime, set LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
./app
```

### Fix 4: Verify library exists and check architecture

```bash
# Find where the library is installed
find /usr -name 'libssl*' 2>/dev/null
ldconfig -p | grep libssl

# Check architecture
file /usr/lib/x86_64-linux-gnu/libssl.so

# If 32-bit needed, install 32-bit version
sudo apt-get install libssl-dev:i386
```

### Fix 5: Check static vs shared availability

```bash
# List what's available
ls /usr/lib/x86_64-linux-gnu/libssl*

# If only .so exists and you need static, build from source
wget https://www.openssl.org/source/openssl-3.0.0.tar.gz
tar xzf openssl-3.0.0.tar.gz
cd openssl-3.0.0
./config --prefix=/usr/local/ssl
make && sudo make install
```

## Examples

```bash
# Real-world: building a project with multiple dependencies
gcc main.c \
    $(pkg-config --libs --cflags libcurl) \
    $(pkg-config --libs --cflags json-c) \
    -L/opt/custom/lib -lcustom \
    -o app

# CMakeLists.txt equivalent
find_package(CURL REQUIRED)
find_library(JSON_C_LIB json-c REQUIRED)
add_executable(app main.c)
target_link_libraries(app CURL::libcurl ${JSON_C_LIB})
```

```bash
# Debugging: trace the linker to see exactly what it searches
gcc -Wl,--verbose main.c -lmylib 2>&1 | grep -i "mylib"

# Check rpath in the built binary
readelf -d app | grep -i path
```

## Related Errors

- [C UNDEFINED_REFERENCE](/languages/c/linker-undefined-reference) — Undefined reference to symbol
- [C SYMBOL_NOT_FOUND](/languages/c/linker-symbol-not-found) — Symbol(s) not found
- [CMAKE_NOT_FOUND_PACKAGE](/languages/c/cmake-not-found-package) — CMake could not find package
