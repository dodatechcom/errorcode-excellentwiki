---
title: "[Solution] Java ClosedSelectorException — Closed Selector I/O Fix"
description: "Fix Java ClosedSelectorException by checking selector isOpen(), handling selector lifecycle, and avoiding closing selector while in use."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClosedSelectorException — Closed Selector I/O Fix

A `ClosedSelectorException` is thrown when an I/O operation is attempted on a NIO selector that has been closed. This is an unchecked exception indicating a lifecycle management issue with the selector.

## Description

`java.nio.channels.ClosedSelectorException` extends `IllegalStateException` and is thrown when calling methods on a `Selector` after `close()` has been called. This commonly occurs when:

- A selector is closed while another thread is using it
- A channel registered with a closed selector attempts to re-register
- `select()` is called on a closed selector

Common message variants:

- `java.nio.channels.ClosedSelectorException`

## Common Causes

```java
// Cause 1: Calling select() on closed selector
Selector selector = Selector.open();
selector.close();
selector.select();  // ClosedSelectorException

// Cause 2: Selector closed by one thread while another is selecting
Selector selector = Selector.open();
Thread selectorThread = new Thread(() -> {
    while (true) {
        selector.select();  // Blocking select
        // Process selected keys
    }
});
selectorThread.start();
selector.close();  // ClosedSelectorException in selectorThread

// Cause 3: Registering channel on closed selector
Selector selector = Selector.open();
selector.close();
SocketChannel channel = SocketChannel.open();
channel.configureBlocking(false);
channel.register(selector, SelectionKey.OP_READ);  // ClosedSelectorException

// Cause 4: Accessing selector after shutdown hook
Runtime.getRuntime().addShutdownHook(new Thread(() -> {
    selector.close();  // Closes selector during shutdown
}));
// Meanwhile, selector thread may still be running
```

## Solutions

### Fix 1: Check selector isOpen() before operations

```java
Selector selector = Selector.open();

// Before select()
if (selector.isOpen()) {
    int ready = selector.select(1000);
    if (ready > 0) {
        processSelectedKeys(selector);
    }
} else {
    // Selector was closed — exit loop
    break;
}
```

### Fix 2: Synchronize selector access across threads

```java
public class ManagedSelector {
    private final Selector selector;
    private final Object closeLock = new Object();
    private volatile boolean closed = false;

    public int select(long timeoutMs) throws IOException {
        synchronized (closeLock) {
            if (closed) throw new IOException("Selector is closed");
            return selector.select(timeoutMs);
        }
    }

    public void close() {
        synchronized (closeLock) {
            closed = true;
            selector.close();
        }
    }

    public boolean isOpen() {
        return !closed && selector.isOpen();
    }
}

// Usage
ManagedSelector managed = new ManagedSelector();
// Thread A
int ready = managed.select(1000);

// Thread B — safe close
managed.close();
```

### Fix 3: Use volatile flag for clean shutdown

```java
public class SelectorLoop implements Runnable {
    private final Selector selector;
    private volatile boolean running = true;

    @Override
    public void run() {
        while (running) {
            try {
                int ready = selector.select(1000);
                if (ready == 0) continue;
                if (!selector.isOpen()) break;

                Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
                while (keys.hasNext()) {
                    SelectionKey key = keys.next();
                    keys.remove();

                    if (!key.isValid()) continue;
                    handleKey(key);
                }
            } catch (ClosedSelectorException e) {
                break;  // Expected during shutdown
            } catch (IOException e) {
                if (running) handleError(e);
            }
        }
    }

    public void shutdown() {
        running = false;
        selector.wakeup();  // Interrupt blocking select()
    }
}
```

### Fix 4: Don't close selector while channels are registered

```java
// Wrong — close selector while channels are still registered
Selector selector = Selector.open();
SocketChannel channel = SocketChannel.open();
channel.configureBlocking(false);
channel.register(selector, SelectionKey.OP_READ);
selector.close();  // Channels become deregistered

// Correct — deregister channels first
SelectionKey key = channel.keyFor(selector);
if (key != null) key.cancel();
selector.close();
channel.close();
```

### Fix 5: Use try-with-resources for selector lifecycle

```java
// Selector used within a bounded scope
try (Selector selector = Selector.open()) {
    SocketChannel channel = SocketChannel.open();
    channel.configureBlocking(false);
    channel.register(selector, SelectionKey.OP_READ);

    while (channel.isOpen()) {
        selector.select(1000);
        Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
        while (keys.hasNext()) {
            SelectionKey key = keys.next();
            keys.remove();
            if (key.isReadable()) {
                ByteBuffer buf = ByteBuffer.allocate(1024);
                ((SocketChannel) key.channel()).read(buf);
            }
        }
    }
}
```

## Prevention Checklist

- Always check `selector.isOpen()` before calling `select()`, `selectNow()`, or `wakeup()`.
- Use synchronization or volatile flags to coordinate selector close with selector loop.
- Deregister all channels before closing the selector.
- Call `selector.wakeup()` before closing to interrupt any blocking `select()`.
- Prefer try-with-resources or explicit lifecycle management for selectors.

## Related Errors

- [ClosedChannelException](../closedchannelexception) — I/O on a closed channel.
- [CancelledKeyException](../cancelledkeyselectionkey) — operation on invalid selection key.
- [ClosedByInterruptException](../closedbyinterruptexception) — channel closed by interrupt.
