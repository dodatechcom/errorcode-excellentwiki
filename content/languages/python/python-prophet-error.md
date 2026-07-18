---
title: "[Solution] Python Prophet Time Series Error — How to Fix"
description: "Fix Python Prophet time series errors. Resolve fitting failures, changelog issues, and seasonality configuration problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Prophet Time Series Error

A `prophet.Prophet` or `ValueError` occurs when Prophet fails to fit a forecasting model due to missing required columns, invalid date formats, or when the time series data violates Prophet's assumptions.

## Why It Happens

Prophet is a time series forecasting library. Errors arise when the input DataFrame does not contain the required `ds` (date) and `y` (value) columns, when dates are not in datetime format, when the data has too few points for the configured seasonality, or when changepoint parameters are invalid.

## Common Error Messages

- `ValueError: Dataframe must have columns ds and y`
- `ValueError: Unable to determine frequency`
- `ProphetError: Less data than horizon`
- `ValueError: Can only include one of yearly, weekly, daily`

## How to Fix It

### Fix 1: Prepare data correctly

```python
import pandas as pd
from prophet import Prophet

# Wrong — missing required columns
# df = pd.DataFrame({"date": ["2024-01-01"], "value": [100]})
# model = Prophet()
# model.fit(df)  # ValueError

# Correct — use ds and y column names
df = pd.DataFrame({
    "ds": pd.date_range("2024-01-01", periods=365),
    "y": range(365),
})
model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
print(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())
```

### Fix 2: Handle date format issues

```python
import pandas as pd
from prophet import Prophet

# Wrong — string dates not converted
# df = pd.DataFrame({"ds": ["01/01/2024", "02/01/2024"], "y": [1, 2]})

# Correct — convert to datetime
df = pd.DataFrame({"ds": ["01/01/2024", "02/01/2024"], "y": [1, 2]})
df["ds"] = pd.to_datetime(df["ds"])
model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=5)
forecast = model.predict(future)
print(forecast.head())
```

### Fix 3: Configure seasonality properly

```python
import pandas as pd
from prophet import Prophet

df = pd.DataFrame({
    "ds": pd.date_range("2024-01-01", periods=365),
    "y": range(365),
})

# Wrong — conflicting seasonality settings
# model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)

# Correct — configure seasonality based on data frequency
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,  # need sub-daily data for this
)
model.fit(df)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Add custom seasonality
model = Prophet(seasonality_mode="multiplicative")
model.add_seasonality(name="monthly", period=30.5, fourier_order=5)
model.fit(df)
```

### Fix 4: Handle outliers and missing values

```python
import pandas as pd
import numpy as np
from prophet import Prophet

# Create data with outliers
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=365)
values = np.sin(np.arange(365) * 2 * np.pi / 365) * 10 + 50
values[50] = 200  # outlier

df = pd.DataFrame({"ds": dates, "y": values})

# Wrong — fitting with outliers
# model = Prophet()
# model.fit(df)  # may produce poor forecasts

# Correct — remove or cap outliers
df_clean = df.copy()
q99 = df["y"].quantile(0.99)
df_clean["y"] = df_clean["y"].clip(upper=q99)

model = Prophet()
model.fit(df_clean)

future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
print(forecast[["ds", "yhat"]].tail(10))
```

## Common Scenarios

- **Wrong column names** — Prophet requires columns named exactly `ds` and `y`.
- **String dates** — Dates as strings cause Prophet to fail during fitting.
- **Insufficient data** — Fewer data points than the seasonality period causes fitting errors.

## Prevent It

- Always rename your date and value columns to `ds` and `y` before creating the Prophet model.
- Use `pd.to_datetime()` on the `ds` column to ensure proper datetime format.
- Set `daily_seasonality=False` unless your data is sub-daily (hourly or more frequent).

## Related Errors

- [ValueError](/languages/python/valueerror/) — invalid input format
- [ProphetError](/languages/python/prophet-error/) — model fitting failed
- [ImportError](/languages/python/importerror/) — pystan or prophet not installed
