---
title: "[Solution] Grafana Time Series Error"
description: "Fix Grafana time series errors. Learn why this happens and how to resolve it quickly."
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Grafana Time Series Error

Grafana time series errors occur when time series panels fail to display data correctly.

## Why This Happens

- Data gap detected
- Legend not showing
- Stacking error
- Fill gradient wrong

## Common Error Messages

- `timeseries_data_gap`
- `timeseries_legend_error`
- `timeseries_stacking_error`
- `timeseries_gradient_error`

## How to Fix It

### Solution 1: Check data continuity

Verify data exists for the selected time range.

### Solution 2: Fix legend configuration

Configure legend display in panel options.

### Solution 3: Adjust stacking

Set stacking mode correctly:

```yaml
stacking:
  mode: normal
```


## Common Scenarios

- **Data gap:** Check if data source is missing data points.
- **Legend not showing:** Verify legend configuration.

## Prevent It

- Monitor data quality
- Test legend options
- Validate stacking
