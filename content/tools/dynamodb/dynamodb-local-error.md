---
title: "[Solution] DynamoDB Local Not Responding — How to Fix"
description: "Fix DynamoDB Local connection issues by checking Java runtime, port availability, database file corruption, upgrading the JAR, and configuring endpoint overrides in SDK clients."
tools: ["dynamodb"]
error-types: ["local-error"]
severities: ["error"]
weight: 5
comments: true
---

A DynamoDB Local error occurs when the local emulator fails to start, stops responding, or your application cannot connect to it. These errors typically manifest as connection refused, timeout, or internal server errors from the emulator.

## What This Error Means

DynamoDB Local is a downloadable version of DynamoDB that runs in your local environment. It mimics the DynamoDB API for development and testing. Unlike the production DynamoDB service, it has limited durability, no replication, and no SLA. Errors are typically caused by Java runtime issues, port conflicts, or database state corruption.

The emulator runs as a Java process on port 8000 by default. If the process dies, crashes, or is unreachable, your application receives connection errors similar to network failures.

## Why It Happens

- Java Runtime Environment (JRE) is not installed or is outdated (requires Java 8+)
- Port 8000 is already in use by another process
- The DynamoDB Local JAR file is corrupted or incompatible
- The shared database file (`.db` or `-shared.db`) is corrupted
- The Java process runs out of heap memory
- The application SDK is configured with the wrong endpoint or region
- A firewall or VPN blocks localhost connections
- The emulator was not properly shut down and left a lock file

## Common Error Messages

```
Unable to connect to DynamoDB Local: Connection refused (localhost:8000)
# or
DynamoDB Local: Internal server error - database file is corrupted
# or
java.net.BindException: Address already in use (Port 8000)
# or
org.apache.http.conn.HttpHostConnectException: Connect to localhost:8000 failed
```

## How to Fix It

### 1. Start DynamoDB Local Correctly

```bash
# Download the latest version
wget https://s3.us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz
tar -xzf dynamodb_local_latest.tar.gz

# Start with default settings (port 8000, in-memory)
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -inMemory

# Start with shared database (persists to disk)
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -port 8000

# Start with custom port and db path
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar \
    -sharedDb -port 8001 -dbPath ./dynamodb-data
```

### 2. Check Java Runtime

```bash
# Check Java version (requires Java 8 or later)
java -version

# If Java is not installed:
sudo apt update && sudo apt install default-jre -y
# or on macOS:
brew install --cask temurin
```

DynamoDB Local requires Java 8 or later. Java 11 and Java 17 are also supported.

### 3. Free Port 8000

```bash
# Check which process is using port 8000
lsof -i :8000

# Kill the process using port 8000
kill -9 $(lsof -ti :8000)

# Or start DynamoDB Local on a different port
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -port 8001
```

### 4. Configure SDK to Connect to DynamoDB Local

```python
import boto3

# DynamoDB Local endpoint configuration
client = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='us-east-1',  # Can be any region for local
    aws_access_key_id='fakeMyKeyId',      # Any dummy value
    aws_secret_access_key='fakeSecretKey' # Any dummy value
)
```

```javascript
// JavaScript SDK v3
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({
  region: "us-east-1",
  endpoint: "http://localhost:8000",
  credentials: {
    accessKeyId: "fakeMyKeyId",
    secretAccessKey: "fakeSecretKey"
  }
});
```

### 5. Clear Corrupted Database Files

```bash
# Stop DynamoDB Local first, then remove db files
rm -f dynamodb-data/*.db dynamodb-data/*.db-shm dynamodb-data/*.db-wal

# Restart with fresh database
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb -dbPath ./dynamodb-data
```

Corrupted database files cause internal server errors. Removing them starts fresh, but you will lose all local data.

### 6. Increase Java Heap Memory

```bash
# DynamoDB Local may crash with large datasets
# Increase heap memory to 2GB
java -Xmx2g -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

# Monitor memory usage
top -p $(pgrep -f DynamoDBLocal)
```

### 7. Use Docker for DynamoDB Local

```bash
# Run DynamoDB Local via Docker
docker run -p 8000:8000 amazon/dynamodb-local

# With persistent data
docker run -p 8000:8000 -v $(pwd)/dynamodb-data:/home/dynamodblocal/data \
    amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath /home/dynamodblocal/data
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  dynamodb-local:
    image: amazon/dynamodb-local
    ports:
      - "8000:8000"
    volumes:
      - ./dynamodb-data:/home/dynamodblocal/data
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath /home/dynamodblocal/data"
```

### 8. Use the Web Shell for Quick Testing

```bash
# Access the DynamoDB Local web shell
# Open http://localhost:8000/shell in your browser
# The web shell provides an interactive JavaScript environment
```

## Common Scenarios

### CI/CD Pipeline Tests Failing Due to DynamoDB Local

A test suite in a GitHub Actions workflow uses DynamoDB Local but consistently fails with connection refused errors. The workflow does not wait for the Java process to start before running tests. Add a health check loop that polls port 8000 before test execution.

### Database File Corruption After Improper Shutdown

A developer closes their terminal without gracefully stopping DynamoDB Local. The shared database file becomes corrupted, causing all subsequent operations to fail with internal server errors. The fix is to delete the `.db` files and restart, accepting data loss.

### Port Conflict with Local Web Server

A developer runs both DynamoDB Local and a local web server that both try to bind to port 8000. The web server starts first and DynamoDB Local fails with `BindException`. Start DynamoDB Local on an alternative port like 8001 and update the SDK endpoint configuration.

## Prevent It

- Always use Docker for DynamoDB Local to avoid Java environment issues
- Create a health check script that verifies DynamoDB Local is responding before tests
- Use a dedicated port range (e.g., 8000-8010) only for development databases
- Back up the local database directory before large-scale testing
- Gracefully stop DynamoDB Local with SIGTERM instead of killing the process
- Pin the DynamoDB Local version in your project dependencies
- Use separate database files for different test suites

## Related Pages

- [DynamoDB Throughput Error](/tools/dynamodb/dynamodb-throughput-error)
- [DynamoDB Access Denied Error](/tools/dynamodb/dynamodb-access-denied)
- [DynamoDB Type Mismatch Error](/tools/dynamodb/dynamodb-type-error)
