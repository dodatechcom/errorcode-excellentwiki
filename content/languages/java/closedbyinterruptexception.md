---
title: "[Solution] Java ClosedByInterruptException — Channel Interrupt Fix"
description: "Fix Java ClosedByInterruptException by handling InterruptedException, using interruptible channels properly, and coordinating interrupts with I/O."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClosedByInterruptException — Channel Interrupt Fix

A `ClosedByInterruptException` is thrown when a thread is interrupted while blocked in an interruptible channel I/O operation. The channel is automatically closed and the interrupt status is set.

## Description

`java.nio.channels.ClosedByInterruptException` extends `AsynchronousCloseException` and is thrown when `Thread.interrupt()` is called while a thread is blocked on a NIO channel operation (e.g., `SocketChannel.read()`, `FileChannel.read()`). The channel is forcibly closed as a side effect.

Common message variants:

- `java.nio.channels.ClosedByInterruptException`
- `Interrupted I/O operation`

This is distinct from `InterruptedException` — the channel is physically closed, not just the blocking operation interrupted.

## Common Causes

```java
// Cause 1: Interrupting thread blocked on channel read
SocketChannel channel = SocketChannel.open();
ByteBuffer buffer = ByteBuffer.allocate(1024);
Thread readerThread = new Thread(() -> {
    try {
        channel.read(buffer);  // Blocks waiting for data
    } catch (ClosedByInterruptException e) {
        // Channel is now closed
    }
});
readerThread.start();
readerThread.interrupt();  // Triggers ClosedByInterruptException

// Cause 2: Thread pool shutdown interrupts active I/O
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.submit(() -> {
    channel.read(buffer);  // Blocks
});
pool.shutdownNow();  // Interrupts all threads — ClosedByInterruptException

// Cause 3: Timeout and interrupt race condition
SocketChannel channel = SocketChannel.open();
Thread t = new Thread(() -> {
    try {
        channel.read(buffer);  // Blocking read
    } catch (ClosedByInterruptException e) {
        // Interrupted during blocking I/O
    }
});
t.start();
t.interrupt();  // Interrupt while blocked

// Cause 4: FileChannel.lock() interrupted
FileChannel channel = FileChannel.open(path, StandardOpenOption.READ);
FileLock lock = channel.lock();  // Blocks if lock held — interruptible
// Thread is interrupted while waiting for lock
```

## Solutions

### Fix 1: Handle ClosedByInterruptException with proper cleanup

```java
SocketChannel channel = SocketChannel.open();
ByteBuffer buffer = ByteBuffer.allocate(1024);

try {
    channel.read(buffer);
} catch (ClosedByInterruptException e) {
    // Channel is automatically closed — do NOT try to use it
    System.err.println("Channel closed by interrupt: " + e.getMessage());
    // Optionally re-interrupt the thread
    Thread.currentThread().interrupt();
} catch (IOException e) {
    // Other I/O errors
}
```

### Fix 2: Use non-interruptible channels when interrupts are not desired

```java
// Force interrupt to NOT close the channel (Java 7+)
SocketChannel channel = SocketChannel.open();
channel.configureBlocking(true);

// Wrap with Thread.currentThread().interrupt() check
// but don't use interruptible channels
try {
    channel.read(buffer);
} catch (ClosedByInterruptException e) {
    // Restore interrupt status
    Thread.currentThread().interrupt();
    // Reopen channel or handle gracefully
    channel = SocketChannel.open();
}
```

### Fix 3: Coordinate thread shutdown with channel operations

```java
public class ManagedChannelReader {
    private final SocketChannel channel;
    private final AtomicBoolean running = new AtomicBoolean(true);

    public void readLoop() {
        ByteBuffer buffer = ByteBuffer.allocate(1024);
        while (running.get() && channel.isOpen()) {
            try {
                int bytesRead = channel.read(buffer);
                if (bytesRead == -1) break;
                processBuffer(buffer);
                buffer.clear();
            } catch (ClosedByInterruptException e) {
                // Interrupt received — clean shutdown
                break;
            } catch (IOException e) {
                if (running.get()) {
                    handleIOException(e);
                }
                break;
            }
        }
    }

    public void shutdown() {
        running.set(false);
        Thread.currentThread().interrupt();  // Unblock channel read
    }
}
```

### Fix 4: Use interruptible channel with proper executor shutdown

```java
ExecutorService pool = Executors.newFixedThreadPool(4);
List<SocketChannel> channels = new ArrayList<>();

pool.submit(() -> {
    try (SocketChannel channel = SocketChannel.open(address)) {
        channels.add(channel);
        ByteBuffer buffer = ByteBuffer.allocate(1024);
        channel.read(buffer);
    } catch (ClosedByInterruptException e) {
        // Expected during shutdown — channel auto-closed
    } catch (IOException e) {
        // Handle other errors
    }
});

// Graceful shutdown
pool.shutdown();
try {
    pool.awaitTermination(5, TimeUnit.SECONDS);
} catch (InterruptedException e) {
    pool.shutdownNow();  // Force interrupt — channels will be closed
}
```

### Fix 5: Use non-blocking I/O with Selector to avoid blocking entirely

```java
SocketChannel channel = SocketChannel.open();
channel.configureBlocking(false);  // Non-blocking — no interruptible block

Selector selector = Selector.open();
channel.register(selector, SelectionKey.OP_READ);

while (channel.isOpen()) {
    int ready = selector.select(1000);  // Timed select — returns 0 on timeout
    if (ready == 0) continue;

    Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
    while (keys.hasNext()) {
        SelectionKey key = keys.next();
        keys.remove();

        if (key.isReadable()) {
            SocketChannel sc = (SocketChannel) key.channel();
            ByteBuffer buffer = ByteBuffer.allocate(1024);
            sc.read(buffer);
        }
    }
}
```

## Prevention Checklist

- Handle `ClosedByInterruptException` explicitly when using interruptible NIO channels.
- Use non-blocking I/O with `Selector` to avoid blocking on channel operations.
- Coordinate thread shutdown with channel lifecycle — close channels before interrupting.
- Use `AtomicBoolean` flags to signal clean shutdown to I/O threads.
- Re-interrupt the thread after catching `ClosedByInterruptException` to preserve interrupt status.

## Related Errors

- [ClosedChannelException](../closedchannelexception) — channel already closed before operation.
- [InterruptedException](../interruptedexception) — thread interrupted outside of channel I/O.
- [AsynchronousCloseException](../asynchronouscloseexception) — channel closed by another thread.
