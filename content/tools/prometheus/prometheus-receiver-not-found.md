---
title: "[Solution] Prometheus Alertmanager Receiver Not Found"
description: "How to fix Alertmanager receiver not found errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Receiver name in route does not match any defined receiver
- Typo in receiver name
- Receiver defined but not referenced in any route
- Receiver deleted but route still references it

## How to Fix

Check receiver names:

```yaml
receivers:
  - name: 'slack-notifications'
    slack_configs:
      - channel: '#alerts'
```

Verify route references existing receiver:

```yaml
route:
  receiver: 'slack-notifications'
```

List configured receivers:

```bash
amtool --alertmanager.url=http://localhost:9093 config show --format=json | jq '.route.receiver'
```

## Examples

```bash
# List receivers
amtool --alertmanager.url=http://localhost:9093 config show | grep "receiver:"

# Check receiver config
amtool check-config /etc/alertmanager/alertmanager.yml

# View all receivers
curl http://localhost:9093/api/v2/status | jq '.config.original.receivers[].name'
```
