---
title: "[Solution] Swift Compiler Error: Use of Unresolved Identifier"
description: "Fix unresolved identifier errors in Swift code."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# Swift Compiler Error: Use of Unresolved Identifier

This error occurs when Swift cannot find a variable, function, or type with the specified name. The identifier has not been declared in the current scope.

## Common Causes
- Variable or function not declared before use
- Typo in the identifier name
- Identifier defined in different scope or module
- Framework not imported where identifier is defined

## How to Fix
1. Verify the identifier is spelled correctly
2. Check that the identifier is in scope where it is used
3. Import the framework containing the identifier
4. Ensure the identifier is declared before its first use

```swift
// WRONG: Identifier not defined
let result = myFunction()  // Error if myFunction not defined

// RIGHT: Define or import first
import UIKit

func myFunction() -> Int { return 42 }
let result = myFunction()
```

## Examples
```swift
// Example: Common unresolved identifier fixes
// 1. Missing import:
import Foundation  // Add this at top of file

// 2. Scope issue:
class MyClass {
    private var value = 10

    func useValue() {
        print(value)  // OK - same scope
    }
}

// 3. Typo correction:
let url = URL(string: "https://example.com")  // Not URl
```
