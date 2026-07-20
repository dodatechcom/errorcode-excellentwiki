---
title: "[Solution] C SEQUENCE_POINT_VIOLATION — Sequence point violation"
description: "Fix C sequence point violations by avoiding ++ in complex expressions and using separate statements. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["warning"]
error-types: ["undefined-behavior"]
weight: 817
---

# C SEQUENCE_POINT_VIOLATION — Sequence point violation

A sequence point violation (unspecified behavior) occurs when the value of an object is modified more than once between sequence points, or when both the old and new values are used to compute something. The most common cases involve multiple modifications or mixed read-modify-write of the same variable in one expression.

## Common Causes

```c
// Cause 1: Multiple modifications of the same variable
int i = 0;
i = i++ + ++i;  // undefined: i modified twice without sequence point
```

```c
// Cause 2: Modification and read in the same expression
int x = 5;
x = x + x;  // well-defined in C (two reads before write), but often confused
// REAL problem:
x = x++ + ++x;  // undefined: multiple modifications
```

```c
// Cause 3: Function arguments with side effects
int a = 1;
printf("%d %d %d\n", a++, a++, a++);  // unspecified: order of evaluation of arguments
```

```c
// Cause 4: Array indexing with side effects
int arr[] = {0, 1, 2, 3, 4};
int i = 0;
arr[i++] = arr[i++];  // undefined: i modified twice
```

```c
// Cause 5: Using ternary operator with side effects on same variable
int x = 0;
int y = (x++) ? x : x++;  // undefined: x modified and read in various ways
```

## How to Fix

### Fix 1: Use separate statements for each side effect

```c
// WRONG:
i = i++ + ++i;

// CORRECT:
int temp1 = ++i;  // i is now 1, temp1 = 1
int temp2 = i;    // i is 1, temp2 = 1
i = temp1 + temp2; // i = 2
```

### Fix 2: Don't use increment operators in function arguments

```c
// WRONG: unspecified evaluation order
int a = 1;
printf("%d %d %d\n", a++, a++, a++);

// CORRECT: evaluate before the function call
int a = 1;
int v1 = a++;  // v1=1, a=2
int v2 = a++;  // v2=2, a=3
int v3 = a++;  // v3=3, a=4
printf("%d %d %d\n", v1, v2, v3);  // 1 2 3
```

### Fix 3: Separate array access from index modification

```c
// WRONG:
int i = 0;
arr[i++] = arr[i++];

// CORRECT:
int i = 0;
int val = arr[i];   // read arr[0]
i++;                // i = 1
arr[i] = val;       // write to arr[1]
i++;                // i = 2
```

### Fix 4: Use intermediate variables to clarify evaluation order

```c
// WRONG:
result = arr[i++] + arr[j++];  // which increments first? unspecified

// CORRECT:
int left = arr[i];
i++;
int right = arr[j];
j++;
result = left + right;
```

### Fix 5: Check compiler warnings for sequence point issues

```bash
# GCC and Clang detect many sequence point violations
gcc -Wall -Wsequence-point main.c -o app
clang -Wall -Wsequence-point main.c -o app
```

## Examples

```c
// Real-world: common interview bug
#include <stdio.h>

int main(void) {
    int i = 3;
    int arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    // Classic "what does this print?"
    arr[i++] = i;  // undefined behavior — don't try to predict the output

    // Fixed version:
    i = 3;
    int val = i;     // val = 3
    arr[val] = val;  // arr[3] = 3
    i++;             // i = 4

    printf("arr[3] = %d, i = %d\n", arr[3], i);  // arr[3] = 3, i = 4
    return 0;
}
```

```c
// Real-world: macro with sequence point issue
// WRONG macro:
#define SWAP(a, b) do { (a) = (a) ^ (b); (b) = (a) ^ (b); (a) = (a) ^ (b); } while(0)
// This is fine for integers but has issues if a and b are the same variable

// CORRECT macro:
#define SWAP(a, b) do { \
    __typeof__(a) _tmp = (a); \
    (a) = (b); \
    (b) = _tmp; \
} while(0)

// Or better yet, use an inline function:
static inline void swap_int(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```

## Related Errors

- [C STRICT_ALIASING_VIOLATION](/languages/c/strict-aliasing-violation) — Strict aliasing violation
- [C SIGNED_INTEGER_OVERFLOW](/languages/c/signed-integer-overflow-ub) — Signed integer overflow UB
- [C MODIFY_CONST_OBJECT](/languages/c/modify-const-object) — Modifying const object UB
