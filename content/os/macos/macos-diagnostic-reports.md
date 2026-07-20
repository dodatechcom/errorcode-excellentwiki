---
title: "[Solution] macOS Diagnostic Reports — Analyze Crash Logs"
description: "Fix and analyze macOS diagnostic reports with these step-by-step solutions. Includes terminal commands and system settings."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime"]
weight: 320
---

# macOS Diagnostic Reports — Analyze Crash Logs

Diagnostic reports are .crash and .diag files generated when apps or system processes fail, containing stack traces and system state information for debugging.

## Common Causes

1. Application encountered an unhandled exception
2. Process exceeded memory limits
3. System resource exhaustion caused termination
4. Kernel panic generated a diagnostic snapshot
5. Hang report generated for unresponsive app

## How to Fix

### Fix 1: Locate and Read Crash Files

```bash
# Find system crash logs
ls ~/Library/Logs/DiagnosticReports/

# Find recent crash reports
find ~/Library/Logs/DiagnosticReports -name "*.crash" -mtime -7

# View crash report content
cat ~/Library/Logs/DiagnosticReports/MyApp_2024-01-01-123456.crash | head -100
```

### Fix 2: Use Console App for Analysis

```bash
# Open Console.app filtered for crashes
open -a Console

# View unified logs with crash predicate
log show --predicate 'eventMessage contains "crash"' --last 1h

# Check for recent hang reports
log show --predicate 'eventMessage contains "hung"' --last 30m
```

### Fix 3: Symbolicate Crash Reports

```bash
# Symbolicate a crash report
xcrun symbolicate ~/Library/Logs/DiagnosticReports/MyApp_2024-01-01.crash

# Find matching dSYM file
mdfind "kMDItemFSName == '*.dSYM'"

# Useatos for manual symbolication
atos -o MyApp.app.dSYM/Contents/Resources/DWARF/MyApp -l 0x100000000 -arch arm64
```

## Related Errors

- [macOS MDM Enrollment Error](/os/macos/macos-mdm-enrollment-error/)
- [macOS VoiceOver Error](/os/macos/macos-voiceover-error/)
- [macOS Stage Manager Error](/os/macos/macos-stage-manager-error/)
