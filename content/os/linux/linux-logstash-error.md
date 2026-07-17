---
title: "[Solution] Linux logstash Pipeline Error — Fix"
description: "Fix Linux 'logstash: pipeline error' and Logstash failures. Resolve input, filter, and output plugin errors in Logstash pipelines."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["logstash", "pipeline-error", "elk", "ingest", "grok", "filter"]
weight: 5
---

# Linux: logstash: pipeline error

The `logstash: pipeline error` message means Logstash encountered a problem processing events through its pipeline. This can appear as filter parsing errors, output delivery failures, or pipeline startup errors. Pipeline errors prevent log data from being indexed into Elasticsearch or sent to other outputs.

## What This Error Means

Logstash processes data through a three-stage pipeline: Input → Filter → Output. Each stage uses plugins. A pipeline error means an event failed processing at one of these stages. Common errors include Grok parse failures (filter), connection refused (output), or codec errors (input). The pipeline continues processing but drops or tags failed events.

## Common Causes

- Grok pattern doesn't match the log format
- Elasticsearch output connection refused
- Mutate/filter plugin configuration errors
- Input plugin misconfiguration (wrong port, codec)
- Insufficient memory for pipeline buffers
- Elasticsearch index mapping conflicts
- DNS resolution failure for output hosts
- TLS/certificate issues with Elasticsearch output

## How to Fix

### 1. Check Logstash Service Status

```bash
# Check Logstash status
sudo systemctl status logstash

# Start Logstash if not running
sudo systemctl start logstash

# Check Logstash logs
sudo tail -f /var/log/logstash/logstash-plain.log
sudo journalctl -u logstash --since "10 minutes ago"
```

### 2. Check Pipeline Configuration

```bash
# Test configuration syntax
sudo /usr/share/logstash/bin/logstash --config.test_and_exit -f /etc/logstash/conf.d/

# Test specific configuration file
sudo /usr/share/logstash/bin/logstash --config.test_and_exit -f /etc/logstash/conf.d/myconfig.conf

# Check for syntax errors in config
sudo /usr/share/logstash/bin/logstash --config.reload.automatic -f /etc/logstash/conf.d/
```

### 3. Debug Grok Parse Failures

```bash
# Check for _grokparsefailure tags
curl -s "http://localhost:9200/logstash-*/_search" \
  -H "Content-Type: application/json" \
  -d '{"query": {"match": {"tags": "_grokparsefailure"}}}'

# Test grok pattern
echo '2025-01-15 10:30:00 ERROR Something failed' | \
  /usr/share/logstash/bin/logstash -e 'filter { grok { match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:text}" } } }'
```

### 4. Fix Elasticsearch Output

```bash
# Check Elasticsearch connectivity
curl http://localhost:9200/_cluster/health

# Check Logstash output configuration
cat /etc/logstash/conf.d/output.conf

# Common output config:
# output {
#   elasticsearch {
#     hosts => ["http://localhost:9200"]
#     index => "logs-%{+YYYY.MM.dd}"
#   }
# }

# Test Logstash pipeline output
echo "test line" | /usr/share/logstash/bin/logstash -e 'input { stdin {} } output { stdout {} }'
```

### 5. Fix Input Plugin Issues

```bash
# Check if Logstash is listening on expected ports
sudo ss -tlnp | grep logstash

# Check input configuration
cat /etc/logstash/conf.d/input.conf

# Common input config:
# input {
#   beats {
#     port => 5044
#   }
#   tcp {
#     port => 5000
#     codec => json_lines
#   }
# }
```

### 6. Increase JVM Heap for Logstash

```bash
# Check current heap settings
cat /etc/logstash/jvm.options | grep -i heap

# Increase heap (set to 50% of available RAM)
sudo nano /etc/logstash/jvm.options
# -Xms4g
# -Xmx4g

# Restart Logstash
sudo systemctl restart logstash
```

### 7. Enable Dead Letter Queue

For events that fail processing:

```bash
# Enable DLQ in logstash.yml
sudo nano /etc/logstash/logstash.yml
# dead_letter_queue.enable: true
# dead_letter_queue.max_bytes: 1024mb

# Check DLQ events
sudo /usr/share/logstash/bin/logstash-plugin install logstash-input-dead_letter_queue
```

### 8. Monitor Pipeline Performance

```bash
# Check pipeline stats via API
curl -s http://localhost:9600/_node/stats/pipelines | jq .

# Check JVM stats
curl -s http://localhost:9600/_node/stats/jvm | jq .

# Monitor queue size
curl -s http://localhost:9600/_node/stats/process | jq .
```

## Examples

```bash
$ sudo tail -f /var/log/logstash/logstash-plain.log
[2025-01-15T10:30:00,123][WARN ][logstash.filters.grok] \
  Failed parsing with grok patterns {:exception=>"No pattern matches", :field=>"message"}

# Fix: update grok pattern to match actual log format
$ sudo nano /etc/logstash/conf.d/filter.conf
# Change: %{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:message}
# To: %{SYSLOGTIMESTAMP:timestamp} %{SYSLOGPROG:program} %{GREEDYDATA:message}

$ sudo systemctl restart logstash
$ sudo tail -f /var/log/logstash/logstash-plain.log
# No more parse failures
```

```bash
$ curl -s http://localhost:9200/_cat/indices?v | grep logstash
health status index                              pri rep docs.count
yellow open   logstash-2025.01.15                 1   1      12345

$ curl -s "http://localhost:9200/logstash-*/_search" \
  -H "Content-Type: application/json" \
  -d '{"query": {"match": {"tags": "_grokparsefailure"}}, "size": 0}'
{"hits":{"total":{"value":42}}
# 42 failed events — update grok pattern
```

## Related Errors

- [Elasticsearch cluster error]({{< relref "/os/linux/linux-elasticsearch-error" >}}) — Elasticsearch storage issues
- [Prometheus scrape error]({{< relref "/os/linux/linux-prometheus-error" >}}) — Monitoring pipeline issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Network connectivity issues
