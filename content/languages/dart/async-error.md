---
title: "Async error"
description: "An async error occurs when an error is thrown in an asynchronous function and not properly caught."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["async", "await", "future", "dart"]
weight: 5
---

## What This Error Means

An async error occurs when an error is thrown during asynchronous execution (in async functions or Futures) and isn't properly caught. These errors can be unhandled if not using try-catch with await.

## Common Causes

- Unhandled exceptions in async functions
- Not awaiting Futures that may fail
- Missing error callbacks on Futures
- Network or I/O errors in async operations

## How to Fix

```dart
// WRONG: Not handling async errors
Future<String> fetchData() async {
  var response = await http.get(Uri.parse('https://api.example.com'));
  return response.body;  // may throw
}

// CORRECT: Use try-catch
Future<String> fetchData() async {
  try {
    var response = await http.get(Uri.parse('https://api.example.com'));
    return response.body;
  } catch (e) {
    return 'Error: $e';
  }
}
```

```dart
// WRONG: Not awaiting or handling Future
void main() {
  fetchData();  // Future not awaited, errors lost
}

// CORRECT: Await and handle
Future<void> main() async {
  try {
    var data = await fetchData();
    print(data);
  } catch (e) {
    print('Error: $e');
  }
}
```

## Examples

```dart
// Example 1: Unhandled Future error
Future<int> divide(int a, int b) async {
  if (b == 0) throw Exception('Division by zero');
  return a ~/ b;
}

// Missing await and error handling

// Example 2: Network error
Future<void> fetchData() async {
  var response = await http.get(Uri.parse('invalid-url'));
  // May throw SocketException
}

// Example 3: JSON parse error
Future<Map> parseJson(String text) async {
  return json.decode(text);  // May throw FormatException
}
```

## Related Errors

- [Null check operator used on null](/languages/dart/null-check-error)
- [type cast error](/languages/dart/type-cast-error)
