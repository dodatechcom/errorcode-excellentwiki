#!/usr/bin/env python3
"""Generate ScyllaDB error pages to reach 100+ total."""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/scylladb'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(slug, title, desc, body):
    return f'''---
title: "[Solution] {title}"
description: "{desc}"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

{body}
'''

PAGES = [
    ("scylladb-schema-version-mismatch", "ScyllaDB Schema Version Mismatch", "How to fix ScyllaDB schema version mismatch errors", "## Common Causes\n\n- Schema agreement not reached\n- Node joined with different schema\n- Gossip protocol inconsistency\n\n## How to Fix\n\n```bash\nnodetool describecluster\n```\n\n## Examples\n\n```bash\nnodetool status\n```"),
    ("scylladb-view-error", "ScyllaDB Materialized View Error", "How to fix ScyllaDB materialized view errors", "## Common Causes\n- View creation fails with timeout\n- View data not consistent with base table\n- View causes write amplification\n\n## How to Fix\n\n```cql\nCREATE MATERIALIZED VIEW myview AS SELECT * FROM mytable WHERE id IS NOT NULL PRIMARY KEY (id);\n```\n\n## Examples\n\n```cql\nSELECT * FROM system_schema.materialized_views WHERE keyspace_name = 'myks';\n```"),
    ("scylladb-dc-error", "ScyllaDB Data Center Error", "How to fix ScyllaDB data center configuration errors", "## Common Causes\n- Node placed in wrong DC\n- DC not defined in topology\n- Snitch configuration wrong\n\n## How to Fix\n\n```bash\nnodetool status\n```\n\n## Examples\n\n```bash\ncat /etc/scylla/cassandra-rackdc.properties\n```"),
    ("scylladb-rack-error", "ScyllaDB Rack Error", "How to fix ScyllaDB rack configuration errors", "## Common Causes\n- All nodes in same rack (no fault tolerance)\n- Rack name mismatch\n- Gossip info inconsistent\n\n## How to Fix\n\n```properties\ndc=dc1\nrack=rack1\n```\n\n## Examples\n\n```bash\nnodetool describecluster | grep -i rack\n```"),
    ("scylladb-sstablesplit-error", "ScyllaDB SSTable Split Error", "How to fix ScyllaDB sstable split errors", "## Common Causes\n- SSTable too large to compact\n- Split producing too many files\n- Disk space insufficient\n\n## How to Fix\n\n```bash\nnodetool sstablesplit /var/lib/scylla/data/myks/mytable/\n```\n\n## Examples\n\n```bash\nls -la /var/lib/scylla/data/myks/mytable/\n```"),
    ("scylladb-incremental-backup-error", "ScyllaDB Incremental Backup Error", "How to fix ScyllaDB incremental backup errors", "## Common Causes\n- Incremental backup not enabled\n- Snapshot hardlinks broken\n- Backup target not writable\n\n## How to Fix\n\n```yaml\nincremental_backups: true\n```\n\n## Examples\n\n```bash\nnodetool snapshot myks -t mybackup\n```"),
    ("scylladb-scrub-error", "ScyllaDB Scrub Error", "How to fix ScyllaDB sstable scrub errors", "## Common Causes\n- Data corruption in SSTables\n- Scrub skipping too many rows\n- Scrub failing on corrupt partition\n\n## How to Fix\n\n```bash\nnodetool scrub myks mytable\n```\n\n## Examples\n\n```bash\nnodetool scrub myks mytable --skip-corrupted\n```"),
    ("scylladb-compact-error", "ScyllaDB Compact Error", "How to fix ScyllaDB compaction strategy errors", "## Common Causes\n- Wrong compaction strategy for workload\n- Compaction throughput too low\n- Tombstone accumulation\n\n## How to Fix\n\n```cql\nALTER TABLE mytable WITH compaction = {'class': 'LeveledCompactionStrategy'};\n```\n\n## Examples\n\n```cql\nSELECT * FROM system_schema.tables WHERE keyspace_name = 'myks';\n```"),
    ("scylladb-ccm-error", "ScyllaDB CCM Error", "How to fix ScyllaDB CCM (Cassandra Cluster Manager) errors", "## Common Causes\n- CCM not installed properly\n- Java version incompatible\n- Port conflicts between nodes\n\n## How to Fix\n\n```bash\nccm create mycluster -n 3 --scylla\n```\n\n## Examples\n\n```bash\nccm list\nccm status\n```"),
    ("scylladb-tracing-error", "ScyllaDB Query Tracing Error", "How to fix ScyllaDB query tracing errors", "## Common Causes\n- Tracing not enabled\n- Tracing session not found\n- Trace output incomplete\n\n## How to Fix\n\n```cql\nTRACING ON;\nSELECT * FROM mytable WHERE id = 1;\nTRACING OFF;\n```\n\n## Examples\n\n```cql\nSELECT * FROM system_traces.sessions WHERE client = inet '127.0.0.1';\n```"),
    ("scylladb-tombstone-overload-error", "ScyllaDB Tombstone Overload Error", "How to fix ScyllaDB tombstone overload errors", "## Common Causes\n- Large range scan hitting many tombstones\n- Delete pattern creating excessive tombstones\n- GC grace seconds too long\n\n## How to Fix\n\n```yaml\ntombstone_failure_threshold: 100000\ntombstone_warn_threshold: 1000\n```\n\n## Examples\n\n```cql\nTRACING ON; SELECT * FROM mytable WHERE status = 'deleted';\n```"),
    ("scylladb-per-partition-rate-limit-error", "ScyllaDB Per Partition Rate Limit Error", "How to fix ScyllaDB per partition rate limit errors", "## Common Causes\n- Hot partition exceeding rate limit\n- Write burst too large\n- Rate limit configuration too restrictive\n\n## How to Fix\n\n```yaml\nper_partition_rate_limit_bytes: 0\n```\n\n## Examples\n\n```bash\nnodetool tablestats myks.mytable | grep -i rate\n```"),
    ("scylladb-io-queue-full-error", "ScyllaDB IO Queue Full Error", "How to fix ScyllaDB IO queue full errors", "## Common Causes\n- Disk I/O saturated\n- Too many concurrent requests\n- IO scheduler misconfigured\n\n## How to Fix\n\n```yaml\ncompaction_throughput_mb_per_sec: 64\n```\n\n## Examples\n\n```bash\niostat -x 1\n```"),
    ("scylladb-seastar-reactor-stall-error", "ScyllaDB Seastar Reactor Stall Error", "How to fix ScyllaDB Seastar reactor stall errors", "## Common Causes\n- Reactor blocked for too long\n- Large allocation causing stall\n- External system call blocking reactor\n\n## How to Fix\n\n```yaml\nreactor-backend: epoll\n```\n\n## Examples\n\n```bash\njournalctl -u scylla-server | grep -i stall\n```"),
    ("scylladb-cpu-overload-error", "ScyllaDB CPU Overload Error", "How to fix ScyllaDB CPU overload errors", "## Common Causes\n- Query too CPU-intensive\n- Compaction using too many CPUs\n- Shard imbalance\n\n## How to Fix\n\n```yaml\ncpu_quota: 2\n```\n\n## Examples\n\n```bash\nnodetool tpstats | grep -i pending\n```"),
    ("scylladb-workload-prioritization-error", "ScyllaDB Workload Prioritization Error", "How to fix ScyllaDB workload prioritization errors", "## Common Causes\n- Workload classes not defined\n- Priority settings not applied\n- High priority workload starving low priority\n\n## How to Fix\n\n```cql\nALTER ROLE myrole WITH properties = {'workload': {'read': 10, 'write': 5}};\n```\n\n## Examples\n\n```bash\nnodetool listroles | grep workload\n```"),
    ("scylladb-redis-error", "ScyllaDB Redis Compatibility Error", "How to fix ScyllaDB Redis protocol compatibility errors", "## Common Causes\n- Redis command not supported\n- Keyspace not using Redis API\n- Protocol version mismatch\n\n## How to Fix\n\n```cql\nCREATE KEYSPACE redis_ks WITH replication = {'class': 'NetworkTopologyStrategy', 'dc1': 3};\n```\n\n## Examples\n\n```bash\nredis-cli -h scylla-host -p 6379 PING\n```"),
    ("scylladb-thrift-error", "ScyllaDB Thrift Error", "How to fix ScyllaDB Thrift protocol errors", "## Common Causes\n- Thrift port not enabled\n- Client using wrong protocol version\n- Thrift deprecated in newer versions\n\n## How to Fix\n\n```yaml\nrpc_port: 9160\n```\n\n## Examples\n\n```bash\nnodetool describecluster | grep -i thrift\n```"),
    ("scylladb-alternator-error", "ScyllaDB Alternator Error", "How to fix ScyllaDB Alternator (DynamoDB-compatible API) errors", "## Common Causes\n- Alternator not enabled\n- DynamoDB API call not supported\n- Throughput exceeded\n\n## How to Fix\n\n```yaml\nalternator_port: 8000\nalternator_write_isolation: use_lwt_if_needed\n```\n\n## Examples\n\n```bash\naws dynamodb list-tables --endpoint-url http://scylla-host:8000\n```"),
    ("scylladb-node-decommission-error", "ScyllaDB Node Decommission Error", "How to fix ScyllaDB node decommission errors", "## Common Causes\n- Not enough nodes remaining after decommission\n- Decommission data streaming stuck\n- Gossip not consistent across cluster\n\n## How to Fix\n\n```bash\nnodetool decommission\n```\n\n## Examples\n\n```bash\nnodetool status\n```"),
    ("scylladb-bootstrap-error", "ScyllaDB Node Bootstrap Error", "How to fix ScyllaDB node bootstrap errors", "## Common Causes\n- Bootstrap token range overlap\n- Existing nodes cannot stream to new node\n- Disk space insufficient\n\n## How to Fix\n\n```bash\nnodetool status\n```\n\n## Examples\n\n```bash\njournalctl -u scylla-server | grep -i bootstrap\n```"),
    ("scylladb-removenode-error", "ScyllaDB Remove Node Error", "How to fix ScyllaDB node removal errors", "## Common Causes\n- Node not fully dead\n- Too many nodes already removed\n- Token ownership mismatch\n\n## How to Fix\n\n```bash\nnodetool removenode UUID_OF_DEAD_NODE\n```\n\n## Examples\n\n```bash\nnodetool status | grep DN\n```"),
    ("scylladb-rebuild-error", "ScyllaDB Rebuild Error", "How to fix ScyllaDB node rebuild errors", "## Common Causes\n- Source node unreachable\n- Keyspace replication factor too high\n- Network bandwidth saturated\n\n## How to Fix\n\n```bash\nnodetool rebuild myks\n```\n\n## Examples\n\n```bash\nnodetool rebuild myks -dc dc1\n```"),
    ("scylladb-scylla-manager-error", "ScyllaDB Manager Error", "How to fix ScyllaDB Manager errors", "## Common Causes\n- Manager agent not running\n- Manager cannot connect to Scylla\n- Repair task failing\n\n## How to Fix\n\n```bash\nsystemctl status scylla-manager-agent\n```\n\n## Examples\n\n```bash\nsctool status\n```"),
    ("scylladb-schema-agreement-error", "ScyllaDB Schema Agreement Error", "How to fix ScyllaDB schema agreement errors", "## Common Causes\n- Schema version mismatch between nodes\n- Gossip protocol failure\n- Node trying to apply schema change while others are down\n\n## How to Fix\n\n```bash\nnodetool describecluster\n```\n\n## Examples\n\n```bash\nnodetool status\n```"),
    ("scylladb-read-repair-error", "ScyllaDB Read Repair Error", "How to fix ScyllaDB read repair errors", "## Common Causes\n- Read repair too aggressive\n- Consistency level mismatch\n- Hinted handoff not working\n\n## How to Fix\n\n```yaml\nread_repair_chance: 0.0\ndclocal_read_repair_chance: 0.0\n```\n\n## Examples\n\n```cql\nSELECT * FROM mytable WHERE id = 1 CONSISTENCY LOCAL_QUORUM;\n```"),
    ("scylladb-hinted-handoff-error", "ScyllaDB Hinted Handoff Error", "How to fix ScyllaDB hinted handoff errors", "## Common Causes\n- Hint directory full\n- Target node unreachable\n- Hint window expired\n\n## How to Fix\n\n```yaml\nmax_hint_window_in_ms: 10800000\nhinted_handoff_throttle_in_kb: 1024\n```\n\n## Examples\n\n```bash\nls /var/lib/scylla/hints/\n```"),
    ("scylladb-commitlog-archive-error", "ScyllaDB Commitlog Archive Error", "How to fix ScyllaDB commitlog archival errors", "## Common Causes\n- Archive directory not writable\n- Archive command failing\n- Disk full in archive location\n\n## How to Fix\n\n```yaml\ncommitlog_archive_command: /usr/bin/cp %c /archive/%f\n```\n\n## Examples\n\n```bash\nls -la /var/lib/scylla/commitlog/\n```"),
    ("scylladb-uptime-error", "ScyllaDB Uptime Check Error", "How to fix ScyllaDB uptime monitoring errors", "## Common Causes\n- Scylla server restarting frequently\n- OOM killer terminating process\n- Configuration error causing crash loop\n\n## How to Fix\n\n```bash\nnodetool info | grep -i uptime\n```\n\n## Examples\n\n```bash\njournalctl -u scylla-server --since \"1 hour ago\" | grep -i restart\n```"),
    ("scylladb-sstable-metadata-error", "ScyllaDB SSTable Metadata Error", "How to fix ScyllaDB SSTable metadata errors", "## Common Causes\n- Metadata file corrupted\n- SSTable format version mismatch\n- Incomplete SSTable write\n\n## How to Fix\n\n```bash\nsstablemetadata /var/lib/scylla/data/myks/mytable/mc-1-big-Data.db\n```\n\n## Examples\n\n```bash\nls /var/lib/scylla/data/myks/mytable/\n```"),
]

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        continue
    path = os.path.join(BASE, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(make_page(slug, title, desc, body))
    count += 1

print(f'Generated {count} new ScyllaDB pages (total: {len(EXISTING) + count})')
