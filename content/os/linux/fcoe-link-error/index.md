---
title: "Fix Linux: fcoe-link-error -- FCoE link error in Linux"
description: "Fix Fibre Channel over Ethernet link errors preventing storage connectivity on Linux."
os: ["linux"]
error-types: [["network", "storage"]]
severities: [["error", "critical"]]
---

FCoE link errors occur when the Fibre Channel over Ethernet session cannot establish or maintain connectivity to the storage array.

## Common Causes
- FCoE switch port misconfiguration
- VLAN tagging issues on FCoE traffic
- CNA firmware out of date
- Dropped FIP frames

## How to Fix
1. Check FCoE interface status:
   fcoemon --debug
   cat /sys/class/fc_host/host*/port_state
2. Verify FCoE VLAN:
   cat /sys/module/fcoe/parameters/fcoe_vlan
3. Reset FCoE interface:
   ifconfig eth0 down && ifconfig eth0 up
4. Update CNA firmware from vendor

## Examples
### Common Error Message
fcoe: FIP FLOGI failed\n
FCoE: link down
