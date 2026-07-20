---
title: "[Solution] COBOL DISPLAY UPON — Console Output"
description: "Fix COBOL DISPLAY UPON errors. Actionable solutions with code examples."
languages: ["cobol"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 1119
---

DISPLAY UPON writes to a specific output device. Errors involve wrong device name, using UPON when simple DISPLAY would suffice, or device not available.

## Common Causes

- Device name not recognized by the runtime
- Using UPON with a device that does not exist
- Missing UPON keyword (DISPLAY without UPON goes to console)
- Displaying to SYSOUT vs SYSERR

## How to Fix

### 1. Use standard device names

```cobol
DISPLAY 'Hello' UPON CONSOLE.     *> console
DISPLAY 'Error' UPON SYSDIAG.     *> diagnostic
DISPLAY 'Log' UPON SYSOUT.        *> standard output
```

### 2. Use DISPLAY without UPON for default console

```cobol
DISPLAY 'Hello'.  *> goes to console by default
```

### 3. Check device availability at runtime

```cobol
DISPLAY 'Test' UPON SYSOUT.
*> If SYSOUT is redirected, output goes there
```

### 4. Use DISPLAY for multiple items

```cobol
DISPLAY 'Name: ' WS-NAME ' Age: ' WS-AGE.
```

### 5. Use DISPLAY UPON for log files

```cobol
DISPLAY WS-LOG-MESSAGE UPON SYSLOG.
```

## Examples

Output to different devices:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. DISPLAY-DEMO.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 WS-MSG          PIC X(50) VALUE 'Processing started'.
01 WS-ERR          PIC X(50) VALUE 'Error occurred'.

PROCEDURE DIVISION.
    DISPLAY WS-MSG UPON CONSOLE.
    DISPLAY 'Info: ' WS-MSG UPON SYSOUT.
    DISPLAY WS-ERR UPON SYSDIAG.
    STOP RUN.
```

## Related Errors

- [COBOL DISPLAY Error](../cobol-display-error)
- [COBOL ACCEPT FROM TIME Error](../cobol-accept-from-time)
- [COBOL SYNC Error](../cobol-sync)
