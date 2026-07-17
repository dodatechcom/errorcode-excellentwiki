---
title: "Redis Pub/Sub - subscription error"
description: "Redis Pub/Sub fails to deliver messages due to subscription issues, connection drops, or channel mismatches"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Redis Pub/Sub subscription error occurs when published messages are not delivered to subscribers, or when the subscription process encounters issues. Pub/Sub is fire-and-forget, so messages published while no subscriber is connected are lost.

## Common Causes

- Subscriber disconnected and not reconnected
- Channel name mismatch between publisher and subscriber
- Subscription pattern not matching published channels
- Redis connection pool exhaustion during high throughput
- Client entered blocking subscription mode incorrectly

## How to Fix

1. Ensure reliable subscription with reconnection:

```javascript
const Redis = require('ioredis');

function createSubscriber() {
  const subscriber = new Redis({ host: '127.0.0.1', port: 6379 });

  subscriber.on('error', (err) => {
    console.error('Subscriber error:', err);
  });

  subscriber.on('close', () => {
    console.log('Reconnecting subscriber...');
    setTimeout(createSubscriber, 1000);
  });

  subscriber.subscribe('notifications', (err) => {
    if (err) console.error('Subscribe error:', err);
  });

  subscriber.on('message', (channel, message) => {
    console.log(`Received on ${channel}: ${message}`);
  });

  return subscriber;
}

const subscriber = createSubscriber();
```

2. Use pattern subscribe for multiple channels:

```javascript
const subscriber = new Redis();
subscriber.psubscribe('user:*:notifications', (err) => {
  if (err) console.error('Pattern subscribe error:', err);
});

subscriber.on('pmessage', (pattern, channel, message) => {
  console.log(`Pattern ${pattern} matched ${channel}: ${message}`);
});
```

3. Use separate connections for subscribe and publish:

```javascript
const publisher = new Redis();
const subscriber = new Redis();

await subscriber.subscribe('channel1');

// Publisher must use a separate connection
await publisher.publish('channel1', 'hello');
```

4. Check subscription count:

```bash
redis-cli PUBSUB NUMSUB channel1 channel2
redis-cli INFO clients
```

5. Handle lost messages with Redis Streams:

```javascript
// Use Streams for reliable message delivery
await publisher.xadd('stream:events', '*', 'type', 'notification', 'data', payload);
// Consumer can track last processed ID
```

## Examples

```javascript
// Error: subscription lost silently
const redis = new Redis();
redis.subscribe('events');
// If connection drops, messages are lost

// Fix: add error handling and reconnect
const redis = new Redis();
redis.on('error', () => {
  setTimeout(() => {
    redis.subscribe('events');
  }, 1000);
});
```

## Related Errors

- [Connection error]({{< relref "/tools/redis/redis-connection-error" >}})
- [Transaction error]({{< relref "/tools/redis/redis-transaction-error" >}})
