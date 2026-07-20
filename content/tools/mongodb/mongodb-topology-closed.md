---
title: "[Solution] MongoDB Topology Closed Error"
description: "Fix MongoDB topology closed or destroyed errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Topology Closed Error

When the driver's topology is closed or destroyed, operations fail:

```
MongoTopologyClosedError: Topology was destroyed
```

```
MongoExpiredSessionError: Cannot use a session that has ended
```

## Common Causes

- The client was closed before operations completed
- A replica set failover occurred and the topology was not refreshed
- The server closed the connection due to an admin command (e.g., shutdown)
- The connection pool was closed during a graceful shutdown
- Network interruption caused the topology to be destroyed
- The `close()` method was called prematurely

## How to Fix

### 1. Do not close the client prematurely

```javascript
// Wrong: closing immediately
const client = new MongoClient(uri);
await client.close();

// Right: keep the client open for the application lifecycle
const client = new MongoClient(uri);
await client.connect();
// ... perform operations ...
// close only during application shutdown
```

### 2. Add retry logic for transient errors

```javascript
async function withRetry(fn, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}

// Usage
await withRetry(() => db.collection('users').findOne({ _id: id }));
```

### 3. Listen for topology events

```javascript
client.on('topologyClosed', () => {
  console.warn('Topology closed - attempting reconnect');
});

client.on('serverDescriptionChanged', (event) => {
  console.log('Server changed:', event.newDescription.address, event.newDescription.rtt);
});
```

### 4. Use unified topology (Node.js driver 4+)

In Node.js driver 4.0+, the unified topology is the default. Ensure you are not using legacy topology settings.

## Examples

```bash
# Check if the server is shutting down
grep -i "shutdown\|close\|shutdownInProgress" /var/log/mongodb/mongod.log

# Verify the client is connecting properly
mongosh --eval "db.runCommand({connectionStatus:1})"

# Monitor topology with server status
mongosh --eval "JSON.stringify(db.serverStatus().connections, null, 2)"
```