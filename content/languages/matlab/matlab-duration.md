---
title: "[Solution] MATLAB duration — Hours/Minutes/Seconds Arithmetic and Format"
description: "Fix MATLAB duration errors: arithmetic operations, format display, and converting between time units."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 115
---

## Common Causes

- Adding duration to datetime and expecting a datetime back (works, but confusing)
- Mixing duration and calendarDuration (incompatible arithmetic)
- Display format showing unexpected units (hours instead of seconds)
- Comparing duration with double values directly
- Using `seconds` vs `duration` vs `calduration` interchangeably

## How to Fix

```matlab
% WRONG: Comparing duration with numeric directly
d = seconds(60);
if d == 60  % Comparison with double fails
    disp('One minute');
end

% CORRECT: Compare duration values directly
d = seconds(60);
if d == minutes(1)
    disp('One minute');
end

% Or convert to numeric
if seconds(d) == 60
    disp('One minute');
end
```

```matlab
% WRONG: Adding calendarDuration to duration (incompatible)
d = hours(2);
cal = calmonths(1);
result = d + cal;  % Error: duration + calendarDuration not allowed

% CORRECT: Convert to compatible type
d = hours(2);
cal = calmonths(1);
result = days(30) + cal;  % Both calendarDuration
% Or
result = d + hours(calmonths(1));  % Approximate conversion
```

```matlab
% CORRECT: Display format control
d = hours(1) + minutes(30) + seconds(45);
d.Format = 'hh:mm:ss';    % Display as 01:30:45
d.Format = 'h';            % Display as 1 (hours)
d.Format = 's';            % Display as 5425 (seconds)
d.Format = 'd hh:mm:ss';  % Display as 0 01:30:45
```

```matlab
% CORRECT: Arithmetic between duration types
d1 = hours(2);
d2 = minutes(90);
total = d1 + d2;           % hours(3.5)
diff = d1 - d2;            % hours(0.5)
scaled = d1 * 3;           % hours(6)

% Convert between units
totalMinutes = minutes(total);   % 210
totalSeconds = seconds(total);   % 12600
```

```matlab
% CORRECT: Create duration from numeric values
d1 = seconds(90);           % 1.5 min
d2 = minutes(2.5);          % 2 min 30 sec
d3 = hours(1, 30, 45);      % 1 hour 30 min 45 sec
d4 = duration(1, 30, 45);   % Same as d3
```

## Examples

```matlab
% Example: Timing code execution with duration
tic;
pause(2.3);
elapsed = toc;
d = seconds(elapsed);
d.Format = 's';
fprintf('Elapsed: %s seconds\n', string(d));
```

## Related Errors

- [Datetime](matlab-datetime) — datetime vs duration
- [TimeSeries](matlab-timeseries) — time-based data
- [Timetable](matlab-timetable) — time-indexed operations
