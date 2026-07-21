---
title: "[Solution] Pascal RANDOMIZE Procedure Error"
description: "Fix Pascal RANDOMIZE errors when initializing the random number generator."
languages: ["pascal"]
error-types: ["runtime-error"]
severities: ["error"]
---

RANDOMIZE errors occur when the random number generator is not initialized or when RANDOMIZE produces non-random sequences.

## Common Causes

- Not calling RANDOMIZE before RANDOM
- Same seed used every run
- RANDOMIZE on system without real-time clock
- RANDOM on non-integer types

## How to Fix

### 1. Call RANDOMIZE at program start

```pascal
begin
  Randomize;  // initialize with time-based seed
  WriteLn(Random(100));  // 0-99
end;
```

### 2. Use proper seeding for reproducibility

```pascal
// For reproducible results
RandSeed := 12345;  // fixed seed
// For different results each time
Randomize;
```

## Examples

```pascal
program RandomDemo;

var
  i, R: Integer;

begin
  Randomize;
  for i := 1 to 10 do
  begin
    R := Random(100);
    Write(R:4);
  end;
  WriteLn;
end.
```

## Related Errors

- [Runtime error](/languages/pascal/pascal-runtime-error)
- [Compile error](/languages/pascal/pascal-compiler-error-new)
- [Type mismatch](/languages/pascal/pascal-type-mismatch)
