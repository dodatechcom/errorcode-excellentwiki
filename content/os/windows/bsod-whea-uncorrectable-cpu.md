---
title: "[Solution] BSOD WHEA_UNCORRECTABLE_ERROR CPU Voltage Fix"
description: "Fix Blue Screen WHEA_UNCORRECTABLE_ERROR caused by CPU voltage issues on Windows 10 and 11. Resolve hardware errors with BIOS settings, CPU diagnostics, and cooling fixes."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD WHEA_UNCORRECTABLE_ERROR CPU Voltage Fix

WHEA_UNCORRECTABLE_ERROR caused by CPU voltage issues is a critical Blue Screen indicating an uncorrectable hardware error from the CPU. This error means the CPU has detected a voltage irregularity that cannot be corrected, forcing an immediate system crash.

This BSOD is commonly caused by unstable CPU overclocks, faulty power delivery, or degraded CPU hardware. It is one of the most serious hardware-related BSODs.

## What This Error Means

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: WHEA_UNCORRECTABLE_ERROR

WHEA (Windows Hardware Error Architecture) reports hardware errors to the operating system. An uncorrectable error means the hardware has failed in a way that cannot be compensated for. When caused by CPU voltage, this indicates:

- **Unstable overclock** — CPU or memory clocked beyond stable voltage
- **Faulty power delivery** — VRM (Voltage Regulator Module) failing to provide stable voltage
- **Degraded CPU** — CPU silicon degradation from prolonged overclocking or high temperatures
- **BIOS settings** — Incorrect voltage or power settings in BIOS

## Common Causes

1. **Unstable CPU overclock** — Overclocked beyond stable voltage limits.
2. **Faulty or insufficient power supply** — PSU unable to deliver stable power.
3. **VRM degradation** — Motherboard voltage regulators failing.
4. **CPU overheating** — Thermal throttling failure causing voltage instability.
5. **BIOS settings** — Incorrect or aggressive voltage settings.

## How to Fix

### Solution 1: Reset CPU to Stock Settings

If you have overclocked the CPU:

1. Enter **BIOS/UEFI** during boot (usually `Del` or `F2`).
2. Load **Optimized Defaults** or **Fail-Safe Defaults**.
3. Save and exit.

For software overclocks (Intel XTU, AMD Ryzen Master):

1. Open the overclocking utility.
2. Click **Reset to Default** or **Default Settings**.
3. Apply and restart.

### Solution 2: Check CPU Temperature

```powershell
Get-CimInstance -Namespace root\wmi -ClassName MSAcpi_ThermalZoneTemperature | Select-Object InstanceName, CurrentTemperature
```

**Check with Core Temp or HWMonitor:**

1. Download [Core Temp](https://www.alcpu.com/CoreTemp/).
2. Run the application and check CPU temperatures.
3. Ensure idle temperatures are **30–50°C** and load temperatures stay below **85°C**.

If temperatures are too high:
- Reapply thermal paste
- Improve CPU cooler mounting pressure
- Upgrade to a better CPU cooler
- Clean dust from heatsinks

### Solution 3: Update BIOS

1. Check your motherboard manufacturer's website for BIOS updates.
2. Download and install the latest version.
3. BIOS updates often include voltage and stability improvements.

### Solution 4: Check Power Supply

1. Ensure your PSU wattage meets the CPU and system requirements.
2. Check that all power connectors (24-pin ATX, 8-pin CPU) are firmly seated.
3. Try a different PSU if possible.
4. Use a PSU tester or multimeter to verify voltage rails.

### Solution 5: Reset CMOS

Reset BIOS to defaults by clearing the CMOS:

1. Shut down and unplug the computer.
2. Locate the CMOS clear jumper on the motherboard (consult manual).
3. Move the jumper to the clear position for 30 seconds.
4. Move it back to the normal position.
5. Plug in and start.

Alternatively, remove the CMOS battery for 5 minutes.

### Solution 6: Check for Hardware Errors in Event Viewer

```powershell
Get-WinEvent -LogName System | Where-Object { $_.ProviderName -like "*WHEA*" -or $_.Id -eq 41 } | Select-Object -First 10 TimeCreated, Id, Message | Format-List
```

Look for WHEA error events with details about the specific hardware component that failed.

## Related Errors

- **[BSOD WHEA_UNCORRECTABLE_ERROR]({{< relref "/windows/bsod-whea-uncorrectable-error" >}})** — Generic WHEA uncorrectable error
- **[BSOD UNEXPECTED_KERNEL_MODE_TRAP]({{< relref "/windows/bsod-unexpected-kernel-mode-cpu" >}})** — CPU double fault error
- **[BSOD CLOCK_WATCHDOG_TIMEOUT]({{< relref "/windows/bsod-clock-watchdog-timeout" >}})** — CPU watchdog timeout
