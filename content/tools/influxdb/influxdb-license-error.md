---
title: "[Solution] InfluxDB License Error — How to Fix"
description: "Fix InfluxDB license errors when the Enterprise license is missing, expired, or invalid"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB License Error

License errors occur in InfluxDB Enterprise when the license key is missing, expired, or cannot be validated against the license server.

## Why It Happens

- Enterprise license has expired
- License key was not applied after installation
- Network cannot reach the InfluxData license server
- License key is for a different cluster size
- License file was accidentally deleted

## Common Error Messages

```
error: license key required for this feature
```

```
license expired: please renew your InfluxDB Enterprise license
```

```
error: unable to validate license: network unreachable
```

```
license mismatch: key is for 3 nodes but cluster has 5 nodes
```

## How to Fix It

### 1. Apply or Update License Key

```bash
influxd-ctl update-license /path/to/license.key
```

### 2. Check Current License Status

```bash
influxd-ctl show
# Look for license expiration info
```

### 3. Apply License via API

```bash
curl -XPOST 'http://localhost:8088/license' \
  -H 'Content-Type: application/json' \
  -d '{"key": "your-license-key"}'
```

### 4. Enable Offline License Validation

```bash
# If license server is unreachable
influxd run -config influxdb.conf -license-path /path/to/license.key
```

## Examples

```
$ influxd-ctl show
Cluster ID: abc123
License: expired on 2024-01-01
```

After applying new license:

```
$ influxd-ctl show
Cluster ID: abc123
License: valid until 2025-01-01, 5 nodes
```

## Prevent It

- Set calendar reminders for license renewal
- Store license keys in a secure, accessible location
- Monitor license expiration in cluster dashboards

## Related Pages

- [InfluxDB Cluster Error](/tools/influxdb/influxdb-cluster-error)
- [InfluxDB Auth Error](/tools/influxdb/influxdb-auth-error)
- [InfluxDB Config Parse Error](/tools/influxdb/influxdb-config-parse-error)
