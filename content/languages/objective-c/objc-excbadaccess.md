---
title: "[Solution] Objective-C EXC_BAD_ACCESS Zombie Object Error"
description: "Fix Objective-C EXC_BAD_ACCESS and zombie object errors. Resolve memory management and use-after-free issues."
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["critical"]
weight: 5
---

## What This Error Means

EXC_BAD_ACCESS indicates that the program attempted to access memory that has been freed or is invalid. Zombie objects occur when you send a message to a deallocated object. This is one of the most difficult bugs to diagnose in Objective-C.

## Why It Happens

- Sending message to deallocated object: The object was released but is still referenced.
- Accessing freed memory in C code: Manual memory management errors in C code.
- Retain cycle causing unexpected deallocation: Circular references lead to premature deallocation.
- Thread safety issues with object lifecycle: Objects are released on one thread while used on another.
- Using MRC without proper retain/release: Manual reference counting errors.

## How to Fix It

Enable zombie objects for debugging:

```objectivec
// In scheme settings or environment variable
// NSZombieEnabled = YES
// This turns deallocated objects into zombies that log messages
```

Use weak references to prevent retain cycles:

```objectivec
@property (nonatomic, weak) id<MyDelegate> delegate;
```

Check object existence before access:

```objectivec
if (object != nil && [object respondsToSelector:@selector(method)]) {
    [object method];
}
```

Use __weak and __strong in blocks:

```objectivec
__weak typeof(self) weakSelf = self;
dispatch_async(queue, ^{
    __strong typeof(weakSelf) strongSelf = weakSelf;
    if (strongSelf) {
        [strongSelf performAction];
    }
});
```

Enable Address Sanitizer in Xcode:

```
// Build Settings > Enable Address Sanitizer: YES
// This detects use-after-free and buffer overflows
```

Use Instrument's Zombies tool:

```
// Profile with Zombies instrument
// This tracks all deallocated objects and messages sent to them
```

Use Thread Sanitizer for detection:

```
// Build Settings > Thread Sanitizer: YES
// This detects data races and other threading issues
```

Analyze with Instruments:

```
// Use Leaks instrument to find memory leaks
// Use Allocations instrument to track memory usage
// Use Zombies instrument to find use-after-free
```

Use static analyzers:

```
// Xcode Analyze (Cmd+Shift+B)
// This finds potential memory management issues
```

## Common Mistakes

- Not using ARC or forgetting manual memory management rules. ARC handles retain/release automatically.
- Retaining self in blocks creating cycles. Use __weak to break cycles.
- Releasing objects that are still in use by other code. Ensure exclusive ownership.
- Not handling memory warnings in view controllers. Override didReceiveMemoryWarning:.
- Using unsafe_unretained instead of weak for delegates. weak zeros out on dealloc.
- Not testing with Instruments regularly. Memory issues can be subtle.
- Forgetting that collections retain their elements. Arrays and dictionaries hold strong references.

## Related Pages

- [objc-block-cycle]({{< relref "/languages/objective-c/objc-block-cycle" >}}) - retain cycle in blocks
- [objc-memory-error]({{< relref "/languages/objective-c/objc-memory-error" >}}) - memory errors
- [memory-warning]({{< relref "/languages/objective-c/memory-warning" >}}) - memory warning
- [objc-notification-leak]({{< relref "/languages/objective-c/objc-notification-leak" >}}) - notification leak
