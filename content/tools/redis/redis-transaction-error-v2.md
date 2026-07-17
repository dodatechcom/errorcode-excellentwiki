---
title: "Redis MULTI/EXEC - transaction error"
description: "Redis MULTI/EXEC transaction fails due to WATCH conflict, command error, or EXECABORT"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Redis MULTI/EXEC transaction error occurs when a transaction fails to execute. This can be caused by a WATCH conflict (optimistic lock failure), a command error within the transaction, or the transaction being aborted.

## Common Causes

- WATCH detected a modified key before EXEC
- Command within MULTI/EXEC block is syntactically invalid
- Not enough arguments for a command in the transaction
- EXECABORT due to WATCH failure
- Client disconnected during transaction

## How to Fix

1. Handle WATCH failures with retry logic:

```javascript
async function transferFunds(redis, from, to, amount) {
  for (let i = 0; i < 3; i++) {
    await redis.watch(from, to);
    const balance = await redis.get(from);

    if (parseInt(balance) < amount) {
      await redis.unwatch();
      throw new Error('Insufficient funds');
    }

    const multi = redis.multi();
    multi.decrby(from, amount);
    multi.incrby(to, amount);

    const result = await multi.exec();
    if (result !== null) {
      return result; // transaction succeeded
    }
    // WATCH failed, retry
    console.log('Transaction conflict, retrying...');
  }
  throw new Error('Transaction failed after retries');
}
```

2. Validate commands before EXEC:

```javascript
const multi = redis.multi();
multi.set('key1', 'value1');
multi.incr('key2');
multi.set('key3', 'value3');

try {
  await multi.exec();
} catch (error) {
  if (error.message.includes('EXECABORT')) {
    console.log('Transaction aborted');
  }
}
```

3. Use optimistic locking pattern:

```javascript
async function updateInventory(redis, productId, quantity) {
  let retries = 3;
  while (retries > 0) {
    await redis.watch(`product:${productId}`);
    const current = await redis.get(`product:${productId}`);

    if (parseInt(current) < quantity) {
      await redis.unwatch();
      return false;
    }

    const multi = redis.multi();
    multi.set(`product:${productId}`, parseInt(current) - quantity);
    const result = await multi.exec();

    if (result) return true;
    retries--;
  }
  return false;
}
```

4. Use Lua scripts for atomic operations without WATCH:

```javascript
const luaScript = `
  local current = tonumber(redis.call('GET', KEYS[1]) or 0)
  if current >= tonumber(ARGV[1]) then
    redis.call('DECRBY', KEYS[1], ARGV[1])
    return 1
  end
  return 0
`;

const result = await redis.eval(luaScript, 1, 'stock:product1', 5);
```

## Examples

```bash
# Error: WATCH failed, transaction aborted
> WATCH key1
OK
> MULTI
OK
> SET key1 newvalue
QUEUED
> EXEC
(nil)
# EXECABORT: Transaction discarded because of previous errors
# Another client modified key1

# Fix: retry with fresh WATCH
> WATCH key1
OK
> GET key1
"original"
> MULTI
OK
> SET key1 updated
QUEUED
> EXEC
1) OK
```

## Related Errors

- [Lua error]({{< relref "/tools/redis/redis-lua-error" >}})
- [Timeout error]({{< relref "/tools/redis/redis-timeout-error" >}})
