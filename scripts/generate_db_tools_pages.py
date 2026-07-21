#!/usr/bin/env python3
"""Generate pages for 5 DB tool sections to reach 100+ pages each."""

import os
import re
import json
from pathlib import Path

BASE = Path("/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools")

TOOLS_DIRS = {
    "sqlserver": BASE / "sqlserver",
    "oracle": BASE / "oracle",
    "cassandra": BASE / "cassandra",
    "cockroachdb": BASE / "cockroachdb",
    "dynamodb": BASE / "dynamodb",
}


def slugify(name):
    """Convert a topic name into a slug like 'server-not-found'."""
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def get_existing_slugs(tool_dir):
    """Return set of existing slug filenames (without .md)."""
    slugs = set()
    if not tool_dir.exists():
        return slugs
    for f in tool_dir.iterdir():
        if f.suffix == ".md" and f.stem != "_index":
            slugs.add(f.stem)
    return slugs


def make_title_raw(name):
    """Return a presentable title string from the raw topic name."""
    return name.strip().title()


def fix_relref(path):
    """Return relref shortcode string, ensuring NO em dashes in the line."""
    return f'({{{{< relref "{path}" >}}}})'


# ---------------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------------

TOOLS = {
    "sqlserver": {
        "tool_name": "sqlserver",
        "display": "SQL Server",
        "topic_key": "sqlserver",
        "topics": [
            "server not found", "connection failed", "login failed",
            "user not found", "database not found", "database already exists",
            "table not found", "column not found", "primary key not found",
            "foreign key violation", "unique constraint violation",
            "check constraint", "null insert", "cannot insert duplicate",
            "deadlock victim", "lock request timeout", "wait resource",
            "transaction log full", "log file full", "data file full",
            "tempdb full", "out of memory", "insufficient memory",
            "maximum degree parallelism", "grant denied", "permission denied",
            "object access denied", "execute permission", "select permission",
            "insert permission", "update permission", "delete permission",
            "server principal", "database principal", "schema not found",
            "schema owner", "ALTER TABLE", "ALTER DATABASE", "DDL statement",
            "DML statement", "TRUNCATE table", "DROP table", "clustered index",
            "nonclustered index", "index rebuild", "index reorganize",
            "index fragmentation", "fill factor", "page split",
            "statistics update", "outdated statistics", "missing index",
            "index recommendation", "query timeout", "XML parsing",
            "XQuery error", "FOR XML path", "FOR JSON", "JSON_VALUE",
            "JSON_QUERY", "OPENJSON", "OPENXML", "stored procedure",
            "parameter sniffing", "recompile", "WITH RECOMPILE",
            "OPTION RECOMPILE", "cursor error", "cursor fetch", "cursor close",
            "deallocate cursor", "trigger error", "DML trigger",
            "DDL trigger", "instead of trigger", "after trigger",
            "recursive trigger", "nested trigger", "function not found",
            "scalar function", "table-valued function", "inline TVF",
            "multi-statement TVF", "aggregate function", "window function",
            "ROW_NUMBER", "RANK", "DENSE_RANK", "NTILE", "LEAD", "LAG",
            "FIRST_VALUE", "LAST_VALUE", "CTE error", "recursive CTE",
            "max recursion", "pivot/unpivot", "dynamic SQL", "sp_executesql",
            "SQL injection", "QUOTENAME", "backup failed", "backup device",
            "backup checksum", "verify backup", "restore failed",
            "restore verify", "restore with recovery",
            "restore with norecovery", "restore standby", "differential backup",
            "transaction log backup", "full backup", "partial backup",
            "filegroup backup", "mirror backup", "database mirroring",
            "mirroring error", "partner not found", "failover error",
            "automatic failover", "manual failover", "high safety",
            "high performance", "witness server", "quorum lost",
            "Always On", "availability group", "AG listener",
            "replica not synchronized", "primary replica", "secondary replica",
            "read-only routing", "failover cluster", "cluster resource",
            "cluster quorum", "WSFC", "FCI error", "SSIS error",
            "package error", "data flow", "control flow", "connection manager",
            "SSRS error", "report server", "data source", "report execution",
            "SSAS error", "dimension processing", "measure group",
            "cube processing", "linked server", "distributed query",
            "4-part name", "OPENQUERY", "OPENROWSET", "BULK INSERT",
            "BCP error", "SQLCMD error",
        ],
    },
    "oracle": {
        "tool_name": "oracle",
        "display": "Oracle",
        "topic_key": "oracle",
        "topics": [
            "ORA-00001 unique constraint", "ORA-00018 max sessions",
            "ORA-00020 max processes", "ORA-00028 session killed",
            "ORA-00054 resource busy", "ORA-00060 deadlock",
            "ORA-00061 resource serial", "ORA-00257 archiver error",
            "ORA-00312 online log", "ORA-00313 log member",
            "ORA-00314 log sequence", "ORA-00904 invalid identifier",
            "ORA-00911 invalid character", "ORA-00917 missing comma",
            "ORA-00923 FROM keyword", "ORA-00932 inconsistent datatypes",
            "ORA-00933 SQL command", "ORA-00936 missing expression",
            "ORA-00942 table or view not found", "ORA-00955 name already used",
            "ORA-01400 cannot insert NULL", "ORA-01401 inserted value too large",
            "ORA-01403 no data found", "ORA-01410 invalid ROWID",
            "ORA-01422 fetch exact returns more",
            "ORA-01438 value larger than precision",
            "ORA-01536 space quota exceeded",
            "ORA-01555 snapshot too old",
            "ORA-01578 file not readable",
            "ORA-01650 rollback segment", "ORA-01652 temp unable",
            "ORA-01653 table unable", "ORA-01654 index unable",
            "ORA-01658 unable to create", "ORA-01683 index unable",
            "ORA-01688 table unable", "ORA-01722 invalid number",
            "ORA-01756 quoted string", "ORA-01790 expression must have",
            "ORA-01830 date format", "ORA-01831 date conversion",
            "ORA-01843 not a valid month",
            "ORA-01861 literal does not match", "ORA-01950 no privileges",
            "ORA-02014 group by", "ORA-02020 too many links",
            "ORA-02021 DDL on remote", "ORA-02049 distributed lock",
            "ORA-02291 integrity constraint",
            "ORA-02292 integrity constraint child",
            "ORA-02293 CHECK constraint", "ORA-02296 cannot enable",
            "ORA-02429 cannot drop", "ORA-04031 unable to allocate",
            "ORA-04036 PGA memory", "ORA-04043 object not found",
            "ORA-04063 view has errors", "ORA-04068 existing state",
            "ORA-04070 trigger not found", "ORA-04088 trigger execution",
            "ORA-04091 mutating table", "ORA-04092 cannot COMMIT",
            "ORA-04093 column check", "ORA-04098 trigger failed",
            "ORA-06502 PL/SQL value error", "ORA-06503 PL/SQL function",
            "ORA-06508 package not loaded", "ORA-06512 at line",
            "ORA-06530 reference variable", "ORA-06531 ref cursor",
            "ORA-06532 subscript outside", "ORA-06533 exceed count",
            "ORA-06550 PLS error", "ORA-12011 execution error",
            "ORA-12034 materialized view", "ORA-12154 TNS not found",
            "ORA-12514 TNS listener", "ORA-12541 TNS no listener",
            "ORA-12545 connect failed", "ORA-12560 protocol adapter",
            "ORA-12638 credential retrieve", "ORA-12704 character set",
            "ORA-12801 parallel query", "ORA-12899 value too large",
            "ORA-12954 request denied", "ORA-13011 coordinate",
            "ORA-13249 spatial index", "ORA-13364 layer",
            "ORA-13496 GeoRaster", "ORA-14102 partition view",
            "ORA-14155 missing partition", "ORA-14257 cannot move",
            "ORA-14258 partition not", "ORA-14400 inserted partition",
            "ORA-14756 prefix compression", "ORA-14758 last partition",
            "ORA-16000 database open", "ORA-16224 standby",
            "ORA-16502 Data Guard", "ORA-16608 broker",
            "ORA-16795 standby", "ORA-16854 application",
            "ORA-16857 member", "ORA-17629 connect string",
            "ORA-17627 ORA error", "ORA-19502 write failed",
            "ORA-19809 limit exceeded", "ORA-19815 flashback",
            "ORA-27037 file I/O", "ORA-27101 shared memory",
            "ORA-27102 out of memory", "ORA-27469 job class",
            "ORA-27476 Scheduler", "ORA-28000 account locked",
            "ORA-28001 password expired", "ORA-28002 password grace",
            "ORA-28003 password verify", "ORA-28134 policy",
            "ORA-28546 connection failed", "ORA-29283 file operation",
            "ORA-29913 ODCI", "ORA-29295 XML",
            "ORA-30673 column not", "ORA-30926 unable to get",
            "ORA-31693 object data", "ORA-31694 master table",
            "ORA-32033 unsupported", "ORA-32034 unsupported use",
            "ORA-32701 possible hung", "ORA-32781 cannot use",
            "ORA-32896 queue", "ORA-32897 message",
            "ORA-38104 ON clause", "ORA-38105 subquery",
            "ORA-38106 MERGE", "ORA-38856 cannot mark",
            "ORA-38936 cannot issue", "ORA-39082 object type",
            "ORA-39111 incompatible", "ORA-39171 job failed",
            "ORA-39760 valid state",
        ],
    },
    "cassandra": {
        "tool_name": "cassandra",
        "display": "Cassandra",
        "topic_key": "cassandra",
        "topics": [
            "connection refused", "auth error", "unauthorized",
            "not enough replicas", "read timeout", "write timeout",
            "unavailable exception", "coordinator timeout", "node down",
            "node not joining", "node join error", "bootstrap failed",
            "decommission failed", "remove node", "rebuild failed",
            "repair failed", "incremental repair", "full repair",
            "repair session", "repair validation", "compaction failed",
            "major compaction", "minor compaction", "compaction strategy",
            "SizeTieredCompaction", "LeveledCompaction",
            "TimeWindowCompaction", "compaction backlog",
            "sstable corrupt", "sstable not found", "commit log corrupt",
            "commit log replay", "memtable flush", "memtable full",
            "memtable OOM", "memtable live", "memtable switch",
            "hinted handoff", "hints not enabled", "batchlog error",
            "batchlog replay", "lightweight transaction", "paxos timeout",
            "serial consistency", "consistency level", "quorum not met",
            "local quorum", "each quorum", "ANY consistency",
            "ALL consistency", "ONE consistency", "TWO consistency",
            "THREE consistency", "local serial", "serial", "read repair",
            "read repair chance", "dclocal_read_repair_chance",
            "GC grace seconds", "tombstone threshold", "tombstone debug",
            "too many tombstones", "user defined type", "UDT field",
            "UDT nested", "tuple error", "frozen collection",
            "non-frozen collection", "list append", "set add", "map entry",
            "collection query", "index error", "secondary index",
            "SASI index", "index not found", "index creation",
            "materialized view", "MV base table", "MV update",
            "MV consistency", "MV not built", "lightweight transaction",
            "paging error", "paging state", "auto paging", "fetch size",
            "limit error", "IN query", "partition key",
            "clustering column", "composite key", "static column",
            "row timestamp", "TTL expiration", "TTL write",
            "writetime update", "now() function", "token function",
            "partitioner token", "murmur3 partitioner",
            "random partitioner", "byte ordered partitioner",
            "vnode error", "virtual node", "num_tokens",
            "bootstrap tokens", "token range", "nodetool error",
            "nodetool status", "nodetool info", "nodetool repair",
            "nodetool cleanup", "nodetool decommission", "nodetool rebuild",
            "nodetool refresh", "nodetool upgradesstables", "cqlsh error",
            "cqlsh connection", "CQL parse", "CQL syntax",
            "prepared statement", "bound statement", "simple statement",
            "batch statement", "logged batch", "unlogged batch",
            "counter batch", "counter column", "CDC error",
            "change data capture", "segment", "commitlogsegment",
            "total space", "schema agreement", "schema version mismatch",
            "gossip error", "failure detector", "phi value",
            "snitch error", "simple snitch", "GossipingPropertyFile",
            "EC2 snitch", "cloud snitch", "dynamic snitch",
            "network topology", "data center", "rack", "seed node",
            "bootstrap seed", "seed not found", "JMX error",
            "JMX port", "JMX auth", "JMX SSL", "remote JMX",
            "metrics error", "JMX metrics", "Dropwizard metrics",
            "Graphite reporter", "nodetool proxyhistograms",
            "cache error", "key cache", "row cache", "counter cache",
            "cache hit ratio", "saving cache", "serialization header",
            "native protocol", "version mismatch", "CQL binary",
            "CQL BATCH", "UNLOGGED BATCH", "COUNTER batch", "MIXED batch",
        ],
    },
    "cockroachdb": {
        "tool_name": "cockroachdb",
        "display": "CockroachDB",
        "topic_key": "cockroachdb",
        "topics": [
            "node not found", "node decommissioned", "node down",
            "node join failed", "node restart", "node liveness",
            "node heartbeat", "clock sync error", "clock offset",
            "max offset", "NTP error", "time jump",
            "transaction retry", "restart transaction",
            "serializable isolation", "read refresh", "write intent",
            "intent resolution", "contention error", "transaction conflict",
            "push transaction", "lock timeout", "deadlock detected",
            "TxnIDResolution", "transaction aborted", "rollback error",
            "retry limit", "max retries", "range not found",
            "range unavailable", "range split", "range merge",
            "range rebalance", "leaseholder error", "lease acquisition",
            "lease transfer", "raft leader", "raft election",
            "raft commit", "raft log", "follower read",
            "closed timestamp", "store error", "store full",
            "disk stall", "disk slow", "capacity error",
            "store not found", "store bootstrap", "encryption error",
            "file registry", "key not found", "SQL error",
            "relation not found", "column not found", "index not found",
            "constraint violation", "unique violation",
            "foreign key violation", "check constraint violation",
            "not null violation", "division by zero", "numeric overflow",
            "array subscript", "duplicate key", "UPSERT conflict",
            "INSERT ON CONFLICT", "UPDATE error", "DELETE error",
            "SELECT error", "subquery error", "JOIN error",
            "HASH JOIN", "MERGE JOIN", "LOOKUP JOIN",
            "INVERTED JOIN", "ZIGZAG JOIN", "distributed query",
            "local query", "SQL exec", "DistSQL error", "plan error",
            "optimizer error", "statistics error", "table statistics",
            "histogram", "cardinality", "scan error", "index join",
            "lookup join", "CockroachDB user", "role not found",
            "privilege error", "grant error", "revoke error",
            "ALTER error", "CREATE error", "DROP error", "TRUNCATE error",
            "BACKUP error", "RESTORE error", "BACKUP target",
            "BACKUP subdir", "BACKUP revocation", "incremental backup",
            "full backup", "schedule backup", "changefeed error",
            "CDC", "enterprise changefeed", "core changefeed",
            "sink error", "Kafka sink", "cloud storage sink",
            "webhook sink", "changefeed retry", "changefeed checkpoint",
            "resolved timestamp", "schema change", "online schema change",
            "DDL job", "schema migration", "job not found",
            "job failed", "job pause", "job resume", "job cancel",
            "schema changer", "declarative schema", "legacy schema",
            "zone config", "replication zone", "GC TTL",
            "number of replicas", "constraints", "lease preferences",
            "locality error", "multi-region", "regional table",
            "global table", "regional by table", "survival goal",
            "region", "primary region", "secondary region", "latency",
            "geo-partitioning", "cluster settings", "setting type",
            "setting scope", "cluster version", "upgrade error",
            "auto upgrade", "finalization", "tenant error",
            "KV tenant", "SQL pod", "serverless", "multi-tenant",
        ],
    },
    "dynamodb": {
        "tool_name": "dynamodb",
        "display": "DynamoDB",
        "topic_key": "dynamodb",
        "topics": [
            "table not found", "table already exists", "table not active",
            "table in use", "table deleting", "index not found",
            "index already exists", "GSI name", "LSI name",
            "GSI projection", "LSI projection", "keys only", "include",
            "all attributes", "partition key", "sort key", "key type",
            "key schema", "attribute definition", "provisioned throughput",
            "read capacity", "write capacity", "read capacity exceeded",
            "write capacity exceeded", "provisioned limit",
            "on-demand capacity", "auto scaling", "target utilization",
            "min capacity", "max capacity", "scaling policy",
            "item not found", "item too large", "batch get limit",
            "batch get error", "batch write limit", "batch write error",
            "transact get error", "transact write error",
            "transaction conflict", "transaction cancel",
            "transaction validation", "conditional check",
            "condition expression", "expression attribute",
            "placeholder name", "attribute path", "update expression",
            "SET action", "REMOVE action", "ADD action", "DELETE action",
            "function in expression", "attribute_exists",
            "attribute_not_exists", "attribute_type", "begins_with",
            "contains", "size function", "filter expression",
            "key condition", "query filter", "scan filter",
            "scan timeout", "page size", "exclusive start key",
            "last evaluated key", "consumed capacity",
            "return consumed", "index query", "index scan",
            "query limit", "scan limit", "consistent read",
            "eventually consistent", "strong consistency",
            "DAX error", "DAX cluster", "DAX endpoint", "DAX discovery",
            "DAX auth", "DAX token", "DAX IAM", "DynamoDB Streams",
            "stream enabled", "stream ARN", "stream view type",
            "keys only", "new image", "old image",
            "new and old images", "shard iterator", "get records",
            "record processing", "Lambda trigger",
            "event source mapping", "stream timeout", "iterator age",
            "TTL enable", "TTL attribute", "expired item",
            "delete expired", "TTL past", "global table",
            "replica table", "replication group", "Region not supported",
            "conflict resolution", "last writer wins",
            "global table version", "2017 version", "2019 version",
            "backup error", "on-demand backup", "continuous backup",
            "point in time", "restore table", "restore progress",
            "restore time", "PITR window", "export to S3",
            "import from S3", "import error", "CSV import",
            "DynamoDB local", "local setup", "local port",
            "local access", "local config", "credential chain",
            "IAM role", "assumed role", "federated identity",
            "Cognito identity", "cognito pool", "web identity",
            "STS assume", "access key", "secret key", "session token",
            "request timeout", "connection timeout", "retry count",
            "max retries", "exponential backoff", "SDK error",
            "Go SDK", "Python SDK", "Java SDK", "Node SDK",
            ".NET SDK", "CLI error", "AWS CLI", "--table-name",
            "--item", "--expression", "DynamoDBMapper",
            "ORM mapping", "@DynamoDBTable", "@DynamoDBHashKey",
            "@DynamoDBRangeKey", "@DynamoDBAttribute",
            "@DynamoDBAutoGeneratedKey", "Document API", "Table class",
            "Item class", "PutItemSpec", "GetItemSpec",
            "UpdateItemSpec", "DeleteItemSpec", "QuerySpec", "ScanSpec",
        ],
    },
}


