---
title: "[Solution] C errno 42 ENOMSG — No message of desired type"
description: "Fix C errno 42 ENOMSG (No message of desired type) by using correct message types, checking IPC permissions, or using appropriate flags."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno 42 ENOMSG — No message of desired type

No message of desired type occurs when a system call fails and sets `errno` to 42. This error indicates that the requested operation cannot be performed due to the specific condition described by ENOMSG.

## Common Causes

- Receiving a message with an unexpected type on a System V message queue.
- Using msgrcv() with a type that doesn't exist in the queue.
- Trying to receive a message when the queue is empty.
- Incorrect message queue permissions.

## How to Fix

```c
#include <sys/msg.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    int msqid = msgget(IPC_PRIVATE, 0600);
    if (msqid == -1) {
        perror("msgget");
        return 1;
    }
    struct {
        long mtype;
        char mtext[100];
    } msg;
    ssize_t n = msgrcv(msqid, &msg, sizeof(msg.mtext), 0, IPC_NOWAIT);
    if (n == -1 && errno == ENOMSG) {
        fprintf(stderr, "No message of desired type\n");
    }
    msgctl(msqid, IPC_RMID, NULL);
    return 0;
}
```

## Examples

```c
#include <sys/msg.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    int msqid = msgget(IPC_PRIVATE, 0600);
    if (msqid == -1) {
        perror("msgget");
        return 1;
    }
    // Send a message first
    struct {
        long mtype;
        char mtext[100];
    } msg = {1, "test"};
    msgsnd(msqid, &msg, strlen(msg.mtext), 0);
    // Now receive it
    ssize_t n = msgrcv(msqid, &msg, sizeof(msg.mtext), 1, 0);
    if (n == -1) {
        perror("msgrcv");
    }
    msgctl(msqid, IPC_RMID, NULL);
    return 0;
}
```

## Related Errors

- [errno-11 EAGAIN]({{< relref "/languages/c/errno-11" >}}) — resource unavailable.
- [errno-42 ENOMSG]({{< relref "/languages/c/errno-42" >}}) — no message of desired type (self).
- [errno-13 EACCES]({{< relref "/languages/c/errno-13" >}}) — permission denied.
