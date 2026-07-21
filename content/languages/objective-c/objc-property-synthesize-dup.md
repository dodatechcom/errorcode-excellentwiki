---
title: "Objective-C Property Synthesize Duplicate Error"
description: "Fix Objective-C @synthesize duplicate errors when property synthesis conflicts with existing ivar or property names."
languages: ["objective-c"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- @synthesize creates ivar with underscore that conflicts with existing ivar
- Property name conflicts with superclass property
- Using @dynamic but property not implemented by runtime
- @synthesize with name parameter does not match property type
- Duplicate property declaration in category

## How to Fix

```objc
// WRONG: @synthesize creates _name conflicting with existing ivar
@interface MyClass : NSObject {
    NSString *_name; // existing ivar
}
@property (nonatomic, copy) NSString *name;
@end

@implementation MyClass
@synthesize name = _name; // conflict with existing ivar
@end

// CORRECT: Use different ivar name
@implementation MyClass
@synthesize name = _customName;
@end
```

```objc
// WRONG: Property in category without @dynamic
@interface MyClass (Category)
@property (nonatomic, strong) NSString *extra;
@end

@implementation MyClass (Category)
// Missing @dynamic extra;  -- warning: auto property synthesis
@end

// CORRECT: Use @dynamic or associated objects
@implementation MyClass (Category)
@dynamic extra;
- (void)setExtra:(NSString *)extra {
    objc_setAssociatedObject(self, @selector(extra), extra,
        OBJC_ASSOCIATION_RETAIN_NONATOMIC);
}
- (NSString *)extra {
    return objc_getAssociatedObject(self, @selector(extra));
}
@end
```

## Examples

```objc
// Example 1: Basic @synthesize
@interface Person : NSObject
@property (nonatomic, copy) NSString *name;
@property (nonatomic, assign) NSInteger age;
@end

@implementation Person
@synthesize name = _name;
@synthesize age = _age;
@end

// Example 2: @dynamic for protocol conformance
@interface MyEntity : NSManagedObject
@property (nonatomic, retain) NSString *entityName;
@end

@implementation MyEntity
@dynamic entityName;
@end
```

## Related Errors

- [Property error](objc-property-error) -- property declaration issues
- [Synthesize error](objc-synthesize-error) -- auto-synthesis problems
