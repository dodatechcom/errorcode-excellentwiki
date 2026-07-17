---
title: "[Solution] C++ nlohmann/json - parse error"
description: "Fix C++ nlohmann/json parse errors. Handle malformed JSON input with nlohmann library."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["nlohmann-json", "json", "parse", "syntax", "exception"]
weight: 5
---

# nlohmann/json - parse error

nlohmann/json throws `nlohmann::json::parse_error` when JSON input has syntax errors.

## Common Causes

```cpp
// Cause 1: Trailing comma
auto j = nlohmann::json::parse(R"({"a": 1,})"); // parse_error

// Cause 2: Unclosed brace
auto j = nlohmann::json::parse(R"({"a": 1)"); // parse_error

// Cause 3: Invalid escape
auto j = nlohmann::json::parse(R"({"a": "\q"})"); // parse_error
```

## How to Fix

### Fix 1: Use try-catch

```cpp
#include <nlohmann/json.hpp>

try {
    auto j = nlohmann::json::parse(input);
} catch (const nlohmann::json::parse_error& e) {
    std::cerr << "Parse error: " << e.what() << std::endl;
}
```

### Fix 2: Use error_code

```cpp
nlohmann::json j;
try {
    j = nlohmann::json::parse(input);
} catch (...) {
    // handle error
}
```

### Fix 3: Validate JSON

```bash
python3 -c "import json; json.loads(open('data.json').read())"
```

## Related Errors

- [RapidJSON - parse error]({{< relref "/languages/cpp/rapidjson-error" >}}) — RapidJSON parse error.
- [Boost.JSON - parse error]({{< relref "/languages/cpp/boost-json-error" >}}) — Boost parse error.
- [yaml-cpp - parse error]({{< relref "/languages/cpp/yaml-cpp-error" >}}) — YAML parse error.
