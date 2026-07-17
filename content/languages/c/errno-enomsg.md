---
title: "[Solution] C errno ENOMSG — No message of desired type Fix"
description: "Fix C ENOMSG (No message of desired type) by checking message queue types and using appropriate receive flags."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno ENOMSG — No message of desired type Fix

When `msgrcv()` is called with a specific message type that does not exist in the message queue, and the `MSG_NOERROR` flag is not set or the queue is empty for that type, the call fails and sets `errno` to `ENOMSG`. This is specific to System V message queues.

## Common Causes

- The message queue does not contain a message matching the requested type.
- The requested message type has already been consumed by another process.
- Using `msgrcv()` with a positive type to receive only messages of that specific type.
- The message queue was created but no messages of the expected type were sent.

## How to Fix

Check if messages are available before receiving, and handle the `ENOMSG` case gracefully.

```c
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    key_t key = ftok("/tmp", 'A');
    int msqid = msgget(key, IPC_CREAT | 0644);

    struct {
        long mtype;
        char mtext[256];
    } msg;

    ssize_t rc = msgrcv(msqid, &msg, sizeof(msg.mtext), 1, IPC_NOWAIT);
    if (rc == -1) {
        if (errno == ENOMSG) {
            fprintf(stderr, "No message of type 1 available\n");
        } else {
            fprintf(stderr, "msgrcv failed: %s\n", strerror(errno));
        }
        return 1;
    }
    printf("Received: %s\n", msg.mtext);
    return 0;
}
```

## Examples

Receiving from an empty message queue with a specific type:

```c
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int msqid = msgget(IPC_PRIVATE, IPC_CREAT | 0644);
    if (msqid == -1) { perror("msgget"); return 1; }

    // Queue is empty — trying to receive type 5
    struct { long mtype; char mtext[256]; } msg;
    if (msgrcv(msqid, &msg, sizeof(msg.mtext), 5, IPC_NOWAIT) == -1) {
        if (errno == ENOMSG) {
            fprintf(stderr, "No message of type 5 (errno %d)\n", errno);
        }
    }
    msgctl(msqid, IPC_RMID, NULL);
    return 0;
}
```

## Related Errors

- [errno-42 ENOMSG](/languages/c/errno-enomsg/) — no message of desired type (numeric).
- [errno-11 EAGAIN](/languages/c/errno-enomsg/) — resource unavailable, try again.
- [errno-22 EINVAL](/languages/c/errno-enomsg/) — invalid argument.
