---
title: "[Solution] InfluxDB CSV Import/Export Error — How to Fix"
description: "Fix InfluxDB CSV errors including import failures, export formatting issues, and CSV parsing problems"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB CSV Error

CSV errors in InfluxDB occur when importing or exporting data in CSV format. This includes parsing failures, formatting issues, and data type mismatches.

## Why It Happens

- The CSV file has incorrect column headers
- The CSV delimiter does not match the expected format
- Data types in the CSV do not match the schema
- The CSV file has encoding issues (UTF-8 vs ISO-8859-1)
- The CSV export format is not compatible with the import tool

## Common Error Messages

```
csv error: unexpected number of columns
```

```
csv error: invalid timestamp format
```

```
csv import failed: column type mismatch
```

```
csv error: could not parse line
```

## How to Fix It

### 1. Export to CSV

```bash
# Export from InfluxDB 1.x
influx -execute 'SELECT * FROM cpu WHERE time > now() - 1h' \
  -format csv > export.csv

# Export from InfluxDB 2.x using flux
influx query 'from(bucket:"mydb") |> range(start:-1h)' \
  -o myorg -f export.flux
```

### 2. Fix CSV Format for Import

```csv
#time,host,cpu_usage,user_usage
2024-01-15T10:00:00Z,server01,50.0,25.0
2024-01-15T10:01:00Z,server01,52.0,26.0
```

### 3. Import CSV

```bash
# Import using influx CLI
influx -import -path=import.csv -format=csv -precision=s

# Or via API
curl -XPOST 'http://localhost:8086/write?db=mydb' \
  --data-binary @import.csv
```

### 4. Fix CSV Encoding

```bash
# Convert encoding
iconv -f ISO-8859-1 -t UTF-8 input.csv > output.csv
```

## Common Scenarios

- **Import fails with column mismatch**: Ensure CSV headers match the measurement schema.
- **Timestamp format is wrong**: Use RFC 3339 format (2024-01-15T10:00:00Z).
- **CSV encoding issues**: Convert to UTF-8 before importing.

## Prevent It

- Validate CSV files before importing
- Use consistent timestamp formats across all exports
- Document the expected CSV format for import scripts

## Related Pages

- [InfluxDB Write Error](/tools/influxdb/influxdb-write-error)
- [InfluxDB Import Error](/tools/influxdb/influxdb-import-error)
- [InfluxDB Line Protocol Error](/tools/influxdb/influxdb-line-protocol-error)
