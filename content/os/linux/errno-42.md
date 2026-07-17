---
title: "[Solution] Linux ENOMSG (errno 42) — No Message of Desired Type Fix"
description: "Fix Linux ENOMSG (errno 42) No message of desired type error. Solutions for IPC and message queue issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENOMSG (errno 42) — No Message of Desired Type

ENOMSG (errno 42) means the specified message type does not exist in the message queue. This error occurs when using `msgrcv()` with a message type that has no matching messages available. It is distinct from EAGAIN (errno 7) because ENOMSG specifically indicates no message of the requested type exists.

## Common Causes

- The message queue has no messages matching the requested type
- The message type filter is too restrictive
- The sender has not yet placed messages in the queue
- Messages were consumed by other receivers

## How to Fix ENOMSG

### 1. Check Message Queue Status

Inspect the current state of the message queue:

```bash
ipcs -q
ipcmid <msqid>
```

### 2. Use Type 0 for Any Message

Receive any message regardless of type:

```c
msgrcv(msqid, &msg, sizeof(msg.mtext), 0, 0);
```

### 3. Send a Message First

Ensure messages are in the queue before receiving:

```bash
# In another process or terminal
ipcrm -q <msqid>
```

### 4. Remove MSG_NOERROR Flag

The `MSG_NOERROR` flag truncates messages; remove it to see full messages:

```c
msgrcv(msqid, &msg, sizeof(msg.mtext), type, 0);
```

## Verification

After ensuring messages exist in the queue, confirm reception:

```bash
ipcs -q -t
```

## Related Error Codes

- [EAGAIN (errno 7)](/os/linux/errno-7/) — Resource temporarily unavailable
- [EIDRM (errno 43)](/os/linux/errno-43/) — Identifier removed
- [EACCES (errno 13)](/os/linux/errno-13/) — Permission denied
