---
title: "[Solution] Rust Sink Error — How to Fix"
description: "Fix Sink trait errors. Resolve async sink implementation, backpressure handling, and flushing issues."
languages: ["rust"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
comments: true
---

# Sink Error

Sink errors occur when using the `futures::Sink` trait — backpressure issues, flushing failures, and poll_ready behavior violations.

## Common Causes

```rust
use futures::SinkExt;
use tokio::sync::mpsc;

// Not calling poll_ready before start_send
// Sink::poll_ready must return Ready before start_send

// Not flushing after sending
async fn bad_send(sink: &mut impl futures::Sink<String>) {
    sink.send("hello".into()).await.unwrap(); // May buffer without flushing
}

// Buffer overflow — sending faster than consuming
```

## How to Fix

1. **Use `SinkExt::send` which handles ready + flush**

```rust
use futures::{SinkExt, StreamExt};
use tokio::sync::mpsc;

#[tokio::main]
async fn main() {
    let (tx, mut rx) = mpsc::channel(10);

    let mut sink = futures::sink::unfold(tx, |mut tx, msg: String| async move {
        tx.send(msg).await.map_err(|e| std::io::Error::new(std::io::ErrorKind::Other, e))?;
        Ok::<_, std::io::Error>(tx)
    });

    sink.send("Hello".into()).await.unwrap();
    sink.send("World".into()).await.unwrap();

    // Flush explicitly if needed
    sink.flush().await.unwrap();
}
```

2. **Handle backpressure with `poll_ready`**

```rust
use futures::{Sink, SinkExt};

async fn process_batch<S: Sink<Item>>(sink: &mut S, items: Vec<S::Item>)
where S::Error: std::fmt::Display
{
    for item in items {
        // Wait until sink is ready
        std::future::poll_fn(|cx| sink.poll_ready(cx)).await.unwrap();
        sink.start_send(item).unwrap();
    }
    sink.flush().await.unwrap();
}
```

3. **Use buffered sinks for throughput**

```rust
use futures::stream::StreamExt;
use futures::sink::Buffer;

// Buffer wraps a sink and batches flush operations
let sink = /* your sink */;
let mut buffered = Buffer::new(sink, 100); // Buffer up to 100 items

for i in 0..1000 {
    buffered.send(i).await.unwrap();
}
buffered.flush().await.unwrap();
```

## Examples

```rust
use futures::{SinkExt, StreamExt};
use tokio::net::TcpStream;
use tokio_util::codec::{Framed, LinesCodec};

#[tokio::main]
async fn main() -> std::io::Result<()> {
    let stream = TcpStream::connect("127.0.0.1:8080").await?;
    let mut framed = Framed::new(stream, LinesCodec::new());

    // Send messages
    framed.send("Hello".to_string()).await?;
    framed.send("World".to_string()).await?;

    // Receive responses
    while let Some(Ok(line)) = framed.next().await {
        println!("Received: {}", line);
    }

    Ok(())
}
```

## Related Errors

- [Stream Error]({{< relref "/languages/rust/rust-stream-error-rs" >}}) — stream issues
- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — async runtime
- [Poll Error]({{< relref "/languages/rust/rust-poll-error" >}}) — polling issues
