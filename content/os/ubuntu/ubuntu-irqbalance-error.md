---
title: "Ubuntu IRQ Balance Service Error"
description: "IRQBalance service fails to optimize interrupt distribution"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu IRQ Balance Service Error

IRQBalance service fails to optimize interrupt distribution

## Common Causes

- irqbalance service not running
- CPU affinity masking interrupts to specific cores
- NUMA node balancing not configured
- Interrupts stuck on single CPU core

## How to Fix

1. Check status: `systemctl status irqbalance`
2. View IRQ distribution: `cat /proc/interrupts`
3. Start service: `sudo systemctl start irqbalance`
4. Check IRQ affinity: `cat /proc/irq/*/smp_affinity`

## Examples

```bash
# Check irqbalance status
systemctl status irqbalance

# View interrupt distribution
cat /proc/interrupts | head -20

# Start irqbalance
sudo systemctl start irqbalance
```
