---
title: "[Solution] Java ClassNotFoundException — ObjectInputStream.readObject encounters class not on reader classpath"
description: "Fix Java ClassNotFoundException when objectinputstream.readobject encounters class not on reader classpath with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — ObjectInputStream.readObject encounters class not on reader classpath

A `ClassNotFoundException` occurs when ObjectInputStream ois = new ObjectInputStream(is);
MyObject obj = (MyObject) ois.readObject();  // ClassNotFoundException.

## Common Causes

```java
ObjectInputStream ois = new ObjectInputStream(is);
MyObject obj = (MyObject) ois.readObject();  // ClassNotFoundException
```

## Solutions

```java
// Fix: use SafeObjectInputStream
public class SafeOIS extends ObjectInputStream {
    private static final Set<String> ALLOWED = Set.of("com.example.Safe","java.lang.String");
    @Override
    protected Class<?> resolveClass(ObjectStreamClass desc) throws IOException, ClassNotFoundException {
        if (!ALLOWED.contains(desc.getName())) throw new InvalidClassException("Unauthorized: "+desc.getName());
        return super.resolveClass(desc);
    }
}

// Better: use JSON instead of native serialization
```

## Prevention Checklist

- Avoid Java native serialization — use JSON/ProtoBuf.
- Implement readObject with class validation.
- Keep serialized classes in stable packages.

## Related Errors

ClassNotFoundException, InvalidClassException
