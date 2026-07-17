---
title: "[Solution] C++ spdlog - logging error"
description: "Fix C++ spdlog logging errors. Resolve spdlog configuration and formatting issues."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["spdlog", "logging", "format", "sink", "async"]
weight: 5
---

# spdlog - logging error

spdlog errors occur from invalid format strings, sink failures, or asynchronous queue overflow.

## Common Causes

```cpp
// Cause 1: Format mismatch
spdlog::info("Hello, {} and {}!", "Alice"); // too few args

// Cause 2: Sink failure
auto file_sink = std::make_shared<spdlog::sinks::basic_file_sink_mt>("readonly/path.log");
// Permission denied

// Cause 3: Async queue overflow
spdlog::set_mode(spdlog::async_mode);
// Queue full when logging too fast
```

## How to Fix

### Fix 1: Match format arguments

```cpp
spdlog::info("Hello, {} and {}!", "Alice", "Bob");
```

### Fix 2: Check sink availability

```cpp
try {
    auto logger = spdlog::basic_logger_mt("file_logger", "logs/app.log");
} catch (const spdlog::spdlog_ex& e) {
    std::cerr << "Logger init failed: " << e.what() << std::endl;
}
```

### Fix 3: Increase async queue size

```cpp
spdlog::init_thread_pool(83886, 1);
```

## Related Errors

- [fmt - formatting error]({{< relref "/languages/cpp/fmt-error" >}}) — format string errors.
- [spdlog error (detailed)]({{< relref "/languages/cpp/spdlog-error" >}}) — detailed spdlog errors.
- [std::ios_base::failure]({{< relref "/languages/cpp/ios-base-failure" >}}) — stream errors.
