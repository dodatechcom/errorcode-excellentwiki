---
title: "Fix Linux: ext4-journal-recovery-error -- ext4 journal recovery failure in Linux"
description: "Fix ext4 journal recovery errors during filesystem mount on Linux systems."
os: ["linux"]
error-types: [["filesystem"]]
severities: [["error", "critical"]]
---

Ext4 journal recovery errors occur when the journal cannot replay transactions during mount, often after a crash.

## Common Causes
- Journal corrupted during write
- Power failure during journal commit
- Journal area on disk damaged
- Incompatible mount options

## How to Fix
1. Try force-checking the filesystem:
   fsck.ext4 -f /dev/sda1
2. Check journal with tune2fs:
   tune2fs -l /dev/sda1 | grep -i journal
3. Create fresh journal if needed:
   tune2fs -O ^has_journal /dev/sda1
   tune2fs -j /dev/sda1
4. Mount read-only to recover data:
   mount -o ro /dev/sda1 /mnt/recovery

## Examples
### Common Error Message
EXT4-fs error: ext4_journal_start_sb: aborted journal\n
JBD2: Recovery-failure
