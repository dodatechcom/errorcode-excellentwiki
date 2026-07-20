---
title: "[Solution] Java StackOverflowError — Deep Recursion Analysis Fix"
description: "Fix Java StackOverflowError by increasing stack size (-Xss), converting recursion to iteration, adding base cases, and using tail recursion."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 10
---

# StackOverflowError — Deep Recursion Analysis Fix

A `StackOverflowError` occurs when a thread's call stack exceeds its maximum depth. This is a subclass of `VirtualMachineError` and most commonly caused by unbounded recursion, but can also result from deeply nested method calls in legitimate scenarios.

## Description

Each method invocation pushes a frame onto the thread's stack. When recursion (or deep nesting) exhausts the allocated stack space, the JVM throws `StackOverflowError`. The default stack size is typically 512KB–1MB per thread, holding roughly 5,000–10,000 frames depending on frame size.

Message variants:

- `java.lang.StackOverflowError`
- `java.lang.StackOverflowError at com.example.RecursiveClass.process(RecursiveClass.java:25)`
- `Exception in thread "main" java.lang.StackOverflowError`

## Common Causes

```java
// Cause 1: Missing or wrong base case in recursion
public int factorial(int n) {
    return n * factorial(n - 1);  // no base case — infinite recursion
}

// Cause 2: Mutual recursion without termination
public boolean isEven(int n) {
    if (n == 0) return true;
    return isOdd(n - 1);
}
public boolean isOdd(int n) {
    if (n == 0) return false;
    return isEven(n - 1);
}
// isEven(Integer.MAX_VALUE) → StackOverflowError

// Cause 3: Circular toString/equals/hashCode
public class Node {
    String name;
    Node next;
    @Override
    public String toString() {
        return "Node{name=" + name + ", next=" + next + "}";  // calls next.toString()
    }
}

// Cause 4: Circular equals causing infinite recursion
@Override
public boolean equals(Object o) {
    return this.name.equals(((Node) o).name);  // if name is also Node, infinite
}

// Cause 5: Self-referencing data structure
public class TreeNode {
    TreeNode parent;
    TreeNode child;
    public int depth() {
        return 1 + parent.depth();  // goes up to root, but what if parent references child?
    }
}
```

## Solutions

### Fix 1: Increase stack size with -Xss

```bash
# Increase stack size per thread (default is 512k-1m)
java -Xss2m -jar myapp.jar       # 2MB stack
java -Xss4m -jar myapp.jar       # 4MB stack — handles deeper recursion

# For specific threads in code
Thread t = new Thread(() -> recursiveWork(), "recursive-worker");
t.setStackSize(1024 * 1024 * 2);  // 2MB stack
t.start();
```

### Fix 2: Convert recursion to iteration

```java
// Recursive — can cause StackOverflowError
public int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Iterative — no stack growth
public int factorial(int n) {
    int result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Recursive tree traversal → iterative with explicit stack
public void traverse(TreeNode root) {
    Deque<TreeNode> stack = new ArrayDeque<>();
    stack.push(root);
    while (!stack.isEmpty()) {
        TreeNode node = stack.pop();
        process(node);
        if (node.right != null) stack.push(node.right);
        if (node.left != null) stack.push(node.left);
    }
}
```

### Fix 3: Add proper base cases to recursive methods

```java
// Wrong — missing base case
public int sum(List<Integer> list, int index) {
    return list.get(index) + sum(list, index + 1);  // no termination
}

// Right — base case present
public int sum(List<Integer> list, int index) {
    if (index >= list.size()) return 0;  // base case
    return list.get(index) + sum(list, index + 1);
}

// Right — tail-recursive style (JVM doesn't optimize, but conceptually correct)
public int sum(List<Integer> list, int index, int accumulator) {
    if (index >= list.size()) return accumulator;
    return sum(list, index + 1, accumulator + list.get(index));
}
```

### Fix 4: Use tail recursion or trampoline pattern

```java
// Trampoline — converts tail recursion to iteration under the hood
public class Trampoline<T> {
    private final Supplier<Trampoline<T>> next;
    private final T result;

    private Trampoline(T result, Supplier<Trampoline<T>> next) {
        this.result = result;
        this.next = next;
    }

    public static <T> Trampoline<T> done(T result) {
        return new Trampoline<>(result, null);
    }

    public static <T> Trampoline<T> call(Supplier<Trampoline<T>> next) {
        return new Trampoline<>(null, next);
    }

    public T compute() {
        Trampoline<T> current = this;
        while (current.next != null) {
            current = current.next.get();
        }
        return current.result;
    }
}

// Usage — no stack growth
public Trampoline<Integer> factorial(int n, int acc) {
    if (n <= 1) return Trampoline.done(acc);
    return Trampoline.call(() -> factorial(n - 1, n * acc));
}

// Compute without stack overflow
int result = factorial(100000, 1).compute();  // works
```

### Fix 5: Detect and break circular references

```java
public class SafeNode {
    private final Set<SafeNode> visited = Collections.newSetFromMap(new IdentityHashMap<>());

    public void traverse(SafeNode node) {
        if (!visited.add(node)) {
            return;  // already visited — break the cycle
        }
        for (SafeNode child : node.getChildren()) {
            traverse(child);
        }
    }
}
```

## Prevention Checklist

- Always define a clear base case in every recursive method.
- Prefer iteration over recursion for potentially deep call chains.
- Use `-Xss` to increase stack size when recursion depth is genuinely needed.
- Implement cycle detection in recursive traversal of graph-like structures.
- Override `toString()`, `equals()`, and `hashCode()` carefully to avoid self-referencing.
- Use trampolines for tail-recursive algorithms that may exceed stack depth.
- Profile recursion depth before deploying to production.

## Related Errors

- [OutOfMemoryError](../outofmemoryerror) — heap exhaustion (different resource)
- [OutOfMemoryError Thread](../oom-thread) — unable to create new thread (stack allocation failure)
- [StackOverflowError Mutual Recursion](../soe-mutual) — mutual recursion pattern
- [StackOverflowError toString](../soe-tostring) — circular toString loop
