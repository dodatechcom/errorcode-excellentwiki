---
title: "[Solution] C++ spdlog Error — How to Fix"
description: "Fix C++ spdlog logging errors including sink configuration failures, format string issues, and thread-safety violations in spdlog usage."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ spdlog Error — How to Fix

spdlog logging errors occur when sinks aren't properly initialized, when format strings contain invalid placeholders, when loggers aren't registered before use, or when thread-safety settings conflict with multi-threaded usage.

## Why It Happens

spdlog errors arise from using a logger before `spdlog::register_logger`, when sink creation fails (e.g., invalid file path), when format strings have mismatched arguments, when `spdlog::set_level` is called on the wrong logger, or when async logging fills the queue and drops messages.

## Common Error Messages

1. `error: spdlog::spdlog_ex: async logger: invalid log level`
2. `error: logger 'name' not found — not registered`
3. `error: sink creation failed — file cannot be opened`
4. `error: format string mismatch in spdlog call`

## How to Fix It

### Fix 1: Initialize Sinks Properly

```cpp
#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_color_sinks.h>
#include <spdlog/sinks/basic_file_sink.h>

int main() {
    // CORRECT — create and register logger
    auto console_sink = std::make_shared<spdlog::sinks::stdout_color_sink_mt>();
    auto file_sink = std::make_shared<spdlog::sinks::basic_file_sink_mt>("app.log", true);

    auto logger = std::make_shared<spdlog::logger>(
        "mylogger", spdlog::sinks_init_list{console_sink, file_sink});

    // CORRECT — register the logger
    spdlog::register_logger(logger);
    spdlog::set_default_logger(logger);

    spdlog::info("Application started");
    spdlog::set_level(spdlog::level::debug);
    spdlog::debug("Debug message");

    return 0;
}
```

### Fix 2: Use Correct Format Strings

```cpp
#include <spdlog/spdlog.h>

int main() {
    auto logger = spdlog::stdout_color_mt("console");

    // CORRECT — use spdlog format syntax
    logger->info("Hello, {}!", "world");
    logger->info("Value: {}, Name: {}", 42, "test");

    // WRONG — spdlog uses {}, not %d
    // logger->info("Value: %d", 42);  // will print literally

    return 0;
}
```

### Fix 3: Handle Thread Safety

```cpp
#include <spdlog/spdlog.h>
#include <thread>
#include <vector>

int main() {
    auto logger = spdlog::stdout_color_mt("threaded");

    // CORRECT — spdlog loggers with _mt suffix are thread-safe
    std::vector<std::thread> threads;
    for (int i = 0; i < 4; i++) {
        threads.emplace_back([logger, i]() {
            for (int j = 0; j < 100; j++) {
                logger->info("Thread {} message {}", i, j);
            }
        });
    }

    for (auto& t : threads) t.join();
    return 0;
}
```

### Fix 4: Use Async Logging Correctly

```cpp
#include <spdlog/async.h>
#include <spdlog/sinks/stdout_sinks.h>

int main() {
    // CORRECT — initialize async logger
    spdlog::init_thread_pool(8192, 1);
    auto sink = std::make_shared<spdlog::sinks::stdout_sink_mt>();
    auto logger = std::make_shared<spdlog::async_logger>(
        "async", sink, spdlog::thread_pool(),
        spdlog::async_overflow_policy::block);

    spdlog::set_default_logger(logger);
    spdlog::info("Async message");

    // CORRECT — flush before exit
    spdlog::shutdown();

    return 0;
}
```

## Common Scenarios

- **Unregistered logger**: Using `spdlog::get()` before registering creates a null logger.
- **Dropped messages**: Async logging with small queue sizes drops messages under heavy load.
- **File sink failure**: Invalid paths cause sink creation to throw.

## Prevent It

1. Always register loggers with `spdlog::register_logger` before use.
2. Use `spdlog::set_default_logger` to set a global default logger.
3. Call `spdlog::shutdown()` before program exit to flush all sinks.

## Related Errors

- [fmt error]({{< relref "/languages/cpp/cpp-fmt-error.md" >}}) — formatting issues.
- [Thread system error]({{< relref "/languages/cpp/thread-system-error" >}}) — thread failures.
- [Filesystem error]({{< relref "/languages/cpp/filesystemerror" >}}) — file operation issues.
