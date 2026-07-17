---
title: "[Solution] Java StackOverflowError — Infinite Recursion Fix"
description: "Fix Java StackOverflowError from infinite recursion. Add base cases, convert recursion to iteration, and increase -Xss stack size for deep but valid recursion."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StackOverflowError

A `StackOverflowError` is thrown when a thread's call stack exceeds its maximum depth. It is a subclass of `VirtualMachineError`, not `Exception`, so it cannot be caught with `catch (Exception e)`. It is almost always caused by infinite recursion or mutually recursive methods without termination.

## Description

Each method call pushes a frame onto the JVM stack. When the stack is full, the JVM throws `StackOverflowError`. The default stack size varies by platform (512KB-1MB). The error is thrown at the exact point where the stack overflows, so the stack trace typically shows the same method repeated hundreds of times.

Common variants:

- `java.lang.StackOverflowError`
- `java.lang.StackOverflowError: null` (minimal info in some JVM versions)

## Common Causes

```java
// Cause 1: Missing base case in recursion
int factorial(int n) {
    return n * factorial(n - 1);  // no base case
}

// Cause 2: Mutual recursion without termination
void methodA() { methodB(); }
void methodB() { methodA(); }

// Cause 3: Circular toString() calls
public class Node {
    Node next;
    public String toString() {
        return "Node{" + next.toString() + "}";  // circular
    }
}

// Cause 4: Circular equals() / hashCode()
public boolean equals(Object o) {
    return this.equals(o);  // infinite recursion
}
```

## How to Fix

### Fix 1: Add a base case to recursive methods

```java
// Wrong
int factorial(int n) {
    return n * factorial(n - 1);
}

// Correct
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Even better — use iteration
int factorial(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

### Fix 2: Break mutual recursion with a termination condition

```java
// Wrong
void methodA() { methodB(); }
void methodB() { methodA(); }

// Correct
void methodA(int depth) {
    if (depth > 100) return;
    methodB(depth + 1);
}
void methodB(int depth) {
    if (depth > 100) return;
    methodA(depth + 1);
}
```

### Fix 3: Fix circular toString() references

```java
// Wrong
public class Employee {
    Employee manager;
    public String toString() {
        return "Employee{manager=" + manager.toString() + "}";
    }
}

// Correct — break the cycle
public class Employee {
    Employee manager;
    public String toString() {
        if (manager == this) return "Employee{manager=self}";
        return "Employee{name=" + name + "}";
    }
}
```

### Fix 4: Use iterative traversal for deep structures

```java
// Wrong — recursive tree traversal
void traverse(TreeNode node) {
    if (node == null) return;
    process(node);
    traverse(node.left);
    traverse(node.right);
}

// Correct — iterative with explicit stack
void traverse(TreeNode root) {
    Deque<TreeNode> stack = new ArrayDeque<>();
    stack.push(root);
    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        if (node == null) continue;
        process(node);
        stack.push(node.right);
        stack.push(node.left);
    }
}
```

### Fix 5: Increase stack size (temporary fix)

```bash
# Default is 512KB — increase it
java -Xss2m -jar myapp.jar

# For very deep recursion
java -Xss8m -jar myapp.jar
```

## Debugging Tips

```bash
# Increase stack trace depth
java -XX:MaxJavaStackTraceDepth=-1 -jar myapp.jar

# Use jstack to dump thread stacks
jstack <PID> > thread_dump.txt
```

- Look for the repeated method in the stack trace
- Check `toString()`, `hashCode()`, `equals()`, and property getters first

## Related Errors

- [OutOfMemoryError](outofmemory-error) — heap memory exhausted (different resource than stack)
- [ConcurrentModificationException](#) — modifying a collection during iteration
- [Infinite Loop / CPU 100%](#) — while loop without exit condition
