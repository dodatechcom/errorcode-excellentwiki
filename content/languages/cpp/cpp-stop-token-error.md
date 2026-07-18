---
title: "[Solution] C++ Stop Token Error — How to Fix"
description: "Fix C++ std::stop_token errors including callback registration failures, stop request races, and jthread integration issues."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
comments: true
---

# [Solution] C++ Stop Token Error — How to Fix

C++20 `std::stop_token` and `std::stop_source` provide cooperative cancellation for threads. Registration after stop, race conditions, and misuse with non-jthread contexts cause errors.

## Why It Happens

Stop token errors occur when registering a callback after stop has already been requested, when `stop_source` is moved-from and used, when `stop_token` is used with threads that don't support it, or when the callback function throws an exception.

## Common Error Messages

1. `error: callback registration after stop requested`
2. `std::system_error: stop token error`
3. Undefined behavior — using moved-from stop_source
4. `error: callback function threw exception`

## How to Fix It

### Fix 1: Register Callbacks Before Starting Work

```cpp
#include <stop_token>
#include <iostream>
#include <thread>

int main() {
    std::stop_source ssource;
    std::stop_token stoken = ssource.get_token();

    // CORRECT — register callback before thread starts
    stoken.request_stop();  // or let thread do it

    // WRONG — callback after stop is lost
    // ssource.request_stop();
    // stoken.stop_requested();  // true, but callback never fires

    std::jthread worker([](std::stop_token token) {
        while (!token.stop_requested()) {
            std::cout << "Working...\n";
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
    });
}
```

### Fix 2: Use Stop Callbacks for Cleanup

```cpp
#include <stop_token>
#include <iostream>
#include <thread>

void worker(std::stop_token token) {
    // Register cleanup callback
    std::stop_callback cb(token, []() {
        std::cout << "Cleaning up resources\n";
    });

    for (int i = 0; i < 10 && !token.stop_requested(); i++) {
        std::cout << "Processing " << i << "\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    std::cout << "Finished: " << (token.stop_requested() ? "cancelled" : "done") << "\n";
}

int main() {
    std::jthread t(worker);
    std::this_thread::sleep_for(std::chrono::milliseconds(300));
    // jthread destructor requests stop and joins
}
```

### Fix 3: Avoid Stop Source Lifetime Issues

```cpp
#include <stop_token>
#include <thread>

// WRONG — stop_source destroyed before thread uses it
void bad() {
    std::stop_token token;
    {
        std::stop_source ssource;
        token = ssource.get_token();
    }  // ssource destroyed — token still works
}

// CORRECT — keep stop_source alive
void good() {
    std::stop_source ssource;
    std::stop_token token = ssource.get_token();

    std::jthread t([token] {
        while (!token.stop_requested()) {
            std::this_thread::sleep_for(std::chrono::milliseconds(50));
        }
    });
}
```

## Common Scenarios

- **Callback registration**: Stop callbacks execute synchronously when stop is requested.
- **Multiple sources**: Multiple stop_sources can share a stop_token through `stop_possible()`.
- **No jthread**: You can use `stop_source`/`stop_token` without `std::jthread`.

## Prevent It

1. Always register stop callbacks before the stop might be requested.
2. Never use a moved-from `std::stop_source` — check `stop_possible()` if uncertain.
3. Use `std::jthread` for automatic stop request on destruction rather than manual management.

## Related Errors

- [Thread error]({{< relref "/languages/cpp/thread-error" >}}) — general threading issues.
- [Jthread error]({{< relref "/languages/cpp/cpp-jthread-error" >}}) — jthread-specific problems.
- [Data race]({{< relref "/languages/cpp/data-race" >}}) — unsynchronized stop checks.
