---
title: "[Solution] RapidJSON SAX Parse Error Fix"
description: "Fix RapidJSON SAX parse errors. Handle handler errors, incomplete input, and SAX callback issues."
languages: ["cpp"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# RapidJSON SAX Parse Error Fix

Fix RapidJSON SAX parse errors. Handle handler errors, incomplete input, and SAX callback issues.

## What This Error Means

RapidJSON SAX parser errors occur when the SAX handler encounters issues:

```
SAX Error: Invalid value while parsing
Parse error: The document root must not follow by other values
```

## Common Causes

```cpp
// Cause 1: Handler returns false during parsing
struct MyHandler : public BaseReaderHandler<UTF8<>, MyHandler> {
    bool Null() { return false; } // Abort parsing
};

// Cause 2: Multiple root values in JSON
// Cause 3: Incomplete JSON input
// Cause 4: Handler throws exception
```

## How to Fix

### Fix 1: Use GenericDocument for DOM parsing instead

```cpp
#include <rapidjson/document.h>

void parse_json(const char* json) {
    rapidjson::Document doc;
    doc.Parse(json);

    if (doc.HasParseError()) {
        fprintf(stderr, "Parse error at offset %zu: %s\n",
            doc.GetErrorOffset(),
            rapidjson::GetParseError_En(doc.GetParseError()));
        return;
    }
}
```

### Fix 2: Implement robust SAX handler

```cpp
#include <rapidjson/reader.h>

struct RobustHandler : public BaseReaderHandler<UTF8<>, RobustHandler> {
    bool Null() { return true; }
    bool Bool(bool b) { return true; }
    bool Int(int i) { return true; }
    bool Uint(unsigned u) { return true; }
    bool Int64(int64_t i) { return true; }
    bool Uint64(uint64_t u) { return true; }
    bool Double(double d) { return true; }
    bool String(const char* str, SizeType length, bool copy) { return true; }
    bool StartObject() { return true; }
    bool Key(const char* str, SizeType length, bool copy) { return true; }
    bool EndObject(SizeType memberCount) { return true; }
    bool StartArray() { return true; }
    bool EndArray(SizeType elementCount) { return true; }
};
```

### Fix 3: Use filters for incremental parsing

```cpp
#include <rapidjson/reader.h>
#include <rapidjson/filereadstream.h>

void stream_parse(FILE* fp) {
    char buf[65536];
    FileReadStream is(fp, buf, sizeof(buf));

    Reader reader;
    RobustHandler handler;

    reader.Parse(is, handler);
}
```

## Examples

```cpp
#include <rapidjson/document.h>
#include <rapidjson/error/en.h>
#include <iostream>

struct UserData {
    std::string name;
    int age;
    double score;
};

bool parse_user(const char* json, UserData& user) {
    rapidjson::Document doc;
    doc.Parse(json);

    if (doc.HasParseError()) {
        std::cerr << "Parse error at offset "
                  << doc.GetErrorOffset() << ": "
                  << rapidjson::GetParseError_En(doc.GetParseError())
                  << std::endl;
        return false;
    }

    if (!doc.IsObject()) {
        return false;
    }

    if (doc.HasMember("name") && doc["name"].IsString()) {
        user.name = doc["name"].GetString();
    }
    if (doc.HasMember("age") && doc["age"].IsInt()) {
        user.age = doc["age"].GetInt();
    }
    if (doc.HasMember("score") && doc["score"].IsNumber()) {
        user.score = doc["score"].GetDouble();
    }

    return true;
}

int main() {
    UserData user;
    if (parse_user(R"({"name": "Alice", "age": 25, "score": 98.5})", user)) {
        std::cout << user.name << " age=" << user.age << std::endl;
    }
    return 0;
}
```

## Related Errors

- [Nlohmann JSON Error]({{< relref "/languages/cpp/nlohmann-json-error-v2" >}}) — nlohmann JSON error
- [Boost JSON Error]({{< relref "/languages/cpp/boost-json-error" >}}) — Boost JSON error
- [Format Error]({{< relref "/languages/cpp/format-error" >}}) — format error
