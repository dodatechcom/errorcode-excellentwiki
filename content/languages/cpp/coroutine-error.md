---
title: "[Solution] C++ Coroutine Error — Coroutine Fix"
description: "Fix C++ coroutine errors including unhandled exceptions, coroutine frame issues, and co_await problems. Learn correct coroutine patterns."
languages: ["cpp"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# [Solution] C++ Coroutine Error — Coroutine Fix

Coroutine errors occur when a coroutine throws an exception that isn't caught, when `co_return` is called without a return object, when the coroutine promise type doesn't satisfy requirements, or when awaiting invalid awaitable objects.

## Why Coroutine Errors Occur

Common causes include unhandled exceptions in coroutine bodies (stored in promise but never retrieved), calling `co_return` with wrong type for the promise, using `co_await` on non-awaitable types, coroutine frame memory allocation failure, and missing required promise methods.

## Wrong: Unhandled Exception in Coroutine

```cpp
// WRONG — exception stored but may never be retrieved
#include <coroutine>
#include <iostream>
#include <exception>

struct Task {
    struct promise_type {
        int result;
        Task get_return_object() { return {*this}; }
        std::suspend_never initial_suspend() { return {}; }
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_value(int v) { result = v; }
        void unhandled_exception() { std::terminate(); }
    };

    std::coroutine_handle<promise_type> handle;
    promise_type& promise;

    Task(promise_type& p) : handle(std::coroutine_handle<promise_type>::from_promise(p)), promise(p) {}
    ~Task() { if (handle) handle.destroy(); }

    int get() { return promise.result; }
};

Task failing_coro() {
    throw std::runtime_error("coroutine failed");  // unhandled_exception called
    co_return 0;
}

int main() {
    auto task = failing_coro();
    std::cout << task.get() << std::endl;
    return 0;
}
```

## Correct: Handle Exceptions in Promise

```cpp
// CORRECT — store exception and rethrow on get
#include <coroutine>
#include <iostream>
#include <exception>
#include <stdexcept>

struct Task {
    struct promise_type {
        int result;
        std::exception_ptr eptr;

        Task get_return_object() { return {*this}; }
        std::suspend_never initial_suspend() { return {}; }
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_value(int v) { result = v; }
        void unhandled_exception() { eptr = std::current_exception(); }
    };

    std::coroutine_handle<promise_type> handle;
    promise_type& promise;

    Task(promise_type& p) : handle(std::coroutine_handle<promise_type>::from_promise(p)), promise(p) {}
    ~Task() { if (handle) handle.destroy(); }

    int get() {
        if (promise.eptr) std::rethrow_exception(promise.eptr);
        return promise.result;
    }
};

Task may_throw(bool fail) {
    if (fail) throw std::runtime_error("coroutine failed");
    co_return 42;
}

int main() {
    try {
        auto task1 = may_throw(false);
        std::cout << "Result: " << task1.get() << std::endl;

        auto task2 = may_throw(true);
        std::cout << task2.get() << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Caught: " << e.what() << std::endl;
    }
    return 0;
}
```

## Use co_await With Valid Awaitables

```cpp
// CORRECT — use proper awaitable types
#include <coroutine>
#include <iostream>

struct Resumable {
    bool await_ready() { return false; }
    void await_suspend(std::coroutine_handle<>) {}
    void await_resume() {}
};

struct VoidTask {
    struct promise_type {
        VoidTask get_return_object() { return {}; }
        std::suspend_never initial_suspend() { return {}; }
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_void() {}
        void unhandled_exception() { std::terminate(); }
    };
};

VoidTask my_coro() {
    co_await Resumable{};
    std::cout << "Resumed" << std::endl;
}

int main() {
    my_coro();
    return 0;
}
```

## Summary

| Fix | When to Use |
|---|---|
| Always implement `unhandled_exception()` | In every coroutine promise type |
| Store and rethrow exceptions | When errors need to propagate to caller |
| Use `std::suspend_never` for eager coroutines | When coroutine should run immediately |
| Use `std::suspend_always` for lazy coroutines | When coroutine should wait for explicit resume |

## Related Errors

- [std::generator error]({{< relref "/languages/cpp/generator-error" >}}) — generator-specific errors.
- [std::future_error]({{< relref "/languages/cpp/future-error" >}}) — future/promise errors.
- [std::runtime_error]({{< relref "/languages/cpp/runtimeerror" >}}) — general runtime failures.
