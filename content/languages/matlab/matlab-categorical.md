---
title: "[Solution] MATLAB categorical — Categories, addcats/removecats Errors"
description: "Fix MATLAB categorical array errors: category management, addcats, removecats, and ordinal vs nominal types."
languages: ["matlab"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 113
---

## Common Causes

- Assigning a value not in the category list to an ordinal categorical
- Using `addcats` or `removecats` on a non-categorical array
- Comparing categorical values with string comparison instead of `==`
- Merging categories without handling duplicates
- Converting between ordinal and nominal loses ordering info

## How to Fix

```matlab
% WRONG: Assigning out-of-range value to ordinal categorical
grades = categorical({'A','B','C'}, {'A','B','C','D','F'}, 'Ordinal', true);
grades(4) = 'Z';  % Error: 'Z' not in category list

% CORRECT: Add categories before assigning
grades = addcats(grades, 'Z');
grades(4) = 'Z';  % Now works
```

```matlab
% WRONG: String comparison with categorical
C = categorical({'red','blue','red'});
if C(1) == "red"  % Works in R2019b+ but may cause issues in older versions
    disp('Match');
end

% CORRECT: Use == operator consistently
C = categorical({'red','blue','red'});
if C(1) == categorical('red')
    disp('Match');
end
```

```matlab
% CORRECT: Convert between types safely
C = categorical({'low','medium','high','low'});
C_ord = reordercats(C, {'low','medium','high'});
C_ord = setcats(C_ord, {'low','medium','high'}, 'Ordinal', true);

% Remove a category
C_no_low = removecats(C, 'low');
```

```matlab
% CORRECT: Merge categories
C = categorical({'cat','dog','cat','bird','dog'});
cats = categories(C);
disp(cats);  % {'bird'; 'cat'; 'dog'}

% Rename a category
C_renamed = renamecats(C, {'bird','cat','dog'}, {'avian','feline','canine'});
```

```matlab
% CORRECT: categorical from numeric data
data = [1 2 3 1 2 3];
C = categorical(data, [1 2 3], {'Low','Medium','High'});

% Merge levels
C_merged = mergecats(C, {'Low','Medium'}, 'BelowHigh');
```

## Examples

```matlab
% Example: Full categorical workflow
function C = processData(rawData)
    C = categorical(rawData);

    % Check for unknown categories
    validCats = {'approved','rejected','pending'};
    unknowns = ~ismember(string(C), validCats);
    if any(unknowns)
        warning('Unknown categories found: %s', ...
            strjoin(unique(string(C(unknowns))), ', '));
    end

    % Reorder for display
    C = reordercats(C, validCats);
end
```

## Related Errors

- [Table Join](matlab-table-join) — categorical keys in joins
- [String Error](matlab-string-error) — string vs categorical
- [Table Index](matlab-table-index) — categorical column access
