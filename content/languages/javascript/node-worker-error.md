---
title: "Node.js Worker Thread Error"
description: "Worker thread errors in Node.js — Fix errors in worker_threads module including unhandled errors and resource exhaustion."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

Worker thread errors occur when a `worker_threads.Workorker` encounters an unhandled exception, resource limit, or communication failure. These errors can be difficult to debug since the error originates in a separate thread.

## Description

Common worker thread error messages include:

- `Worker terminated with exit code 1` — unhandled exception in worker
- `Error [ERR_WORKER_PATH]: ...` — invalid worker script path
- `Error: write EPIPE` — worker process exited before message was sent
- `DataCloneError: ...` — cannot transfer non-cloneable data via postMessage

## Common Causes

```javascript
// Cause 1: Unhandled exception inside the worker
const { Worker } = require("node:worker_threads");
const worker = new Worker("./worker.js");
worker.on("error", (err) => {
  // Error: worker threw an exception
});

// Cause 2: Trying to transfer non-cloneable objects
worker.postMessage({ buffer: new WeakMap() }); // DataCloneError

// Cause 3: Worker script path is incorrect
const worker = new Worker("./nonexistent-worker.js"); // ERR_WORKER_PATH

// Cause 4: CPU exhaustion from too many workers
for (let i = 0; i < 100; i++) {
  new Worker("./worker.js"); // too many threads
}
```

## Solutions

### Fix 1: Add error handlers to workers

```javascript
const { Worker } = require("node:worker_threads");

function createWorker(scriptPath, data) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(scriptPath, { workerData: data });

    worker.on("message", resolve);
    worker.on("error", (err) => {
      console.error(`Worker error in ${scriptPath}:`, err.message);
      reject(err);
    });
    worker.on("exit", (code) => {
      if (code !== 0) {
        reject(new Error(`Worker exited with code ${code}`));
      }
    });
  });
}

// Usage
try {
  const result = await createWorker("./worker.js", { input: "data" });
  console.log("Result:", result);
} catch (err) {
  console.error("Worker failed:", err.message);
}
```

### Fix 2: Use transferable objects correctly

```javascript
const { Worker, isMainThread, parentPort } = require("node:worker_threads");

if (!isMainThread) {
  parentPort.on("message", (data) => {
    // Process data and return
    parentPort.postMessage({ result: data.input * 2 });
  });
} else {
  const worker = new Worker(__filename);

  // Use SharedArrayBuffer for shared memory (transferable)
  const sharedBuffer = new SharedArrayBuffer(1024);
  const sharedArray = new Int32Array(sharedBuffer);
  sharedArray[0] = 42;

  // Transfer the buffer instead of copying
  worker.postMessage({ buffer: sharedBuffer }, [sharedBuffer]);
}
```

### Fix 3: Limit concurrent workers

```javascript
const { Worker } = require("node:worker_threads");
const os = require("node:os");

class WorkerPool {
  constructor(scriptPath, maxWorkers = os.cpus().length) {
    this.scriptPath = scriptPath;
    this.maxWorkers = maxWorkers;
    this.activeWorkers = 0;
    this.queue = [];
  }

  run(data) {
    return new Promise((resolve, reject) => {
      if (this.activeWorkers >= this.maxWorkers) {
        this.queue.push({ data, resolve, reject });
        return;
      }
      this._startWorker(data, resolve, reject);
    });
  }

  _startWorker(data, resolve, reject) {
    this.activeWorkers++;
    const worker = new Worker(this.scriptPath, { workerData: data });

    worker.on("message", (result) => {
      resolve(result);
      this.activeWorkers--;
      if (this.queue.length > 0) {
        const next = this.queue.shift();
        this._startWorker(next.data, next.resolve, next.reject);
      }
    });

    worker.on("error", (err) => {
      reject(err);
      this.activeWorkers--;
    });
  }
}
```

### Fix 4: Handle worker termination

```javascript
const { Worker } = require("node:worker_threads");

async function runWithTimeout(scriptPath, data, timeoutMs = 30000) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(scriptPath, { workerData: data });
    const timer = setTimeout(() => {
      worker.terminate();
      reject(new Error(`Worker timed out after ${timeoutMs}ms`));
    }, timeoutMs);

    worker.on("message", (result) => {
      clearTimeout(timer);
      resolve(result);
    });

    worker.on("error", (err) => {
      clearTimeout(timer);
      reject(err);
    });
  });
}
```

## Examples

```javascript
// Worker thread crash: unhandled error in worker.js
// worker.js:
// const data = JSON.parse(undefined); // throws in worker
// parentPort.postMessage("done");

// Fix: handle errors in the worker
// worker.js:
// try {
//   const data = JSON.parse(input);
//   parentPort.postMessage({ result: data });
// } catch (err) {
//   parentPort.postMessage({ error: err.message });
// }
```

## Related Errors

- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream destroyed before operation completes.
- [UnhandledPromiseRejection]({{< relref "/languages/javascript/node-unhandled-rejection" >}}) — unhandled promise rejection.
- [ERR_BUFFER_NOT_INITIALIZED]({{< relref "/languages/javascript/err-buffer-not-initialized" >}}) — buffer not initialized.
