#!/usr/bin/env python3
"""Generate new RabbitMQ error pages to expand to 100+ total."""
import os

TOOL_DIR = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/rabbitmq/'
EXISTING = {f.replace('.md', '') for f in os.listdir(TOOL_DIR) if f.endswith('.md')}

PAGES = [
    ("rabbitmq-connection-refused", "RabbitMQ Connection Refused Error",
     "Fix RabbitMQ connection refused error. Resolve TCP connection issues to the broker.",
     "The client cannot connect to the RabbitMQ broker. The connection is actively refused by the server.",
     ["RabbitMQ service is not running", "RabbitMQ is not listening on the expected port", "Firewall is blocking the connection"],
     ["rabbitmqctl status", "ss -tlnp | grep 5672", "sudo systemctl start rabbitmq-server"]),

    ("rabbitmq-amqp-handshake-timeout", "RabbitMQ AMQP Handshake Timeout Error",
     "Fix RabbitMQ AMQP handshake timeout error. Resolve connection establishment timeout issues.",
     "The AMQP handshake times out before completing. The client and broker fail to negotiate protocol parameters.",
     ["Network latency between client and broker", "Broker is overloaded", "Handshake timeout is too low"],
     ["rabbitmqctl status", "netstat -an | grep 5672"]),

    ("rabbitmq-authentication-failure", "RabbitMQ Authentication Failure Error",
     "Fix RabbitMQ authentication failure error. Resolve user credential and authentication issues.",
     "The client fails to authenticate with the broker. The username or password is incorrect.",
     ["Username or password is incorrect", "User does not exist", "Authentication backend is misconfigured"],
     ["rabbitmqctl list_users", "rabbitmqctl authenticate_user myuser mypassword"]),

    ("rabbitmq-login-refused", "RabbitMQ Login Refused Error",
     "Fix RabbitMQ login refused error. Resolve authentication refusal issues.",
     "The broker refuses the login attempt. The user is not authorized or the account is locked.",
     ["User account is disabled", "User not allowed from this IP", "SASL mechanism not supported"],
     ["rabbitmqctl list_users", "rabbitmqctl set_user_tags myuser administrator"]),

    ("rabbitmq-guest-user-restricted", "RabbitMQ Guest User Restricted Error",
     "Fix RabbitMQ guest user restricted error. Resolve guest user access limitations.",
     "The guest user can only connect from localhost by default. Remote connections with guest are rejected.",
     ["Guest user trying to connect remotely", "loopback_users not configured", "Default security policy restricts guest"],
     ["rabbitmqctl add_user myuser mypassword",
      "rabbitmqctl set_user_tags myuser administrator",
      "rabbitmqctl set_permissions -p / myuser '.*' '.*' '.*'"]),

    ("rabbitmq-user-not-found", "RabbitMQ User Not Found Error",
     "Fix RabbitMQ user not found error. Resolve user existence issues.",
     "The specified user does not exist in RabbitMQ. The user may have been deleted or was never created.",
     ["User was never created", "User was deleted", "Username is misspelled"],
     ["rabbitmqctl list_users", "rabbitmqctl add_user myuser mypassword"]),

    ("rabbitmq-vhost-not-found", "RabbitMQ Virtual Host Not Found Error",
     "Fix RabbitMQ virtual host not found error. Resolve vhost reference issues.",
     "The virtual host does not exist. The client is connecting to a vhost that was never created.",
     ["Virtual host was never created", "Virtual host was deleted", "Vhost name is misspelled"],
     ["rabbitmqctl list_vhosts", "rabbitmqctl add_vhost myvhost"]),

    ("rabbitmq-permissions-not-granted", "RabbitMQ Permissions Not Granted Error",
     "Fix RabbitMQ permissions not granted error. Resolve user permission issues.",
     "The user does not have the required permissions on the virtual host.",
     ["User has no permissions on target vhost", "Permission regex does not match", "Configure or write permissions missing"],
     ["rabbitmqctl list_permissions -p myvhost",
      "rabbitmqctl set_permissions -p myvhost myuser '.*' '.*' '.*'"]),

    ("rabbitmq-channel-error", "RabbitMQ Channel Error",
     "Fix RabbitMQ channel error. Resolve AMQP channel-level issues.",
     "A channel-level error occurs. The channel is closed by the broker due to an invalid operation.",
     ["Protocol violation on channel", "Queue or exchange does not exist", "Channel max exceeded"],
     ["rabbitmqctl list_queues", "rabbitmqctl list_exchanges"]),

    ("rabbitmq-channel-max-exceeded", "RabbitMQ Channel Max Exceeded Error",
     "Fix RabbitMQ channel max exceeded error. Resolve channel limit issues.",
     "The connection has reached the maximum number of channels allowed.",
     ["Channel limit per connection is reached", "Default limit is 2047", "Application opens too many channels"],
     ["grep channel_max /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-connection-blocked", "RabbitMQ Connection Blocked Error",
     "Fix RabbitMQ connection blocked error. Resolve memory or disk alarm blocking issues.",
     "The broker blocks the connection due to resource alarms (memory or disk). Publish operations are paused.",
     ["Memory alarm is triggered", "Disk free space alarm is triggered", "Flow control is active"],
     ["rabbitmqctl status", "rabbitmqctl set_vm_memory_high_watermark.relative 0.6"]),

    ("rabbitmq-alarm-in-effect", "RabbitMQ Alarm In Effect Error",
     "Fix RabbitMQ alarm in effect error. Resolve broker alarm conditions.",
     "An alarm is active on the broker, preventing normal operations. The broker may block publishers.",
     ["Memory high watermark alarm", "Disk free space alarm", "Partition alarm in cluster"],
     ["rabbitmqctl status"]),

    ("rabbitmq-memory-alarm", "RabbitMQ Memory Alarm Error",
     "Fix RabbitMQ memory alarm error. Resolve memory usage threshold issues.",
     "The memory high watermark alarm is triggered. The broker blocks publishers to prevent OOM.",
     ["Memory usage exceeds high watermark", "Queues accumulating faster than consumed", "Memory-intensive operations running"],
     ["rabbitmqctl set_vm_memory_high_watermark.relative 0.6", "rabbitmqctl status"]),

    ("rabbitmq-disk-alarm", "RabbitMQ Disk Alarm Error",
     "Fix RabbitMQ disk alarm error. Resolve disk space threshold issues.",
     "The disk free space alarm is triggered. The broker blocks publishers to prevent running out of disk space.",
     ["Disk free space is below limit", "Queues accumulating messages on disk", "Log files consuming too much space"],
     ["df -h", "rabbitmqctl set_disk_free_limit '2GB'"]),

    ("rabbitmq-low-disk-watermark", "RabbitMQ Low Disk Watermark Error",
     "Fix RabbitMQ low disk watermark error. Resolve disk space monitoring issues.",
     "The disk space is approaching the low watermark. The broker may trigger the disk alarm soon.",
     ["Disk space is declining", "Large queues filling disk", "Retention policies not set"],
     ["df -h", "rabbitmqctl status"]),

    ("rabbitmq-free-disk-space", "RabbitMQ Free Disk Space Error",
     "Fix RabbitMQ free disk space error. Resolve disk space exhaustion issues.",
     "RabbitMQ has insufficient free disk space. The broker cannot write messages to disk.",
     ["Disk is full or nearly full", "Mnesia database grown too large", "Message store files consuming disk"],
     ["df -h", "rabbitmqctl list_queues name messages disk_persistent"]),

    ("rabbitmq-too-many-connections", "RabbitMQ Too Many Connections Error",
     "Fix RabbitMQ too many connections error. Resolve connection limit issues.",
     "The broker has too many connections. New connection attempts are rejected.",
     ["Connection limit is reached", "Applications not closing connections", "Connection pooling not configured"],
     ["rabbitmqctl list_connections"]),

    ("rabbitmq-connection-forced-close", "RabbitMQ Connection Forced Close Error",
     "Fix RabbitMQ connection forced close error. Resolve broker-initiated connection closures.",
     "The broker forcibly closes a connection. This may be due to protocol errors, idle timeout, or policy.",
     ["Heartbeat timeout exceeded", "Protocol violation detected", "Connection was idle too long"],
     ["grep heartbeat /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-frame-too-large", "RabbitMQ Frame Too Large Error",
     "Fix RabbitMQ frame too large error. Resolve frame size limit issues.",
     "The client sends a frame that exceeds the broker maximum frame size.",
     ["Frame exceeds frame_max setting", "Message is larger than allowed", "Client and broker frame_max mismatch"],
     ["grep frame_max /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-heartbeat-timeout", "RabbitMQ Heartbeat Timeout Error",
     "Fix RabbitMQ heartbeat timeout error. Resolve connection keepalive issues.",
     "The connection heartbeat times out. The broker or client detects a dead connection.",
     ["Heartbeat timeout is too short", "Network issues cause delayed heartbeats", "Client is too busy to send heartbeats"],
     ["grep heartbeat /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-channel-connection-not-found", "RabbitMQ Channel or Connection Not Found Error",
     "Fix RabbitMQ channel or connection not found error. Resolve resource reference issues.",
     "The specified channel or connection does not exist. It may have been closed.",
     ["Channel was already closed", "Connection was dropped", "Resource ID is incorrect"],
     ["rabbitmqctl list_connections", "rabbitmqctl list_channels"]),

    ("rabbitmq-queue-not-found", "RabbitMQ Queue Not Found Error",
     "Fix RabbitMQ queue not found error. Resolve missing queue issues.",
     "The specified queue does not exist. Publishing or consuming from a non-existent queue fails.",
     ["Queue was never declared", "Queue was deleted by policy or TTL", "Queue name is misspelled"],
     ["rabbitmqctl list_queues name",
      "rabbitmqadmin declare queue name=myqueue durable=true"]),

    ("rabbitmq-queue-exists", "RabbitMQ Queue Already Exists Error",
     "Fix RabbitMQ queue already exists error. Resolve queue declaration conflicts.",
     "The queue already exists with different properties than requested. AMQP requires matching properties.",
     ["Queue declared with different arguments", "Durable setting conflicts", "Autodelete setting conflicts"],
     ["rabbitmqctl list_queues name durable auto_delete"]),

    ("rabbitmq-queue-already-declared", "RabbitMQ Queue Already Declared Error",
     "Fix RabbitMQ queue already declared error. Resolve duplicate queue declaration issues.",
     "The queue is already declared with incompatible properties by another connection.",
     ["Another connection declared with different properties", "Auto-delete or exclusive settings conflict", "Arguments do not match"],
     ["rabbitmqctl list_queues name arguments"]),

    ("rabbitmq-queue-not-bound", "RabbitMQ Queue Not Bound Error",
     "Fix RabbitMQ queue not bound error. Resolve missing queue binding issues.",
     "The queue is not bound to any exchange. Messages published to exchanges may not reach the queue.",
     ["Queue was never bound to an exchange", "Binding was deleted", "Binding key does not match routing key"],
     ["rabbitmqctl list_bindings",
      "rabbitmqadmin declare binding source=myexchange destination=myqueue routing_key=mykey"]),

    ("rabbitmq-queue-exclusive", "RabbitMQ Exclusive Queue Error",
     "Fix RabbitMQ exclusive queue error. Resolve exclusive queue access issues.",
     "An exclusive queue can only be used by the connection that declared it. Other connections cannot access it.",
     ["Another connection tries to consume from exclusive queue", "Owner connection is closed", "Queue declared as exclusive by another client"],
     ["rabbitmqadmin declare queue name=myqueue exclusive=false"]),

    ("rabbitmq-exclusive-consumer", "RabbitMQ Exclusive Consumer Error",
     "Fix RabbitMQ exclusive consumer error. Resolve exclusive consumer lock issues.",
     "The queue already has an exclusive consumer. Only one consumer can be exclusive on a queue.",
     ["Another consumer already has exclusive access", "basic.consume with exclusive=true on occupied queue", "Previous consumer did not cancel properly"],
     ["rabbitmqctl list_consumers"]),

    ("rabbitmq-consumer-cancelled", "RabbitMQ Consumer Cancelled Error",
     "Fix RabbitMQ consumer cancelled error. Resolve unexpected consumer cancellation issues.",
     "The broker cancels the consumer. This can happen due to queue deletion, TTL expiry, or policy changes.",
     ["Queue was deleted or expired", "Consumer cancelled via management UI", "Queue was moved or redeclared"],
     ["rabbitmqctl list_queues name"]),

    ("rabbitmq-consumer-not-found", "RabbitMQ Consumer Not Found Error",
     "Fix RabbitMQ consumer not found error. Resolve consumer reference issues.",
     "The specified consumer does not exist. It may have been cancelled or the consumer tag is wrong.",
     ["Consumer was cancelled", "Consumer tag is incorrect", "Connection dropped and consumer removed"],
     ["rabbitmqctl list_consumers"]),

    ("rabbitmq-basic-get-empty", "RabbitMQ basic.get Empty Error",
     "Fix RabbitMQ basic.get empty error. Resolve empty queue polling issues.",
     "The basic.get request returns no messages. The queue is empty or all messages have been consumed.",
     ["Queue has no messages", "Messages consumed by other consumers", "Message TTL expired all messages"],
     ["rabbitmqctl list_queues name messages"]),

    ("rabbitmq-basic-return", "RabbitMQ basic.return Error",
     "Fix RabbitMQ basic.return error. Resolve unroutable message return issues.",
     "The broker returns a message that could not be routed to any queue. The message is returned to the producer.",
     ["No queue bound with matching routing key", "Mandatory flag set and message unroutable", "Exchange type does not route expected"],
     ["rabbitmqctl list_bindings", "rabbitmqctl list_exchanges"]),

    ("rabbitmq-message-not-routed", "RabbitMQ Message Not Routed Error",
     "Fix RabbitMQ message not routed error. Resolve message delivery failures.",
     "The message is not routed to any queue. The exchange does not have a matching binding.",
     ["Exchange has no bindings to queues", "Routing key does not match binding key", "Exchange type does not match routing pattern"],
     ["rabbitmqadmin list bindings",
      "rabbitmqadmin declare binding source=myexchange destination=myqueue routing_key=mykey"]),

    ("rabbitmq-mandatory-flag", "RabbitMQ Mandatory Flag Error",
     "Fix RabbitMQ mandatory flag error. Resolve mandatory message delivery issues.",
     "Messages published with mandatory flag are returned because they cannot be routed to any queue.",
     ["No queue bound with matching routing key", "Exchange type does not support routing pattern", "Queue deleted after binding"],
     ["rabbitmqctl list_bindings"]),

    ("rabbitmq-immediate-flag", "RabbitMQ Immediate Flag Error",
     "Fix RabbitMQ immediate flag error. Resolve immediate delivery issues.",
     "Messages published with immediate flag are returned because no consumer is ready to receive them.",
     ["No consumer available on target queue", "All consumers are busy", "Queue is empty and no consumer waiting"],
     ["rabbitmqctl list_consumers"]),

    ("rabbitmq-publish-not-confirmed", "RabbitMQ Publish Not Confirmed Error",
     "Fix RabbitMQ publish not confirmed error. Resolve publisher confirm issues.",
     "The publisher confirm is not received. The broker did not confirm the message was received.",
     ["Publisher confirms not enabled on channel", "Broker crashed before confirming", "Channel closed before confirm"],
     ["rabbitmqctl list_channels confirm"]),

    ("rabbitmq-publisher-confirm-timeout", "RabbitMQ Publisher Confirm Timeout Error",
     "Fix RabbitMQ publisher confirm timeout error. Resolve confirm timeout issues.",
     "The publisher confirm times out. The broker is too slow to confirm the message.",
     ["Broker is overloaded", "Confirm timeout is too low", "Disk I/O is slow"],
     ["rabbitmqctl status"]),

    ("rabbitmq-publisher-confirm-error", "RabbitMQ Publisher Confirm Error",
     "Fix RabbitMQ publisher confirm error. Resolve confirm notification issues.",
     "The publisher confirm indicates a negative acknowledgment. The message was not stored.",
     ["Broker rejected the message", "Disk alarm is active", "Memory alarm is active"],
     ["rabbitmqctl status"]),

    ("rabbitmq-transaction-commit-failed", "RabbitMQ Transaction Commit Failed Error",
     "Fix RabbitMQ transaction commit failed error. Resolve AMQP transaction issues.",
     "The AMQP transaction commit fails. Operations within the transaction cannot be committed.",
     ["Transaction includes invalid operations", "Channel closed during transaction", "Broker error during commit"],
     ["rabbitmqctl list_channels"]),

    ("rabbitmq-transaction-rollback", "RabbitMQ Transaction Rollback Error",
     "Fix RabbitMQ transaction rollback error. Resolve AMQP transaction rollback issues.",
     "The AMQP transaction rollback fails. The transaction state cannot be properly reverted.",
     ["Channel closed before rollback", "Broker error during rollback", "Transaction state is inconsistent"],
     ["rabbitmqctl list_channels"]),

    ("rabbitmq-tx-select-error", "RabbitMQ tx.select Error",
     "Fix RabbitMQ tx.select error. Resolve AMQP transaction mode activation issues.",
     "The tx.select command fails. The channel cannot enter transaction mode.",
     ["Channel is already in transaction mode", "Channel was closed", "Protocol error occurred"],
     ["rabbitmqctl list_channels"]),

    ("rabbitmq-binding-not-found", "RabbitMQ Binding Not Found Error",
     "Fix RabbitMQ binding not found error. Resolve binding deletion or lookup issues.",
     "The specified binding does not exist. It may have been deleted or the parameters are wrong.",
     ["Binding was deleted", "Binding key or arguments do not match", "Exchange or queue does not exist"],
     ["rabbitmqctl list_bindings"]),

    ("rabbitmq-exchange-not-found", "RabbitMQ Exchange Not Found Error",
     "Fix RabbitMQ exchange not found error. Resolve missing exchange issues.",
     "The specified exchange does not exist. Publishing to a non-existent exchange fails.",
     ["Exchange was never declared", "Exchange was deleted", "Exchange name is misspelled"],
     ["rabbitmqctl list_exchanges",
      "rabbitmqadmin declare exchange name=myexchange type=direct durable=true"]),

    ("rabbitmq-exchange-exists", "RabbitMQ Exchange Already Exists Error",
     "Fix RabbitMQ exchange already exists error. Resolve exchange declaration conflicts.",
     "The exchange already exists with different properties than requested.",
     ["Exchange declared with different type or properties", "Durable setting conflicts", "Auto-delete setting conflicts"],
     ["rabbitmqctl list_exchanges name type durable auto_delete"]),

    ("rabbitmq-exchange-type-invalid", "RabbitMQ Exchange Type Invalid Error",
     "Fix RabbitMQ exchange type invalid error. Resolve exchange type configuration issues.",
     "The specified exchange type is not valid. RabbitMQ does not recognize the type.",
     ["Exchange type name is misspelled", "Exchange type plugin is not enabled", "Custom exchange type not installed"],
     ["rabbitmq-plugins list"]),

    ("rabbitmq-direct-exchange", "RabbitMQ Direct Exchange Error",
     "Fix RabbitMQ direct exchange error. Resolve direct exchange routing issues.",
     "Messages in a direct exchange are not routed correctly. The routing key does not match binding keys.",
     ["Routing key does not exactly match binding key", "No binding exists for routing key", "Exchange type is not direct"],
     ["rabbitmqctl list_bindings"]),

    ("rabbitmq-topic-exchange-pattern", "RabbitMQ Topic Exchange Pattern Error",
     "Fix RabbitMQ topic exchange pattern error. Resolve topic routing pattern issues.",
     "Messages in a topic exchange are not routed correctly. The routing key does not match binding patterns.",
     ["Routing key does not match binding pattern", "Binding pattern syntax is incorrect", "Dot separator is missing"],
     ["rabbitmqctl list_bindings"]),

    ("rabbitmq-fanout-exchange", "RabbitMQ Fanout Exchange Error",
     "Fix RabbitMQ fanout exchange error. Resolve fanout broadcasting issues.",
     "Messages in a fanout exchange are not delivered to all bound queues. Some queues may be missing.",
     ["Not all queues bound to fanout exchange", "Queue binding was removed", "Queue is exclusive or auto-delete"],
     ["rabbitmqctl list_bindings source=fanout-exchange"]),

    ("rabbitmq-headers-exchange", "RabbitMQ Headers Exchange Error",
     "Fix RabbitMQ headers exchange error. Resolve header-based routing issues.",
     "Messages in a headers exchange are not routed correctly. Header matching is not working as expected.",
     ["x-match logic is incorrect (all vs any)", "Headers do not match binding arguments", "Message headers are missing"],
     ["rabbitmqctl list_bindings"]),

    ("rabbitmq-binding-key-mismatch", "RabbitMQ Binding Key Mismatch Error",
     "Fix RabbitMQ binding key mismatch error. Resolve routing key and binding key mismatches.",
     "The routing key on the published message does not match the binding key on the queue binding.",
     ["Routing key format is wrong", "Binding key was set incorrectly", "Case sensitivity in routing keys"],
     ["rabbitmqctl list_bindings"]),

    ("rabbitmq-queue-length-limit", "RabbitMQ Queue Length Limit Error",
     "Fix RabbitMQ queue length limit error. Resolve maximum queue length issues.",
     "The queue has reached its maximum length limit. New messages are rejected or dropped.",
     ["Queue max-length is set and reached", "Messages published faster than consumed", "DLX not configured for overflow"],
     ["rabbitmqctl list_queues name messages consumers"]),

    ("rabbitmq-max-length-bytes", "RabbitMQ Max Length Bytes Error",
     "Fix RabbitMQ max length bytes error. Resolve byte-size queue limit issues.",
     "The queue has reached its maximum byte size limit. New messages are rejected.",
     ["Queue max-length-bytes is reached", "Messages are large and fill limit quickly", "Consumers are not keeping up"],
     ["rabbitmqctl list_queues name messages bytes"]),

    ("rabbitmq-overflow-behaviour", "RabbitMQ Overflow Behaviour Error",
     "Fix RabbitMQ overflow behaviour error. Resolve queue overflow handling issues.",
     "The queue overflow behaviour is not configured as expected. Messages are dropped instead of rejected.",
     ["Overflow not set (default: drop-head)", "reject-publish needed but not configured", "Dead-lettering not configured"],
     ["rabbitmqadmin declare queue name=myqueue arguments='{\"x-max-length\":1000,\"x-overflow\":\"reject-publish\"}'"]),

    ("rabbitmq-per-queue-ttl", "RabbitMQ Per-Queue TTL Error",
     "Fix RabbitMQ per-queue TTL error. Resolve queue time-to-live issues.",
     "Messages in the queue expire before being consumed. The TTL is set too low.",
     ["x-message-ttl is set too short", "Messages expire before consumers process them", "TTL value in ms is too small"],
     ["rabbitmqadmin declare queue name=myqueue arguments='{\"x-message-ttl\":86400000}'"]),

    ("rabbitmq-message-ttl-expired", "RabbitMQ Message TTL Expired Error",
     "Fix RabbitMQ message TTL expired error. Resolve message expiration issues.",
     "Messages expire before they can be consumed. The TTL value is too short for the processing time.",
     ["Message TTL is too short", "Per-message expiration is too small", "Consumer processing time exceeds TTL"],
     ["rabbitmqctl list_queues name messages consumers"]),

    ("rabbitmq-queue-ttl-expired", "RabbitMQ Queue TTL Expired Error",
     "Fix RabbitMQ queue TTL expired error. Resolve queue expiration issues.",
     "The queue itself has expired and been deleted. The queue x-expires argument caused deletion.",
     ["x-expires set and queue is idle", "No consumers or publishes happened", "Queue was auto-deleted by TTL"],
     ["rabbitmqadmin declare queue name=myqueue arguments='{\"x-expires\":3600000}'"]),

    ("rabbitmq-dlx-not-configured", "RabbitMQ Dead Letter Exchange Not Configured Error",
     "Fix RabbitMQ DLX not configured error. Resolve dead lettering setup issues.",
     "Messages are rejected or expire but no dead-letter exchange is configured. Messages are lost.",
     ["No dead-letter-exchange on queue", "Dead-letter-exchange does not exist", "Dead-letter routing key not set"],
     ["rabbitmqadmin declare exchange name=dlx type=fanout",
      "rabbitmqadmin declare queue name=dlq",
      "rabbitmqadmin declare binding source=dlx destination=dlq"]),

    ("rabbitmq-dead-letter-limit", "RabbitMQ Dead Letter Limit Error",
     "Fix RabbitMQ dead letter limit error. Resolve dead letter queue overflow issues.",
     "The dead-letter queue has reached its own limit. Dead-lettered messages are dropped.",
     ["Dead-letter queue has max-length set", "DLQ is not being consumed", "Too many messages being dead-lettered"],
     ["rabbitmqctl list_queues name messages"]),

    ("rabbitmq-message-redelivered", "RabbitMQ Message Redelivered Error",
     "Fix RabbitMQ message redelivered error. Resolve message redelivery issues.",
     "Messages are being redelivered to consumers. The consumer is not acknowledging messages properly.",
     ["Consumer does not send basic.ack", "Consumer crashes before acknowledging", "Requeue is set to true on reject"],
     ["rabbitmqctl list_queues name messages consumers"]),

    ("rabbitmq-requeue-error", "RabbitMQ Requeue Error",
     "Fix RabbitMQ requeue error. Resolve message requeueing issues.",
     "Messages are requeued but cannot be delivered. The requeue operation fails or causes infinite loops.",
     ["Message causes consumer crash and is requeued infinitely", "Requeue puts message at front of queue", "No DLX for poison messages"],
     ["rabbitmqadmin declare queue name=myqueue arguments='{\"x-dead-letter-exchange\":\"dlx\"}'"]),

    ("rabbitmq-cluster-node-not-found", "RabbitMQ Cluster Node Not Found Error",
     "Fix RabbitMQ cluster node not found error. Resolve cluster membership issues.",
     "A node referenced in the cluster is not found or not running. Cluster formation is incomplete.",
     ["Node is down or removed", "Node name mismatch in cluster config", "Erlang cookie is different across nodes"],
     ["rabbitmqctl cluster_status"]),

    ("rabbitmq-cluster-partition", "RabbitMQ Cluster Partition Error",
     "Fix RabbitMQ cluster partition error. Resolve network partition and split-brain issues.",
     "The cluster is partitioned due to a network split. Nodes cannot communicate with each other.",
     ["Network failure split the cluster", "Split-brain handling needs configuration", "Nodes in different availability zones"],
     ["rabbitmqctl cluster_status",
      "grep cluster_partition_handling /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-mnesia-lock", "RabbitMQ Mnesia Lock Error",
     "Fix RabbitMQ Mnesia lock error. Resolve Mnesia database locking issues.",
     "Mnesia cannot acquire the required lock. The database is locked by another process or node.",
     ["Another process is using Mnesia", "Node was not cleanly shut down", "Mnesia waiting for table copy"],
     ["rabbitmqctl status"]),

    ("rabbitmq-schema-db-corruption", "RabbitMQ Schema DB Corruption Error",
     "Fix RabbitMQ schema DB corruption error. Resolve Mnesia schema corruption issues.",
     "The Mnesia schema database is corrupted. RabbitMQ cannot start or operate correctly.",
     ["Disk failure corrupted Mnesia files", "Incomplete shutdown caused corruption", "Transaction log is corrupted"],
     ["rabbitmqctl force_boot", "rabbitmqctl reset"]),

    ("rabbitmq-node-type-mismatch", "RabbitMQ Node Type Mismatch Error",
     "Fix RabbitMQ node type mismatch error. Resolve cluster node role issues.",
     "A node has an incompatible type or role in the cluster. Disc, RAM, or quorum node types conflict.",
     ["Mixing disc and quorum nodes inappropriately", "Node started with wrong type", "Mixed node types conflict"],
     ["rabbitmqctl cluster_status"]),

    ("rabbitmq-cookie-mismatch", "RabbitMQ Cookie Mismatch Error",
     "Fix RabbitMQ cookie mismatch error. Resolve Erlang cookie authentication issues.",
     "Nodes cannot join the cluster because their Erlang cookies do not match.",
     ["Erlang cookie file is different on each node", "Cookie changed after cluster formation", "Cookie file has wrong permissions"],
     ["cat /var/lib/rabbitmq/.erlang.cookie",
      "ls -la /var/lib/rabbitmq/.erlang.cookie"]),

    ("rabbitmq-erlang-cookie", "RabbitMQ Erlang Cookie Error",
     "Fix RabbitMQ Erlang cookie error. Resolve Erlang cookie configuration issues.",
     "The Erlang cookie is not properly configured. Nodes cannot authenticate with each other.",
     ["Cookie file does not exist", "Cookie file has wrong content", "Cookie is not the same on all nodes"],
     ["cat /var/lib/rabbitmq/.erlang.cookie"]),

    ("rabbitmq-cluster-link-error", "RabbitMQ Cluster Link Error",
     "Fix RabbitMQ cluster link error. Resolve inter-node communication issues.",
     "Nodes cannot communicate with each other over the Erlang distribution protocol.",
     ["Network connectivity between nodes broken", "Firewall blocking Erlang ports", "Erlang distribution cookie is wrong"],
     ["ping node2", "nc -zv node2 4369", "nc -zv node2 25672"]),

    ("rabbitmq-federation-link", "RabbitMQ Federation Link Error",
     "Fix RabbitMQ federation link error. Resolve cross-node message federation issues.",
     "The federation link between nodes or exchanges fails. Messages are not federated.",
     ["Federation plugin not enabled", "Upstream URI is wrong", "Network connectivity to upstream broken"],
     ["rabbitmq-plugins list | grep federation", "rabbitmqctl status"]),

    ("rabbitmq-shovel-error", "RabbitMQ Shovel Error",
     "Fix RabbitMQ shovel error. Resolve message shoveling issues between nodes.",
     "The shovel fails to move messages between brokers. The shovel configuration is wrong or the connection fails.",
     ["Shovel plugin not enabled", "Source or destination connection fails", "Shovel configuration is invalid"],
     ["rabbitmq-plugins list | grep shovel", "rabbitmqctl status"]),

    ("rabbitmq-shovel-worker", "RabbitMQ Shovel Worker Error",
     "Fix RabbitMQ shovel worker error. Resolve shovel worker thread issues.",
     "The shovel worker process fails. The worker encounters errors during message transfer.",
     ["Shovel worker encounters connection errors", "Source or destination queue does not exist", "Worker is overloaded"],
     ["rabbitmqctl status"]),

    ("rabbitmq-shovel-reconnection", "RabbitMQ Shovel Reconnection Error",
     "Fix RabbitMQ shovel reconnection error. Resolve shovel auto-recovery issues.",
     "The shovel fails to reconnect after a connection drop. Manual intervention is required.",
     ["Auto-recovery is not enabled", "Reconnection timeout is too short", "Upstream broker is permanently down"],
     ["rabbitmqctl Shovel.status"]),

    ("rabbitmq-management-plugin", "RabbitMQ Management Plugin Error",
     "Fix RabbitMQ management plugin error. Resolve management UI and API issues.",
     "The management plugin is not functioning. The management UI is inaccessible or returning errors.",
     ["Management plugin not enabled", "Management port is blocked", "Management database is overloaded"],
     ["rabbitmq-plugins list | grep management", "ss -tlnp | grep 15672"]),

    ("rabbitmq-management-http-api", "RabbitMQ Management HTTP API Error",
     "Fix RabbitMQ management HTTP API error. Resolve REST API issues.",
     "The management HTTP API returns errors. The request format is wrong or the API is unavailable.",
     ["API endpoint URL is wrong", "Authentication credentials are wrong", "Request body format is invalid"],
     ["curl -u guest:guest http://localhost:15672/api/overview"]),

    ("rabbitmq-stats-not-enabled", "RabbitMQ Stats Not Enabled Error",
     "Fix RabbitMQ stats not enabled error. Resolve statistics collection issues.",
     "Statistics are not being collected. The management stats are disabled or not functioning.",
     ["Stats collection is disabled", "Management database is disabled", "Stats emission interval is too high"],
     ["grep management /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-monitoring-metrics", "RabbitMQ Monitoring Metrics Error",
     "Fix RabbitMQ monitoring metrics error. Resolve Prometheus and monitoring integration issues.",
     "Monitoring metrics are not available or incorrect. The metrics endpoint is not configured.",
     ["Prometheus plugin not enabled", "Metrics endpoint URL is wrong", "Metrics format is incompatible"],
     ["rabbitmq-plugins list | grep prometheus",
      "curl http://localhost:15692/metrics"]),

    ("rabbitmq-mqtt-plugin", "RabbitMQ MQTT Plugin Error",
     "Fix RabbitMQ MQTT plugin error. Resolve MQTT protocol support issues.",
     "The MQTT plugin fails to handle MQTT connections. MQTT clients cannot connect or subscribe.",
     ["MQTT plugin not enabled", "MQTT port 1883 not listening", "MQTT protocol version issue"],
     ["rabbitmq-plugins list | grep mqtt", "ss -tlnp | grep 1883"]),

    ("rabbitmq-stomp-plugin", "RabbitMQ STOMP Plugin Error",
     "Fix RabbitMQ STOMP plugin error. Resolve STOMP protocol support issues.",
     "The STOMP plugin fails to handle STOMP connections. STOMP clients cannot connect or subscribe.",
     ["STOMP plugin not enabled", "STOMP port 61613 not listening", "STOMP frame format is invalid"],
     ["rabbitmq-plugins list | grep stomp", "ss -tlnp | grep 61613"]),

    ("rabbitmq-web-stomp-plugin", "RabbitMQ Web STOMP Plugin Error",
     "Fix RabbitMQ Web STOMP plugin error. Resolve WebSocket-based STOMP issues.",
     "The Web STOMP plugin fails. WebSocket-based STOMP connections are not working.",
     ["Web STOMP plugin not enabled", "WebSocket port not listening", "Web STOMP handler is misconfigured"],
     ["rabbitmq-plugins list | grep web_stomp"]),

    ("rabbitmq-federation-plugin", "RabbitMQ Federation Plugin Error",
     "Fix RabbitMQ federation plugin error. Resolve federation plugin configuration issues.",
     "The federation plugin encounters errors during operation. Links fail or messages are not federated.",
     ["Federation plugin has configuration errors", "Upstream exchange or queue does not exist", "Federation link in error state"],
     ["rabbitmqctl federation.status"]),

    ("rabbitmq-shovel-plugin", "RabbitMQ Shovel Plugin Error",
     "Fix RabbitMQ shovel plugin error. Resolve shovel plugin configuration issues.",
     "The shovel plugin encounters errors during configuration or operation.",
     ["Shovel plugin configuration is invalid", "Shovel source or destination unreachable", "Shovel parameters are wrong"],
     ["rabbitmqctl Shovel.status"]),

    ("rabbitmq-peer-verification", "RabbitMQ Peer Verification Error",
     "Fix RabbitMQ peer verification error. Resolve TLS peer certificate verification issues.",
     "TLS peer certificate verification fails. The client or server rejects the peer certificate.",
     ["Peer certificate is invalid", "Certificate CN does not match hostname", "CA certificate is not trusted"],
     ["openssl s_client -connect localhost:5671 -showcerts"]),

    ("rabbitmq-tls-options", "RabbitMQ TLS Options Error",
     "Fix RabbitMQ TLS options error. Resolve TLS configuration issues.",
     "TLS options are misconfigured. The broker cannot establish or accept TLS connections.",
     ["TLS certificate path is wrong", "TLS key path is wrong", "TLS options are incomplete"],
     ["grep 'listeners.ssl' /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-certificate-auth", "RabbitMQ Certificate Authentication Error",
     "Fix RabbitMQ certificate authentication error. Resolve client certificate authentication issues.",
     "Client certificate authentication fails. The client certificate is not trusted or does not match.",
     ["Client certificate is not signed by trusted CA", "Certificate is expired", "Certificate mapping is wrong"],
     ["openssl x509 -in client.crt -noout -subject"]),

    ("rabbitmq-crl-checking", "RabbitMQ CRL Checking Error",
     "Fix RabbitMQ CRL checking error. Resolve Certificate Revocation List issues.",
     "CRL checking fails. The CRL is expired or the revocation list does not cover the certificate.",
     ["CRL is expired", "CRL does not cover the certificate", "CRL distribution point is unreachable"],
     ["openssl crl -in ca.crl -noout -text"]),

    ("rabbitmq-oauth-2-0", "RabbitMQ OAuth 2.0 Error",
     "Fix RabbitMQ OAuth 2.0 error. Resolve OAuth authentication issues.",
     "OAuth 2.0 authentication fails. The token is invalid, expired, or the OAuth provider is unreachable.",
     ["Token is invalid or expired", "OAuth provider is unreachable", "Token endpoint URL is wrong"],
     ["rabbitmqctl status"]),

    ("rabbitmq-jwt-auth", "RabbitMQ JWT Authentication Error",
     "Fix RabbitMQ JWT authentication error. Resolve JWT token validation issues.",
     "JWT authentication fails. The token is invalid, expired, or the signing key is wrong.",
     ["JWT token is expired", "Signing key does not match", "JWT claim validation failed"],
     ["rabbitmqctl status"]),

    ("rabbitmq-ldap-auth", "RabbitMQ LDAP Authentication Error",
     "Fix RabbitMQ LDAP authentication error. Resolve LDAP backend authentication issues.",
     "LDAP authentication fails. The LDAP server is unreachable or the credentials are wrong.",
     ["LDAP server is unreachable", "Bind DN or password is wrong", "User search base is incorrect"],
     ["grep 'auth_backends' /etc/rabbitmq/rabbitmq.conf"]),

    ("rabbitmq-credential-validator", "RabbitMQ Credential Validator Error",
     "Fix RabbitMQ credential validator error. Resolve custom credential validation issues.",
     "The custom credential validator fails. The validator logic is wrong or the backend is unavailable.",
     ["Credential validator is misconfigured", "Validation backend is unreachable", "Validator logic has bugs"],
     ["rabbitmqctl status"]),

    ("rabbitmq-internal-auth-backend", "RabbitMQ Internal Auth Backend Error",
     "Fix RabbitMQ internal auth backend error. Resolve internal authentication backend issues.",
     "The internal authentication backend fails. The internal user database is corrupted.",
     ["Internal user database is corrupted", "Mnesia is not available", "User data is inconsistent"],
     ["rabbitmqctl list_users"]),

    ("rabbitmq-node-health-check", "RabbitMQ Node Health Check Error",
     "Fix RabbitMQ node health check error. Resolve health monitoring issues.",
     "The node health check fails. The node is not responding or is in a degraded state.",
     ["Node is overloaded", "Mnesia is not running", "Node is partitioned from cluster"],
     ["rabbitmq-diagnostics check_running"]),

    ("rabbitmq-rabbitmqctl-error", "RabbitMQ rabbitmqctl Error",
     "Fix RabbitMQ rabbitmqctl error. Resolve command-line tool issues.",
     "The rabbitmqctl command fails. The node is not reachable or the command is wrong.",
     ["Node is not running", "Command syntax is wrong", "Erlang cookie mismatch"],
     ["rabbitmqctl status"]),

    ("rabbitmq-rabbitmq-diagnostics", "RabbitMQ rabbitmq-diagnostics Error",
     "Fix RabbitMQ rabbitmq-diagnostics error. Resolve diagnostics tool issues.",
     "The rabbitmq-diagnostics command fails. The diagnostics cannot connect to the node.",
     ["Node is not running", "Diagnostics port is not accessible", "Erlang cookie mismatch"],
     ["rabbitmq-diagnostics check_running"]),

    ("rabbitmq-channel-flow-control", "RabbitMQ Channel Flow Control Error",
     "Fix RabbitMQ channel flow control error. Resolve channel-level flow control issues.",
     "Channel flow control is activated. The broker tells the producer to stop sending messages.",
     ["Consumer is too slow", "Queue is filling up", "Memory pressure is high"],
     ["rabbitmqctl list_channels"]),

    ("rabbitmq-consumer-prefetch", "RabbitMQ Consumer Prefetch Error",
     "Fix RabbitMQ consumer prefetch error. Resolve QoS prefetch configuration issues.",
     "The consumer prefetch (QoS) setting is causing issues. Too many or too few messages are delivered.",
     ["Prefetch count is too high causing memory issues", "Prefetch set to 0 (unlimited)", "Prefetch set on non-channel scope"],
     ["rabbitmqctl list_consumers"]),

    ("rabbitmq-global-qos", "RabbitMQ Global QoS Error",
     "Fix RabbitMQ global QoS error. Resolve global prefetch limit issues.",
     "The global QoS setting affects all consumers on the connection. Some consumers are starved.",
     ["Global QoS is too restrictive", "Multiple consumers share global prefetch", "QoS scope is connection instead of channel"],
     ["rabbitmqctl list_consumers"]),

    ("rabbitmq-lazy-queues", "RabbitMQ Lazy Queue Error",
     "Fix RabbitMQ lazy queue error. Resolve lazy queue configuration issues.",
     "Lazy queue configuration is not working as expected. Messages are not being paged to disk.",
     ["Lazy queue mode is not enabled", "Queue arguments are not set correctly", "Disk I/O is slow causing paging issues"],
     ["rabbitmqadmin declare queue name=myqueue arguments='{\"x-queue-mode\":\"lazy\"}'"]),

    ("rabbitmq-quorum-queue-error", "RabbitMQ Quorum Queue Error",
     "Fix RabbitMQ quorum queue error. Resolve Raft-based quorum queue issues.",
     "The quorum queue fails to operate correctly. Raft consensus cannot be maintained.",
     ["Quorum queue members are down", "Raft log is too large", "Network partition prevents quorum"],
     ["rabbitmqctl quorum_queues status"]),

    ("rabbitmq-stream-queue-error", "RabbitMQ Stream Queue Error",
     "Fix RabbitMQ stream queue error. Resolve stream queue protocol issues.",
     "The stream queue fails to handle messages. The stream protocol is not functioning correctly.",
     ["Stream plugin not enabled", "Stream segment files are corrupted", "Consumer offset tracking failing"],
     ["rabbitmq-plugins list | grep stream"]),

    ("rabbitmq-classic-queue-migration", "RabbitMQ Classic Queue Migration Error",
     "Fix RabbitMQ classic queue migration error. Resolve queue type migration issues.",
     "Migration from classic queue to quorum or stream queue fails.",
     ["Queue cannot be converted in-place", "Queue has messages that block migration", "Properties incompatible with target type"],
     ["rabbitmqadmin declare queue name=newqueue queue_type=quorum"]),

    ("rabbitmq-mirroring-deprecated", "RabbitMQ Mirroring Deprecated Error",
     "Fix RabbitMQ mirroring deprecated error. Resolve legacy mirroring migration issues.",
     "Queue mirroring is deprecated in favor of quorum queues. Policies using mirroring should be migrated.",
     ["Mirroring policy is still in use", "Application relies on mirrored queues", "Migration not planned"],
     ["rabbitmqctl list_policies"]),

    ("rabbitmq-policy-not-matched", "RabbitMQ Policy Not Matched Error",
     "Fix RabbitMQ policy not matched error. Resolve policy application issues.",
     "The policy does not match any queues or exchanges. The policy is not being applied.",
     ["Policy pattern does not match resources", "Policy priority is too low", "Policy vhost does not match"],
     ["rabbitmqctl list_policies"]),

    ("rabbitmq-parameter-not-found", "RabbitMQ Parameter Not Found Error",
     "Fix RabbitMQ parameter not found error. Resolve runtime parameter issues.",
     "The specified parameter does not exist. The parameter was never set or was removed.",
     ["Parameter was never configured", "Parameter was removed", "Parameter vhost does not match"],
     ["rabbitmqctl list_parameters"]),

    ("rabbitmq-runtime-parameter-error", "RabbitMQ Runtime Parameter Error",
     "Fix RabbitMQ runtime parameter error. Resolve runtime parameter configuration issues.",
     "The runtime parameter is invalid. The parameter value does not meet the component requirements.",
     ["Parameter value format is wrong", "Parameter value is out of valid range", "Component does not recognize parameter"],
     ["rabbitmqctl list_parameters"]),

    ("rabbitmq-feature-flag", "RabbitMQ Feature Flag Error",
     "Fix RabbitMQ feature flag error. Resolve feature flag compatibility issues.",
     "A required feature flag is not enabled. The feature is not available in this cluster version.",
     ["Feature flag is not enabled", "Cluster has mixed versions", "Flag requires all nodes to be upgraded first"],
     ["rabbitmqctl feature_flags list"]),

    ("rabbitmq-erlang-version", "RabbitMQ Erlang Version Error",
     "Fix RabbitMQ Erlang version error. Resolve Erlang compatibility issues.",
     "The Erlang version is not compatible with the RabbitMQ version. Startup fails or features are broken.",
     ["Erlang version is too old", "Erlang compiled without required features", "Erlang package from incompatible source"],
     ["rabbitmq-diagnostics erlang_version"]),

    ("rabbitmq-upgrade-error", "RabbitMQ Upgrade Error",
     "Fix RabbitMQ upgrade error. Resolve version upgrade and migration issues.",
     "The RabbitMQ upgrade fails. The upgrade process encounters errors during migration.",
     ["Mnesia schema incompatible between versions", "Plugins not compatible with new version", "Mixed versions during rolling upgrade"],
     ["rabbitmqctl status", "rabbitmq-diagnostics erlang_version"]),

    ("rabbitmq-plugin-not-compatible", "RabbitMQ Plugin Not Compatible Error",
     "Fix RabbitMQ plugin not compatible error. Resolve plugin version mismatch issues.",
     "A plugin is not compatible with the current RabbitMQ version. The plugin fails to load.",
     ["Plugin version does not match RabbitMQ", "Plugin from incompatible source", "Plugin API changed in new version"],
     ["rabbitmq-plugins list"]),

    ("rabbitmq-plugin-enable-error", "RabbitMQ Plugin Enable Error",
     "Fix RabbitMQ plugin enable error. Resolve plugin activation issues.",
     "The plugin fails to enable. The plugin file is missing or has dependency issues.",
     ["Plugin file is missing or corrupted", "Plugin has unmet dependencies", "Plugin is not compatible"],
     ["rabbitmq-plugins list -v"]),
]

def make_page(slug, title, desc, body, causes, fixes, examples):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["rabbitmq"]',
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
        '- [RabbitMQ Connection Error]({{< relref "/tools/rabbitmq/rabbitmq-connection-error" >}})',
        '- [RabbitMQ Queue Error]({{< relref "/tools/rabbitmq/rabbitmq-queue-error" >}})',
        '- [RabbitMQ Exchange Error]({{< relref "/tools/rabbitmq/rabbitmq-exchange-error" >}})',
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
print(f"Total .md files in rabbitmq/: {total}")
