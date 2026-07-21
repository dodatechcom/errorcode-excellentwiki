---
title: "Fix Linux: overlayfs-upper-dir-error -- overlayfs upper dir error in Linux"
description: "Fix overlayfs upper directory errors causing filesystem mount failures on Linux."
os: ["linux"]
error-types: [["filesystem"]]
severities: [["error", "warning"]]
---

Overlayfs upper directory errors occur when the writable upper layer cannot be accessed or mounted properly.

## Common Causes
- Upper directory on different filesystem than workdir
- SELinux blocking upper directory access
- Filesystem type mismatch between layers
- Upper directory permissions incorrect

## How to Fix
1. Verify upper and work directories exist:
   ls -la /var/lib/docker/overlay2/upper
   ls -la /var/lib/docker/overlay2/work
2. Check SELinux context:
   ls -Z /var/lib/docker/overlay2/upper
3. Set correct permissions:
   chmod 0700 /var/lib/docker/overlay2/upper
4. Remount with explicit options:
   mount -t overlay overlay -o lowerdir=/lower,upperdir=/upper,workdir=/work /merged

## Examples
### Common Error Message
overlayfs: upper fs needs to support xattr\n
VFS: Cannot open root device
