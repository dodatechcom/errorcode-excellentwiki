---
title: "[Solution] BSOD IRQL_NOT_LESS_OR_EQUAL (Driver) Windows 11/10 — Fixed"
description: "Fix Blue Screen IRQL_NOT_LESS_OR_EQUAL caused by faulty drivers on Windows 10 and 11. Update drivers, analyze dump files, and resolve kernel memory violations."
platforms: ["windows"]
severities: ["critical"]
error_types: ["bsod"]
weight: 5
---

# [Solution] BSOD IRQL_NOT_LESS_OR_EQUAL (Driver) Windows 11/10 — Fixed

IRQL_NOT_LESS_OR_EQUAL caused by a faulty driver is a critical Blue Screen of Death error with stop code `0x0000000A`. It indicates that a specific kernel-mode driver attempted to access memory at an invalid Interrupt Request Level (IRQL), violating the Windows memory protection model.

Unlike the generic IRQL violation, this variant is directly tied to a single identifiable driver — typically shown in the "What failed" field of the blue screen. The offending driver accesses memory it does not own or uses an address at an IRQL that is too high for the operation.

## Description

The full blue screen message reads:

> **Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.**
>
> Stop code: IRQL_NOT_LESS_OR_EQUAL
> What failed: [driver name, e.g., ndis.sys, tcpip.sys, nvlddmkm.sys, afd.sys]

The IRQL system enforces memory access rules in the Windows kernel. Each driver operates at a specific IRQL, and accessing paged memory at a high IRQL is forbidden. When a driver has a bug — accessing freed memory, using incorrect memory pool types, or dereferencing invalid pointers — it triggers this bug check.

Common scenarios for this BSOD:

- **After installing a new driver** — The driver contains a memory access bug
- **During network activity** — Network drivers (ndis.sys, tcpip.sys, afd.sys) are frequent offenders
- **After Windows update** — Updated driver is incompatible with hardware
- **With VPN or firewall software** — Network filter drivers interfere with kernel memory

## Common Causes

1. **Buggy or outdated driver** — The specific driver identified in the "What failed" field has a memory access violation.
2. **Network driver conflicts** — VPN, firewall, or antivirus network filter drivers are common culprits.
3. **Corrupted driver installation** — Partially installed or incorrectly updated driver files.
4. **Driver incompatibility with Windows update** — A driver that worked before now conflicts with updated kernel components.

## Solutions

### Solution 1: Identify and Update the Faulty Driver

The "What failed" field on the blue screen directly names the problematic driver. Focus on updating or replacing that specific driver.

**Check the blue screen "What failed" field** and note the driver name (e.g., `nvlddmkm.sys`, `ndis.sys`, `tcpip.sys`).

**Find which device uses that driver:**

```powershell
Get-WmiObject Win32_PnPSignedDriver | Where-Object {$_.DriverName -like "*ndis*"} | Select-Object DeviceName, DriverVersion, InfName | Format-Table -AutoSize
```

Replace `*ndis*` with a partial match for your driver name.

**If the faulty driver is a network driver (ndis.sys, tcpip.sys, afd.sys):**

- Update your **network adapter** driver from the manufacturer's website.
- If using VPN software, uninstall it temporarily to test.
- Disable third-party firewall software.

**If the faulty driver is a GPU driver (nvlddmkm.sys, atikmpag.sys):**

- Download the latest driver from [nvidia.com/drivers](https://www.nvidia.com/Download/index.aspx) or [amd.com/support](https://www.amd.com/en/support).
- Perform a **clean installation** during setup.

### Solution 2: Boot into Safe Mode and Remove the Driver

If the BSOD prevents normal startup, boot into Safe Mode and remove the problematic driver.

**Boot into Safe Mode:**

1. Force shutdown 3 times during boot to trigger Recovery Environment.
2. Select **Advanced options** > **Troubleshoot** > **Advanced options** > **Startup Settings**.
3. Click **Restart** and press `4` or `F4` for Safe Mode.

**Uninstall the faulty driver in Safe Mode:**

1. Right-click **Start** and select **Device Manager**.
2. Find the device with the faulty driver (check the "What failed" field name).
3. Right-click the device and select **Uninstall device**.
4. Check **Delete the driver software for this device** if available.
5. Restart your computer — Windows will install a default driver.

### Solution 3: Analyze the Minidump to Identify the Root Cause

WinDbg pinpoints the exact code location and driver responsible.

**Find the latest minidump:**

```powershell
Get-ChildItem "C:\Windows\Minidump" | Sort-Object LastWriteTime -Descending | Select-Object -First 5 Name, LastWriteTime, Length
```

**Analyze with WinDbg:**

1. Install **WinDbg** from the Microsoft Store.
2. Open WinDbg and select **File > Open dump file**.
3. Open the most recent `.dmp` file from `C:\Windows\Minidump\`.
4. Type `!analyze -v` and press Enter.
5. Look for:
   - **MODULE_NAME** — The driver module that faulted
   - **IMAGE_NAME** — The exact driver file name
   - **FOLLOWUP_IP** — The instruction pointer that caused the fault

### Solution 4: Run Driver Verifier to Catch the Problematic Driver

Driver Verifier monitors drivers for illegal operations and can help identify the exact culprit.

**Enable Driver Verifier:**

```cmd
verifier /standard /all
```

Restart your computer. Driver Verifier will monitor all drivers and trigger a BSOD with detailed information when a driver misbehaves. After the next crash, analyze the minidump to identify the exact driver.

**Disable Driver Verifier when done:**

```cmd
verifier /reset
```

**Warning:** Driver Verifier may cause additional BSODs while monitoring. This is expected behavior — each crash provides diagnostic information.

### Solution 5: Update BIOS/UEFI

An outdated BIOS can cause drivers to receive incorrect hardware information.

```cmd
wmic baseboard get product,Manufacturer,version
```

Visit your motherboard manufacturer's website (ASUS, MSI, Gigabyte, ASRock, Dell, HP) and download the latest BIOS update for your exact model. Follow the manufacturer's flashing instructions carefully.

## Related Errors

- **[BSOD IRQL_NOT_LESS_OR_EQUAL (General)]({{< relref "/windows/bsod-irql-not-less-or-equal" >}})** — The broader IRQL violation covering multiple root causes
- **[BSOD KMODE_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-kmode-exception" >}})** — Another driver-related kernel exception
- **[BSOD SYSTEM_THREAD_EXCEPTION_NOT_HANDLED]({{< relref "/windows/bsod-system-thread-exception" >}})** — System thread failure from faulty drivers
- **[BSOD DPC_WATCHDOG_VIOLATION]({{< relref "/windows/bsod-dpc-watchdog-violation" >}})** — Driver timeout errors with similar storage driver causes
