---
title: "[Solution] C++ RapidJSON - parse error"
description: "Fix C++ RapidJSON parse errors. Handle malformed JSON input with RapidJSON."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["rapidjson", "json", "parse", "dom", "sax"]
weight: 5
---

# RapidJSON - parse error

RapidJSON parse errors occur when JSON input has syntax errors, such as trailing commas, missing quotes, or invalid characters.

## Common Causes

```cpp
// Cause 1: Trailing comma
const char* json = R"({"a": 1,})"; // error

// Cause 2: Missing quote
const char* json = R"({"a": 1})"; // error if malformed

// Cause 3: Wrong encoding
const char* json = "{\xe2\x80\"invalid\"}"; // bad UTF-8
```

## How to Fix

### Fix 1: Use Parse with error handling

```cpp
#include <rapidjson/document.h>

rapidjson::Document doc;
rapidjson::ParseResult ok = doc.Parse(json);
if (!ok) {
    std::cerr << "JSON parse error at offset " << ok.Offset() << std::endl;
}
```

### Fix 2: Use SAX handler for streaming

```cpp
#include <rapidjson/reader.h>

struct Handler : public rapidjson::BaseReaderHandler<rapidjson::UTF8<>, Handler> {
    bool Null() { return true; }
    bool Bool(bool b) { return true; }
    // ...
};

rapidjson::Reader reader;
Handler handler;
reader.Parse(handler, json);
```

### Fix 3: Validate JSON first

```bash
python3 -c "import json; json.loads(open('data.json').read())"
```

## Related Errors

- [nlohmann/json - parse error]({{< relref "/languages/cpp/nlohmann-json-error" >}}) — nlohmann parse error.
- [Boost.JSON - parse error]({{< relref "/languages/cpp/boost-json-error" >}}) — Boost parse error.
- [yaml-cpp - parse error]({{< relref "/languages/cpp/yaml-cpp-error" >}}) — YAML parse error.
