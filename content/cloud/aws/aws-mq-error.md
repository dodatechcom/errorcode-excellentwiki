---
title: "[Solution] AWS MQ Error — broker/queue/ActiveMQ/RabbitMQ failures"
description: "Fix AWS MQ errors. Resolve broker, queue, and ActiveMQ/RabbitMQ connectivity issues."
error-types: ["api-error"]
severities: ["error"]
weight: 146
---

An AWS MQ error occurs when brokers fail to create, queues become unavailable, or messaging protocols encounter connection issues. Amazon MQ provides managed ActiveMQ and RabbitMQ brokers but requires proper networking and configuration.

## Common Causes

- Broker storage size exceeded
- Security group blocks AMQP/STOMP/ActiveMQ ports
- Maintenance window causing broker restart
- Engine version not compatible with client library
- IAM user cannot access Amazon MQ console

## How to Fix

### Check Broker Status

```bash
aws mq list-brokers \
  --query 'BrokerSummaries[*].{ID:BrokerId,Name:BrokerName,Status:BrokerStatus}'
```

### Describe Broker

```bash
aws mq describe-broker \
  --broker-id my-broker
```

### Create Broker

```bash
aws mq create-broker \
  --broker-name my-rabbit-mq \
  --engine-type RABBITMQ \
  --engine-version 3.11.20 \
  --host-instance-type mq.m5.large \
  --users '[{"Username":"admin","Password":"mypassword123"}]' \
  --deployment-mode SINGLE_INSTANCE \
  --auto_minor_version_upgrade
```

### Update Broker

```bash
aws mq update-broker \
  --broker-id my-broker \
  --engine-version 3.11.20 \
  --auto-minor-version-upgrade
```

### Reboot Broker

```bash
aws mq reboot-broker --broker-id my-broker
```

## Examples

```bash
# Example 1: Storage exceeded
# StorageQuotaExceededException: Storage limit reached
# Fix: increase storage or clean up old messages

# Example 2: Connection refused
# Connection refused to broker endpoint:5671
# Fix: verify security group allows traffic on port 5671
```

## Related Errors

- [AWS EC2 Error]({{< relref "/cloud/aws/aws-ec2-error" >}}) — EC2 instance errors
- [AWS VPC Error]({{< relref "/cloud/aws/vpc-error" >}}) — VPC connectivity errors
- [AWS IAM Error]({{< relref "/cloud/aws/aws-iam-error" >}}) — IAM permission errors
