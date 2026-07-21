---
title: "Objective-C NSFileManager File Permission Error"
description: "Fix Objective-C NSFileManager file permission errors when reading, writing, or deleting files without proper access rights."
languages: ["objective-c"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- App sandbox prevents access to files outside container
- File is write-protected or owned by different user
- Attempting to delete file that does not exist
- Entitlements missing for file access (iCloud, Documents)
- File handle not closed before attempting to delete

## How to Fix

```objc
// WRONG: Not checking error on file operations
[[NSFileManager defaultManager] removeItemAtPath:path error:nil];
// Silent failure

// CORRECT: Always check error
NSError *error = nil;
BOOL success = [[NSFileManager defaultManager] removeItemAtPath:path error:&error];
if (!success) {
    NSLog(@"Delete failed: %@", error.localizedDescription);
}
```

```objc
// WRONG: Writing outside sandbox
NSString *path = @"/etc/myfile.txt"; // will fail in sandbox
[@"data" writeToFile:path atomically:YES];

// CORRECT: Use Documents directory
NSArray *paths = NSSearchPathForDirectoriesInDomains(
    NSDocumentDirectory, NSUserDomainMask, YES);
NSString *docPath = [paths.firstObject stringByAppendingPathComponent:@"myfile.txt"];
[@"data" writeToFile:docPath atomically:YES];
```

## Examples

```objc
// Example 1: Check file existence
NSFileManager *fm = [NSFileManager defaultManager];
if ([fm fileExistsAtPath:path]) {
    NSDictionary *attrs = [fm attributesOfItemAtPath:path error:nil];
    NSLog(@"Size: %@", attrs[NSFileSize]);
}

// Example 2: Safe file write
NSString *docPath = NSSearchPathForDirectoriesInDomains(
    NSDocumentDirectory, NSUserDomainMask, YES).firstObject;
NSString *filePath = [docPath stringByAppendingPathComponent:@"data.json"];
NSData *jsonData = [NSJSONSerialization dataWithJSONObject:dict options:0 error:nil];
[jsonData writeToFile:filePath atomically:YES];

// Example 3: Copy with overwrite check
NSError *error = nil;
if ([fm fileExistsAtPath:destPath]) {
    [fm removeItemAtPath:destPath error:nil];
}
[fm copyItemAtPath:srcPath toPath:destPath error:&error];
```

## Related Errors

- [File error](objc-file-error) -- file operation problems
- [File not found error](objc-file-not-found) -- missing files
