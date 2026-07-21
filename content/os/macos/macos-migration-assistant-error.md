---
title: "[Solution] macOS Migration Assistant Error -- Migration Failed or Stuck"
description: "Fix macOS Migration Assistant error when migrating data from another Mac fails or gets stuck. Resolve migration issues on Mac."
os: ["macos"]
error-types: ["os-error"]
severities: ["error"]
---

# macOS Migration Assistant Error -- Migration Failed or Stuck

Migration Assistant transfers data from an old Mac or backup to a new Mac. When migration fails, data may be partially transferred, the process may hang, or the new Mac may not boot correctly after migration.

## Common Causes
- Network connection between Macs is unstable
- Source Mac has corrupted data that cannot be migrated
- Insufficient disk space on the destination Mac
- Migration was interrupted by power loss or sleep
- Source and destination macOS versions are incompatible

## How to Fix
1. Ensure both Macs are connected to the same network via Ethernet
2. Check disk space on the destination Mac
3. Run Disk Utility First Aid on both Macs before migrating
4. Do not let either Mac sleep during migration
5. Try migrating specific data types instead of everything at once

```bash
# Check disk space on destination
df -h /

# Run Migration Assistant
# Open Migration Assistant from Applications > Utilities
```

## Examples

```bash
# Check migration logs
log show --predicate 'process == "MigrationAssistant"' --last 30m
```

This error is common when the network connection drops during migration, when the source Mac has corrupted data, or when there is insufficient disk space on the destination.
