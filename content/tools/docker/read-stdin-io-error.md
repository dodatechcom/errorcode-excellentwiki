---
title: "[Solution] Docker Read /dev/stdin: I/O Error — read /dev/stdin: input/output error"
description: "Fix Docker stdin I/O error. Resolve interactive container input issues."
tools: ["docker"]
error-types: ["tool-error"]
severities: ["error"]
weight: 7
---

# read /dev/stdin: input/output error

This error occurs when a container tries to read from standard input but encounters an I/O error. This commonly happens with interactive containers or when stdin is not properly attached.

## Common Causes

- Container running without -i (interactive) flag
- stdin not properly attached
- Process expecting input but none provided
- Docker not allocating pseudo-TTY
- Container running in background without stdin

## How to Fix

### Run with Interactive Mode

```bash
docker run -it my-image /bin/sh
# -i = interactive (keep stdin open)
# -t = pseudo-TTY (allocate terminal)
```

### Run with Detached stdin

```bash
docker run -i my-image
```

### Use docker exec with Interactive

```bash
docker exec -it <container> /bin/sh
```

### Provide Input via Pipe

```bash
echo "input" | docker run -i my-image
```

### Run Non-Interactive

```bash
docker run -d my-image
# Container runs in background without stdin
```

## Examples

```bash
# Example 1: Interactive shell
docker run -it ubuntu /bin/bash
# -i keeps stdin open, -t allocates TTY

# Example 2: Pipe input
docker run -i my-image cat <<< "hello"
# Or
echo "hello" | docker run -i my-image cat

# Example 3: Exec into running container
docker exec -it my-container /bin/sh
```

## Related Errors

- [Docker exec error]({{< relref "/tools/docker/docker-exec-error" >}}) — related error
- [Container is not running]({{< relref "/tools/docker/container-is-not-running" >}}) — related error
