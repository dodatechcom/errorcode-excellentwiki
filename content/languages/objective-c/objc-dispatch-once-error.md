---
title: "Objective-C GCD Dispatch Once Initialization Error"
description: "Fix Objective-C dispatch_once errors when singleton or one-time initialization patterns are implemented incorrectly."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Using dispatch_once with wrong static predicate variable
- Predicate variable not static or not at file scope
- Calling dispatch_once with nil block
- Not using dispatch_once for thread-safe singleton creation
- Accidentally resetting the once predicate

## How to Fix

```objc
// WRONG: Predicate not static
- (MyClass *)sharedInstance {
    dispatch_once_t onceToken;  // not static -- wrong!
    static MyClass *instance = nil;
    dispatch_once(&onceToken, ^{
        instance = [[MyClass alloc] init];
    });
    return instance;
}

// CORRECT: Static predicate at file scope or in function
static MyClass *_sharedInstance = nil;
+ (instancetype)sharedInstance {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        _sharedInstance = [[MyClass alloc] init];
    });
    return _sharedInstance;
}
```

```enrl
// WRONG: Forgetting static on instance variable
+ (instancetype)shared {
    dispatch_once_t token;
    MyClass *inst = nil;  // not static!
    dispatch_once(&token, ^{
        inst = [[MyClass alloc] init];
    });
    return inst;  // returns nil after first call
}

// CORRECT: Instance must be static
+ (instancetype)shared {
    static MyClass *inst = nil;
    static dispatch_once_t token;
    dispatch_once(&token, ^{
        inst = [[MyClass alloc] init];
    });
    return inst;
}
```

## Examples

```objc
// Example 1: Standard singleton pattern
+ (instancetype)sharedManager {
    static Manager *sharedManager = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        sharedManager = [[Manager alloc] initPrivate];
    });
    return sharedManager;
}

// Example 2: Thread-safe lazy initialization
- (NSDateFormatter *)dateFormatter {
    static NSDateFormatter *formatter = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        formatter = [[NSDateFormatter alloc] init];
        formatter.dateFormat = @"yyyy-MM-dd";
    });
    return formatter;
}

// Example 3: One-time configuration
+ (void)configureOnce {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        [AVAudioSession sharedInstance];
        // other one-time setup
    });
}
```

## Related Errors

- [Singleton error](objc-singleton-error) -- singleton pattern issues
- [Thread error](objc-thread-error) -- threading problems
