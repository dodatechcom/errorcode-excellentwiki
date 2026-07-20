---
title: "[Solution] Java WritePendingException — Async Write Pending Fix"
description: "Fix Java WritePendingException by waiting for previous write callback, using CompletionHandler properly, and queuing writes."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# WritePendingException — Async Write Pending Fix

A `WritePendingException` is thrown when a write operation is attempted on an asynchronous socket channel while a previous asynchronous write operation is still pending. Only one asynchronous write can be in progress at a time per channel.

## Description

`java.nio.channels.WritePendingException` extends `IllegalStateException` and is thrown by `AsynchronousSocketChannel.write()` and `AsynchronousFileChannel.write()` when:

- A second `write()` call is made before the first completes
- A `write()` is attempted while a pending write is still being serviced
- Multiple writes are initiated concurrently on the same channel

Common message variants:

- `java.nio.channels.WritePendingException`
- `Write already pending`

## Common Causes

```java
// Cause 1: Two overlapping async writes on the same channel
AsynchronousSocketChannel channel = AsynchronousSocketChannel.open();
ByteBuffer buf1 = ByteBuffer.wrap("First".getBytes());
ByteBuffer buf2 = ByteBuffer.wrap("Second".getBytes());

channel.write(buf1, null, new CompletionHandler<Integer, Void>() {
    public void completed(Integer result, Void att) { /* slow */ }
    public void failed(Throwable exc, Void att) {}
});

// Second write before first completes — WritePendingException
channel.write(buf2, null, new CompletionHandler<Integer, Void>() {
    public void completed(Integer result, Void att) {}
    public void failed(Throwable exc, Void att) {}
});

// Cause 2: Write during read completion callback
channel.read(inBuffer, null, new CompletionHandler<Integer, Void>() {
    public void completed(Integer result, Void att) {
        channel.write(outBuffer, null, writeHandler);  // May conflict
    }
    public void failed(Throwable exc, Void att) {}
});

// Cause 3: Multiple threads writing to same channel
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.submit(() -> channel.write(buf1, null, handler1));
pool.submit(() -> channel.write(buf2, null, handler2));  // WritePendingException

// Cause 4: Write from completion handler of another write
channel.write(buf1, null, new CompletionHandler<Integer, Void>() {
    public void completed(Integer result, Void att) {
        channel.write(buf2, null, this);  // WritePendingException if prior not done
    }
    public void failed(Throwable exc, Void att) {}
});
```

## Solutions

### Fix 1: Wait for previous write to complete using Future

```java
AsynchronousSocketChannel channel = AsynchronousSocketChannel.open();
ByteBuffer buf1 = ByteBuffer.wrap("First".getBytes());
ByteBuffer buf2 = ByteBuffer.wrap("Second".getBytes());

Future<Integer> future1 = channel.write(buf1);
future1.get();  // Blocks until first write completes

// Now safe to write second
Future<Integer> future2 = channel.write(buf2);
future2.get();
```

### Fix 2: Use CompletionHandler chain for sequential writes

```java
public void sequentialWrite(AsynchronousSocketChannel channel,
        List<ByteBuffer> buffers, int index,
        CompletionHandler<Integer, Void> finalHandler) {
    if (index >= buffers.size()) {
        finalHandler.completed(0, null);
        return;
    }

    channel.write(buffers.get(index), null, new CompletionHandler<Integer, Void>() {
        @Override
        public void completed(Integer bytesWritten, Void att) {
            sequentialWrite(channel, buffers, index + 1, finalHandler);
        }

        @Override
        public void failed(Throwable exc, Void att) {
            finalHandler.failed(exc, null);
        }
    });
}

// Usage
sequentialWrite(channel, buffers, 0, finalHandler);
```

### Fix 3: Track pending writes with atomic flag

```java
public class AsyncWriter {
    private final AsynchronousSocketChannel channel;
    private final AtomicBoolean writePending = new AtomicBoolean(false);

    public void write(ByteBuffer buffer, CompletionHandler<Integer, Void> handler) {
        if (!writePending.compareAndSet(false, true)) {
            handler.failed(new WritePendingException(), null);
            return;
        }

        channel.write(buffer, null, new CompletionHandler<Integer, Void>() {
            @Override
            public void completed(Integer result, Void att) {
                writePending.set(false);
                handler.completed(result, att);
            }

            @Override
            public void failed(Throwable exc, Void att) {
                writePending.set(false);
                handler.failed(exc, att);
            }
        });
    }
}
```

### Fix 4: Queue writes for sequential processing

```java
public class QueuedAsyncWriter {
    private final AsynchronousSocketChannel channel;
    private final Queue<WriteRequest> pendingWrites = new ConcurrentLinkedQueue<>();
    private final AtomicBoolean writing = new AtomicBoolean(false);

    public void write(ByteBuffer buffer, CompletionHandler<Integer, Void> handler) {
        pendingWrites.add(new WriteRequest(buffer, handler));
        processNext();
    }

    private void processNext() {
        if (!writing.compareAndSet(false, true)) return;

        WriteRequest req = pendingWrites.poll();
        if (req == null) {
            writing.set(false);
            return;
        }

        channel.write(req.buffer, null, new CompletionHandler<Integer, Void>() {
            @Override
            public void completed(Integer result, Void att) {
                writing.set(false);
                req.handler.completed(result, att);
                processNext();
            }

            @Override
            public void failed(Throwable exc, Void att) {
                writing.set(false);
                req.handler.failed(exc, att);
                processNext();
            }
        });
    }

    private static class WriteRequest {
        final ByteBuffer buffer;
        final CompletionHandler<Integer, Void> handler;
        WriteRequest(ByteBuffer buffer, CompletionHandler<Integer, Void> handler) {
            this.buffer = buffer;
            this.handler = handler;
        }
    }
}
```

### Fix 5: Use synchronized block for shared channel writes

```java
public class SynchronizedAsyncWriter {
    private final AsynchronousSocketChannel channel;
    private final Object writeLock = new Object();

    public Future<Integer> write(ByteBuffer buffer) {
        synchronized (writeLock) {
            return channel.write(buffer);
        }
    }
}
```

## Prevention Checklist

- Ensure only one asynchronous write is in progress at a time per channel.
- Use `Future` return values to wait for write completion before initiating new writes.
- Chain sequential writes inside completion handlers to avoid overlap.
- Use atomic flags or queues to coordinate concurrent write requests.
- Avoid sharing async channels across threads without synchronization.

## Related Errors

- [ReadPendingException](../readpendingexception) — read overlap on async channel.
- [ClosedChannelException](../closedchannelexception) — I/O on a closed channel.
- [AsynchronousCloseException](../asynchronouscloseexception) — channel closed during async operation.
