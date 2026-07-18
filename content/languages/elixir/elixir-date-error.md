---
title: "[Solution] Elixir Calendar.CompatibilityError — Invalid Date or Time"
description: "Fix Elixir Calendar.CompatibilityError with invalid dates. Learn about Date, Time, and NaiveDateTime validation and construction."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
---

## What This Error Means

A `Calendar.CompatibilityError` is raised when you try to create a date, time, or datetime value with invalid components. The error message shows which component is invalid (like a day of 32 or a month of 13).

## Why It Happens

The most common cause is constructing a date with invalid day, month, or year values. For example, `~D[2024-02-30]` is invalid because February does not have 30 days.

Another frequent cause is using the wrong calendar system. Elixir's `Calendar` behaviour allows custom calendars, and if two dates use different calendars that are not compatible, operations between them fail.

Time values with invalid hour, minute, or second components also cause this error. For example, `~T[25:00:00]` is invalid because hours only go up to 23.

Leap second handling can cause issues. While Elixir supports leap seconds in some contexts, not all operations handle them correctly.

Finally, parsing date strings with invalid formats causes this error. If the string does not match the expected date format, parsing fails.

## How to Fix It

### Validate date components before construction

```elixir
def safe_date(year, month, day) do
  case Date.new(year, month, day) do
    {:ok, date} -> {:ok, date}
    {:error, reason} -> {:error, reason}
  end
end
```

### Use Date.new instead of sigils for dynamic dates

```elixir
# Wrong — may fail with invalid date
date = ~D[2024-02-30]

# Correct — validates during construction
case Date.new(2024, 2, 29) do
  {:ok, date} -> date
  {:error, reason} -> handle_error(reason)
end
```

### Check for valid ranges

```elixir
def valid_date?(year, month, day) do
  year in 1..9999 and
  month in 1..12 and
  day in 1..31
end
```

### Use Calendar.ISO for standard dates

```elixir
date = %Date{year: 2024, month: 1, day: 15, calendar: Calendar.ISO}
```

### Parse dates safely

```elixir
case Date.from_iso8601("2024-01-15") do
  {:ok, date} -> process(date)
  {:error, reason} -> handle_error(reason)
end
```

## Common Mistakes

- Not validating date components before constructing dates
- Assuming all months have 31 days
- Not using Date.new for dynamic date construction
- Mixing different calendar systems without compatibility checks
- Not handling Date.from_iso8601 errors

## Related Pages

- [Elixir ArgumentError](/languages/elixir/elixir-argumenterror-elixir/)
- [Elixir FunctionClauseError](/languages/elixir/elixir-clause-error/)
- [Elixir MatchError](/languages/elixir/elixir-matcherror-elixir/)
