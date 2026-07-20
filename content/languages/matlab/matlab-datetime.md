---
title: "[Solution] MATLAB datetime/NaT — Timezone, Format, caldiff/between Errors"
description: "Fix MATLAB datetime errors: NaT handling, timezone conversion, format strings, and caldiff/between usage."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 114
---

## Common Causes

- Comparing datetime with NaT (Not-a-Time) using standard comparison
- Mixing datetime with different timezones in arithmetic
- Incorrect format string in `datetime` constructor or `format`
- `caldiff` or `between` with incompatible calendar components
- Using `datenum` instead of datetime for modern date handling

## How to Fix

```matlab
% WRONG: NaT comparison with == or <
t1 = datetime('2024-01-01');
t2 = NaT;
result = t1 < t2;  % Returns logical.empty, not false

% CORRECT: Check for NaT before comparison
t1 = datetime('2024-01-01');
t2 = NaT;
if isnat(t2)
    disp('t2 is NaT — cannot compare');
elseif t1 < t2
    disp('t1 is earlier');
end
```

```matlab
% WRONG: Timezone mismatch in arithmetic
t1 = datetime('2024-06-01', 'TimeZone', 'America/New_York');
t2 = datetime('2024-06-01', 'TimeZone', 'Europe/London');
diff = t2 - t1;  % Includes timezone offset, may be unexpected

% CORRECT: Convert to same timezone first
t2_utc = t2; t2_utc.TimeZone = 'UTC';
t1_utc = t1; t1_utc.TimeZone = 'UTC';
diff = t2_utc - t1_utc;  % Pure time difference
```

```matlab
% CORRECT: Format datetime properly
t = datetime('now');
formatted = t; % Display format
formatted.Format = 'yyyy-MM-dd HH:mm:ss';
disp(formatted);

% Custom parsing
t = datetime('25-12-2024', 'InputFormat', 'dd-MM-yyyy');
```

```matlab
% CORRECT: caldiff and between with correct components
t1 = datetime('2024-01-01');
t2 = datetime('2024-06-15');

% Difference in specific calendar components
diffMonths = between(t1, t2, 'months');
diffDays = between(t1, t2, 'days');

% caldiff for sequences
T = datetime({'2024-01-01','2024-02-15','2024-03-20'});
gaps = caldiff(T, {'days'});  % Days between consecutive dates
```

```matlab
% CORRECT: Round datetime to specific precision
t = datetime('2024-06-15 14:32:45');
t_day = dateshift(t, 'start', 'day');
t_hour = dateshift(t, 'start', 'hour');
t_month = dateshift(t, 'start', 'month');
```

## Examples

```matlab
% Example: Working with business days
startDate = datetime('2024-01-01');
endDate = datetime('2024-12-31');
allDays = startDate:caldays(1):endDate;
weekdays = allDays(weekday(allDays) >= 2 & weekday(allDays) <= 6);
fprintf('Business days in 2024: %d\n', numel(weekdays));
```

## Related Errors

- [Duration](matlab-duration) — time arithmetic differences
- [TimeSeries](matlab-timeseries) — time-based data
- [Timetable](matlab-timetable) — time-indexed tables
