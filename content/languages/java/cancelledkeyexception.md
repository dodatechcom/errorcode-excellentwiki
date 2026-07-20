---
title: "[Solution] Java CancelledKeyException — NIO SelectionKey Fix"
description: "Fix Java CancelledKeyException by checking key.isValid(), re-registering channels with selector, and handling deregistration properly."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# CancelledKeyException — NIO SelectionKey Fix

A `CancelledKeyException` is thrown when an attempt is made to use a `SelectionKey` that has been cancelled. Once a key is cancelled, it is invalid and cannot be used for I/O operations with its selector.

## Description

`java.nio.channels.CancelledKeyException` is an unchecked exception extending `java.lang.IllegalStateException`. A `SelectionKey` is cancelled when:

- `key.cancel()` is called explicitly
- The channel associated with the key is closed
- The selector associated with the key is closed

Common message variants:

- `java.nio.channels.CancelledKeyException`

The key remains in the key set until the next `select()` operation removes it, but any attempt to use it between cancellation and removal triggers this exception.

## Common Causes

```java
// Cause 1: Using a key after explicit cancellation
SelectionKey key = channel.register(selector, SelectionKey.OP_READ);
key.cancel();
selector.select();         // Key removed from key set
key.interestOps(SelectionKey.OP_WRITE);  // CancelledKeyException

// Cause 2: Closing a channel while its key is being processed
for (SelectionKey key : selector.selectedKeys()) {
    if (key.isReadable()) {
        SocketChannel sc = (SocketChannel) key.channel();
        sc.close();        // Cancels the key
        key.interestOps(SelectionKey.OP_WRITE);  // CancelledKeyException
    }
}

// Cause 3: Re-registering a cancelled key without checking validity
SelectionKey key = channel.register(selector, SelectionKey.OP_READ);
key.cancel();
// Later...
key.interestOps(SelectionKey.OP_READ);  // CancelledKeyException

// Cause 4: Thread race — key cancelled while another thread uses it
// Thread A: key.cancel();
// Thread B: key.isReadable();  // May throw CancelledKeyException
```

## Solutions

### Fix 1: Check key.isValid() before using it

```java
for (SelectionKey key : selector.selectedKeys()) {
    if (!key.isValid()) {
        continue;  // Skip cancelled keys
    }
    if (key.isReadable()) {
        handleRead(key);
    }
    if (key.isWritable()) {
        handleWrite(key);
    }
}
```

### Fix 2: Re-register the channel with the selector after cancellation

```java
SelectionKey oldKey = channel.keyFor(selector);
if (oldKey != null) {
    oldKey.cancel();
}

// Re-register with new interest set
SelectionKey newKey = channel.register(selector, SelectionKey.OP_READ);
```

### Fix 3: Handle deregistration in a separate cleanup step

```java
Set<SelectionKey> keysToCancel = new HashSet<>();

for (SelectionKey key : selector.selectedKeys()) {
    if (!key.isValid()) {
        continue;
    }
    try {
        if (key.isReadable()) {
            processRead(key);
        }
    } catch (CancelledKeyException e) {
        keysToCancel.add(key);
    }
}

// Remove cancelled keys outside the iteration
for (SelectionKey key : keysToCancel) {
    key.cancel();
}
```

### Fix 4: Synchronize selector access to prevent race conditions

```java
public class SafeSelector {
    private final Selector selector;
    private final Object lock = new Object();

    public void register(SelectableChannel channel, int ops) throws IOException {
        synchronized (lock) {
            channel.register(selector, ops);
        }
    }

    public void select(long timeout) throws IOException {
        synchronized (lock) {
            selector.select(timeout);
            Iterator<SelectionKey> it = selector.selectedKeys().iterator();
            while (it.hasNext()) {
                SelectionKey key = it.next();
                it.remove();
                if (key.isValid()) {
                    handleKey(key);
                }
            }
        }
    }
}
```

## Prevention Checklist

- Always check `key.isValid()` before performing operations on a `SelectionKey`.
- Remove cancelled keys from the selected key set promptly.
- Avoid closing channels or selectors while other threads are iterating keys.
- Re-register channels rather than modifying interest ops on potentially cancelled keys.
- Catch `CancelledKeyException` when keys may be cancelled mid-processing.

## Related Errors

- [ClosedChannelException](../closedchannelexception) — I/O operation on a closed channel.
- [ClosedSelectorException](../closedchannelexception) — selector closed while channels are registered.
- [AsynchronousCloseException](../asynchronouscloseexception) — channel closed by another thread during I/O.
