---
title: "[Solution] MATLAB timetable — retime, synchronize, uniqueTimestamps Errors"
description: "Fix MATLAB timetable errors: retime alignment, synchronize merging, uniqueTimestamps deduplication."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 117
---

## Common Causes

- `retime` with time step smaller than data resolution
- `synchronize` between timetables with non-overlapping time ranges
- Duplicate timestamps causing aggregation errors
- Mixing different time units (seconds vs hours) in synchronize
- Using `synchronize` instead of `innerjoin` for non-time keys

## How to Fix

```matlab
% WRONG: retime with mismatched time step
tt = timetable((0:0.1:10)', rand(101,1), 'VariableNames', {'Value'});
tt_re = retime(tt, 'regular', 'linear', 'TimeStep', seconds(0.01));
% Creates 1001 rows — may be excessive

% CORRECT: Choose appropriate time step
tt_re = retime(tt, 'regular', 'linear', 'TimeStep', seconds(0.5));
```

```matlab
% WRONG: Synchronize with non-overlapping time ranges
tt1 = timetable((0:0.1:5)', rand(51,1), 'VariableNames', {'A'});
tt2 = timetable((6:0.1:10)', rand(51,1), 'VariableNames', {'B'});
tt_sync = synchronize(tt1, tt2, 'union');  % Fills NaN for non-overlapping

% CORRECT: Use inner join to keep only overlapping range
tt_sync = synchronize(tt1, tt2, 'intersection');  % Empty result if no overlap

% Or extend one timetable to cover the other's range
tt1_ext = retime(tt1, tt2.Time, 'linear');  % Extrapolate/interpolate
tt_sync = synchronize(tt1_ext, tt2);
```

```matlab
% CORRECT: Remove duplicate timestamps
tt = timetable([1;1;2;3;3;3], [10;20;30;40;50;60], 'VariableNames', {'Val'});
tt_clean = uniqueTimestamps(tt);  % Keeps first occurrence

% Or aggregate duplicates
tt_agg = retime(tt, @mean);  % Average values at same timestamp
```

```matlab
% CORRECT: Synchronize with proper method selection
tt1 = timetable(seconds(0:1:10)', (0:10)', 'VariableNames', {'Pressure'});
tt2 = timetable(seconds(0:2:10)', (0:5)', 'VariableNames', {'Temp'});

% linear interpolation for missing values
tt_sync = synchronize(tt1, tt2, 'linear');
```

```matlab
% CORRECT: Create timetable from raw data
t = datetime('2024-01-01') + days(0:99);
temp = 20 + 10*rand(100,1);
pressure = 1013 + 5*rand(100,1);
tt = timetable(t', temp, pressure, 'VariableNames', {'Temperature','Pressure'});
tt.Properties.TimeUnit = 'days';
```

## Examples

```matlab
% Example: Resample sensor data to uniform time grid
raw = timetable(seconds(rand(500,1)*60), randn(500,1), 'VariableNames', {'Sensor'});
raw = sortrows(raw);  % Ensure time sorted

uniformGrid = timetable(seconds(0:1:60)', zeros(61,1), 'VariableNames', {'Sensor'});
tt_clean = synchronize(raw, uniformGrid, 'linear');
tt_clean = removevars(tt_clean, 'Sensor_2');  % Remove duplicate column
```

## Related Errors

- [TimeSeries](matlab-timeseries) — older time-series API
- [Table Join](matlab-table-join) — non-time table operations
- [Datetime](matlab-datetime) — datetime fundamentals
