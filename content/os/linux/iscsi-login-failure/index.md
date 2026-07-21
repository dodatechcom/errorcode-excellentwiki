---
title: "Fix Linux: iscsi-login-failure -- iSCSI login failure in Linux"
description: "Resolve iSCSI login failures preventing storage connectivity on Linux systems."
os: ["linux"]
error-types: [["network", "storage"]]
severities: [["error", "warning"]]
---

iSCSI login failures occur when the initiator cannot authenticate or establish a session with the target.

## Common Causes
- CHAP authentication mismatch
- Target portal IP or port unreachable
- ACL restrictions on target
- Session limit reached on target

## How to Fix
1. Verify iSCSI target connectivity:
   ping <target_ip>
   nc -zv <target_ip> 3260
2. Check CHAP credentials:
   cat /etc/iscsi/iscsid.conf | grep -i chap
3. Restart iSCSI service:
   systemctl restart iscsid
4. Manually attempt login:
   iscsiadm -m node -T <target> -p <portal> --login

## Examples
### Common Error Message
iscsid: login authentication failed\n
iscsiadm: Failed to connect to portal
