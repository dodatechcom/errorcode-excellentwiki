---
title: "[Solution] C++ Boost.JSON - parse error"
description: "Fix C++ Boost.JSON parse errors. Handle malformed JSON input."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["boost", "json", "parse", "syntax", "malformed"]
weight: 5
---

# Boost.JSON - parse error

Boost.JSON parse errors occur when the input JSON string has syntax errors, such as missing commas, unclosed brackets, or invalid characters.

## Common Causes

```cpp
// Cause 1: Missing comma
auto val = boost::json::parse(R"({"a": 1 "b": 2})"); // error

// Cause 2: Trailing comma
auto val = boost::json::parse(R"({"a": 1,})"); // error

// Cause 3: Unclosed bracket
auto val = boost::json::parse(R"({"a": 1)"); // error
```

## How to Fix

### Fix 1: Use error_code overload

```cpp
boost::system::error_code ec;
auto val = boost::json::parse(input, ec);
if (ec) {
    std::cerr << "Parse error: " << ec.message() << std::endl;
}
```

### Fix 2: Validate JSON before parsing

```cpp
try {
    auto val = boost::json::parse(input);
} catch (const boost::system::system_error& e) {
    std::cerr << "Invalid JSON: " << e.what() << std::endl;
}
```

### Fix 3: Use JSON schema validation

```cpp
boost::json::object obj = boost::json::parse(input).as_object();
// validate fields
```

## Related Errors

- [nlohmann/json - parse error]({{< relref "/languages/cpp/nlohmann-json-error" >}}) — nlohmann parse error.
- [RapidJSON - parse error]({{< relref "/languages/cpp/rapidjson-error" >}}) — RapidJSON error.
- [yaml-cpp - parse error]({{< relref "/languages/cpp/yaml-cpp-error" >}}) — YAML parse error.
