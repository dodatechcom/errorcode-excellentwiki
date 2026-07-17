---
title: "[Solution] nlohmann/json Parse Error at Offset Fix"
description: "Fix nlohmann/json parse errors at offset. Handle unexpected tokens, trailing characters, and encoding issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# nlohmann/json Parse Error at Offset Fix

Fix nlohmann/json parse errors at offset. Handle unexpected tokens, trailing characters, and encoding issues.

## What This Error Means

nlohmann/json throws `json::parse_error` with the exact byte offset:

```
[json.exception.parse_error.101] parse error at line 2, column 5: syntax error while parsing value - unexpected ';'
```

## Common Causes

```cpp
// Cause 1: Trailing comma
auto j = json::parse(R"({"a": 1,})");

// Cause 2: Trailing characters after JSON
auto j = json::parse(R"({"a": 1} some text)");

// Cause 3: Unescaped control characters
auto j = json::parse(R"({"key": "line1\nline2"})"); // Wrong

// Cause 4: Single quotes instead of double quotes
auto j = json::parse("{'key': 'value'}");

// Cause 5: Comments in JSON (not standard)
auto j = json::parse(R"({"a": 1 /* comment */})");
```

## How to Fix

### Fix 1: Use try-catch for error handling

```cpp
#include <nlohmann/json.hpp>
#include <iostream>

using json = nlohmann::json;

json safe_parse(const std::string& input) {
    try {
        return json::parse(input);
    } catch (const json::parse_error& e) {
        std::cerr << "Parse error at byte " << e.byte
                  << ": " << e.what() << std::endl;
        return json(); // Return null JSON
    }
}
```

### Fix 2: Accept trailing commas with option

```cpp
#include <nlohmann/json.hpp>

json parse_relaxed(const std::string& input) {
    return json::parse(input, nullptr, false); // Allow exceptions to be ignored
}
```

### Fix 3: Use json::accept to validate first

```cpp
#include <nlohmann/json.hpp>

bool is_valid_json(const std::string& input) {
    return json::accept(input);
}
```

## Examples

```cpp
#include <nlohmann/json.hpp>
#include <iostream>

using json = nlohmann::json;

void process_json(const std::string& raw) {
    try {
        json data = json::parse(raw);

        if (data.contains("name")) {
            std::string name = data["name"].get<std::string>();
            std::cout << "Name: " << name << std::endl;
        }

        if (data.contains("items") && data["items"].is_array()) {
            for (const auto& item : data["items"]) {
                std::cout << "Item: " << item.dump() << std::endl;
            }
        }
    } catch (const json::parse_error& e) {
        std::cerr << "Parse error at offset " << e.byte << ": " << e.what() << std::endl;
    } catch (const json::type_error& e) {
        std::cerr << "Type error: " << e.what() << std::endl;
    }
}

int main() {
    process_json(R"({"name": "test", "items": [1, 2, 3]})");
    return 0;
}
```

## Related Errors

- [Nlohmann JSON Error]({{< relref "/languages/cpp/nlohmann-json-error" >}}) — nlohmann JSON error
- [Boost JSON Error]({{< relref "/languages/cpp/boost-json-error" >}}) — Boost JSON error
- [RapidJSON Error]({{< relref "/languages/cpp/rapidjson-error-v2" >}}) — RapidJSON error
