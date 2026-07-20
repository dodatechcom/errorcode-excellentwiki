---
title: "[Solution] Java StreamCorruptedException — Invalid Serialized Data Fix"
description: "Fix Java StreamCorruptedException by verifying serialized data integrity, checking class version compatibility, and using serialVersionUID."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# StreamCorruptedException — Invalid Serialized Data Fix

A `StreamCorruptedException` is thrown when control information read from an `ObjectInputStream` is invalid. This occurs when serialized data is corrupted, truncated, or written by an incompatible class version.

## Description

The `java.io.StreamCorruptedException` extends `IOException` and indicates that the stream data does not follow the expected serialization protocol. The serialization stream format includes magic numbers, version info, and type descriptors — any corruption to these will trigger this exception.

Common message variants:

- `java.io.StreamCorruptedException: invalid stream header`
- `java.io.StreamCorruptedException: unknown stream version`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── java.io.IOException
                    └── java.io.StreamCorruptedException
```

## Common Causes

```java
// Cause 1: File contains data that was not written by ObjectOutputStream
FileInputStream fis = new FileInputStream("plain_text.txt");
ObjectInputStream ois = new ObjectInputStream(fis);  // StreamCorruptedException

// Cause 2: Serialized file is partially overwritten or truncated
FileOutputStream fos = new FileOutputStream("data.ser");
ObjectOutputStream oos = new ObjectOutputStream(fos);
oos.writeObject(myObject);
oos.close();
// Later, another process partially overwrites data.ser

// Cause 3: Class serialVersionUID mismatch after code change
public class User implements Serializable {
    private static final long serialVersionUID = 1L;  // Was 1L, changed to 2L
    String name;
}
// Reading old serialized data with new serialVersionUID causes StreamCorruptedException

// Cause 4: Mixing serialization protocols
DataOutputStream dos = new DataOutputStream(new FileOutputStream("mixed.ser"));
dos.writeUTF("hello");
dos.writeInt(42);
ObjectInputStream ois = new ObjectInputStream(new FileInputStream("mixed.ser"));
ois.readObject();  // StreamCorruptedException — data was not written as an object

// Cause 5: Network transmission corrupted the byte stream
Socket socket = new Socket("example.com", 8080);
ObjectInputStream ois = new ObjectInputStream(socket.getInputStream());
MyObject obj = (MyObject) ois.readObject();  // Network corruption
```

## Solutions

### Fix 1: Define serialVersionUID on all Serializable classes

```java
// Wrong — auto-generated serialVersionUID may change between compiler versions
public class User implements Serializable {
    String name;
    int age;
}

// Correct — explicit serialVersionUID ensures compatibility
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    String name;
    int age;
}
```

### Fix 2: Validate the serialized data source before deserializing

```java
// Check file magic number before creating ObjectInputStream
try (FileInputStream fis = new FileInputStream("data.ser")) {
    byte[] header = new byte[2];
    int bytesRead = fis.read(header);
    if (bytesRead < 2 || header[0] != (byte) 0xAC || header[1] != (byte) 0xED) {
        throw new StreamCorruptedException("Invalid serialization stream header");
    }
}

// Or wrap in try-catch with clear error handling
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("data.ser"))) {
    MyObject obj = (MyObject) ois.readObject();
} catch (StreamCorruptedException e) {
    System.err.println("Data file is corrupted or not a valid serialization stream");
}
```

### Fix 3: Use separate streams for different data types

```java
// Wrong — mixing DataOutputStream and ObjectInputStream
DataOutputStream dos = new DataOutputStream(new FileOutputStream("mixed.ser"));
dos.writeUTF("metadata");
dos.writeInt(123);
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("mixed.ser"));
oos.writeObject(myObject);  // Overwrites previous data

// Correct — use separate files or a clear protocol
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("objects.ser"))) {
    oos.writeObject(myObject);
}

try (DataOutputStream dos = new DataOutputStream(new FileOutputStream("metadata.ser"))) {
    dos.writeUTF("metadata");
    dos.writeInt(123);
}
```

### Fix 4: Implement custom readObject/writeObject for safe deserialization

```java
public class SafeUser implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private int age;

    private void readObject(ObjectInputStream ois) throws IOException, ClassNotFoundException {
        try {
            ois.defaultReadObject();
        } catch (StreamCorruptedException e) {
            throw new IOException("Serialized data is incompatible with current class version", e);
        }
    }
}
```

## Prevention Checklist

- Always define `serialVersionUID` explicitly on all `Serializable` classes.
- Never mix `DataOutputStream`/`DataInputStream` with `ObjectOutputStream`/`ObjectInputStream` on the same stream.
- Store serialized objects in separate files or use a framing protocol.
- Test serialization round-trips when changing class structure.
- Validate stream headers before deserializing data from untrusted sources.

## Related Errors

- [InvalidClassException](../invalidclassexception) — class descriptor mismatch during deserialization.
- [ClassNotFoundException](../classnotfoundexception) — serialized class not found on classpath.
- [EOFException](../eofexception) — stream ends prematurely during deserialization.
- [OptionalDataException](../optionaldataexception) — primitive data encountered instead of object.
