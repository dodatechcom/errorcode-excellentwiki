---
title: "Objective-C NSBundle Resource Not Found Error"
description: "Fix Objective-C NSBundle resource errors when loading files or bundles from the app bundle that do not exist."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- Resource file not added to Xcode project target
- File extension mismatch (case-sensitive on some systems)
- Using wrong bundle path for framework resources
- Resource in wrong build phase (Compile Sources instead of Copy Bundle Resources)
- Missing file from build due to conditional compilation

## How to Fix

```objc
// WRONG: Resource path is nil
NSString *path = [[NSBundle mainBundle] pathForResource:@"config" ofType:@"json"];
// path is nil if file not in bundle

// CORRECT: Check for nil
NSString *path = [[NSBundle mainBundle] pathForResource:@"config" ofType:@"json"];
if (!path) {
    NSLog(@"config.json not found in bundle");
    return;
}
NSData *data = [NSData dataWithContentsOfFile:path];
```

```objc
// WRONG: Case-sensitive filename mismatch
NSString *path = [[NSBundle mainBundle] pathForResource:@"Config" ofType:@"json"];
// File is actually "config.json" -- may fail on case-sensitive FS

// CORRECT: Use exact filename
NSString *path = [[NSBundle mainBundle] pathForResource:@"config" ofType:@"json"];
```

## Examples

```objc
// Example 1: Load bundled image
UIImage *image = [UIImage imageNamed:@"logo"];
if (!image) {
    NSLog(@"logo image not found");
}

// Example 2: Load bundled plist
NSString *path = [[NSBundle mainBundle] pathForResource:@"Settings" ofType:@"plist"];
NSDictionary *settings = [NSDictionary dictionaryWithContentsOfFile:path];

// Example 3: Load bundled framework
NSBundle *bundle = [NSBundle bundleForClass:[MyFramework class]];
NSString *resourcePath = [bundle pathForResource:@"data" ofType:@"json"];
```

## Related Errors

- [File not found error](objc-file-not-found) -- file path issues
- [File error](objc-file-error) -- file operation problems
