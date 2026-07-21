---
title: "Objective-C NSCoding Secure Coding Error"
description: "Fix Objective-C NSCoding secure coding errors when archiving or unarchiving objects without proper NSSecureCoding conformance."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Object conforms to NSCoding but not NSSecureCoding
- decodeObjectOfClass called without specifying expected class
- Archived data contains object types not registered with secure coding
- Missing encodeWithCoder implementation for new properties
- Decoding data archived with different class version

## How to Fix

```objc
// WRONG: Using insecure NSCoding
- (void)encodeWithCoder:(NSCoder *)coder {
    [coder encodeObject:self.name forKey:@"name"];
}

// CORRECT: Implement NSSecureCoding
+ (BOOL)supportsSecureCoding { return YES; }

- (void)encodeWithCoder:(NSCoder *)coder {
    [coder encodeObject:self.name forKey:@"name"];
}

- (instancetype)initWithCoder:(NSCoder *)coder {
    self = [super init];
    if (self) {
        _name = [coder decodeObjectOfClass:[NSString class] forKey:@"name"];
    }
    return self;
}
```

```objc
// WRONG: decodeObject without class specification
NSString *name = [coder decodeObjectForKey:@"name"]; // insecure

// CORRECT: Use decodeObjectOfClass
NSString *name = [coder decodeObjectOfClass:[NSString class] forKey:@"name"];
```

## Examples

```objc
// Example 1: Complete NSSecureCoding implementation
@interface Person : NSObject <NSSecureCoding>
@property (nonatomic, copy) NSString *name;
@property (nonatomic, assign) NSInteger age;
@end

@implementation Person
+ (BOOL)supportsSecureCoding { return YES; }

- (void)encodeWithCoder:(NSCoder *)coder {
    [coder encodeObject:self.name forKey:@"name"];
    [coder encodeInteger:self.age forKey:@"age"];
}

- (instancetype)initWithCoder:(NSCoder *)coder {
    self = [super init];
    if (self) {
        _name = [coder decodeObjectOfClass:[NSString class] forKey:@"name"];
        _age = [coder decodeIntegerForKey:@"age"];
    }
    return self;
}
@end

// Example 2: Archive and unarchive
NSData *data = [NSKeyedArchiver archivedDataWithRootObject:person
    requiringSecureCoding:YES error:nil];
Person *restored = [NSKeyedArchiver unarchivedObjectOfClass:[Person class]
    fromData:data error:nil];
```

## Related Errors

- [NSCoding error](objc-nscoding-error) -- coding protocol issues
- [Archiving error](objc-archiving-error) -- archive/unarchive problems
