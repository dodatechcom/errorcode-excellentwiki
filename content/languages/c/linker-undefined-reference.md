---
title: "[Solution] C UNDEFINED_REFERENCE — Undefined reference to symbol"
description: "Fix C undefined reference errors by checking function names, linking object files, and library order. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["linker-error"]
weight: 801
---

# C UNDEFINED_REFERENCE — Undefined reference to symbol

The linker cannot find the definition of a function or variable that is referenced in your code. This typically happens when the object file or library containing the symbol is not linked, or the symbol name does not match.

## Common Causes

```c
// Cause 1: Forgetting to link the object file containing the function
// main.c
void greet(void);  // declaration exists
int main(void) {
    greet();
    return 0;
}
// greet.c has the definition, but you compile only: gcc main.c -o app
```

```c
// Cause 2: Typo in function name
// Header declares: void print_message(void);
// Source defines:  void printmessage(void);
void print_message(void);  // declaration
int main(void) {
    print_message();  // linker error: undefined reference to print_message
    return 0;
}
```

```c
// Cause 3: Missing library at the end of the command line
// gcc main.c -lm   WRONG order
// gcc main.c -lm   gcc requires libraries AFTER the objects that use them
#include <math.h>
int main(void) {
    double x = sqrt(4.0);  // undefined reference to sqrt
    return (int)x;
}
```

```c
// Cause 4: C++ name mangling when linking C code
// If a C library is compiled as C++ but headers lack extern "C"
void my_c_function(void);  // declared in header without extern "C"
// Linker looks for _Z15my_c_functionv but symbol is my_c_function
```

```c
// Cause 5: Conditional compilation excluding the definition
// config.h: #define HAS_FEATURE 0
// feature.c:
#if HAS_FEATURE
void feature_init(void) { /* ... */ }
#endif
// Linker cannot find feature_init when HAS_FEATURE is 0
```

## How to Fix

### Fix 1: Link all required object files and libraries

```bash
# Compile all source files together
gcc main.c utils.c -o app

# Or compile separately, then link
gcc -c main.c
gcc -c utils.c
gcc main.o utils.o -o app
```

### Fix 2: Place libraries after object files

```bash
# WRONG: library before object files
gcc -lm main.c -o app

# CORRECT: library after objects that use it
gcc main.c -o app -lm

# For multiple interdependent libraries, use -Wl,--start-group
gcc main.o -Wl,--start-group -lfoo -lbar -lbaz -Wl,--end-group -o app
```

### Fix 3: Verify function names match between declaration and definition

```c
// header.h
void calculate_sum(int a, int b);  // note: underscore between words

// source.c — make sure the name matches exactly
void calculate_sum(int a, int b) {  // not calculateSum or calc_sum
    printf("%d\n", a + b);
}
```

### Fix 4: Use extern "C" when linking C code from C++

```cpp
#ifdef __cplusplus
extern "C" {
#endif

void my_c_function(void);

#ifdef __cplusplus
}
#endif
```

### Fix 5: Check that conditional compilation includes the needed symbols

```c
// Ensure the definition is always compiled, or always excluded with the declaration
#if !defined(HAS_FEATURE)
// Provide a stub so linking succeeds even without the feature
void feature_init(void) { /* no-op */ }
#endif
```

## Examples

```c
// A common real-world scenario: linking with pthread
#include <pthread.h>
#include <stdio.h>

void* thread_func(void* arg) {
    printf("Hello from thread\n");
    return NULL;
}

int main(void) {
    pthread_t tid;
    pthread_create(&tid, NULL, thread_func, NULL);
    pthread_join(tid, NULL);
    return 0;
}
// Compile: gcc main.c -o app          ← undefined reference to pthread_create
// Fix:     gcc main.c -o app -lpthread ← library AFTER source
```

```c
// Splitting code across files
// math_utils.h
int add(int a, int b);

// math_utils.c
#include "math_utils.h"
int add(int a, int b) { return a + b; }

// main.c
#include "math_utils.h"
#include <stdio.h>
int main(void) {
    printf("%d\n", add(2, 3));  // undefined reference if math_utils.c not compiled
    return 0;
}
// Fix: gcc main.c math_utils.c -o app
```

## Related Errors

- [C MULTIPLE_DEFINITION](/languages/c/linker-multiple-definition) — Multiple definition of symbol
- [C CANNOT_FIND_LIBRARY](/languages/c/linker-cannot-find-library) — Cannot find -l
- [C IMPLICIT_DECLARATION](/languages/c/gcc-implicit-declaration) — Implicit function declaration
- [C UNDEFINED_REFERENCE_STATIC](/languages/c/linker-undefined-reference-static) — Undefined reference in static library
