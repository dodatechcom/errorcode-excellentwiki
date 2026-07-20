---
title: "[Solution] Docker Logs Error — failed to get logs"
description: "Fix Docker 'failed to get logs' error. Retrieve container logs and resolve logging driver issues."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "docker"
tags: ["docker", "containers", "logs", "logging", "debugging"]
severity: "error"
weight: 6
---

# ERROR: failed to get logs

## Error Message

```
Error: failed to get logs for container myapp: configured logging driver does not support reading

Error response from daemon: No such container: myapp
```

This error occurs when `docker logs` cannot retrieve logs from a container. The container may not exist, the logging driver may not support reading, or the logs may have been rotated and removed.

## Common Causes

- The container does not exist or has been removed
- The logging driver is set to a non-readable driver like `journald` or `fluentd`
- The container was started with `--log-driver none` which discards all logs
- Log rotation settings removed older log data
- The container is still starting and has not written any output yet

## Solutions

### Solution 1: Verify the Container Exists and Is Running

Check that the container is present and running before attempting to fetch logs. A stopped container can still provide logs if it has not been removed.

```bash
docker ps -a
docker logs myapp
```

### Solution 2: Use the json-file Driver for Log Access

The `json-file` driver is the default and supports `docker logs`. Recreate the container with this driver if another was configured.

```bash
docker rm -f myapp
docker run -d --name myapp   --log-driver json-file   --log-opt max-size=10m   --log-opt max-file=3   myimage
docker logs myapp
```

### Solution 3: Access Logs on Disk Directly

The `json-file` driver stores logs in the Docker data directory. You can read them directly even if `docker logs` fails.

```bash
# Find the container ID
docker inspect myapp --format '{{.Id}}'
# Read the log file
cat /var/lib/docker/containers/<container-id>/<container-id>-json.log
```

### Solution 4: Use docker events for Real-Time Monitoring

If `docker logs` does not work, `docker events` captures container lifecycle events in real time. Combine with `docker exec` to tail application-level logs.

```bash
docker events --filter container=myapp &
docker exec myapp tail -f /var/log/app.log
```

## Prevention Tips

- Stick with the `json-file` logging driver for local development where `docker logs` is essential
- Configure log rotation with `max-size` and `max-file` to prevent disk fill
- Use an external logging stack (ELK, Loki) for production log aggregation
- Store application logs in shared volumes for persistence beyond container lifecycle

## Related Errors

- [Container Not Running]({{< relref "/tools/docker/container-is-not-running" >}}) — container must be running
- [Docker Socket Permission]({{< relref "/tools/docker/docker-socket-permission" >}}) — permission denied on docker.sock
