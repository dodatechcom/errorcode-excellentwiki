---
title: "[Solution] Java WriteAbortedException — Serialization Write Abort Fix"
description: "Fix Java WriteAbortedException by handling underlying IOExceptions, checking disk space, and verifying serialization compatibility before writing."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# WriteAbortedException — Serialization Write Abort Fix

A `WriteAbortedException` is thrown when an `ObjectOutputStream` aborts writing due to an underlying error during serialization. It wraps the original exception that caused the write failure and indicates that the stream is in an inconsistent state.

## Description

The `java.io.WriteAbortedException` extends `IOException` and is thrown when `ObjectOutputStream.writeObject()` encounters an error while serializing an object. The stream is typically unusable after this exception because it may be left in a partially written state.

Message variants:

- `java.io.WriteAbortedException: Stream closed`
- `java.io.WriteAbortedException: java.io.IOException: [underlying cause]`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── java.io.IOException
                    └── java.io.WriteAbortedException
```

## Common Causes

```java
// Cause 1: Disk full during serialization
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("/full/disk/data.ser"));
oos.writeObject(largeObject);  // WriteAbortedException if disk is full

// Cause 2: Non-serializable field encountered during object graph traversal
public class Order implements Serializable {
    private static final long serialVersionUID = 1L;
    private String orderId;
    private transient Connection connection;  // If not transient, throws NotSerializableException
    // which causes WriteAbortedException
}

// Cause 3: Output stream closed during write operation
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("data.ser"));
oos.writeObject(user1);
fos.close();  // Close underlying stream
oos.writeObject(user2);  // WriteAbortedException: Stream closed

// Cause 4: Network connection lost during serialization
Socket socket = new Socket("example.com", 8080);
ObjectOutputStream oos = new ObjectOutputStream(socket.getOutputStream());
oos.writeObject(largeObject);  // WriteAbortedException if connection drops

// Cause 5: Permission denied during file write
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("/root/protected.ser"));
oos.writeObject(data);  // WriteAbortedException wrapping FileNotFoundException
```

## Solutions

### Fix 1: Check disk space before writing serialized data

```java
File outputFile = new File("data.ser");
File parentDir = outputFile.getParentFile();

// Check available disk space before writing
long availableBytes = parentDir.getUsableSpace();
long estimatedSize = estimateSerializedSize(myObject);

if (availableBytes < estimatedSize) {
    throw new IOException("Insufficient disk space: need " + estimatedSize
        + " bytes, only " + availableBytes + " available");
}

try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(outputFile))) {
    oos.writeObject(myObject);
}
```

### Fix 2: Validate the object graph before serialization

```java
// Use a validation method to check all fields are serializable
public class Order implements Serializable {
    private static final long serialVersionUID = 1L;
    private String orderId;
    private List<OrderItem> items;
    private transient Connection connection;

    // Validate before serialization
    public void validateForSerialization() {
        if (orderId == null || orderId.isEmpty()) {
            throw new IllegalArgumentException("orderId must not be null or empty");
        }
        if (items != null) {
            for (OrderItem item : items) {
                if (item == null) {
                    throw new IllegalArgumentException("items must not contain null elements");
                }
            }
        }
    }
}

// Use it before writing
order.validateForSerialization();
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("order.ser"));
oos.writeObject(order);
```

### Fix 3: Use try-catch to handle write failures gracefully

```java
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("data.ser"))) {
    oos.writeObject(myObject);
    oos.flush();  // Force buffered data to be written
} catch (WriteAbortedException e) {
    Throwable cause = e.getCause();
    System.err.println("Serialization aborted due to: " + cause.getMessage());
    // Delete partially written file
    File partialFile = new File("data.ser");
    partialFile.delete();
} catch (IOException e) {
    System.err.println("I/O error during serialization: " + e.getMessage());
}
```

### Fix 4: Use try-with-resources to ensure stream cleanup

```java
// Wrong — stream may not be closed on error
ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("data.ser"));
oos.writeObject(largeObject);
oos.close();  // May not execute if writeObject throws

// Correct — try-with-resources ensures close even on exception
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("data.ser"))) {
    oos.writeObject(largeObject);
    oos.flush();
} catch (WriteAbortedException e) {
    System.err.println("Write aborted: " + e.getMessage());
    File partialFile = new File("data.ser");
    if (partialFile.exists()) {
        partialFile.delete();
    }
}
```

## Prevention Checklist

- Check disk space before writing large serialized objects.
- Validate the entire object graph before calling `writeObject()`.
- Always use try-with-resources for `ObjectOutputStream`.
- Call `flush()` after `writeObject()` to ensure data is written to disk.
- Delete partially written files after a `WriteAbortedException`.

## Related Errors

- [IOException](../ioexception) — parent class for general I/O failures.
- [NotSerializableException](../notserializableexception) — non-serializable class in object graph.
- [StreamCorruptedException](../streamcorruptedexception) — invalid serialization stream format.
- [FileNotFoundException](../filenotfoundexception) — output file cannot be created or opened.
