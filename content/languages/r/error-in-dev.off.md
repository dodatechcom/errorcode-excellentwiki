---
title: "[Solution] R Error — Error in Dev.off Fix"
description: "Fix R 'error in dev.off' when closing graphics devices. Check device number and open devices."
languages: ["r"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dev.off", "graphics", "device", "close"]
weight: 5
---

# Error in Dev.off — Fix

The error `Error in dev.off() : cannot shut down device 1 (the null device)` occurs when trying to close a device that doesn't exist or the null device which cannot be closed.

## Common Causes

```r
# Cause 1: Closing null device
dev.off()  # Error when no devices are open

# Cause 2: Wrong device number
dev.off(3)  # Error: device 3 is not active

# Cause 3: Closing device twice
dev.off(2)
dev.off(2)  # Error: device already closed

# Cause 4: No graphics device open
# After closing all devices
dev.off()
# Error: cannot shut down device 1
```

## How to Fix

### Fix 1: Check if devices are open

```r
# Wrong
dev.off()

# Correct
if (length(dev.list()) > 1) {  # null device is always 1
  dev.off()
}
```

### Fix 2: Use dev.list() to see open devices

```r
# Wrong
dev.off(3)

# Correct
devices <- dev.list()
cat("Open devices:", devices, "\n")
if (length(devices) > 1) {
  dev.off(devices[length(devices)])  # Close last opened
}
```

### Fix 3: Use on.exit for cleanup

```r
# Wrong — may not close device on error
pdf("plot.pdf")
plot(1:10)
dev.off()

# Correct — automatic cleanup
pdf("plot.pdf")
on.exit(dev.off())
plot(1:10)
```

### Fix 4: Reset graphics state

```r
# Wrong — device may not close properly
dev.off()

# Correct — close all non-null devices
while (length(dev.list()) > 1) {
  dev.off(dev.list()[length(dev.list())])
}
```

## Examples

```r
# Example 1: No devices open
dev.off()
# Error in dev.off() : cannot shut down device 1

# Example 2: Working dev.off
pdf("plot.pdf")
plot(1:10)
dev.off()  # Closes PDF device

# Example 3: Close specific device
pdf("plot1.pdf")
pdf("plot2.pdf")
dev.off(3)  # Close last opened device

# Example 4: List devices
dev.list()
# Returns vector of open device numbers
```

## Related Errors

- [error-in-par]({{< relref "/languages/r/error-in-par" >}}) — graphical parameters
- [error-in-plot]({{< relref "/languages/r/error-in-plot" >}}) — plot function errors
- [error-in-ggplot]({{< relref "/languages/r/error-in-ggplot" >}}) — ggplot errors
