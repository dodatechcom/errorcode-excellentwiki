---
title: "[Solution] Azure Defender Alert Error"
description: "Fix Azure Defender alert generation failures and missed threat detection issues."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Defender alert errors prevent Azure from detecting and reporting security threats. This can leave resources vulnerable to attacks without proper alerting.

## Common Causes

- Defender for Cloud is disabled for the resource type
- Alert rules are suppressed or filtered incorrectly
- Log Analytics workspace does not receive security events
- Alert volume is too high and alerts are being deduplicated

## How to Fix

### Check Defender status

```bash
az security pricing show --name VirtualMachines
```

### List security alerts

```bash
az security alert list \
  --resource-group myRG \
  --query "[].{Title:title,Severity:severity,Status:status}"
```

### Dismiss a false positive alert

```bash
az security alert update \
  --name alertId \
  --resource-group myRG \
  --action Dismiss
```

### Check alert sync status

```bash
az security alert list \
  --query "[?status.code=='Dismissed'].{Title:title,Time:timeGenerated}"
```

## Examples

- No alerts are generated for suspicious sign-ins because Defender for Identity is disabled
- Alert is created but not forwarded to Logic App because the action rule filters it out
- Alert appears as `In Progress` but never resolves because the remediation script fails

## Related Errors

- [Azure Security Center Error]({{< relref "/cloud/azure/azure-security-center-error" >}}) -- General Security Center errors.
- [Azure Sentinel Error]({{< relref "/cloud/azure/azure-sentinel-error" >}}) -- Sentinel issues.