DESC_TEMPLATES = {
    "sqlserver": "Understand and resolve the SQL Server '{topic}' error with causes, T-SQL fixes, and examples.",
    "oracle": "Understand and resolve the Oracle {topic} error with causes, SQL fixes, and examples.",
    "cassandra": "Understand and resolve the Cassandra '{topic}' error with causes, CQL fixes, and examples.",
    "cockroachdb": "Understand and resolve the CockroachDB '{topic}' error with causes, SQL fixes, and examples.",
    "dynamodb": "Understand and resolve the DynamoDB '{topic}' error with causes, AWS CLI and SDK fixes, and examples.",
}


def page_body(tool_name, topic):
    """Generate the body content for a page."""
    tool_display = TOOLS[tool_name]["display"]
    lines = []
    lines.append(f"# {tool_display} - {topic}")
    lines.append("")
    lines.append(f"The {tool_display} `{topic}` error can occur during database operations. "
                 f"This page explains what causes it and how to resolve it.")
    lines.append("")
    lines.append("## What This Error Means")
    lines.append("")
    lines.append(f"Encountering the `{topic}` error in {tool_display} indicates a problem "
                 f"that prevents normal database operations from completing successfully. "
                 f"Identifying the root cause quickly is key to minimizing downtime.")
    lines.append("")
    lines.append("## Common Causes")
    lines.append("")
    lines.append(f"- Configuration mismatch or missing setup")
    lines.append(f"- Resource constraints or capacity limits")
    lines.append(f"- Permission or authentication failures")
    lines.append(f"- Query or syntax issues")
    lines.append(f"- Concurrent access or lock contention")
    lines.append("")
    lines.append("## How to Fix")
    lines.append("")
    lines.append("### Check Configuration")
    lines.append("")
    lines.append(f"Verify that all configuration settings related to this error are correct "
                 f"for your {tool_display} environment. Review server logs for additional details.")
    lines.append("")
    lines.append("### Verify Permissions")
    lines.append("")
    lines.append(f"Ensure the connecting user or application has the necessary permissions "
                 f"to perform the requested operation in {tool_display}.")
    lines.append("")
    lines.append("### Review Resources")
    lines.append("")
    lines.append(f"Check that sufficient resources (memory, disk space, connections) are available "
                 f"for the {tool_display} instance.")
    lines.append("")
    # Add tool-specific code block
    if tool_name == "sqlserver":
        lines.append("```sql")
        lines.append("-- Check SQL Server error log for details")
        lines.append("EXEC xp_readerrorlog;")
        lines.append("```")
    elif tool_name == "oracle":
        lines.append("```sql")
        lines.append("-- Check Oracle alert log for details")
        lines.append("SELECT * FROM V$DIAG_INFO;")
        lines.append("```")
    elif tool_name == "cassandra":
        lines.append("```cql")
        lines.append("-- Check system.log for error details")
        lines.append("-- tail -f /var/log/cassandra/system.log")
        lines.append("```")
    elif tool_name == "cockroachdb":
        lines.append("```sql")
        lines.append("-- Check CockroachDB cluster settings")
        lines.append("SHOW CLUSTER SETTINGS;")
        lines.append("```")
    elif tool_name == "dynamodb":
        lines.append("```bash")
        lines.append("# Describe the DynamoDB table")
        lines.append("aws dynamodb describe-table --table-name your-table")
        lines.append("```")
    lines.append("")
    lines.append("## Examples")
    lines.append("")
    lines.append(f"A typical occurrence of the `{topic}` error in {tool_display}:")
    lines.append("")
    if tool_name == "sqlserver":
        lines.append("```sql")
        lines.append(f"-- Example scenario")
        lines.append(f"SELECT * FROM sys.dm_exec_requests;")
        lines.append("```")
    elif tool_name == "oracle":
        lines.append("```sql")
        lines.append("-- Example diagnostic query")
        lines.append("SELECT * FROM V$SESSION WHERE STATUS = 'ACTIVE';")
        lines.append("```")
    elif tool_name == "cassandra":
        lines.append("```cql")
        lines.append("-- Example diagnostic query")
        lines.append("SELECT * FROM system_schema.tables;")
        lines.append("```")
    elif tool_name == "cockroachdb":
        lines.append("```sql")
        lines.append("-- Example diagnostic query")
        lines.append("SHOW TABLES;")
        lines.append("```")
    elif tool_name == "dynamodb":
        lines.append("```bash")
        lines.append("# Example diagnostic command")
        lines.append("aws dynamodb list-tables --region us-east-1")
        lines.append("```")
    lines.append("")
    lines.append("## Related Errors")
    lines.append("")
    lines.append(f"- Related error in {tool_display}")
    lines.append("")
    return "\n".join(lines)


