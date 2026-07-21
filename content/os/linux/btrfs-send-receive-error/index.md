---
title: "Fix Linux: btrfs-send-receive-error -- btrfs send/receive error in Linux"
description: "Resolve btrfs send/receive errors preventing snapshot replication on Linux."
os: ["linux"]
error-types: [["filesystem"]]
severities: [["error", "warning"]]
---

Btrfs send/receive errors occur during snapshot replication, often due to subvolume changes or storage issues.

## Common Causes
- Subvolume deleted during send operation
- Destination filesystem full
- Network interruption during remote send
- Corrupt source snapshot

## How to Fix
1. Verify source snapshot exists:
   btrfs subvolume list /mnt/source
2. Check destination space:
   df -h /mnt/destination
3. Restart the send operation:
   btrfs send /mnt/source/@snapshot | btrfs receive /mnt/dest
4. Check filesystem health:
   btrfs scrub start /mnt/source

## Examples
### Common Error Message
ERROR: send ioctl failed with -32\n
ERROR: cannot recv, no snapshot found
