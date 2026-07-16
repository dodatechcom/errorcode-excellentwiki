---
title: "[Solution] C Stack Overflow — Recursive Function Fix"
description: "Fix C stack overflow errors caused by infinite recursion quickly using these proven methods. Debug and fix recursive functions by adding proper base cases."
languages: ["c"]
severities: ["error"]
error_types: ["runtime"]
tags: ["stack-overflow", "recursion", "stack"]
weight: 30
---

# [Solution] C Stack Overflow — Recursive Function Fix

A stack overflow in C occurs when a function calls itself recursively without a proper termination condition, exhausting the call stack. The operating system terminates the process with a signal (`SIGSEGV` on Linux, or "stack smashing detected" if stack protectors are enabled).

## Why Stack Overflows Happen

Each function call allocates a new stack frame containing local variables, parameters, and return address. The default stack size on Linux is typically 8 MB. Without a base case, recursion pushes unlimited frames onto the stack until it overflows.

## Wrong: Infinite Recursion Without a Base Case

```c
// WRONG — no base case, guaranteed stack overflow
#include <stdio.h>

int factorial(int n) {
    return n * factorial(n - 1); // never stops
}

int main(void) {
    printf("%d\n", factorial(5));
    return 0;
}
```

## Correct: Add a Proper Base Case

```c
// CORRECT — base case stops the recursion
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) return 1;       // base case
    return n * factorial(n - 1);
}

int main(void) {
    printf("%d\n", factorial(5)); // 120
    return 0;
}
```

## Wrong: Missing Base Case in Fibonacci

```c
// WRONG — infinite recursion
int fib(int n) {
    return fib(n - 1) + fib(n - 2); // no stop condition
}
```

## Correct: Fibonacci With Base Case

```c
// CORRECT
int fib(int n) {
    if (n <= 0) return 0;  // base case 1
    if (n == 1) return 1;  // base case 2
    return fib(n - 1) + fib(n - 2);
}
```

## Converting Recursion to Iteration

Iterative solutions use constant stack space and avoid stack overflow entirely:

```c
// CORRECT — iterative factorial, no stack risk
#include <stdio.h>

long factorial_iterative(int n) {
    long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main(void) {
    printf("%ld\n", factorial_iterative(20));
    return 0;
}
```

Iterative Fibonacci with O(1) space:

```c
// CORRECT — iterative fibonacci
#include <stdio.h>

int fib_iterative(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    int prev = 0, curr = 1;
    for (int i = 2; i <= n; i++) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}

int main(void) {
    printf("%d\n", fib_iterative(40));
    return 0;
}
```

## Increasing Stack Size (Linux)

If recursion depth is genuinely needed, you can increase the stack size:

```bash
# Temporarily for the current shell
ulimit -s unlimited

# Or compile and set stack size at link time
gcc -Wl,--stack,16777216 -o myprogram myprogram.c
```

For pthreads, set the stack size in the thread attribute:

```c
#include <pthread.h>
#include <stdio.h>

void *deep_task(void *arg) {
    // deep recursion here
    return NULL;
}

int main(void) {
    pthread_t thread;
    pthread_attr_t attr;
    pthread_attr_init(&attr);
    pthread_attr_setstacksize(&attr, 16 * 1024 * 1024); // 16 MB
    pthread_create(&thread, &attr, deep_task, NULL);
    pthread_join(thread, NULL);
    pthread_attr_destroy(&attr);
    return 0;
}
```

## Tail Call Optimization (TCO)

Some compilers optimize tail calls (the recursive call is the last operation) into loops, preventing stack overflow. Enable with:

```bash
gcc -O2 -foptimize-sibling-calls -o myprogram myprogram.c
```

**Note:** TCO only works when the recursive call is in tail position — the very last operation in the function with no additional computation.

```c
// Tail-recursive — compiler may optimize this into a loop
int sum(int n, int acc) {
    if (n <= 0) return acc;
    return sum(n - 1, acc + n); // tail call
}
```

## Debugging Stack Overflow

```bash
gcc -g -fsanitize=address -o myprogram myprogram.c
./myprogram
```

AddressSanitizer will report the exact stack size used and the call chain leading to overflow.

## Summary

| Fix | When to Use |
|---|---|
| Add a base case | Every recursive function must have one |
| Convert to iteration | When recursion depth is unbounded |
| Increase stack size | When deep recursion is genuinely needed |
| Use TCO | When recursive call is in tail position |
| Use `-fsanitize=address` | To debug and pinpoint the overflow source |
