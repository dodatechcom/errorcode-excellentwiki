---
title: "Julia Logging Level Configuration Error"
description: "Fix Julia logging errors when log level configuration produces unexpected output or missing log messages."
languages: ["julia"]
error-types: ["runtime-error"]
severities: ["warning"]
weight: 5
---

## What This Error Means

Logging configuration errors in Julia occur when the log level is set incorrectly, preventing expected messages from being displayed, or when custom loggers are not properly configured.

## Common Causes

- Default log level suppresses Debug and Info messages
- Custom logger not registered as global logger
- Log level set at wrong scope (local vs global)
- Using `@info` with wrong interpolation syntax
- Logger stream not available in non-interactive environments

## How to Fix

```julia
# WRONG: Debug messages not shown
@debug "This message is hidden"  # not visible by default

# CORRECT: Enable debug logging
ENV["JULIA_DEBUG"] = "all"
@debug "Now visible"
```

```julia
# WRONG: Custom logger not active
using Logging
logger = ConsoleLogger(stdout, Logging.Debug)
# messages still use default logger

# CORRECT: Set as global logger
global_logger(logger)
@info "This uses custom logger"
```

## Examples

```julia
# Example 1: Basic logging levels
@debug "Debug details"
@info "Informational message"
@warn "Warning message"
@error "Error occurred"

# Example 2: Configure via environment
ENV["JULIA_DEBUG"] = "MyModule"  # debug for specific module
ENV["JULIA_WARN"] = "all"        # enable warnings

# Example 3: Custom logger
using Logging
logger = ConsoleLogger(stdout, Logging.Info;
    show_limited=false,
    right_justify=0)
global_logger(logger)
@info "Configured logger" count=42
```

## Related Errors

- [IO error](julia-io-stream-error) -- I/O issues
- [System error](julia-system-error) -- system-level problems
