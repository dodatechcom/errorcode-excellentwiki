---
title: "[Solution] C errno EBADMSG — Not a STREAMS message Fix"
description: "Fix C EBADMSG (Not a STREAMS message) by validating STREAMS message format and checking control data."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
tags: ["ebadmsg", "bad-streams-message", "streams", "putmsg", "getmsg"]
weight: 5
---

# [Solution] C errno EBADMSG — Not a STREAMS message Fix

When `getmsg()`, `getpmsg()`, or a STREAMS ioctl receives a message that does not have a valid format, or when a control message is expected but not present, the call sets `errno` to `EBADMSG`. This error indicates corrupted or unexpected STREAMS message data.

## Common Causes

- The message received via `getmsg()` has invalid control information.
- A STREAMS module sent a malformed or unexpected message type.
- The message was corrupted during transit through the STREAMS pipeline.
- An ioctl operation received unexpected data from the stream head.

## How to Fix

Validate STREAMS messages before processing them. Check that control and data portions are well-formed.

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main(void) {
    struct strbuf ctl, data;
    char cbuf[128], dbuf[1024];
    ctl.buf = cbuf; ctl.maxlen = sizeof(cbuf);
    data.buf = dbuf; data.maxlen = sizeof(dbuf);
    int flags = 0;

    int ret = getmsg(fd, &ctl, &data, &flags);
    if (ret == -1) {
        if (errno == EBADMSG) {
            fprintf(stderr, "Received invalid STREAMS message\n");
        } else {
            fprintf(stderr, "getmsg failed: %s\n", strerror(errno));
        }
        return 1;
    }
    return 0;
}
```

## Examples

Receiving a bad STREAMS message:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    // If the stream delivers a malformed control message
    struct strbuf ctl;
    char cbuf[64];
    ctl.buf = cbuf; ctl.maxlen = sizeof(cbuf);

    int ret = getpmsg(fd, &ctl, NULL, NULL);
    if (ret == -1 && errno == EBADMSG) {
        fprintf(stderr, "Bad STREAMS message received (errno %d)\n", errno);
    }
    return 0;
}
```

## Related Errors

- [errno-45 EBADMSG](/languages/c/errno-ebadmsg/) — not a STREAMS message (numeric).
- [errno-22 EINVAL](/languages/c/errno-ebadmsg/) — invalid argument.
- [errno-44 ERMSR]({{< relref "/languages/c/errno-ermsr" >}}) — no STREAMS resources.
