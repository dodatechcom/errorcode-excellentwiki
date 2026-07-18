---
title: "Solved Python SQS Error — How to Fix"
date: 2026-03-12T08:50:34+00:00
description: "Learn how to resolve Python AWS SQS message sending, receiving, and visibility timeout errors."
categories: ["python"]
keywords: ["python sqs", "aws sqs error", "sqs message error", "sqs visibility timeout", "sqs permission error"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

Amazon SQS errors in Python typically arise from credential issues, incorrect queue URLs, message size violations, or visibility timeout misconfigurations. The boto3 SQS client provides minimal error detail, making debugging challenging.

Common causes include:
- Incorrect queue URL or region mismatch
- IAM permissions not granting `sqs:SendMessage` or `sqs:ReceiveMessage`
- Message body exceeding 256 KB limit
- Visibility timeout expiring before processing completes
- Reusing a deleted queue URL

## Common Error Messages

```python
import boto3

sqs = boto3.client("sqs")
try:
    sqs.send_message(QueueUrl="https://sqs.wrong-region.amazonaws.com/123/queue", MessageBody="test")
except Exception as e:
    print(e)
# An error occurred (AWS.SimpleQueueService.NonExistentQueue) when calling the SendMessage operation
```

```python
# Access denied
try:
    sqs.send_message(QueueUrl=queue_url, MessageBody="test")
except sqs.exceptions.ClientError as e:
    print(e.response["Error"]["Code"])
# AuthorizationError
```

```python
# Message too long
long_msg = "x" * (257 * 1024)
try:
    sqs.send_message(QueueUrl=queue_url, MessageBody=long_msg)
except sqs.exceptions.ClientError as e:
    print(e.response["Error"]["Code"])
# InvalidParameterValue
```

## How to Fix It

### 1. Validate Queue URL and Region

Always verify queue URL before operations.

```python
import boto3
from botocore.exceptions import ClientError

def get_queue_url_safe(sqs_client, queue_name, region="us-east-1"):
    try:
        response = sqs_client.get_queue_url(QueueName=queue_name)
        return response["QueueUrl"]
    except ClientError as e:
        if e.response["Error"]["Code"] == "AWS.SimpleQueueService.NonExistentQueue":
            print(f"Queue '{queue_name}' does not exist in {region}")
        raise

sqs = boto3.client("sqs", region_name="us-east-1")
url = get_queue_url_safe(sqs, "my-queue")
```

### 2. Handle Message Size Limits

Use S3 for large payloads with SQSExtendedClient pattern.

```python
import boto3
import json
import uuid

sqs = boto3.client("sqs")
s3 = boto3.client("s3")

LARGE_MSG_THRESHOLD = 200 * 1024  # 200KB

def send_large_message(queue_url, body, bucket_name):
    payload = json.dumps(body).encode("utf-8")
    
    if len(payload) <= LARGE_MSG_THRESHOLD:
        sqs.send_message(QueueUrl=queue_url, MessageBody=payload.decode())
        return
    
    msg_id = str(uuid.uuid4())
    s3.put_object(
        Bucket=bucket_name,
        Key=f"sqs-large/{msg_id}.json",
        Body=payload
    )
    
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps({
            "large_payload": True,
            "s3_key": f"sqs-large/{msg_id}.json",
            "bucket": bucket_name
        }),
        MessageAttributes={
            "PayloadType": {"DataType": "String", "StringValue": "s3_reference"}
        }
    )
```

### 3. Implement Proper Visibility Timeout Management

Extend visibility timeout for long-running tasks.

```python
import boto3
import threading
import time

class VisibilityExtender:
    def __init__(self, sqs_client, queue_url, message, extend_interval=25):
        self.sqs = sqs_client
        self.queue_url = queue_url
        self.message = message
        self.handle = message["ReceiptHandle"]
        self.extend_interval = extend_interval
        self._stop = threading.Event()
        self._thread = None
    
    def start(self):
        self._stop.clear()
        self._thread = threading.Thread(target=self._extend_loop, daemon=True)
        self._thread.start()
    
    def _extend_loop(self):
        while not self._stop.wait(self.extend_interval):
            try:
                self.sqs.change_message_visibility(
                    QueueUrl=self.queue_url,
                    ReceiptHandle=self.handle,
                    VisibilityTimeout=300
                )
            except Exception as e:
                print(f"Failed to extend visibility: {e}")
                break
    
    def stop(self):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=5)

# Usage
sqs = boto3.client("sqs")
response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
msg = response["Messages"][0]

extender = VisibilityExtender(sqs, queue_url, msg)
extender.start()
try:
    process_message(msg)
    sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=msg["ReceiptHandle"])
finally:
    extender.stop()
```

## Common Scenarios

### Scenario 1: FIFO Queue Ordering Violation

When message group IDs cause unexpected ordering:

```python
import boto3
import hashlib

sqs = boto3.client("sqs")

def send_order_event(queue_url, order_id, event_type):
    group_id = hashlib.md5(order_id.encode()).hexdigest()[:10]
    
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps({
            "order_id": order_id,
            "event": event_type
        }),
        MessageGroupId=group_id,
        MessageDeduplicationId=f"{order_id}-{event_type}"
    )
```

### Scenario 2: Dead Letter Queue Redrive

Redrive failed messages from DLQ back to the main queue:

```python
def redrive_dlq(main_queue_url, dlq_url, max_messages=10):
    sqs = boto3.client("sqs")
    
    response = sqs.receive_message(
        QueueUrl=dlq_url,
        MaxNumberOfMessages=max_messages,
        WaitTimeSeconds=5
    )
    
    for msg in response.get("Messages", []):
        sqs.send_message(
            QueueUrl=main_queue_url,
            MessageBody=msg["Body"],
            MessageAttributes=msg.get("MessageAttributes", {})
        )
        sqs.delete_message(
            QueueUrl=dlq_url,
            ReceiptHandle=msg["ReceiptHandle"]
        )
    
    return len(response.get("Messages", []))
```

## Prevent It

- Always use `get_queue_url` instead of hardcoding queue URLs
- Set visibility timeout to at least 6x your maximum processing time
- Use FIFO queues when ordering or exactly-once delivery is required
- Monitor SQS metrics: `ApproximateNumberOfMessagesVisible`, `ApproximateAgeOfOldestMessage`
- Implement a dead letter queue with redrive policy for failed messages