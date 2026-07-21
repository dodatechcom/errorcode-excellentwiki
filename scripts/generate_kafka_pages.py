#!/usr/bin/env python3
"""Generate new Kafka error pages to expand to 100+ total."""
import os

TOOL_DIR = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/kafka/'
EXISTING = {f.replace('.md', '') for f in os.listdir(TOOL_DIR) if f.endswith('.md')}

PAGES = [
    ("kafka-broker-not-available", "Kafka Broker Not Available Error",
     "Fix Kafka broker not available error. Resolve broker connectivity issues in Apache Kafka clusters.",
     "The Kafka broker is not reachable. Clients receive broker not available when the broker process is down, the listener is misconfigured, or network connectivity is broken.",
     ["The broker process is not running", "Listener configuration is wrong in server.properties", "Firewall blocks the listener port"],
     ["kafka-broker-api-versions.sh --bootstrap-server localhost:9092",
      "grep '^listeners' /etc/kafka/server.properties",
      "telnet broker-host 9092"]),

    ("kafka-leader-not-available", "Kafka Leader Not Available Error",
     "Fix Kafka leader not available error. Resolve leader election failures for Kafka partitions.",
     "A partition has no elected leader. This happens during broker failures, under-replicated partitions, or when the controller cannot complete leader election.",
     ["All replicas for a partition are down", "Controller is not elected", "Under-replicated partitions prevent election"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --under-replicated-partitions",
      "kafka-leader-election.sh --bootstrap-server localhost:9092 --election-type preferred --all-topic-partitions"]),

    ("kafka-topic-not-found", "Kafka Topic Not Found Error",
     "Fix Kafka topic not found error. Resolve missing or deleted topic issues in Kafka.",
     "The requested topic does not exist. The topic may have been deleted, auto.create.topics.enable is false, or the topic name is misspelled.",
     ["Topic was deleted", "auto.create.topics.enable is false", "Topic name is misspelled"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --list",
      "kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic"]),

    ("kafka-topic-exists", "Kafka Topic Already Exists Error",
     "Fix Kafka topic already exists error. Resolve topic creation failures when topic name is taken.",
     "Topic creation fails because a topic with the same name already exists. This can happen when auto.create.topics.enable creates topics automatically before manual creation.",
     ["Topic was already created", "Auto-creation created the topic first", "Name collision with existing topic"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --list",
      "kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic"]),

    ("kafka-partition-not-found", "Kafka Partition Not Found Error",
     "Fix Kafka partition not found error. Resolve partition reference issues in Kafka topics.",
     "The requested partition does not exist for the given topic. This may indicate topic metadata is stale or the partition was removed during rebalancing.",
     ["Partition metadata is stale", "Topic was recreated with fewer partitions", "Consumer is using old metadata"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic",
      "kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group"]),

    ("kafka-offset-out-of-range", "Kafka Offset Out of Range Error",
     "Fix Kafka offset out of range error. Resolve consumer offset issues when offsets are expired or invalid.",
     "The consumer requests an offset that no longer exists on the broker. This happens when log retention has deleted the segments containing that offset.",
     ["Log retention deleted segments", "Consumer offset is too old", "Topic retention policy is aggressive"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my-group --reset-offsets --to-earliest --all-topics --execute",
      "kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all"]),

    ("kafka-replication-factor-too-high", "Kafka Replication Factor Too High Error",
     "Fix Kafka replication factor too high error. Resolve replication factor exceeding available broker count.",
     "The replication factor exceeds the number of available brokers. You cannot have a replication factor greater than the number of brokers in the cluster.",
     ["Replication factor set higher than broker count", "Brokers went offline reducing count", "New topic created with wrong RF"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic",
      "kafka-broker-api-versions.sh --bootstrap-server localhost:9092"]),

    ("kafka-min-isr-not-met", "Kafka Min ISR Not Met Error",
     "Fix Kafka min ISR not met error. Resolve produce failures when insufficient in-sync replicas exist.",
     "Produce requests fail because the number of in-sync replicas is below min.insync.replicas. Writes are rejected to prevent data loss when too many replicas are down.",
     ["Too many replicas are down", "Replicas cannot keep up with leader", "Network issues between replicas and leader"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic",
      "kafka-configs.sh --bootstrap-server localhost:9092 --alter --topic my-topic --add-config min.insync.replicas=1"]),

    ("kafka-unclean-leader-election", "Kafka Unclean Leader Election Error",
     "Fix Kafka unclean leader election error. Resolve data loss risk from unclean leader elections.",
     "An out-of-sync replica was elected leader because all in-sync replicas are unavailable. This can cause data loss when unclean.leader.election.enable is true.",
     ["All in-sync replicas are down", "unclean.leader.election.enable is true", "No ISR members available"],
     ["kafka-configs.sh --bootstrap-server localhost:9092 --alter --topic my-topic --add-config unclean.leader.election.enable=false",
      "kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic"]),

    ("kafka-controller-failover", "Kafka Controller Failover Error",
     "Fix Kafka controller failover error. Resolve issues during controller election and failover.",
     "The controller failover process fails or takes too long. This happens when ZooKeeper or KRaft cannot elect a new controller, or the new controller cannot load partition metadata.",
     ["ZooKeeper session expired", "KRaft quorum is unavailable", "Controller metadata is corrupted"],
     ["kafka-metadata.sh --snapshot /path/to/metadata.log",
      "echo ruok | nc localhost 2181"]),

    ("kafka-consumer-group-not-found", "Kafka Consumer Group Not Found Error",
     "Fix Kafka consumer group not found error. Resolve consumer group reference issues.",
     "The specified consumer group does not exist. The group may have expired due to inactivity or was never created.",
     ["Group expired from inactivity", "Group was never created", "Group coordinator lost metadata"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list",
      "kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group"]),

    ("kafka-consumer-rebalance-failed", "Kafka Consumer Rebalance Failed Error",
     "Fix Kafka consumer rebalance failed error. Resolve consumer group coordination issues.",
     "The consumer group fails to complete a rebalance. This can be caused by session timeouts, coordinator failures, or consumers failing to rejoin in time.",
     ["Session timeout too short", "Coordinator broker is down", "Consumer takes too long to rejoin"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group",
      "kafka-configs.sh --bootstrap-server localhost:9092 --describe --group my-group --all"]),

    ("kafka-commit-offset-failed", "Kafka Commit Offset Failed Error",
     "Fix Kafka commit offset failed error. Resolve consumer offset commit failures.",
     "The consumer cannot commit offsets to Kafka. This happens when the group coordinator is unavailable, the consumer is not a group member, or there is a rebalance in progress.",
     ["Group coordinator is unavailable", "Consumer is not a group member", "Rebalance is in progress"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group"]),

    ("kafka-max-poll-interval-exceeded", "Kafka Max Poll Interval Exceeded Error",
     "Fix Kafka max.poll.interval.ms exceeded error. Resolve consumer eviction from group.",
     "The consumer is removed from the group because it failed to call poll() within max.poll.interval.ms. The processing time between polls exceeds the configured interval.",
     ["Processing time between polls is too long", "max.poll.interval.ms is set too low", "Consumer is doing heavy processing"],
     ["grep max.poll /path/to/consumer.config",
      "kafka-configs.sh --bootstrap-server localhost:9092 --describe --group my-group --all"]),

    ("kafka-session-timeout", "Kafka Session Timeout Error",
     "Fix Kafka session timeout error. Resolve consumer session timeout issues in Kafka.",
     "The consumer session times out and it is removed from the group. This happens when the consumer fails to send heartbeats within session.timeout.ms.",
     ["Heartbeat interval is too long", "Network latency delays heartbeats", "GC pauses prevent heartbeat sending"],
     ["grep 'session.timeout.ms\\|heartbeat.interval.ms' /path/to/consumer.config"]),

    ("kafka-heartbeat-failure", "Kafka Heartbeat Failure Error",
     "Fix Kafka heartbeat failure error. Resolve consumer heartbeat delivery issues.",
     "The consumer fails to send heartbeats to the group coordinator. This can be caused by network issues, long GC pauses, or the coordinator being unavailable.",
     ["Network connectivity issues", "Long GC pauses", "Coordinator broker is down"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group"]),

    ("kafka-fetch-request-timeout", "Kafka Fetch Request Timeout Error",
     "Fix Kafka fetch request timeout error. Resolve consumer fetch timeout issues.",
     "The fetch request from the consumer times out. This happens when the broker is slow to respond, the fetch size is too large, or network latency is high.",
     ["Broker is overloaded", "fetch.size is too large", "Network latency is high"],
     ["grep 'fetch.max.wait.ms\\|fetch.min.bytes\\|fetch.size' /path/to/consumer.config"]),

    ("kafka-produce-request-timeout", "Kafka Produce Request Timeout Error",
     "Fix Kafka produce request timeout error. Resolve producer timeout issues.",
     "The produce request times out waiting for broker acknowledgment. This happens when the broker is overloaded, replication is slow, or the acks setting requires all replicas.",
     ["Broker is overloaded", "acks=all requires all replicas", "Replication is slow"],
     ["grep 'request.timeout.ms\\|delivery.timeout.ms\\|acks' /path/to/producer.config"]),

    ("kafka-request-too-large", "Kafka Request Too Large Error",
     "Fix Kafka request too large error. Resolve message batch size issues.",
     "The request payload exceeds max.request.size. The producer cannot send messages that large to the broker.",
     ["Message or batch exceeds max.request.size", "Batch contains too many messages", "Broker has lower message.max.bytes"],
     ["kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all",
      "grep 'max.request.size\\|batch.size' /path/to/producer.config"]),

    ("kafka-message-too-large", "Kafka Message Too Large Error",
     "Fix Kafka message too large error. Resolve individual message size limit issues.",
     "A single message exceeds the broker message.max.bytes or the topic max.message.bytes. The broker rejects the oversized message.",
     ["Single message exceeds broker limit", "Topic max.message.bytes is too low", "Producer sends unbounded messages"],
     ["kafka-configs.sh --bootstrap-server localhost:9092 --alter --topic my-topic --add-config message.max.bytes=10485760"]),

    ("kafka-batch-size-exceeded", "Kafka Batch Size Exceeded Error",
     "Fix Kafka batch size exceeded error. Resolve producer batch configuration issues.",
     "The producer batch of messages exceeds the configured batch.size. The batch is forcibly sent before reaching the configured size limit.",
     ["batch.size is too small", "linger.ms is too low", "Messages are large and fill batch quickly"],
     ["grep 'batch.size\\|linger.ms' /path/to/producer.config"]),

    ("kafka-compression-error", "Kafka Compression Error",
     "Fix Kafka compression error. Resolve message compression and decompression failures.",
     "The broker or consumer cannot decompress a message. The compression codec does not match between producer and consumer, or the compressed data is corrupted.",
     ["Producer and consumer use different compression codecs", "Compressed data is corrupted", "Codec is not supported by broker"],
     ["grep compression.type /path/to/producer.config /path/to/consumer.config"]),

    ("kafka-serialization-error", "Kafka Serialization Error",
     "Fix Kafka serialization error. Resolve producer message serialization failures.",
     "The producer cannot serialize the message key or value. The serializer class is misconfigured or the data type is incompatible with the serializer.",
     ["Serializer class is misconfigured", "Data type is incompatible", "Schema registry mismatch"],
     ["grep 'key.serializer\\|value.serializer' /path/to/producer.config"]),

    ("kafka-deserialization-error", "Kafka Deserialization Error",
     "Fix Kafka deserialization error. Resolve consumer message deserialization failures.",
     "The consumer cannot deserialize a message. The deserializer class does not match the serializer used by the producer, or the schema has changed.",
     ["Deserializer does not match producer serializer", "Schema has changed", "Message is corrupted"],
     ["grep 'key.deserializer\\|value.deserializer' /path/to/consumer.config"]),

    ("kafka-avro-schema-not-found", "Kafka Avro Schema Not Found Error",
     "Fix Kafka Avro schema not found error. Resolve Schema Registry lookup failures.",
     "The Avro schema is not found in the Schema Registry. The schema may not have been registered or the schema ID is incorrect.",
     ["Schema was never registered", "Schema ID is wrong in message header", "Schema Registry is unreachable"],
     ["curl http://localhost:8081/subjects",
      "curl http://localhost:8081/subjects/my-topic-value/versions"]),

    ("kafka-schema-registry-error", "Kafka Schema Registry Error",
     "Fix Kafka Schema Registry error. Resolve Schema Registry connectivity and operational issues.",
     "The Schema Registry is unreachable or returns an error. This can be caused by network issues, registry overload, or configuration problems.",
     ["Schema Registry is down", "Network connectivity issue", "Registry configuration is wrong"],
     ["curl http://localhost:8081/subjects",
      "curl http://localhost:8081/config"]),

    ("kafka-schema-compatibility", "Kafka Schema Compatibility Error",
     "Fix Kafka schema compatibility error. Resolve schema evolution and compatibility issues.",
     "The new schema version is incompatible with the existing schema. Schema Registry rejects the registration due to compatibility rule violations.",
     ["Schema change is breaking", "Compatibility mode is too strict", "New field has no default value"],
     ["curl http://localhost:8081/config/my-topic-value",
      "curl -X PUT -H 'Content-Type: application/json' --data '{\"compatibility\":\"BACKWARD\"}' http://localhost:8081/config/my-topic-value"]),

    ("kafka-acl-authorization", "Kafka ACL Authorization Error",
     "Fix Kafka ACL authorization error. Resolve access control list permission issues.",
     "The client is not authorized to perform the requested operation. The ACL does not grant the required permission for the principal on the resource.",
     ["ACL does not include the required operation", "Principal does not match", "Authorizer is not configured"],
     ["kafka-acls.sh --bootstrap-server localhost:9092 --list",
      "kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:myuser --operation Read --topic my-topic"]),

    ("kafka-sasl-auth-failed", "Kafka SASL Authentication Failed Error",
     "Fix Kafka SASL authentication failed error. Resolve SASL handshake and authentication issues.",
     "The SASL authentication fails. The credentials are wrong, the mechanism is misconfigured, or the SASL handshake failed.",
     ["Credentials are wrong", "SASL mechanism is misconfigured", "JAAS config is invalid"],
     ["grep 'security.protocol\\|sasl.mechanism\\|sasl.jaas.config' /path/to/client.config"]),

    ("kafka-ssl-handshake", "Kafka SSL Handshake Error",
     "Fix Kafka SSL handshake error. Resolve TLS/SSL connection establishment issues.",
     "The SSL handshake between client and broker fails. This can be caused by certificate issues, protocol version mismatch, or cipher suite incompatibility.",
     ["Certificate is expired or invalid", "SSL protocol version mismatch", "Cipher suite not supported"],
     ["openssl s_client -connect broker-host:9093 -showcerts",
      "grep 'ssl\\|truststore\\|keystore' /path/to/client.config"]),

    ("kafka-kerberos-auth", "Kafka Kerberos Authentication Error",
     "Fix Kafka Kerberos authentication error. Resolve GSSAPI/Kerberos authentication issues.",
     "Kerberos authentication fails. The keytab is missing, the principal is wrong, or the KDC is unreachable.",
     ["Keytab file is missing or wrong", "Principal name does not match", "KDC is unreachable"],
     ["klist -kt /path/to/keytab",
      "kinit -kt /path/to/keytab kafka/broker.example.com@EXAMPLE.COM"]),

    ("kafka-plain-login", "Kafka PLAIN Login Error",
     "Fix Kafka PLAIN login error. Resolve SASL/PLAIN authentication issues.",
     "PLAIN authentication fails. The username or password does not match the broker credentials configuration.",
     ["Username or password is wrong", "PLAIN mechanism is not enabled", "SASL protocol is not used"],
     ["grep 'sasl.mechanism\\|sasl.jaas.config' /path/to/client.config"]),

    ("kafka-scram-auth", "Kafka SCRAM Authentication Error",
     "Fix Kafka SCRAM authentication error. Resolve SCRAM-SHA-256/512 authentication issues.",
     "SCRAM authentication fails. The SCRAM credentials were not properly created or the mechanism name is incorrect.",
     ["SCRAM credentials were not created", "Mechanism name is wrong", "Broker does not store SCRAM credentials"],
     ["kafka-configs.sh --bootstrap-server localhost:9092 --describe --user myuser --all"]),

    ("kafka-delegation-token-auth", "Kafka Delegation Token Authentication Error",
     "Fix Kafka delegation token authentication error. Resolve delegation token lifecycle issues.",
     "Delegation token authentication fails. The token may have expired, not been renewed, or was not properly created.",
     ["Token has expired", "Token was not renewed", "Token was never created"],
     ["kafka-delegation-tokens.sh --bootstrap-server localhost:9092 --describe"]),

    ("kafka-zookeeper-connection-loss", "Kafka ZooKeeper Connection Loss Error",
     "Fix Kafka ZooKeeper connection loss error. Resolve ZooKeeper connectivity issues.",
     "The Kafka broker loses connection to ZooKeeper. This can be caused by network issues, ZooKeeper overload, or session timeout expiry.",
     ["ZooKeeper is down or overloaded", "Network issues between broker and ZK", "Session timeout expired"],
     ["echo ruok | nc localhost 2181",
      "echo stat | nc localhost 2181"]),

    ("kafka-zookeeper-session-expired", "Kafka ZooKeeper Session Expired Error",
     "Fix Kafka ZooKeeper session expired error. Resolve ZK session lifecycle issues.",
     "The ZooKeeper session has expired. The broker was disconnected for longer than the session timeout and ZK has removed its ephemeral nodes.",
     ["Broker was disconnected too long", "Session timeout is too short", "Network instability"],
     ["grep zookeeper /etc/kafka/server.properties"]),

    ("kafka-cluster-id-mismatch", "Kafka Cluster ID Mismatch Error",
     "Fix Kafka cluster ID mismatch error. Resolve KRaft cluster identity issues.",
     "The cluster ID in the metadata log does not match the expected ID. This happens when a broker is mistakenly added to the wrong cluster.",
     ["Broker added to wrong cluster", "Metadata log was copied from another cluster", "Cluster ID was changed"],
     ["kafka-metadata.sh --snapshot /path/to/metadata.log"]),

    ("kafka-broker-connection-refused", "Kafka Broker Connection Refused Error",
     "Fix Kafka broker connection refused error. Resolve TCP connection issues to brokers.",
     "The client cannot establish a TCP connection to the broker. The broker may be down, the port is wrong, or a firewall is blocking the connection.",
     ["Broker is not running", "Wrong port number", "Firewall blocks the port"],
     ["jps -l | grep Kafka",
      "ss -tlnp | grep 9092"]),

    ("kafka-network-timeout", "Kafka Network Timeout Error",
     "Fix Kafka network timeout error. Resolve broker communication timeout issues.",
     "Network requests to the broker time out. This can be caused by broker overload, high network latency, or misconfigured timeout settings.",
     ["Broker is overloaded", "Network latency is high", "Timeout settings are too low"],
     ["ping broker-host",
      "grep 'socket.timeout.ms\\|request.timeout.ms' /path/to/client.config"]),

    ("kafka-dns-resolution", "Kafka DNS Resolution Error",
     "Fix Kafka DNS resolution error. Resolve hostname lookup failures for Kafka brokers.",
     "The client cannot resolve the broker hostname. DNS configuration is incorrect or the hostname does not exist.",
     ["DNS server is not configured", "Hostname does not exist in DNS", "/etc/hosts is missing entry"],
     ["nslookup broker-hostname",
      "dig broker-hostname"]),

    ("kafka-controller-quorum", "Kafka Controller Quorum Error",
     "Fix Kafka controller quorum error. Resolve KRaft quorum formation issues.",
     "The KRaft controller quorum cannot form or maintain a majority. This prevents the cluster from electing a controller and serving metadata requests.",
     ["Not enough controller nodes", "Network partition between controllers", "Quorum voters configuration is wrong"],
     ["grep 'controller.quorum.voters\\|controller.listener.names' /etc/kafka/server.properties"]),

    ("kafka-kraft-mode-error", "Kafka KRaft Mode Error",
     "Fix Kafka KRaft mode error. Resolve KRaft metadata log and mode transition issues.",
     "The broker encounters errors in KRaft mode. The metadata log may be corrupted, or the mode transition from ZooKeeper was incomplete.",
     ["Metadata log is corrupted", "ZK migration was incomplete", "process.roles is misconfigured"],
     ["kafka-metadata.sh --snapshot /path/to/metadata.log",
      "grep 'process.roles\\|node.id\\|controller.quorum.voters' /etc/kafka/server.properties"]),

    ("kafka-metadata-fetch-failure", "Kafka Metadata Fetch Failure Error",
     "Fix Kafka metadata fetch failure error. Resolve metadata request issues.",
     "The client cannot fetch topic metadata from the broker. The broker may not have the topic metadata or the request is being rejected.",
     ["Topic metadata is not available", "Client lacks permissions", "Broker cannot serve metadata"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --list"]),

    ("kafka-coordinator-not-available", "Kafka Coordinator Not Available Error",
     "Fix Kafka coordinator not available error. Resolve group coordinator lookup issues.",
     "The group coordinator for the consumer group is not available. The coordinator broker may have failed or the group metadata is not yet propagated.",
     ["Coordinator broker is down", "Group metadata not propagated", "Broker just restarted"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group"]),

    ("kafka-group-coordinator-failure", "Kafka Group Coordinator Failure Error",
     "Fix Kafka group coordinator failure error. Resolve group coordination service issues.",
     "The group coordinator service fails. The broker hosting the coordinator has issues or the group metadata is corrupted.",
     ["Coordinator broker has issues", "Group metadata is corrupted", "__consumer_offsets topic has issues"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list",
      "kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic __consumer_offsets"]),

    ("kafka-transaction-coordinator", "Kafka Transaction Coordinator Error",
     "Fix Kafka transaction coordinator error. Resolve transactional producer coordination issues.",
     "The transaction coordinator is unavailable. The producer cannot begin or complete transactions without a functioning coordinator.",
     ["Transaction coordinator broker is down", "transactional.id is misconfigured", "Coordinator metadata is stale"],
     ["kafka-transactions.sh --bootstrap-server localhost:9092 --describe --transactional-id my-tx-id"]),

    ("kafka-producer-idempotence", "Kafka Producer Idempotence Error",
     "Fix Kafka producer idempotence error. Resolve exactly-once delivery guarantee issues.",
     "The producer cannot enable idempotence. This can be caused by setting acks=0, or using a transactional.id with idempotence disabled.",
     ["acks is set to 0", "idempotence is not enabled", "max.in.flight.requests.per.connection exceeds 5"],
     ["grep 'enable.idempotence\\|acks\\|max.in.flight' /path/to/producer.config"]),

    ("kafka-transactional-produce", "Kafka Transactional Produce Error",
     "Fix Kafka transactional produce error. Resolve transactional producer failures.",
     "The transactional producer fails to send messages. The transaction may have been aborted, the producer fenced, or the coordinator is unavailable.",
     ["Transaction was aborted", "Producer was fenced by newer instance", "Coordinator is unavailable"],
     ["kafka-transactions.sh --bootstrap-server localhost:9092 --describe --transactional-id my-tx-id"]),

    ("kafka-abort-transaction-error", "Kafka Abort Transaction Error",
     "Fix Kafka abort transaction error. Resolve transaction abort and rollback issues.",
     "A transaction is aborted. The consumer with isolation.level=read_committed will not see messages from aborted transactions.",
     ["Transaction logic has errors", "Producer crashed during transaction", "Coordinator timed out transaction"],
     ["grep 'abort\\|transaction' /path/to/producer-logs/stderr.log"]),

    ("kafka-concurrent-transaction", "Kafka Concurrent Transaction Error",
     "Fix Kafka concurrent transaction error. Resolve multiple concurrent transaction issues.",
     "Two producers with the same transactional.id attempt concurrent transactions. One producer fences the other.",
     ["Multiple producers share same transactional.id", "Producer instances not managed", "Application restart caused duplicate ID"],
     ["grep 'transactional.id' /path/to/producer.config"]),

    ("kafka-log-cleaner-error", "Kafka Log Cleaner Error",
     "Fix Kafka log cleaner error. Resolve log compaction and cleanup issues.",
     "The log cleaner encounters errors while compacting topic logs. This can be caused by corrupted log segments or insufficient memory.",
     ["Log segments are corrupted", "Cleaner threads have insufficient memory", "log.cleaner.enable is false"],
     ["grep 'log.cleaner' /etc/kafka/server.properties"]),

    ("kafka-unclean-shutdown", "Kafka Unclean Shutdown Error",
     "Fix Kafka unclean shutdown error. Resolve broker recovery after unclean termination.",
     "The broker was not shut down gracefully. On restart, it needs to recover logs and may encounter data corruption or inconsistent state.",
     ["Broker was killed with SIGKILL", "Power failure caused shutdown", "OOM killed the broker process"],
     ["kafka-log-dirs.sh --bootstrap-server localhost:9092 --verify --broker-ids 0"]),

    ("kafka-corrupt-log-segment", "Kafka Corrupt Log Segment Error",
     "Fix Kafka corrupt log segment error. Resolve log file corruption issues.",
     "A log segment file is corrupted. The broker cannot read the segment, which may cause data loss or partition unavailability.",
     ["Disk failure corrupted the segment", "Unclean shutdown caused corruption", "Bug in Kafka log handling"],
     ["kafka-log-dirs.sh --bootstrap-server localhost:9092 --verify --broker-ids 0"]),

    ("kafka-disk-full", "Kafka Disk Full Error",
     "Fix Kafka disk full error. Resolve disk space exhaustion on broker nodes.",
     "The broker runs out of disk space. New message production fails and the broker may go offline if log.dirs is full.",
     ["Disk usage has reached capacity", "Log retention is not cleaning up", "Topics have grown too large"],
     ["df -h /var/lib/kafka",
      "kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all"]),

    ("kafka-log-retention", "Kafka Log Retention Error",
     "Fix Kafka log retention error. Resolve log segment retention and cleanup issues.",
     "Log retention is not working as expected. Segments may not be deleted, or data is being deleted too aggressively.",
     ["retention.ms or retention.bytes is misconfigured", "Log cleaner is disabled", "Segment files are locked"],
     ["kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all"]),

    ("kafka-segment-bytes-exceeded", "Kafka Segment Bytes Exceeded Error",
     "Fix Kafka segment bytes exceeded error. Resolve log segment size issues.",
     "A log segment exceeds the configured segment.bytes size. This can affect performance and compaction efficiency.",
     ["segment.bytes is too small", "Roll interval triggered early", "Message sizes are inconsistent"],
     ["kafka-configs.sh --bootstrap-server localhost:9092 --describe --topic my-topic --all"]),

    ("kafka-index-corruption", "Kafka Index Corruption Error",
     "Fix Kafka index corruption error. Resolve offset and time index file issues.",
     "The offset or time index file is corrupted. The broker cannot efficiently locate messages in the log.",
     ["Disk failure corrupted index", "Unclean shutdown during index write", "Index file exceeded max size"],
     ["kafka-log-dirs.sh --bootstrap-server localhost:9092 --verify --broker-ids 0"]),

    ("kafka-time-index-not-found", "Kafka Time Index Not Found Error",
     "Fix Kafka time index not found error. Resolve time-based index lookup issues.",
     "The time index for a log segment is missing or corrupt. Time-based lookups fall back to linear search, degrading performance.",
     ["Time index was deleted during cleanup", "Segment was created without index", "Index corruption caused deletion"],
     ["kafka-log-dirs.sh --bootstrap-server localhost:9092 --describe --broker-ids 0"]),

    ("kafka-memory-buffer-exhausted", "Kafka Memory Buffer Exhausted Error",
     "Fix Kafka memory buffer exhausted error. Resolve broker memory pressure issues.",
     "The broker memory buffer is exhausted. Too many requests are queued, or the broker is under memory pressure.",
     ["Heap size is too small", "Too many concurrent requests", "Memory leak in broker"],
     ["grep 'KAFKA_HEAP_OPTS' /etc/kafka/kafka-server-start.sh"]),

    ("kafka-replica-fetch-failure", "Kafka Replica Fetch Failure Error",
     "Fix Kafka replica fetch failure error. Resolve inter-broker replication issues.",
     "A follower replica fails to fetch data from the leader. The replica falls out of sync and may be removed from the ISR.",
     ["Network between brokers is slow", "Leader is overloaded", "replica.fetch.max.bytes is too low"],
     ["kafka-replica-verification.sh --bootstrap-server localhost:9092 --topic-Whitelist '.*'"]),

    ("kafka-out-of-sync-replica", "Kafka Out of Sync Replica Error",
     "Fix Kafka out of sync replica error. Resolve replica synchronization issues.",
     "A replica is out of sync with the leader. The replica may be lagging due to network issues, broker overload, or configuration problems.",
     ["Replica cannot keep up with leader", "Network latency between brokers", "Replica fetch settings are too restrictive"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic"]),

    ("kafka-isr-shrink", "Kafka ISR Shrink Error",
     "Fix Kafka ISR shrink error. Resolve in-sync replica set reduction issues.",
     "The ISR shrinks because a replica cannot keep up with the leader. This reduces fault tolerance.",
     ["Replica is falling behind", "replica.lag.time.max.ms is too short", "Broker is overloaded"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic"]),

    ("kafka-partition-reassignment", "Kafka Partition Reassignment Error",
     "Fix Kafka partition reassignment error. Resolve partition movement issues.",
     "The partition reassignment fails or gets stuck. This can be caused by broker failures during reassignment or insufficient disk space.",
     ["Target broker has insufficient disk space", "Reassignment JSON is invalid", "Broker failed during reassignment"],
     ["kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --verify --reassignment-json-file reassignment.json"]),

    ("kafka-preferred-leader-election", "Kafka Preferred Leader Election Error",
     "Fix Kafka preferred leader election error. Resolve leader balance issues.",
     "Preferred leader election fails or does not complete. The preferred leader may not be in the ISR or the election is not triggered.",
     ["Preferred leader is not in ISR", "auto.leader.rebalance.enable is false", "Controller is not available"],
     ["kafka-leader-election.sh --bootstrap-server localhost:9092 --election-type preferred --all-topic-partitions"]),

    ("kafka-rack-awareness", "Kafka Rack Awareness Error",
     "Fix Kafka rack awareness error. Resolve cross-rack replication placement issues.",
     "Partition replicas are not distributed across racks as expected. The rack configuration is incorrect or broker.rack is not set.",
     ["broker.rack is not configured", "Rack IDs are wrong", "Replication does not respect rack placement"],
     ["grep broker.rack /etc/kafka/server.properties",
      "kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic"]),

    ("kafka-mirror-maker-error", "Kafka MirrorMaker Error",
     "Fix Kafka MirrorMaker error. Resolve cross-cluster replication issues.",
     "MirrorMaker fails to replicate data between clusters. This can be caused by connectivity issues, configuration errors, or consumer lag.",
     ["Source or target cluster is unreachable", "MirrorMaker config is wrong", "Consumer lag on MirrorMaker group"],
     ["kafka-consumer-groups.sh --bootstrap-server source:9092 --describe --group mirror-maker-2"]),

    ("kafka-connect-worker-error", "Kafka Connect Worker Error",
     "Fix Kafka Connect worker error. Resolve Connect cluster worker issues.",
     "A Kafka Connect worker fails to start or crashes. This can be caused by configuration errors, plugin issues, or resource exhaustion.",
     ["Worker configuration is wrong", "Plugin JARs are missing", "Worker ran out of memory"],
     ["curl http://localhost:8083/connectors",
      "curl http://localhost:8083/connector-plugins"]),

    ("kafka-connector-failed", "Kafka Connector Failed Error",
     "Fix Kafka connector failed error. Resolve connector task failures.",
     "A connector task fails and enters the FAILED state. The connector stops processing data until it is restarted or reconfigured.",
     ["Task configuration is wrong", "Target system is unreachable", "Schema mismatch"],
     ["curl http://localhost:8083/connectors/my-connector/status"]),

    ("kafka-connector-not-found", "Kafka Connector Not Found Error",
     "Fix Kafka connector not found error. Resolve connector reference issues.",
     "The requested connector does not exist in the Connect cluster. It may have been deleted or never created.",
     ["Connector was never created", "Connector was deleted", "Connector name is misspelled"],
     ["curl http://localhost:8083/connectors"]),

    ("kafka-smt-transformation", "Kafka SMT Transformation Error",
     "Fix Kafka SMT transformation error. Resolve Single Message Transform issues.",
     "A Single Message Transform fails during message processing. The transform configuration is incorrect or the message format is incompatible.",
     ["SMT class is not in classpath", "Transform config is wrong", "Message format is incompatible"],
     ["curl http://localhost:8083/connectors/my-connector/config"]),

    ("kafka-sink-connector-error", "Kafka Sink Connector Error",
     "Fix Kafka sink connector error. Resolve sink connector data delivery issues.",
     "The sink connector fails to deliver data to the target system. This can be caused by connectivity issues, schema mismatches, or target system errors.",
     ["Target system is unreachable", "Schema does not match target", "Connector config is wrong"],
     ["curl http://localhost:8083/connectors/my-sink/status"]),

    ("kafka-source-connector", "Kafka Source Connector Error",
     "Fix Kafka source connector error. Resolve source connector data ingestion issues.",
     "The source connector fails to ingest data from the source system. This can be caused by connectivity issues, authentication failures, or schema problems.",
     ["Source system is unreachable", "Authentication failed", "Schema does not match"],
     ["curl http://localhost:8083/connectors/my-source/status"]),

    ("kafka-connect-rest-api", "Kafka Connect REST API Error",
     "Fix Kafka Connect REST API error. Resolve Connect HTTP API issues.",
     "The Connect REST API returns errors. The request format is invalid, the connector does not exist, or the API is not available.",
     ["Connect worker is not running", "Request format is wrong", "Connector does not exist"],
     ["curl http://localhost:8083/",
      "curl http://localhost:8083/connectors"]),

    ("kafka-connect-cluster", "Kafka Connect Cluster Error",
     "Fix Kafka connect cluster error. Resolve Connect cluster formation issues.",
     "The Connect cluster cannot form or maintain a stable state. Workers cannot coordinate or share connector assignments.",
     ["group.id is misconfigured", "Workers cannot reach Kafka", "Worker heartbeats are failing"],
     ["curl http://localhost:8083/ | python3 -m json.tool"]),

    ("kafka-exactly-once-source", "Kafka Exactly-Once Source Connector Error",
     "Fix Kafka exactly-once source connector error. Resolve EOS source connector issues.",
     "The exactly-once source connector fails. The offset and record tracking are not properly coordinated.",
     ["exactly.once.support is not enabled", "Connector does not support EOS", "Offset flush is misconfigured"],
     ["grep 'exactly.once\\|offset.flush' /etc/kafka/connect-distributed.properties"]),

    ("kafka-status-storage-topic", "Kafka Connect Status Storage Topic Error",
     "Fix Kafka status storage topic error. Resolve Connect status tracking issues.",
     "The status storage topic is not available or misconfigured. Connect cannot track connector and task statuses.",
     ["Status topic does not exist", "Status topic replication factor is too low", "Topic config is wrong"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic connect-cluster-status"]),

    ("kafka-offset-storage-topic", "Kafka Connect Offset Storage Topic Error",
     "Fix Kafka offset storage topic error. Resolve Connect offset tracking issues.",
     "The offset storage topic is not available or misconfigured. Connect cannot track source connector offsets.",
     ["Offset topic does not exist", "Offset topic config is wrong", "Topic retention is too short"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic connect-cluster-offsets"]),

    ("kafka-config-storage-topic", "Kafka Connect Config Storage Topic Error",
     "Fix Kafka config storage topic error. Resolve Connect configuration storage issues.",
     "The config storage topic is not available or misconfigured. Connect cannot store or retrieve connector configurations.",
     ["Config topic does not exist", "Config topic replication is too low", "Topic retention is too short"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic connect-cluster-configs"]),

    ("kafka-stream-thread-error", "Kafka Streams Thread Error",
     "Fix Kafka Streams thread error. Resolve Streams processing thread issues.",
     "A Kafka Streams processing thread fails. This can be caused by deserialization errors, state store issues, or unhandled exceptions in processors.",
     ["Deserialization error in processor", "State store is corrupted", "Unhandled exception in processor"],
     ["grep -i 'exception\\|error' /path/to/streams-logs/stderr.log"]),

    ("kafka-state-store-error", "Kafka Streams State Store Error",
     "Fix Kafka Streams state store error. Resolve RocksDB state store issues.",
     "The Streams state store encounters errors. RocksDB may have corruption, disk full, or configuration issues.",
     ["RocksDB data is corrupted", "Disk is full", "RocksDB native libraries are missing"],
     ["df -h /tmp/kafka-streams",
      "grep -i 'state.store\\|rocksdb' /path/to/streams-logs/stderr.log"]),

    ("kafka-ktable-not-materialized", "Kafka KTable Not Materialized Error",
     "Fix Kafka KTable not materialized error. Resolve KTable state store issues.",
     "A KTable is not materialized and cannot be queried. The KTable was created without a materialized store or the store was lost.",
     ["KTable was not materialized", "State store was deleted", "Store name is wrong"],
     ["grep -i 'ktable\\|materialized' /path/to/streams-logs/stderr.log"]),

    ("kafka-global-ktable-error", "Kafka Global KTable Error",
     "Fix Kafka Global KTable error. Resolve GlobalKTable replication issues.",
     "A GlobalKTable fails to fully replicate the source topic. The table may not have all partitions or the replication is incomplete.",
     ["Source topic is not fully available", "Replication is slow", "GlobalKTable store is corrupted"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-global-topic"]),

    ("kafka-interactive-query", "Kafka Interactive Query Error",
     "Fix Kafka interactive query error. Resolve Streams interactive query issues.",
     "Interactive queries to a Kafka Streams application fail. The state store is not available or the query is incorrectly formed.",
     ["State store is not queryable", "Streams app is not running", "Store name does not match"],
     ["grep -i 'interactive.query\\|queryable' /path/to/streams-logs/stderr.log"]),

    ("kafka-stream-topology-error", "Kafka Stream Topology Error",
     "Fix Kafka stream topology error. Resolve Streams topology build issues.",
     "The Kafka Streams topology fails to build or execute. The topology graph has errors or invalid processor connections.",
     ["Topology has invalid processor", "Source and sink topics do not exist", "Processor is not connected"],
     ["grep -i 'topology\\|processor' /path/to/streams-logs/stderr.log"]),

    ("kafka-processor-not-connected", "Kafka Processor Not Connected Error",
     "Fix Kafka processor not connected error. Resolve Streams processor wiring issues.",
     "A processor in the Streams topology is not connected to other processors. The topology graph is broken.",
     ["Processor was not added to topology", "Edges are missing between processors", "Branch predicate is wrong"],
     ["grep -i 'processor\\|topology' /path/to/streams-logs/stderr.log"]),

    ("kafka-window-time", "Kafka Window Time Error",
     "Fix Kafka window time error. Resolve Streams windowing configuration issues.",
     "The window time configuration in Kafka Streams is invalid. Windows are not aligned or the grace period is wrong.",
     ["Window size is too small", "Grace period is negative", "Time semantics are wrong"],
     ["grep -i 'window\\|grace' /path/to/streams-logs/stderr.log"]),

    ("kafka-suppress-operator", "Kafka Suppress Operator Error",
     "Fix Kafka suppress operator error. Resolve Streams suppress configuration issues.",
     "The suppress operator in Kafka Streams is misconfigured. Buffered records are not released as expected.",
     ["Suppress buffer is too small", "Time window is too long", "Emit strategy is wrong"],
     ["grep -i 'suppress\\|buffer' /path/to/streams-logs/stderr.log"]),

    ("kafka-punctuation-not-scheduled", "Kafka Punctuation Not Scheduled Error",
     "Fix Kafka punctuation not scheduled error. Resolve Streams periodic task scheduling issues.",
     "The punctuation (periodic callback) in Kafka Streams is not being scheduled. The processor does not execute timed operations.",
     ["Punctuation was not registered", "Scheduler is not started", "Interval is too large"],
     ["grep -i 'punctuation\\|scheduler' /path/to/streams-logs/stderr.log"]),

    ("kafka-rebalance-in-streams", "Kafka Rebalance in Streams Error",
     "Fix Kafka rebalance in streams error. Resolve Streams rebalancing issues.",
     "Frequent rebalances occur in Kafka Streams. The application is slow to rebalance or rebalances too often.",
     ["Rebalance interval is too short", "Processing is slow causing timeout", "State store restoration is slow"],
     ["grep -i 'rebalance\\|assignor' /path/to/streams-logs/stderr.log"]),

    ("kafka-console-tools-error", "Kafka Console Tools Error",
     "Fix Kafka console tools error. Resolve kafka-console-consumer.sh and kafka-console-producer.sh issues.",
     "The console consumer or producer fails. The topic does not exist, the broker is unreachable, or serialization fails.",
     ["Broker is unreachable", "Topic does not exist", "Serializer is misconfigured"],
     ["kafka-topics.sh --bootstrap-server localhost:9092 --list",
      "kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my-topic --from-beginning"]),

    ("kafka-storage-tool-error", "Kafka Storage Tool Error",
     "Fix Kafka storage tool error. Resolve kafka-storage.sh command issues.",
     "The kafka-storage.sh tool fails to format or verify storage. The cluster ID is wrong or the directory is not empty.",
     ["Cluster ID is wrong", "Storage directory is not empty", "Config file is wrong"],
     ["kafka-metadata.sh --snapshot /path/to/metadata.log"]),

    ("kafka-reassign-partitions-error", "Kafka Reassign Partitions Error",
     "Fix Kafka reassign partitions error. Resolve partition reassignment failures.",
     "Partition reassignment fails. The target broker does not have enough disk space or the reassignment JSON is invalid.",
     ["Target broker disk space is low", "Reassignment JSON is invalid", "Broker is offline"],
     ["kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --verify --reassignment-json-file reassignment.json"]),

    ("kafka-producer-performance", "Kafka Producer Performance Error",
     "Fix Kafka producer performance error. Resolve producer throughput issues.",
     "Producer throughput is lower than expected. This can be caused by batches being too small, acks=all, or network congestion.",
     ["Batches are too small", "acks=all adds latency", "Network is congested"],
     ["grep 'batch.size\\|linger.ms\\|compression.type' /path/to/producer.config"]),

    ("kafka-consumer-lag", "Kafka Consumer Lag Error",
     "Fix Kafka consumer lag error. Resolve consumer falling behind issues.",
     "Consumer lag increases over time. The consumer processes messages slower than they are produced.",
     ["Consumer processing is slow", "Not enough consumers for partitions", "Message production rate is high"],
     ["kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group"]),

    ("kafka-message-conversion", "Kafka Message Conversion Error",
     "Fix Kafka message conversion error. Resolve inter-protocol message conversion issues.",
     "Message conversion between protocol versions fails. This happens when clients use different API versions or formats.",
     ["Clients use different API versions", "message.format.version is wrong", "Compression type mismatch"],
     ["grep 'message.format.version\\|compression.type' /etc/kafka/server.properties"]),

    ("kafka-jmx-metrics-error", "Kafka JMX Metrics Error",
     "Fix Kafka JMX metrics error. Resolve JMX monitoring and metrics issues.",
     "JMX metrics are not available or incorrectly reported. The JMX port is not configured or the MBeans are not registered.",
     ["JMX port is not enabled", "JMX authentication is blocking access", "MBeans are not registered"],
     ["grep 'JMX_OPTS\\|KAFKA_JMX_OPTS' /etc/kafka/kafka-server-start.sh"]),

    ("kafka-metrics-reporter", "Kafka Metrics Reporter Error",
     "Fix Kafka metrics reporter error. Resolve custom metrics reporter issues.",
     "A custom metrics reporter fails to report metrics. The reporter class is missing or misconfigured.",
     ["Reporter class is missing from classpath", "Reporter config is wrong", "Reporter throws exceptions"],
     ["grep 'metric.reporters' /etc/kafka/server.properties"]),

    ("kafka-deprecated-api", "Kafka Deprecated API Error",
     "Fix Kafka deprecated API error. Resolve usage of deprecated Kafka APIs.",
     "The application uses a deprecated Kafka API. The API may be removed in a future version and should be migrated.",
     ["API is deprecated in current version", "Client library is outdated", "Feature was removed"],
     ["grep -r 'api.version' /path/to/application"]),
]

def make_page(slug, title, desc, body, causes, fixes, examples):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["kafka"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        '---',
        '',
        f'# {title}',
        '',
        body,
        '',
        '## Common Causes',
        '',
    ]
    for c in causes:
        lines.append(f'- {c}')
    lines.append('')
    lines.append('## How to Fix')
    lines.append('')
    for i, fix in enumerate(fixes, 1):
        lines.append(f'### Solution {i}')
        lines.append('')
        lines.append('```bash')
        lines.append(fix)
        lines.append('```')
        lines.append('')
    if examples:
        lines.append('## Examples')
        lines.append('')
        for ex in examples:
            lines.append('```bash')
            lines.append(ex)
            lines.append('```')
            lines.append('')
    related = [
        '- [Kafka Broker Error]({{< relref "/tools/kafka/kafka-broker-error" >}})',
        '- [Kafka Topic Error]({{< relref "/tools/kafka/kafka-topic-error" >}})',
        '- [Kafka Consumer Error]({{< relref "/tools/kafka/kafka-consumer-error" >}})',
        '- [Kafka Producer Error]({{< relref "/tools/kafka/kafka-producer-error" >}})',
    ]
    lines.append('## Related Pages')
    lines.append('')
    lines.extend(related)
    lines.append('')
    return '\n'.join(lines)


count = 0
skipped = 0
for page in PAGES:
    slug, title, desc, body, causes, fixes = page[:6]
    examples = page[6] if len(page) > 6 else []
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        skipped += 1
        continue
    content = make_page(slug, title, desc, body, causes, fixes, examples)
    path = os.path.join(TOOL_DIR, f'{slug}.md')
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {skipped}")
total = len([f for f in os.listdir(TOOL_DIR) if f.endswith('.md')])
print(f"Total .md files in kafka/: {total}")
