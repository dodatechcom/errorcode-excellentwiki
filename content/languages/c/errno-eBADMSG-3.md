---
title: "[Solution] C errno EBADMSG — Bad message (variant) Fix"
description: "Fix C EBADMSG (Bad message variant) by validating message integrity, checking STREAMS data, and handling malformed input."
languages: ["c"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# [Solution] C errno EBADMSG — Bad message (variant) Fix

An alternate manifestation of `EBADMSG` occurring when `ioctl(I_FLUSH)` or other STREAMS control operations receive a message that does not match the expected protocol or format. The message type or content is invalid for the requested operation.

## Common Causes

- A STREAMS ioctl received a message with an unexpected type field.
- The control message length or format does not match the protocol specification.
- A flush operation was requested on a stream with no pending messages.
- The message was corrupted during kernel processing.

## How to Fix

Validate messages before processing. Use `I_PEEK` to inspect messages without consuming them.

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int peek_and_validate(int fd) {
    struct strioctl ic;
    struct strpeek peek;

    ic.ic_cmd = I_PEEK;
    ic.ic_len = sizeof(peek);
    ic.ic_dp = (char *)&peek;

    if (ioctl(fd, I_STR, &ic) == -1) {
        if (errno == EBADMSG) {
            fprintf(stderr, "Bad message on stream — discarding\n");
            return -1;
        }
        return -1;
    }

    // Validate message type before processing
    if (peek ctl.len == 0 && peek ctl.type == 0) {
        return 0;  // Empty — no action needed
    }
    return 1;
}

int main(void) {
    if (peek_and_validate(stream_fd) == -1) {
        fprintf(stderr, "Message validation failed\n");
    }
    return 0;
}
```

## Examples

Flushing a stream with invalid message state:

```c
#include <stropts.h>
#include <stdio.h>
#include <errno.h>

int main(void) {
    if (ioctl(stream_fd, I_FLUSH, FLUSHR) == -1) {
        if (errno == EBADMSG) {
            fprintf(stderr, "Bad message during flush (errno %d)\n", errno);
        }
    }
    return 0;
}
```

## Related Errors

- [errno-45 EBADMSG]({{< relref "/languages/c/errno-ebadmsg" >}}) — not a STREAMS message.
- [errno-45 EBADMSG]({{< relref "/languages/c/errno-eBADMSG-2" >}}) — bad message (variant 2).
- [errno-22 EINVAL](/languages/c/errno-eBADMSG-3/) — invalid argument.
