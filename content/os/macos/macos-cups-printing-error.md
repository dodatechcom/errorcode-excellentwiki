---
title: "[Solution] macOS CUPS Printing Error -- Print Jobs Stuck or Failing"
description: "Fix macOS CUPS printing error when print jobs are stuck in the queue or fail to print. Resolve CUPS printing issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS CUPS Printing Error -- Print Jobs Stuck or Failing in CUPS

CUPS (Common Unix Printing System) is the printing backend on macOS. When CUPS encounters errors, print jobs may be stuck in the queue, fail to spool, or produce blank pages.

## Common Causes
- Print queue has a stuck job blocking subsequent jobs
- CUPS configuration is corrupted
- Printer driver is incompatible or missing
- CUPS service has crashed or is not running
- Printer is offline in CUPS configuration

## How to Fix
1. Open the CUPS web interface to manage the print queue
2. Cancel all stuck print jobs
3. Restart the CUPS service
4. Remove and re-add the printer
5. Update or reinstall the printer driver

```bash
# Restart CUPS
sudo launchctl stop org.cups.cupsd
sudo launchctl start org.cups.cupsd

# Cancel all print jobs
cancel -a -

# List all print jobs
lpstat -o
```

## Examples

```bash
# Open CUPS web interface
open http://localhost:631

# Check CUPS error log
tail -50 /var/log/cups/error_log
```

This error is common after a macOS update removes a printer driver, when a large document fails to spool and blocks the queue, or when CUPS crashes and needs to be restarted.