def build_slug(tool_name, topic):
    """Build the filename slug. For Oracle preserve ORA-XXXX pattern."""
    if tool_name == "oracle":
        base = topic.lower().strip()
        base = base.replace("ora-", "ora-")  # keep ORA-
        base = re.sub(r"[^a-z0-9\s-]", "", base)
        base = re.sub(r"[\s_]+", "-", base)
        base = re.sub(r"-+", "-", base)
        return base.strip("-")
    elif tool_name == "sqlserver":
        s = slugify(topic)
        if s.startswith("sqlserver-"):
            return s
        return s
    elif tool_name == "cockroachdb":
        s = slugify(topic)
        if s.startswith("cockroachdb-"):
            return s
        return s
    elif tool_name == "dynamodb":
        s = slugify(topic)
        if s.startswith("dynamodb-"):
            return s
        return s
    elif tool_name == "cassandra":
        s = slugify(topic)
        if s.startswith("cassandra-"):
            return s
        return s
    return slugify(topic)


def make_page(tool_name, topic, slug):
    """Create the full .md page content."""
    tool_display = TOOLS[tool_name]["display"]

    # Build frontmatter title
    fm_title = f"[Solution] {tool_display} - {topic}"
    desc = DESC_TEMPLATES[tool_name].format(topic=topic)

    parts = []
    parts.append("---")
    parts.append(f'title: "{fm_title}"')
    parts.append(f'description: "{desc}"')
    parts.append(f'tools: ["{tool_name}"]')
    parts.append('error-types: ["database-error"]')
    parts.append('severities: ["error"]')
    parts.append("weight: 5")
    parts.append("---")
    parts.append("")
    parts.append(page_body(tool_name, topic))

    return "\n".join(parts)


def main():
    total_new = {}
    for tool_name, info in TOOLS.items():
        d = TOOLS_DIRS[tool_name]
        os.makedirs(d, exist_ok=True)
        existing = get_existing_slugs(d)
        slug_to_topic = {}
        # Pre-summarize: try to detect all existing slugs from current data
        for topic in info["topics"]:
            slug = build_slug(tool_name, topic)
            slug_to_topic[slug] = topic

        new_count = 0
        for topic in info["topics"]:
            slug = build_slug(tool_name, topic)
            if slug in existing:
                continue
            content = make_page(tool_name, topic, slug)
            filepath = d / f"{slug}.md"
            with open(filepath, "w") as f:
                f.write(content)
            existing.add(slug)
            new_count += 1

        total_existing = len(get_existing_slugs(d))
        total_new[tool_name] = (new_count, total_existing)
        print(f"{tool_name}: created {new_count} new pages, total now {total_existing}")

    print("\n--- Summary ---")
    for tool_name, (new, total) in total_new.items():
        print(f"  {tool_name}: +{new} new pages, total {total} pages")


if __name__ == "__main__":
    main()
