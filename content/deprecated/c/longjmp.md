---
title: "[Solution] C longjmp() Deprecated — Use C++ Exceptions or Error Handling"
description: "Replace longjmp() with C++ exceptions, RAII, or structured error handling. Migration guide with code examples."
deprecated_function: "longjmp"
replacement_function: "C++ exceptions / goto cleanup"
languages: ["c"]
error-types: ["deprecated"]
severities: ["warning"]
tags: ["longjmp", "setjmp", "exceptions", "error-handling", "c", "cpp"]
weight: 5
---

# [Solution] C longjmp() Deprecated — Use C++ Exceptions or Error Handling

The `longjmp()` function is deprecated because it performs a non-local jump that bypasses all intermediate stack frames, skipping destructors, resource cleanup, and security checks. It must be used with `setjmp()` and is the counterpart to that deprecated function. In C++, use exceptions. In C, use `goto` for structured cleanup.

## What You'll See

Compiler warnings:

```
warning: 'longjmp' is deprecated: use exceptions or structured error handling
```

## Why Deprecated

`longjmp()` is deprecated because:

- **Skips destructors**: C++ objects on the stack are not destroyed, causing resource leaks.
- **Stack unwinding bypassed**: RAII patterns, lock guards, and smart pointers are ineffective.
- **Undefined behavior**: `longjmp()` into a function that has returned is undefined behavior.
- **No stack trace**: Debugging becomes extremely difficult when the stack is unwound non-locally.
- **Variable state uncertainty**: Automatic variables modified after `setjmp` and before `longjmp` may have indeterminate values.

## Old Code (Deprecated)

```c
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

jmp_buf error_handler;

void allocate_resources(void) {
    printf("Allocating resources...\n");
}

void release_resources(void) {
    printf("Releasing resources...\n");
}

void risky_operation(void) {
    allocate_resources();

    if (rand() % 2 == 0) {
        printf("Error occurred!\n");
        longjmp(error_handler, 1);  // Skips release_resources!
    }

    release_resources();
}

int main(void) {
    if (setjmp(error_handler) != 0) {
        fprintf(stderr, "Recovering from error\n");
        // release_resources() was never called — leak!
        return 1;
    }

    risky_operation();
    return 0;
}
```

## New Code — C: goto Cleanup Pattern

```c
#include <stdio.h>
#include <stdlib.h>

int risky_operation(void) {
    int result = -1;
    int *buffer = NULL;
    FILE *fp = NULL;

    buffer = malloc(1024);
    if (buffer == NULL) {
        goto cleanup;
    }

    fp = fopen("data.txt", "w");
    if (fp == NULL) {
        goto cleanup;
    }

    // Simulate error condition
    if (rand() % 2 == 0) {
        goto cleanup;
    }

    printf("Operation succeeded\n");
    result = 0;

cleanup:
    if (fp != NULL) {
        fclose(fp);
    }
    free(buffer);
    return result;
}

int main(void) {
    if (risky_operation() != 0) {
        fprintf(stderr, "Operation failed\n");
        return 1;
    }
    return 0;
}
```

## New Code — C: Function-Level Cleanup

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    FILE *fp;
    char *buffer;
    int initialized;
} OperationContext;

int operation_init(OperationContext *ctx) {
    ctx->fp = NULL;
    ctx->buffer = NULL;
    ctx->initialized = 1;

    ctx->buffer = malloc(1024);
    if (ctx->buffer == NULL) {
        return -1;
    }

    ctx->fp = fopen("data.txt", "w");
    if (ctx->fp == NULL) {
        return -1;
    }

    return 0;
}

void operation_cleanup(OperationContext *ctx) {
    if (!ctx->initialized) return;
    if (ctx->fp != NULL) fclose(ctx->fp);
    free(ctx->buffer);
    ctx->initialized = 0;
}

int main(void) {
    OperationContext ctx = {0};

    if (operation_init(&ctx) != 0) {
        fprintf(stderr, "Failed to initialize\n");
        operation_cleanup(&ctx);
        return 1;
    }

    // Use ctx...
    printf("Operation succeeded\n");

    operation_cleanup(&ctx);
    return 0;
}
```

## New Code — C++ Exception Replacement

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <stdexcept>
#include <string>

class Resource {
    std::string name;
    std::ofstream file;
public:
    Resource(const std::string& n) : name(n), file(n) {
        if (!file.is_open()) {
            throw std::runtime_error("Cannot open: " + n);
        }
        std::cout << "Acquired " << name << std::endl;
    }
    ~Resource() {
        if (file.is_open()) file.close();
        std::cout << "Released " << name << std::endl;
    }
    void write(const std::string& data) { file << data; }
};

void risky_operation() {
    Resource r1("a.txt");  // RAII — guaranteed cleanup
    Resource r2("b.txt");

    if (rand() % 2 == 0) {
        throw std::runtime_error("Random failure");  // Resources cleaned up
    }

    r1.write("data");
    r2.write("data");
}

int main() {
    try {
        risky_operation();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}
```

## Migration Steps

1. **Find all longjmp() calls**:

```bash
grep -rn "\blongjmp\s*(" --include="*.c" --include="*.cpp" /path/to/project/
```

2. **Identify what cleanup is skipped** by each `longjmp()` — memory, file handles, locks, network connections.

3. **For C code**: Replace with `goto cleanup` at the end of the function, with cleanup code before the label.

4. **For C++ code**: Replace with `throw` and rely on RAII for cleanup.

5. **Use scope-bound resource management** — ensure every resource has a cleanup mechanism.

6. **Remove all `setjmp()` calls** after migrating `longjmp()`.

## Related Deprecations

- [setjmp → C++ exceptions]({{< relref "/deprecated/c/setjmp" >}}) — the counterpart function.
- [exit → atexit cleanup]({{< relref "/deprecated/c/exit" >}}) — program exit alternatives.
- [abort → proper error handling]({{< relref "/deprecated/c/abort" >}}) — graceful error recovery.
