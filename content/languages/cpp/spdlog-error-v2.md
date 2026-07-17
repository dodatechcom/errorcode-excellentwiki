---
title: "[Solution] spdlog Sink Creation Error Fix"
description: "Fix spdlog sink creation errors. Handle file sink failures, async queue overflow, and sink configuration issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# spdlog Sink Creation Error Fix

Fix spdlog sink creation errors. Handle file sink failures, async queue overflow, and sink configuration issues.

## What This Error Means

spdlog sink errors occur when log sinks cannot be created or configured:

```
spdlog error: Failed opening file "app.log" for writing
spdlog error: async logger queue overflow
```

## Common Causes

```cpp
// Cause 1: Invalid file path or permissions
auto file_sink = std::make_shared<spdlog::sinks::basic_file_sink_mt>("/root/app.log");

// Cause 2: Directory does not exist
// Cause 3: Async queue size too small
// Cause 4: Logger name already registered
// Cause 5: Rotating file size limit reached
```

## How to Fix

### Fix 1: Ensure directory exists before creating file sink

```cpp
#include "spdlog/spdlog.h"
#include "spdlog/sinks/basic_file_sink.h"
#include <filesystem>

void setup_logger(const std::string& path) {
    auto parent = std::filesystem::path(path).parent_path();
    if (!parent.empty()) {
        std::filesystem::create_directories(parent);
    }
    auto logger = spdlog::basic_logger_mt("app", path);
}
```

### Fix 2: Use async logger with larger queue

```cpp
#include "spdlog/async.h"
#include "spdlog/sinks/basic_file_sink.h"

void setup_async_logger() {
    spdlog::init_thread_pool(8192, 1);
    auto file_sink = std::make_shared<spdlog::sinks::basic_file_sink_mt>("app.log");
    auto logger = std::make_shared<spdlog::async_logger>(
        "app", file_sink, spdlog::thread_pool(),
        spdlog::async_overflow_policy::block);
    spdlog::set_default_logger(logger);
}
```

### Fix 3: Check logger name before creating

```cpp
#include "spdlog/spdlog.h"

void ensure_logger(const std::string& name) {
    if (spdlog::get(name)) {
        return; // Already exists
    }
    auto logger = spdlog::daily_logger_mt(name, "logs/" + name + ".log", 0, 0);
    spdlog::set_default_logger(logger);
}
```

## Examples

```cpp
#include "spdlog/spdlog.h"
#include "spdlog/sinks/stdout_color_sinks.h"
#include "spdlog/sinks/rotating_file_sink.h"

void init_logging() {
    auto console_sink = std::make_shared<spdlog::sinks::stdout_color_sink_mt>();
    auto file_sink = std::make_shared<spdlog::sinks::rotating_file_sink_mt>(
        "logs/app.log", 1048576 * 5, 3); // 5MB max, 3 rotated files

    std::vector<spdlog::sink_ptr> sinks{console_sink, file_sink};
    auto logger = std::make_shared<spdlog::logger>("app", sinks.begin(), sinks.end());

    logger->set_level(spdlog::level::debug);
    spdlog::set_default_logger(logger);
}

int main() {
    init_logging();
    spdlog::info("Application started");
    spdlog::debug("Debug message");
    spdlog::error("Error: {}", "something went wrong");
    return 0;
}
```

## Related Errors

- [Log Error]({{< relref "/languages/rust/log-error" >}}) — log error
- [FStream Error]({{< relref "/languages/cpp/fstream-error" >}}) — fstream error
- [Format Error]({{< relref "/languages/cpp/format-error" >}}) — format error
