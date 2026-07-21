---
title: "Objective-C Delegate Nil Callback Error"
description: "Fix Objective-C delegate nil callback errors when delegate is deallocated before callback is invoked."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Delegate is weak but no strong reference exists during operation
- Asynchronous callback arrives after delegate object is deallocated
- Delegate protocol method not implemented by delegate object
- Using assign instead of weak for delegate property (pre-ARC)
- Setting delegate to nil before async operation completes

## How to Fix

```objc
// WRONG: Weak delegate with no strong reference during async
@protocol DataDelegate <NSObject>
@end

@interface DataManager : NSObject
@property (nonatomic, weak) id<DataDelegate> delegate;
@end

// If delegate is deallocated during async fetch, callback crashes

// CORRECT: Use weak but check before calling
- (void)didReceiveData:(NSData *)data {
    if ([self.delegate respondsToSelector:@selector(dataManager:didReceiveData:)]) {
        [self.delegate dataManager:self didReceiveData:data];
    }
}
```

```objc
// WRONG: Strong delegate causes retain cycle
@interface MyController : NSObject
@property (nonatomic, strong) id<MyDelegate> delegate; // retain cycle!
@end

// CORRECT: Use weak for delegates
@interface MyController : NSObject
@property (nonatomic, weak) id<MyDelegate> delegate;
@end
```

## Examples

```objc
// Example 1: Safe delegate callback
- (void)complete {
    id<MyDelegate> strongDelegate = self.delegate;
    if ([strongDelegate respondsToSelector:@selector(didComplete)]) {
        [strongDelegate didComplete];
    }
}

// Example 2: Delegate protocol with optional methods
@protocol DownloadDelegate <NSObject>
@required
- (void)downloadDidFinish:(NSData *)data;
@optional
- (void)downloadDidProgress:(float)progress;
@end

// Example 3: Block-based alternative to delegates
typedef void (^CompletionBlock)(NSData *data, NSError *error);
- (void)fetchWithCompletion:(CompletionBlock)completion {
    // async work...
    completion(data, nil);
}
```

## Related Errors

- [Delegate error](objc-delegate-error) -- delegate pattern issues
- [Weak reference error](objc-weak-reference-error) -- memory management
