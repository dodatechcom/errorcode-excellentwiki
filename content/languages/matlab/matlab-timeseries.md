---
title: "[Solution] MATLAB timeseries — Resample, getsampleusingtime, synchronize Errors"
description: "Fix MATLAB timeseries errors: resample alignment, getsampleusingtime time bounds, and synchronize mismatch."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 116
---

## Common Causes

- Resampling with time range outside original data bounds
- `getsampleusingtime` with start time after end time
- Synchronizing timeseries with incompatible time vectors
- Confusing timeseries with timetable (different APIs)
- Missing or non-uniform time spacing causing interpolation issues

## How to Fix

```matlab
% WRONG: Resample outside data time range
ts = timeseries([1;2;3], [0; 1; 2]);
ts_resampled = resample(ts, 0:0.5:5);  % Extrapolation beyond t=2 gives NaN

% CORRECT: Resample within valid time range
ts = timeseries([1;2;3], [0; 1; 2]);
validTime = linspace(0, 2, 11);  % Stay within [0, 2]
ts_resampled = resample(ts, validTime);
```

```matlab
% WRONG: getsampleusingtime with swapped arguments
ts = timeseries(rand(10,1), linspace(0, 1, 10));
samples = getsampleusingtime(ts, 0.8, 0.2);  % Start > end

% CORRECT: Ensure start < end
samples = getsampleusingtime(ts, 0.2, 0.8);
```

```matlab
% CORRECT: Synchronize two timeseries to common time
ts1 = timeseries([1;2;3], [0; 1; 2]);
ts2 = timeseries([10;20;30], [0.5; 1.5; 2.5]);

% Find overlapping time range
tMin = max(ts1.Time(1), ts2.Time(1));
tMax = min(ts1.Time(end), ts2.Time(end));
commonTime = linspace(tMin, tMax, 100);

ts1_r = resample(ts1, commonTime);
ts2_r = resample(ts2, commonTime);
```

```matlab
% CORRECT: Convert timeseries to timetable for modern API
ts = timeseries(rand(100,1), linspace(0, 10, 100));
tt = timetable(seconds(ts.Time), ts.Data);
tt.Properties.VariableNames = {'Value'};

% Now use timetable functions
tt_resampled = retime(tt, 'regular', 'linear', 'TimeStep', seconds(0.1));
```

```matlab
% CORRECT: Create timeseries with uniform spacing
t = 0:0.01:10;
data = sin(2*pi*0.5*t);
ts = timeseries(data', t');
ts.Name = 'SineWave';
ts.TimeInfo.Units = 'seconds';
```

## Examples

```matlab
% Example: Overlay two sensors with different sampling rates
sensor1 = timeseries(randn(1000,1), linspace(0, 10, 1000));
sensor2 = timeseries(randn(200,1), linspace(0.5, 9.5, 200));

commonTime = linspace(0.5, 9.5, 500);
s1 = resample(sensor1, commonTime);
s2 = resample(sensor2, commonTime);

combined = s1 + s2;  % Element-wise after resampling
```

## Related Errors

- [Timetable](matlab-timetable) — modern time-indexed tables
- [Datetime](matlab-datetime) — datetime handling
- [Duration](matlab-duration) — time arithmetic
