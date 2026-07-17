---
title: "ERROR_MORE_DATA (234) - How to Fix"
description: "Fix Windows ERROR_MORE_DATA (234). Handle partial data returns, allocate larger buffers, and process multi-call data retrieval operations on Windows."
platforms: ["windows"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ERROR_MORE_DATA (Win32 Error 234)

This Win32 API error occurs when a function returns more data than the buffer can hold, indicating there is more data available. The error code is `ERROR_MORE_DATA` (value 234). The full message reads:

> "More data is available."

Unlike ERROR_INSUFFICIENT_BUFFER (122), this error often means the function partially succeeded but couldn't return all data. It typically signals that you need to call the function again with a larger buffer or continue enumeration.

## Common Causes

- **Buffer too small for all data** — Partial data returned, more remains.
- **Enumeration in progress** — More items to enumerate.
- **Large registry values** — Value data exceeds buffer.
- **Network data fragmentation** — Response split across multiple calls.
- **Multi-string values** — REG_MULTI_SZ contains many strings.

## How to Fix

### Continue Enumeration

```powershell
# PowerShell handles this automatically with pipelines
Get-ChildItem "C:\Path" -Recurse | ForEach-Object { $_.FullName }
```

### Allocate Larger Buffer and Retry

```powershell
function Get-DataWithRetry {
    param([scriptblock]$Action)
    $bufferSize = 4096
    do {
        $buffer = New-Object byte[] $bufferSize
        $returned = & $Action $buffer $bufferSize
        if ($returned -eq 234) {
            $bufferSize *= 2
            continue
        }
        return $buffer[0..($returned-1)]
    } while ($true)
}
```

### Use Loops for Data Collection

```powershell
$allData = @()
do {
    $batch = Get-NextBatch
    $allData += $batch
} while ($batch.Count -eq $batchSize)
```

### Process Multi-String Values

```powershell
$value = (Get-ItemProperty -Path "HKLM:\SOFTWARE\Key" -Name "Value").Value
$strings = $value -split "`0" | Where-Object { $_ -ne "" }
```

### Use PowerShell Pipeline for Automatic Handling

```powershell
# PowerShell handles ERROR_MORE_DATA internally
Get-WmiObject Win32_Process | ForEach-Object {
    [PSCustomObject]@{
        Name = $_.Name
        PID = $_.ProcessId
        Memory = $_.WorkingSetSize
    }
}
```

### Increase Buffer for Network Operations

```powershell
$request = [System.Net.HttpWebRequest]::Create("https://api.example.com/data")
$request.Timeout = 300000
$response = $request.GetResponse()
```

## Related Errors

- [ERROR_INSUFFICIENT_BUFFER (122)]({{< relref "/os/windows/win32-insufficient-buffer" >}}) — Buffer too small for any data
- [ERROR_NOT_ENOUGH_MEMORY (8)]({{< relref "/os/windows/win32-not-enough-memory" >}}) — Memory allocation failed
- [ERROR_NO_MORE_FILES (18)]({{< relref "/os/windows/win32-no-more-files" >}}) — Enumeration complete
