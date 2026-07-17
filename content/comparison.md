---
title: "Cross-Platform Error Code Comparison Table"
description: "Compare equivalent error codes across Windows, Linux, macOS, and programming languages. Find the same error in different systems."
severities: ["info"]
weight: 4
---

## What is This Table?

This table maps equivalent error codes across different operating systems and programming languages. If you know an error in one system, you can find the equivalent in another.

**How to use:** Find your error in the left column, then look across to see the equivalent codes in other systems.

## File Not Found Errors

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| [0x80070002]({{< relref "/os/windows/0x80070002" >}}) | [errno-2 (ENOENT)]({{< relref "/os/linux/errno-2" >}}) | [-43 (fnfErr)]({{< relref "/os/macos/-43" >}}) | [FileNotFoundError]({{< relref "/languages/python/filenotfounderror" >}}) | [FileNotFoundException]({{< relref "/languages/java/filenotfoundexception" >}}) | errno 2 (ENOENT) | E_WARNING |
| ERROR_FILE_NOT_FOUND | ENOENT | fnfErr | FileNotFoundError | FileNotFoundException | ENOENT | file not found |

## Permission Denied Errors

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| [0x80070005]({{< relref "/os/windows/0x80070005" >}}) | [errno-13 (EACCES)]({{< relref "/os/linux/errno-13" >}}) | [-50 (paramErr)]({{< relref "/os/macos/-50" >}}) | [PermissionError]({{< relref "/languages/python/permissionerror" >}}) | N/A | errno 13 (EACCES) | E_WARNING |
| E_ACCESSDENIED | EACCES | paramErr | PermissionError | — | EACCES | Permission denied |

## Out of Memory Errors

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| [0x8007000e]({{< relref "/os/windows/0x8007000e" >}}) | [errno-12 (ENOMEM)]({{< relref "/os/linux/errno-12" >}}) | [-108 (memFullErr)]({{< relref "/os/macos/-108" >}}) | [MemoryError]({{< relref "/languages/python/memoryerror" >}}) | [OutOfMemoryError]({{< relref "/languages/java/outofmemoryerror" >}}) | errno 12 (ENOMEM) | E_ERROR |
| E_OUTOFMEMORY | ENOMEM | memFullErr | MemoryError | OutOfMemoryError | ENOMEM | Allowed memory |

## Segment Fault / Access Violation

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| [0xc0000005]({{< relref "/os/windows/0xc0000005" >}}) | SIGSEGV | SIGSEGV | [Segmentation Fault]({{< relref "/languages/c/segmentation-fault" >}}) | N/A | [Segmentation Fault]({{< relref "/languages/c/segmentation-fault" >}}) | E_ERROR |
| STATUS_ACCESS_VIOLATION | segmentation fault | segmentation fault | Segfault | — | SIGSEGV | Segmentation fault |

## Division by Zero

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| N/A | SIGFPE | SIGFPE | [ZeroDivisionError]({{< relref "/languages/python/zerodivisionerror" >}}) | [ArithmeticException]({{< relref "/languages/java/arithmeticexception" >}}) | SIGFPE | E_WARNING |
| — | floating point exception | floating point exception | ZeroDivisionError | ArithmeticException | SIGFPE | Division by zero |

## Null Pointer / Reference Errors

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0xc0000005 | SIGSEGV | SIGSEGV | [AttributeError]({{< relref "/languages/python/attributeerror" >}}) | [NullPointerException]({{< relref "/languages/java/nullpointerexception" >}}) | SIGSEGV | E_WARNING |
| STATUS_ACCESS_VIOLATION | segmentation fault | segmentation fault | 'NoneType' has no attribute | null pointer dereference | SIGSEGV | Trying to access property of non-object |

## Stack Overflow

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0xc00000fd | SIGSEGV | SIGSEGV | [RecursionError]({{< relref "/languages/python/recursionerror" >}}) | [StackOverflowError]({{< relref "/languages/java/stackoverflowerror" >}}) | [Stack Overflow]({{< relref "/languages/c/stack-overflow" >}}) | E_ERROR |
| STATUS_STACK_OVERFLOW | segmentation fault | segmentation fault | maximum recursion depth exceeded | stack overflow | stack smashing | Allowed stack size |

