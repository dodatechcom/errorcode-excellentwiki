---
title: "[Solution] C++ Folly Error — How to Fix"
description: "Fix C++ Folly library errors including Futures failures, string optimization issues, and container misuse in Facebook's Folly library."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime", "compile-time"]
weight: 5
comments: true
---

# [Solution] C++ Folly Error — How to Fix

Facebook's Folly library errors occur from incorrect Future chaining, misuse of `folly::Optional` and `folly::StringPiece`, event base loop issues, and thread-safety violations with Folly containers.

## Why It Happens

Folly errors arise from chaining `.then()` on unfulfilled futures, using `folly::future` without an executor, incorrect `folly::makeFuture` usage, accessing moved-from `folly::IOBuf` objects, or using `folly::thread_local_ptr` without proper initialization.

## Common Error Messages

1. `error: future not yet fulfilled — .then() called prematurely`
2. `error: folly::Future requires an executor for .then()`
3. `error: IOBuf already moved`
4. `error: thread_local_ptr not initialized`

## How to Fix It

### Fix 1: Use Folly Futures Correctly

```cpp
#include <folly/futures/Future.h>
#include <folly/executors/InlineExecutor.h>
#include <iostream>

int main() {
    // CORRECT — create and chain futures
    folly::Promise<int> promise;
    folly::Future<int> future = promise.getFuture();

    auto result = future
        .thenValue([](int val) { return val * 2; })
        .thenValue([](int val) { return val + 10; });

    promise.setValue(21);
    std::cout << result.get() << "\n";  // 52

    return 0;
}
```

### Fix 2: Handle Future Errors

```cpp
#include <folly/futures/Future.h>
#include <iostream>

folly::Future<int> safe_divide(int a, int b) {
    if (b == 0) {
        return folly::makeFuture<int>(
            std::runtime_error("division by zero"));
    }
    return folly::makeFuture(a / b);
}

int main() {
    auto result = safe_divide(10, 0)
        .thenValue([](int val) {
            return val * 2;
        })
        .toUnsafeBox();

    // CORRECT — check if future has error
    if (result.hasException()) {
        std::cout << "Error occurred\n";
    }

    auto good = safe_divide(10, 2).get();
    std::cout << "Result: " << good << "\n";  // 5

    return 0;
}
```

### Fix 3: Use IOBuf Correctly

```cpp
#include <folly/io/IOBuf.h>
#include <iostream>

int main() {
    // CORRECT — create and use IOBuf
    auto buf = folly::IOBuf::create(1024);
    buf->append(5);
    std::memcpy(buf->writableData(), "hello", 5);

    std::cout << std::string(
        reinterpret_cast<const char*>(buf->data()),
        buf->length()
    ) << "\n";

    // CORRECT — chain IOBuf correctly
    auto chain = folly::IOBuf::create(256);
    chain->append(3);
    std::memcpy(chain->writableData(), "foo", 3);

    // Move, don't copy
    auto moved = std::move(chain);
    // chain is now invalid — don't use

    return 0;
}
```

### Fix 4: Use Folly Containers Safely

```cpp
#include <folly/container/F14Map.h>
#include <string>
#include <iostream>

int main() {
    // CORRECT — F14 fast hash map
    folly::F14FastMap<std::string, int> map;
    map.emplace("key1", 100);
    map.emplace("key2", 200);

    auto it = map.find("key1");
    if (it != map.end()) {
        std::cout << it->second << "\n";
    }

    // CORRECT — iterate safely
    for (const auto& [key, value] : map) {
        std::cout << key << ": " << value << "\n";
    }

    return 0;
}
```

## Common Scenarios

- **Future chaining**: Calling `.then()` before the future is fulfilled produces errors.
- **IOBuf moves**: IOBuf is move-only — copying or double-moving causes crashes.
- **Executor requirements**: Some Future operations require explicit executors.

## Prevent It

1. Always check `future.hasException()` or use `.get()` to retrieve values/errors.
2. Use `std::move` with IOBuf — never copy an IOBuf.
3. Provide executors explicitly: `.via(&executor).thenValue(...)` for thread control.

## Related Errors

- [Abseil error]({{< relref "/languages/cpp/cpp-abseil-error.md" >}}) — Google's library issues.
- [Boost ASIO error]({{< relref "/languages/cpp/boost-asio-error" >}}) — async I/O issues.
- [Thread system error]({{< relref "/languages/cpp/thread-system-error" >}}) — thread failures.
