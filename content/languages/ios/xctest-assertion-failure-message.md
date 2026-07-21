---
title: "[Solution] XCTest Assertion Failure Message"
description: "Fix XCTest assertion failures providing unclear error messages in unit tests."
languages: ["ios"]
error-types: ["language-error"]
severities: ["error"]
---

# XCTest Assertion Failure Message

XCTest assertion failures with unclear messages make debugging difficult. Proper message formatting helps identify test failures quickly.

## Common Causes
- Missing failure message in XCTAssert calls
- Incorrect comparison operators in assertions
- Testing asynchronous code without expectations
- Wrong assertion type for the comparison

## How to Fix
1. Always include descriptive failure messages
2. Use the correct assertion type for each comparison
3. Use XCTestExpectation for async tests
4. Organize assertions logically with clear messages

```swift
// GOOD: Clear failure messages
XCTAssertEqual(result, expected, "Result should match expected value")
XCTAssertTrue(items.count > 0, "Items array should not be empty")

// BETTER: Use trailing closure for message
XCTAssertEqual(result, expected) {
    "Expected \(expected) but got \(result)"
}
```

## Examples
```swift
// Async testing with expectations:
func testAsyncDataFetch() {
    let expectation = XCTestExpectation(description: "Data fetch")
    service.fetchData { result in
        XCTAssertNotNil(result, "Fetch should return data")
        XCTAssertEqual(result?.count, 5, "Should return 5 items")
        expectation.fulfill()
    }
    wait(for: [expectation], timeout: 5.0)
}
```
