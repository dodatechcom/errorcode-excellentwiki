---
title: "[Solution] Prometheus Alertmanager WeChat Receiver Error"
description: "How to fix Alertmanager WeChat notification errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Invalid WeChat Corp ID or agent secret
- WeChat API token expired
- Party or tag IDs not found
- Message template rendering error

## How to Fix

Configure WeChat receiver:

```yaml
receivers:
  - name: 'wechat'
    wechat_configs:
      - corp_id: 'your-corp-id'
        to_party: '1'
        to_tag: 'tag1'
        agent_id: 'your-agent-id'
        api_secret: 'your-api-secret'
        message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Test WeChat API token
curl "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=YOUR_ID&corpsecret=YOUR_SECRET"

# Send test message
curl -X POST "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=YOUR_TOKEN"   -d '{"touser":"@all","msgtype":"text","agentid":1,"text":{"content":"Test alert"}}'
```
