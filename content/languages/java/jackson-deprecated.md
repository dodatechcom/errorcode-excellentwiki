---
title: "[Solution] SimpleModule Deprecated API — Jackson Migration Fix"
description: "Fix warnings when using deprecated Jackson APIs like SimpleModule. Migrate to newer Jackson module system."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jackson", "json", "deprecated", "simple-module", "migration"]
weight: 5
---

# SimpleModule Deprecated API — Jackson Migration Fix

Warnings or errors when using deprecated Jackson APIs. `SimpleModule` and related classes may be deprecated in newer Jackson versions.

## What This Error Means

Common warnings:

- `SimpleModule is deprecated`
- `addSerializer overload is deprecated`

## Common Causes

```java
// Cause 1: Using deprecated SimpleModule
SimpleModule module = new SimpleModule("MyModule");
module.addSerializer(MyClass.class, new MySerializer());

// Cause 2: Deprecated addSerializer overloads
module.addSerializer(MyClass.class, (jsonSerializer, value) -> { });
```

## How to Fix

### Fix 1: Use Module instead of SimpleModule

```java
Module module = new SimpleModule("MyModule")
    .addSerializer(MyClass.class, new MyClassSerializer())
    .addDeserializer(MyClass.class, new MyClassDeserializer());

ObjectMapper mapper = new ObjectMapper();
mapper.registerModule(module);
```

### Fix 2: Use annotations instead

```java
public class MyClass {
    @JsonSerialize(using = MyClassSerializer.class)
    private String value;
}
```

### Fix 3: Use StdSerializer/StdDeserializer

```java
public class MyClassSerializer extends StdSerializer<MyClass> {
    public MyClassSerializer() {
        super(MyClass.class);
    }

    @Override
    public void serialize(MyClass value, JsonGenerator gen,
                          SerializerProvider provider) throws IOException {
        gen.writeString(value.getValue());
    }
}
```

## Related Errors

- {{< relref "jackson-module" >}} — UnresolvedTypeVariableException
- {{< relref "jackson-deserialization" >}} — MismatchedInputException
