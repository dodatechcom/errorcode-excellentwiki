---
title: "Fix Linux: dm-cache-corruption -- device-mapper cache corruption in Linux"
description: "Resolve device-mapper cache corruption causing data loss on Linux systems."
os: ["linux"]
error-types: [["filesystem", "disk"]]
severities: [["error", "critical"]]
---

Device-mapper cache corruption occurs when the dm-cache metadata becomes inconsistent, leading to incorrect data reads or writes.

## Common Causes
- Unclean shutdown during cache writes
- Cache device failure (SSD or NVMe)
- Metadata journal corruption
- Kernel bug in dm-cache target

## How to Fix
1. Check for cache errors:
   dmesg | grep -i 'dm-cache\|dm_bufio'
2. Verify cache status:
   dmsetup status --target cache <device>
3. Check metadata integrity:
   dmsetup suspend <device> && dmsetup resume <device>
4. Rebuild cache if needed:
   dmsetup remove <cache_device>
   cache_check <metadata_device>

## Examples
### Common Error Message
dm-cache: error copying object\n
device-mapper: cache: metadata operation failed
