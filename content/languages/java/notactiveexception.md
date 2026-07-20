---
title: "[Solution] Java NotActiveException — Serialization Order Fix"
description: "Fix Java NotActiveException by ensuring proper serialization order, calling defaultReadObject/defaultWriteObject correctly, and following the serialization protocol."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NotActiveException — Serialization Order Fix

A `NotActiveException` is thrown when methods are called in the wrong order during serialization or deserialization. This typically occurs when `defaultReadObject()` or `defaultWriteObject()` are called outside the correct serialization context, or when `readObject()`/`writeObject()` methods are invoked incorrectly.

## Description

The `java.io.NotActiveException` extends `ObjectStreamException` and signals that a serialization method was called when the stream is not in the appropriate active state. For example, calling `defaultReadObject()` outside of `readObject()`, or calling `writeObject()` on a stream that is not currently writing an object.

Message variants:

- `java.io.NotActiveException: writeObject()`
- `java.io.NotActiveException: readObject()`
- `java.io.NotActiveException: defaultWriteObject()`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── java.io.IOException
                    └── java.io.ObjectStreamException
                          └── java.io.NotActiveException
```

## Common Causes

```java
// Cause 1: Calling defaultWriteObject() outside of writeObject()
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;

    // This is wrong — defaultWriteObject() must be called inside writeObject()
    public void saveTo(ObjectOutputStream oos) throws IOException {
        oos.defaultWriteObject();  // NotActiveException if called outside writeObject()
    }
}

// Cause 2: Calling defaultReadObject() outside of readObject()
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;

    public void loadFrom(ObjectInputStream ois) throws IOException, ClassNotFoundException {
        ois.defaultReadObject();  // NotActiveException if called outside readObject()
    }
}

// Cause 3: Incorrect serialization protocol ordering
public class User implements Serializable {
    private static final long serialVersionUID = 1L;

    private void writeObject(ObjectOutputStream oos) throws IOException {
        oos.writeUTF(name);       // Write custom data first
        oos.defaultWriteObject(); // Then write default data — correct order
    }
}

// Cause 4: Calling ObjectOutputStream methods on a deserialization stream
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("data.ser"));
ois.defaultReadObject();  // Correct inside readObject()
// But calling ois.writeObject() on an input stream would be wrong

// Cause 5: Multiple calls to defaultWriteObject() in one writeObject()
public class User implements Serializable {
    private static final long serialVersionUID = 1L;

    private void writeObject(ObjectOutputStream oos) throws IOException {
        oos.defaultWriteObject();  // First call — correct
        oos.defaultWriteObject();  // Second call — NotActiveException
    }
}
```

## Solutions

### Fix 1: Call defaultWriteObject() only inside writeObject()

```java
// Wrong — defaultWriteObject() called in wrong context
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;
    int age;

    public void serialize(ObjectOutputStream oos) throws IOException {
        oos.defaultWriteObject();  // NotActiveException
    }
}

// Correct — call inside writeObject()
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;
    int age;

    private void writeObject(ObjectOutputStream oos) throws IOException {
        oos.defaultWriteObject();  // Correct — called inside writeObject()
    }
}
```

### Fix 2: Follow the correct serialization protocol order

```java
// Correct order for custom writeObject()
private void writeObject(ObjectOutputStream oos) throws IOException {
    oos.writeObject(name);           // Write field 1
    oos.writeInt(age);               // Write field 2
    oos.defaultWriteObject();        // Write remaining default fields
}

// Correct order for custom readObject()
private void readObject(ObjectInputStream ois)
    throws IOException, ClassNotFoundException {
    this.name = (String) ois.readObject();  // Read field 1
    this.age = ois.readInt();                // Read field 2
    ois.defaultReadObject();                 // Read remaining default fields
}
```

### Fix 3: Use Externalizable for full control when protocol is complex

```java
public class User implements Externalizable {
    private static final long serialVersionUID = 1L;
    String name;
    int age;

    public User() {}  // Required no-arg constructor

    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeObject(name);  // No defaultWriteObject() needed
        out.writeInt(age);
    }

    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        this.name = (String) in.readObject();  // No defaultReadObject() needed
        this.age = in.readInt();
    }
}
```

### Fix 4: Prevent accidental calls outside serialization context

```java
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;
    private boolean serializing = false;

    private void writeObject(ObjectOutputStream oos) throws IOException {
        serializing = true;
        try {
            oos.defaultWriteObject();
        } finally {
            serializing = false;
        }
    }

    // Guard method to prevent misuse
    public void saveExternal(ObjectOutputStream oos) throws IOException {
        if (!serializing) {
            throw new IllegalStateException(
                "saveExternal() must not be called outside writeObject()");
        }
        oos.defaultWriteObject();
    }
}
```

## Prevention Checklist

- Always call `defaultWriteObject()` inside `writeObject()` and `defaultReadObject()` inside `readObject()`.
- Ensure `writeObject()` and `readObject()` write/read fields in the same order.
- Never call `defaultWriteObject()` or `defaultReadObject()` more than once per serialization cycle.
- Use `Externalizable` when the serialization protocol is complex and needs explicit control.
- Test serialization round-trips thoroughly after implementing custom `readObject()`/`writeObject()`.

## Related Errors

- [NotSerializableException](../notserializableexception) — class does not implement Serializable.
- [InvalidClassException](../invalidclassexception) — class descriptor mismatch during deserialization.
- [StreamCorruptedException](../streamcorruptedexception) — invalid serialization stream format.
- [OptionalDataException](../optionaldataexception) — primitive data found instead of expected object.
