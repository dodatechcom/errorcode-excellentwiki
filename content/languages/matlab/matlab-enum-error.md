---
title: "[Solution] MATLAB Enumeration Class — Enumerated Values and ordinal method"
description: "Fix MATLAB enumeration class errors: enumerated value access, ordinal method, class enumeration rules, and string conversion."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 119
---

## Common Causes

- Accessing enumeration member that doesn't exist
- Comparing enumeration with string or numeric using `==`
- Using `ordinal` on non-categorical data
- Defining enumeration class with duplicate member names
- Converting between enumeration and numeric/string incorrectly

## How to Fix

```matlab
% WRONG: Comparing enumeration with string
classdef Color
    enumeration
        Red, Green, Blue
    end
end

c = Color.Red;
if c == 'Red'  % Error: enum vs string comparison
    disp('Red');
end

% CORRECT: Compare enum values directly or use string conversion
c = Color.Red;
if c == Color.Red
    disp('Red');
end
% Or
if string(c) == "Red"
    disp('Red');
end
```

```matlab
% WRONG: Accessing nonexistent member
c = Color.Purple;  % Error: 'Purple' is not a member of Color

% CORRECT: Use validatestring or ismember
validMembers = {'Red','Green','Blue'};
input = 'Purple';
if ismember(input, validMembers)
    c = Color.(input);
else
    error('Invalid color: %s. Use: %s', input, strjoin(validMembers, ', '));
end
```

```matlab
% CORRECT: Enum class definition with methods
classdef Weekday
    enumeration
        Mon, Tue, Wed, Thu, Fri, Sat, Sun
    end

    methods
        function tf = isWeekday(obj)
            tf = obj <= Weekday.Fri;
        end

        function str = char(obj)
            str = char(string(obj));
        end
    end
end
```

```matlab
% CORRECT: ordinal() creates ordinal categorical, not enum class
levels = {'low','medium','high'};
values = {'high','low','medium','high','low'};
ord = ordinal(values, levels, levels);

% Access ordinal properties
disp(levels(get(ord, 'Code')));  % Convert back to string
```

```matlab
% CORRECT: Enum to numeric mapping
classdef StatusCode
    enumeration
        OK(200), NotFound(404), Error(500)
    end

    properties
        Code double
    end

    methods
        function obj = StatusCode(code)
            obj.Code = code;
        end
    end
end

s = StatusCode.OK;
fprintf('Status: %d\n', s.Code);  % 200
```

## Examples

```matlab
% Example: Using enum for state machine
classdef RobotState
    enumeration
        Idle, Moving, Charging, Error
    end

    methods
        function next = transition(obj, event)
            switch obj
                case RobotState.Idle
                    if strcmp(event, 'start')  next = RobotState.Moving;
                    else                       next = obj;
                    end
                case RobotState.Moving
                    if strcmp(event, 'stop')   next = RobotState.Idle;
                    else                       next = obj;
                    end
                otherwise
                    next = obj;
            end
        end
    end
end
```

## Related Errors

- [Categorical](matlab-categorical) — categorical arrays
- [String Error](matlab-string-error) — string conversion
- [Struct Error](matlab-struct-error) — named field access
