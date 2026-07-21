---
title: "[Solution] Xcode Error: Could Not Find Module XCTest"
description: "Fix XCTest module not found errors when running unit tests in Xcode."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Xcode Error: Could Not Find Module XCTest

This error happens when Xcode cannot locate the XCTest framework for running tests. It prevents test targets from compiling and executing.

## Common Causes
- Xcode installation is corrupted or incomplete
- Test target not properly linked to XCTest
- Derived data contains stale module references
- Command-line tools not installed alongside Xcode

## How to Fix
1. Install Command Line Tools via Xcode preferences
2. Clean DerivedData and rebuild the test target
3. Verify XCTest.framework is linked in test target's frameworks
4. Reinstall Xcode if the installation is corrupted

```swift
// Ensure XCTest is imported in test files:
import XCTest

class MyTests: XCTestCase {
    func testExample() {
        XCTAssertEqual(1 + 1, 2)
    }
}

// For Swift Package Manager tests:
// @testable import YourModule
```

## Examples
```swift
// Example: Verifying XCTest availability
// Terminal commands to check:
// $ xcrun --find xctest
// /Applications/Xcode.app/Contents/Developer/usr/bin/xctest

// $ xcode-select -p
// /Applications/Xcode.app/Contents/Developer

// If the path is wrong, reset it:
// $ sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```