## Too Many Open Files

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0x80070006 | [errno-24 (EMFILE)]({{< relref "/os/linux/errno-24" >}}) | -24 (tooManyOpenFilesErr) | OSError | N/A | errno 24 (EMFILE) | E_WARNING |
| ERROR_TOO_MANY_OPEN_FILES | EMFILE | tooManyOpenFilesErr | Too many open files | — | EMFILE | Too many open files |

## Connection Refused

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0x8007274d | ECONNREFUSED | ECONNREFUSED | [ConnectionRefusedError]({{< relref "/languages/python/connectionrefusederror" >}}) | [ConnectException]({{< relref "/languages/java/ioexception" >}}) | ECONNREFUSED | E_WARNING |
| WSAECONNREFUSED | ECONNREFUSED | connection refused | Connection refused | Connection refused | ECONNREFUSED | Connection refused |

## Timeout Errors

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0x800705b4 | ETIMEDOUT | ETIMEDOUT | [TimeoutError]({{< relref "/languages/python/timeouterror" >}}) | [SocketTimeoutException]({{< relref "/languages/java/ioexception" >}}) | ETIMEDOUT | E_WARNING |
| ERROR_TIMEOUT | ETIMEDOUT | operation timed out | Timed out | Read timed out | ETIMEDOUT | Connection timed out |

## Device/Resource Busy

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0x80070020 | [errno-16 (EBUSY)]({{< relref "/os/linux/errno-16" >}}) | -16 (devBusyErr) | N/A | N/A | errno 16 (EBUSY) | E_WARNING |
| ERROR_BUSY | EBUSY | devBusyErr | — | — | EBUSY | Device or resource busy |

## Broken Pipe

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0x8007006d | [errno-32 (EPIPE)]({{< relref "/os/linux/errno-32" >}}) | -32 (brokenPipeErr) | [BrokenPipeError]({{< relref "/languages/python/brokenpipeerror" >}}) | N/A | errno 32 (EPIPE) | E_WARNING |
| ERROR_BROKEN_PIPE | EPIPE | brokenPipeErr | Broken pipe | — | EPIPE | Broken pipe |

## File Already Exists

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0x800700b7 | [errno-17 (EEXIST)]({{< relref "/os/linux/errno-17" >}}) | -48 (dupFNErr) | [FileExistsError]({{< relref "/languages/python/fileexistserror" >}}) | [FileAlreadyExistsException]({{< relref "/languages/java/filealreadyexistsexception" >}}) | errno 17 (EEXIST) | E_WARNING |
| ERROR_ALREADY_EXISTS | EEXIST | dupFNErr | File exists | File already exists | EEXIST | File already exists |

## Network Unreachable

| Windows | Linux | macOS | Python | Java | C/C++ | PHP |
|---------|-------|-------|--------|------|-------|-----|
| 0x80072751 | ENETUNREACH | ENETUNREACH | [ConnectionError]({{< relref "/languages/python/connectionerror" >}}) | [NoRouteToHostException]({{< relref "/languages/java/ioexception" >}}) | ENETUNREACH | E_WARNING |
| WSAENETUNREACH | ENETUNREACH | network is unreachable | Network is unreachable | Network is unreachable | ENETUNREACH | Network unreachable |

## How to Use This Table

1. **Find your error** in the system you're working with
2. **Look across the row** to find equivalent errors in other systems
3. **Click the link** to go to the detailed error page with fixes
4. **Use the "Quick Fix" column** for immediate solutions

## Related Pages

- [Quick Reference Table]({{< relref "/quick-reference" >}}) — All error codes in one table
- [Windows NTSTATUS Reference]({{< relref "/os/windows/NTSTATUS-reference" >}}) — Complete Windows NTSTATUS codes
- [Search]({{< relref "/search" >}}) — Search for any error code
