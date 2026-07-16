---
title: "[Solution] C errno ERFKILL — Operation not possible due to RF-kill Fix"
description: "Fix C ERFKILL (Operation not possible due to RF-kill) by unblocking RF-kill switches and checking wireless device state."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["erfkill", "rf-kill", "wireless-blocked", "wifi", "bluetooth"]
weight: 5
---

# [Solution] C errno ERFKILL — Operation not possible due to RF-kill Fix

When a wireless operation fails because the device is blocked by an RF-kill switch (hardware or software), the system call sets `errno` to `ERFKILL`. This error indicates the radio frequency transmitter is disabled.

## Common Causes

- The hardware wireless switch is in the off position.
- The software RF-kill block is active (`rfkill block wifi`).
- The wireless device firmware is in a blocked state.
- Bluetooth or WiFi is soft-blocked via the kernel's RF-kill subsystem.

## How to Fix

Unblock the RF-kill switch using `rfkill` or by toggling the hardware switch.

```bash
# Check RF-kill status
rfkill list

# Unblock all wireless devices
sudo rfkill unblock all

# Unblock only WiFi
sudo rfkill unblock wifi
```

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock == -1) { perror("socket"); return 1; }

    struct sockaddr_in addr = {0};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(80);
    addr.sin_addr.s_addr = inet_addr("192.168.1.1");

    if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1) {
        if (errno == ERFKILL) {
            fprintf(stderr, "Wireless device is RF-kill blocked\n");
            fprintf(stderr, "Run: sudo rfkill unblock wifi\n");
        } else {
            perror("connect");
        }
        close(sock);
        return 1;
    }
    close(sock);
    return 0;
}
```

## Examples

WiFi operation blocked by RF-kill:

```c
#include <stdio.h>
#include <errno.h>

int main(void) {
    // Attempting WiFi operation when RF-kill is active
    fprintf(stderr, "Operation blocked by RF-kill (errno %d)\n", ERFKILL);
    fprintf(stderr, "Check: rfkill list\n");
    fprintf(stderr, "Unblock: sudo rfkill unblock wifi\n");
    return 1;
}
```

## Related Errors

- [errno-132 ERFKILL]({{< relref "/languages/c/errno-eRFKILL" >}}) — operation not possible due to RF-kill (numeric).
- [errno-19 ENODEV](/languages/c/errno-eRFKILL/) — no such device.
- [errno-16 EBUSY](/languages/c/errno-eRFKILL/) — device or resource busy.
