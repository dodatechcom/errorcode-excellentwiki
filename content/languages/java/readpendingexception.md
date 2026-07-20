---
title: "[Solution] Java ReadPendingException — NIO Async Read Fix"
description: "Fix Java ReadPendingException by waiting for previous reads to complete, using callbacks, and tracking pending operations."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ReadPendingException — NIO Async Read Fix

A `ReadPendingException` is thrown when attempting to initiate an asynchronous read on a channel when a previous asynchronous read operation is still pending. Only one asynchronous read can be in progress at a time per channel.

## Description

`java.nio.channels.ReadPendingException` is an unchecked exception extending `IllegalStateException`. It occurs with asynchronous channel groups (e.g., `AsynchronousSocketChannel`, `AsynchronousFileChannel`) when:

- A second `read()` call is made before the first completes
- A `read()` is attempted while a pending read is still being serviced
- An asynchronous scatter read is initiated while another read is pending

Common message variants:

- `java.nio.channels.ReadPendingException`
- `Read already pending`

This is specific to `java.nio.channels.AsynchronousSocketChannel` and `java.nio.channels.AsynchronousFileChannel`.

## Common Causes

```java
// Cause 1: Two overlapping async reads on the same channel
AsynchronousSocketChannel channel = AsynchronousSocketChannel.open();
ByteBuffer buffer1 = ByteBuffer.allocate(1024);
ByteBuffer buffer2 = ByteBuffer.allocate(1024);

channel.read(buffer1, null, new CompletionHandler<Integer, Void>() {
    public void completed(Integer result, Void att) { /* slow processing */ }
    public void failed(Throwable exc, Void att) {}
});

// Second read before first completes — ReadPendingException
channel.read(buffer2, null, new CompletionHandler<Integer, Void>() {
    public void completed(Integer result, Void att) {}
    public void failed(Throwable exc, Void att) {}
});

// Cause 2: Multiple blocking reads on async channel
AsynchronousFileChannel afc = AsynchronousFileChannel.open(path, StandardOpenOption.READ);
ByteBuffer buf1 = ByteBuffer.allocate(4096);
ByteBuffer buf2 = ByteBuffer.allocate(4096);
afc.read(buf1, 0);  // Returns Future
afc.read(buf2, 0);  // ReadPendingException if first hasn't completed

// Cause 3: Read during write completion handler
channel.write(outBuffer, null, new CompletionHandler<Integer, Void>() {
    public void completed(Integer result, Void att) {
        channel.read(inBuffer, null, handler);  // May conflict with other pending ops
    }
    public void failed(Throwable exc, Void att) {}
});

// Cause 4: Using the same channel from multiple threads without coordination
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.submit(() -> channel.read(buffer1, null, handler1));
pool.submit(() -> channel.read(buffer2, null, handler2));  // ReadPendingException
```

## Solutions

### Fix 1: Wait for the previous read to complete using a Future

```java
AsynchronousFileChannel channel = AsynchronousFileChannel.open(path, StandardOpenOption.READ);
ByteBuffer buffer = ByteBuffer.allocate(4096);

Future<Integer> readFuture = channel.read(buffer, 0);
Integer bytesRead = readFuture.get();  // Blocks until first read completes

// Now safe to start a second read
ByteBuffer buffer2 = ByteBuffer.allocate(4096);
channel.read(buffer2, 0);
```

### Fix 2: Use a single callback chain for sequential reads

```java
public void sequentialRead(AsynchronousSocketChannel channel, ByteBuffer buffer,
        CompletionHandler<Integer, Void> finalHandler) {
    channel.read(buffer, null, new CompletionHandler<Integer, Void>() {
        @Override
        public void completed(Integer bytesRead, Void att) {
            if (bytesRead == -1 || !buffer.hasRemaining()) {
                finalHandler.completed(bytesRead, null);
                return;
            }
            // Continue reading in the completion handler — no overlap
            channel.read(buffer, null, this);
        }

        @Override
        public void failed(Throwable exc, Void att) {
            finalHandler.failed(exc, null);
        }
    });
}
```

### Fix 3: Track pending operations with a state flag

```java
public class AsyncReader {
    private final AsynchronousSocketChannel channel;
    private final AtomicBoolean readPending = new AtomicBoolean(false);

    public void read(ByteBuffer buffer, CompletionHandler<Integer, Void> handler) {
        if (!readPending.compareAndSet(false, true)) {
            handler.failed(new ReadPendingException(), null);
            return;
        }

        channel.read(buffer, null, new CompletionHandler<Integer, Void>() {
            @Override
            public void completed(Integer result, Void att) {
                readPending.set(false);
                handler.completed(result, att);
            }

            @Override
            public void failed(Throwable exc, Void att) {
                readPending.set(false);
                handler.failed(exc, att);
            }
        });
    }
}
```

### Fix 4: Use a queue for pending read requests

```java
public class QueuedAsyncReader {
    private final AsynchronousSocketChannel channel;
    private final Queue<ReadRequest> pendingReads = new ConcurrentLinkedQueue<>();
    private final AtomicBoolean reading = new AtomicBoolean(false);

    public void read(ByteBuffer buffer, CompletionHandler<Integer, Void> handler) {
        pendingReads.add(new ReadRequest(buffer, handler));
        processNext();
    }

    private void processNext() {
        if (!reading.compareAndSet(false, true)) return;

        ReadRequest req = pendingReads.poll();
        if (req == null) {
            reading.set(false);
            return;
        }

        channel.read(req.buffer, null, new CompletionHandler<Integer, Void>() {
            @Override
            public void completed(Integer result, Void att) {
                reading.set(false);
                req.handler.completed(result, att);
                processNext();
            }

            @Override
            public void failed(Throwable exc, Void att) {
                reading.set(false);
                req.handler.failed(exc, att);
                processNext();
            }
        });
    }

    private static class ReadRequest {
        final ByteBuffer buffer;
        final CompletionHandler<Integer, Void> handler;
        ReadRequest(ByteBuffer buffer, CompletionHandler<Integer, Void> handler) {
            this.buffer = buffer;
            this.handler = handler;
        }
    }
}
```

## Prevention Checklist

- Ensure only one asynchronous read is in progress at a time per channel.
- Use `Future` return values to wait for read completion before initiating new reads.
- Chain sequential reads inside completion handlers to avoid overlap.
- Use atomic flags or queues to coordinate concurrent read requests.
- Avoid sharing async channels across threads without synchronization.

## Related Errors

- [WritePendingException](../readpendingexception) — write overlap on async channel.
- [ClosedChannelException](../closedchannelexception) — I/O on a closed channel.
- [AsynchronousCloseException](../asynchronouscloseexception) — channel closed during async operation.
