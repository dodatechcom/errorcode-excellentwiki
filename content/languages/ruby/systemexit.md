---
title: "[Solution] Ruby SystemExit — Program Exit Fix"
description: "Handle Ruby SystemExit. Understand when exit is called and how to catch program termination for cleanup."
languages: ["ruby"]
severities: ["error"]
error_types: ["exit"]
weight: 170
---

# SystemExit — Program Exit Fix

A `SystemExit` is raised when `exit` is called in a Ruby program. It can be caught to perform cleanup before the program terminates.

## Description

`SystemExit` is a subclass of `Exception` (not `StandardError`). It's raised by `exit`, `exit!`, and `abort`. Unlike most exceptions, it signals normal program termination, not an error.

Common scenarios:

- **Explicit exit call** — `exit`, `exit(0)`, `exit(1)`.
- **abort method** — prints message and exits with status 1.
- **at_exit handlers** — run when program exits.
- **Script end-of-file** — normal termination.

## Common Causes

```ruby
# Cause 1: Explicit exit call
def process(input)
  exit if input.nil?  # Raises SystemExit
end

# Cause 2: abort with message
abort "Error: file not found"  # Raises SystemExit

# Cause 3: exit in at_exit handler
at_exit { exit }  # Infinite loop! Raises SystemExit

# Cause 4: exit in thread
Thread.new { exit }  # May raise SystemExit in main thread
```

## Solutions

### Fix 1: Catch SystemExit for cleanup

```ruby
begin
  main_process
rescue SystemExit => e
  status = e.status  # 0 for exit(0), 1 for exit(1)
  puts "Program exited with status: #{status}"
  cleanup
end
```

### Fix 2: Use at_exit for cleanup

```ruby
# Register cleanup handler
at_exit do
  puts "Cleaning up..."
  remove_temp_files
end

# Main program
main_process
```

### Fix 3: Use ensure for cleanup

```ruby
# Correct — ensure runs even on SystemExit
begin
  main_process
ensure
  cleanup  # Runs even on SystemExit
end
```

### Fix 4: Use Kernel#exit carefully

```ruby
# Wrong — exit in library code
def helper
  exit 1 if error  # Bad: kills the entire program
end

# Correct — raise an exception instead
def helper
  raise StandardError, "Fatal error" if error
end
```

## Related Errors

- [Interrupt](interrupt) — user interrupt (Ctrl+C).
- [SignalException](signal-exception) — signal-based exceptions.
- [IOError](io-error) — stream closed during shutdown.
