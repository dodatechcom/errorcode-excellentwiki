---
title: "[Solution] Systemd Dependency Cycle Detected Error — How to Fix"
description: "Fix systemd dependency cycle errors by analyzing unit dependencies, breaking circular references, using Wants instead of Requires, and restructuring service ordering"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Dependency Cycle Detected Error

This error means systemd detected a circular dependency between two or more units, where each unit requires the other to start first. Systemd cannot resolve this cycle and fails to start the affected units.

## Why It Happens

- Two services both have `Requires=` or `Wants=` pointing at each other
- A `Before=` directive on one unit conflicts with an `After=` directive on another
- `WantedBy=` and `Requires=` create an indirect circular path
- Socket-activated services create a cycle with their parent service
- A mount unit depends on a service that depends on the mount
- Timer units activate services that restart the timer

## Common Error Messages

```
systemd[1]: myapp.service: Found dependency on postgresql.service
systemd[1]: postgresql.service: Found dependency on myapp.service
systemd[1]: Requested transaction generates an infinite loop. Aborting.
```

```
systemd[1]: Transaction is destructive.
```

```
systemd[1]: myapp.service: Dependency cycle detected.
```

## How to Fix It

### 1. Visualize the Dependency Graph

```bash
# Generate a dependency graph for the problematic unit
systemd-analyze dot myapp.service | dot -Tpng > deps.png

# Check the full dependency tree
systemctl list-dependencies myapp.service

# Find the cycle
systemd-analyze verify myapp.service
```

### 2. Remove the Circular Dependency

```bash
# Check both unit files
systemctl cat myapp.service
systemctl cat postgresql.service

# Look for Requires=, Wants=, After=, Before= directives
```

```ini
# WRONG: Both require each other
# myapp.service:
Requires=postgresql.service
After=postgresql.service

# postgresql.service:
Requires=myapp.service     # <- This creates the cycle
After=myapp.service

# RIGHT: Use Wants= and make postgresql independent
# myapp.service:
Wants=postgresql.service
After=postgresql.service
Requires=postgresql.service

# postgresql.service: (no reference to myapp)
After=network.target
```

### 3. Use Wants Instead of Requires

```ini
# Instead of hard requirements that can create cycles:
[Service]
Requires=myapp.service     # Creates hard dependency

# Use soft dependencies:
[Service]
Wants=myapp.service        # Fails gracefully if not available
After=myapp.service
```

### 4. Separate Socket Activation from Service Dependency

```ini
# WRONG: Service requires its own socket, creating a cycle
[Service]
Requires=myapp.socket
After=myapp.socket

# RIGHT: Use socket activation properly
# myapp.service:
[Service]
ExecStart=/usr/bin/myapp
# The socket is activated automatically, no explicit Requires needed

# myapp.socket:
[Socket]
ListenStream=8080
Service=myapp.service
```

### 5. Break Cycles with Conflicts or Target Separation

```ini
# Use a target to break the cycle
# Instead of services referencing each other:
[Service]
Requires=myapp.target
After=myapp.target

# myapp.target:
[Unit]
Description=My App Target
After=postgresql.service redis.service
Requires=postgresql.service
Wants=redis.service
```

## Common Scenarios

- **Web app and database**: The web app requires the database, and the database initialization script requires the web app to validate configuration. Move the validation to a separate one-shot unit.
- **Monitoring agent and service**: The monitoring agent requires the service to check health, and the service requires the agent for configuration. Use `Wants=` instead of `Requires=` on the agent side.
- **Socket-activated service**: The service unit has `Requires=myapp.socket` but the socket also has `Wants=myapp.service`. Remove the explicit `Requires` from the service — socket activation handles this.

## Prevent It

- Always check for cycles with `systemd-analyze verify` after editing unit files
- Prefer `Wants=` over `Requires=` unless hard dependency is truly needed
- Use `systemd-analyze dot | dot -Tpng` to visually inspect dependency graphs

## Related Pages

- [Systemd Unit Failed](/tools/systemd/systemd-unit-failed)
- [Systemd Masked Unit](/tools/systemd/systemd-masked-unit)
- [Systemd Dependency Cycle](/tools/systemd/systemd-dependency-cycle)
