---
title: "[Solution] C errno EBADMSG — Bad message Fix"
description: "Fix C EBADMSG (Bad message) by validating message format, checking control data, and handling STREAMS message errors."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EBADMSG — Bad message Fix

When a STREAMS message received via `getmsg()` or `getpmsg()` has an invalid format, unexpected type, or corrupted control data, the operation fails and sets `errno` to `EBADMSG`. This indicates the message does not conform to the expected STREAMS protocol.

## Common Causes

- The message received has an unexpected control message type.
- The message format is corrupted or truncated.
- A STREAMS module sent a protocol-violating message.
- The message queue contains a malformed System V message.

## How to Fix

Validate message types and control data before processing. Discard or log invalid messages.

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct strbuf ctl, data;
    char cbuf[128], dbuf[1024];
    ctl.buf = cbuf; ctl.maxlen = sizeof(cbuf);
    data.buf = dbuf; data.maxlen = sizeof(dbuf);
    int flags = 0;

    int ret = getmsg(stream_fd, &ctl, &data, &flags);
    if (ret == -1) {
        if (errno == EBADMSG) {
            fprintf(stderr, "Bad message received — discarding\n");
            // Optionally log or report the error
        } else {
            perror("getmsg");
        }
        return 1;
    }

    // Validate control data before processing
    if (ctl.len > 0 && ctl.len <= ctl.maxlen) {
        // Process valid message
    }
    return 0;
}
```

## Examples

Receiving a corrupted STREAMS message:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    struct strbuf data;
    char buf[256];
    data.buf = buf;
    data.maxlen = sizeof(buf);
    int flags = 0;

    int ret = getpmsg(stream_fd, NULL, &data, &flags);
    if (ret == -1 && errno == EBADMSG) {
        fprintf(stderr, "Received bad message on stream (errno %d)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-45 EBADMSG]({{< relref "/languages/c/errno-ebadmsg" >}}) — not a STREAMS message.
- [errno-22 EINVAL](/languages/c/errno-eBADMSG-2/) — invalid argument.
- [errno-42 ENOMSG]({{< relref "/languages/c/errno-enomsg" >}}) — no message of desired type.
