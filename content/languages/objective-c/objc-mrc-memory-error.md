---
title: "Objective-C MRC Memory Management Error"
description: "Fix Objective-C Manual Reference Counting errors when retain, release, or autorelease are used incorrectly."
languages: ["objective-c"]
error-types: ["memory-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Forgetting to release objects created with alloc/init
- Over-releasing objects you do not own
- Using autorelease in tight loops causing memory spikes
- Not retaining objects stored in instance variables
- Releasing objects in dealloc that are not owned

## How to Fix

```objc
// WRONG: Memory leak in MRC
- (void)doWork {
    NSString *str = [[NSString alloc] initWithFormat:@"hello"];
    // Forgot [str release] -- memory leak
}

// CORRECT: Release when done
- (void)doWork {
    NSString *str = [[NSString alloc] initWithFormat:@"hello"];
    [str release];
}
```

```objc
// WRONG: Over-releasing
- (void)doWork {
    NSString *str = [NSString stringWithString:@"hello"]; // autoreleased
    [str release];  // over-release!
}

// CORRECT: Do not release autoreleased objects
- (void)doWork {
    NSString *str = [NSString stringWithString:@"hello"];
    // str released at end of autorelease pool
}
```

## Examples

```objc
// Example 1: Proper retain/release
- (void)processData {
    NSMutableData *data = [[NSMutableData alloc] init];
    [data appendData:someData];
    // use data
    [data release];
}

// Example 2: Property retain semantics
@interface MyClass : NSObject {
    NSString *_name;
}
@property (nonatomic, retain) NSString *name;
@end

@implementation MyClass
@synthesize name = _name;
- (void)setName:(NSString *)newName {
    [newName retain];
    [_name release];
    _name = newName;
}
- (void)dealloc {
    [_name release];
    [super dealloc];
}
@end

// Example 3: Autorelease pool in loops
NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
for (int i = 0; i < 100000; i++) {
    NSString *str = [NSString stringWithFormat:@"item %d", i];
    // use str
}
[pool release];
```

## Related Errors

- [Memory leak error](objc-memory-leak) -- memory management issues
- [MRC error](objc-mrc-error) -- manual reference counting
