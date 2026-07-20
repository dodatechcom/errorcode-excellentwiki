#!/usr/bin/env python3
"""Generate MongoDB error pages"""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/mongodb'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["mongodb"]',
        'error-types: ["database-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
    ]
    return '\n'.join(lines)

PAGES = [
    # ============================================================
    # 1. CONNECTION ERRORS
    # ============================================================
    (
        "mongodb-authentication-failed",
        "MongoDB Authentication Failed",
        "Fix MongoDB authentication failed error when connecting to the database server",
        r"""## MongoDB Authentication Failed Error

The `auth failed` error occurs when MongoDB rejects the credentials provided during connection. This typically appears as:

```
MongoServerError: Authentication failed.
```

or in older versions:

```
auth failed, username: myuser db: admin code: 18 AuthenticationFailed
```

## Common Causes

- Incorrect username or password
- The user does not exist in the authentication database
- The user does not have sufficient privileges
- `authSource` parameter is missing or incorrect in the connection string
- Password contains special characters that are not URL-encoded
- SCRAM-SHA-256 vs SCRAM-SHA-1 mismatch between client and server
- The user was created on a different database than the one specified in `authSource`
- Kerberos or LDAP token has expired
- MongoDB Atlas password contains characters that break the connection URI

## How to Fix

### 1. Verify the user exists

```javascript
use admin
db.getUsers()
// or for a specific user
db.getUser("myuser")
```

### 2. Check the authSource

The connection string must include the correct `authSource`:

```
mongodb://myuser:mypassword@localhost:27017/mydatabase?authSource=admin
```

If the user was created in `admin`, the `authSource` must be `admin`, not `mydatabase`.

### 3. Re-create the user with correct permissions

```javascript
use admin
db.createUser({
  user: "myuser",
  pwd: "securePassword123!",
  roles: [
    { role: "readWrite", db: "mydatabase" },
    { role: "dbAdmin", db: "mydatabase" }
  ]
})
```

### 4. URL-encode special characters in the password

If your password is `p@ss:word/123`, it must be encoded as:

```
mongodb://myuser:p%40ss%3Aword%2F123@localhost:27017/mydatabase?authSource=admin
```

### 5. Force SCRAM-SHA-256 authentication mechanism

```
mongodb://myuser:password@localhost:27017/mydatabase?authSource=admin&authMechanism=SCRAM-SHA-256
```

## Examples

```bash
# Test authentication from the command line
mongosh --username myuser --password mypassword --authenticationDatabase admin

# Verify with a direct connection
mongosh "mongodb://myuser:password@localhost:27017/admin"

# Check server logs for auth details
tail -f /var/log/mongodb/mongod.log | grep -i auth

# Drop and recreate the user
mongosh --eval '
  use admin;
  db.dropUser("myuser");
  db.createUser({
    user: "myuser",
    pwd: "newSecurePass!",
    roles: [{ role: "readWrite", db: "mydatabase" }]
  });
'
```"""
    ),
    (
        "mongodb-connection-refused",
        "MongoDB Connection Refused",
        "Fix MongoDB connection refused error on port 27017",
        r"""## MongoDB Connection Refused Error

The `connection refused` error means the client cannot establish a TCP connection to the MongoDB server. Typical messages:

```
MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017
```

```
Error: connect ECONNREFUSED ::1:27017
```

## Common Causes

- MongoDB service is not running
- MongoDB is listening on a different port or interface
- A firewall is blocking port 27017
- The `bindIp` configuration in `mongod.conf` does not include the client's address
- SELinux or AppArmor is blocking the connection
- MongoDB is bound to `127.0.0.1` only, and the client connects remotely
- Port 27017 is already in use by another process
- Docker container networking misconfiguration
- Cloud security group rules do not allow inbound traffic on 27017

## How to Fix

### 1. Check if MongoDB is running

```bash
sudo systemctl status mongod
# or on newer systems
sudo systemctl status mongodb
```

### 2. Start MongoDB if it is not running

```bash
sudo systemctl start mongod
sudo systemctl enable mongod
```

### 3. Verify the listening address and port

```bash
ss -tlnp | grep 27017
# or
netstat -tlnp | grep 27017
```

### 4. Update bindIp in mongod.conf

```yaml
# /etc/mongod.conf
net:
  port: 27017
  bindIp: 0.0.0.0   # Listen on all interfaces
```

Then restart:

```bash
sudo systemctl restart mongod
```

### 5. Configure the firewall

```bash
# UFW
sudo ufw allow 27017/tcp

# firewalld
sudo firewall-cmd --permanent --add-port=27017/tcp
sudo firewall-cmd --reload

# iptables
sudo iptables -A INPUT -p tcp --dport 27017 -j ACCEPT
```

## Examples

```bash
# Test connection with mongosh
mongosh --host 127.0.0.1 --port 27017

# Check if the port is open
nc -zv 127.0.0.1 27017

# Verify MongoDB log for binding issues
sudo tail -50 /var/log/mongodb/mongod.log | grep -i "waiting for connections\|error\|address already in use"

# Verify Docker container is exposing the port
docker ps | grep mongo
docker logs <container_name> --tail 50
```"""
    ),
    (
        "mongodb-connection-timed-out",
        "MongoDB Connection Timed Out",
        "Resolve MongoDB connection timeout errors during server selection",
        r"""## MongoDB Connection Timed Out Error

A connection timeout occurs when the driver cannot reach the MongoDB server within the expected timeframe:

```
MongoServerSelectionError: connection timed out
```

```
MongoNetworkError: Server selection timed out after 30000 ms
```

## Common Causes

- Network latency between the client and server is too high
- The server is overloaded and cannot accept new connections
- DNS resolution is slow or failing
- The server firewall silently drops packets (no RST sent)
- MongoDB is starting up and not yet ready for connections
- Connection pool is exhausted -- all connections are in use
- VPN or proxy is interfering with the TCP connection
- IPv6 vs IPv4 mismatch

## How to Fix

### 1. Increase the server selection timeout

```javascript
const client = new MongoClient(uri, {
  serverSelectionTimeoutMS: 60000,  // 60 seconds
  connectTimeoutMS: 10000,
  socketTimeoutMS: 20000
});
```

### 2. Check network connectivity

```bash
# Ping the server
ping mongo-host.example.com

# Test the port
nc -zv mongo-host.example.com 27017

# Trace the route
traceroute mongo-host.example.com
```

### 3. Verify DNS resolution

```bash
nslookup mongo-host.example.com
dig mongo-host.example.com

# Try with IP directly to rule out DNS
mongosh --host 10.0.1.50 --port 27017
```

### 4. Check for firewall drops

```bash
# On the server
sudo tcpdump -i eth0 port 27017 -n

# Check iptables
sudo iptables -L -n | grep 27017
```

### 5. Optimize connection pool settings

```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 100,
  minPoolSize: 10,
  waitQueueTimeoutMS: 5000
});
```

## Examples

```bash
# Measure latency to the server
time mongosh --host mongo-host --eval "db.runCommand({ping:1})"

# Check server resource usage
ssh mongo-host "uptime && free -h && df -h"

# Monitor active connections
mongosh --eval "db.serverStatus().connections"

# Test with a simpler query to verify connectivity
mongosh --host mongo-host --eval "db.runCommand({connectionStatus:1})"
```"""
    ),
    (
        "mongodb-dns-resolution-failed",
        "MongoDB DNS Resolution Failed",
        "Fix DNS resolution failures when connecting to MongoDB",
        r"""## MongoDB DNS Resolution Failed Error

When the MongoDB driver cannot resolve the hostname to an IP address, you will see:

```
MongoNetworkError: getaddrinfo ENOTFOUND mongo.example.com
```

```
MongoServerSelectionError: DNS resolution failed for mongo.example.com
```

## Common Causes

- The hostname is misspelled in the connection string
- DNS server is unreachable or misconfigured
- `/etc/resolv.conf` has incorrect nameserver entries
- The DNS record for the MongoDB host does not exist
- Private DNS zones are not accessible from the client network
- The hostname uses an internal domain not resolvable externally
- `/etc/hosts` file is missing the entry for the MongoDB host

## How to Fix

### 1. Verify the hostname resolves

```bash
nslookup mongo.example.com
host mongo.example.com
dig mongo.example.com
```

### 2. Check DNS configuration

```bash
cat /etc/resolv.conf
# Ensure nameserver entries are correct
nameserver 8.8.8.8
nameserver 8.8.4.4
```

### 3. Add an entry to /etc/hosts (temporary fix)

```bash
sudo bash -c 'echo "192.168.1.100  mongo.example.com" >> /etc/hosts'
```

### 4. Use IP address directly

```
mongodb://user:password@192.168.1.100:27017/mydb?authSource=admin
```

### 5. Configure SRV record for replica sets

For DNS seedlist connections (`mongodb+srv://`), ensure the SRV record exists:

```bash
dig _mongodb._tcp.mongo.example.com SRV
```

## Examples

```bash
# Test DNS resolution from the application server
python3 -c "import socket; print(socket.getaddrinfo('mongo.example.com', 27017))"

# Flush DNS cache
sudo systemd-resolve --flush-caches
sudo resolvectl flush-caches

# Test with dig to see full DNS info
dig mongo.example.com ANY

# Try connecting with the IP directly to confirm DNS is the issue
mongosh --host 192.168.1.100 --port 27017
```"""
    ),
    (
        "mongodb-ssl-tls-handshake-failed",
        "MongoDB SSL TLS Handshake Failed",
        "Fix MongoDB SSL/TLS handshake errors during secure connections",
        r"""## MongoDB SSL/TLS Handshake Failed Error

The TLS handshake failure prevents the client from establishing a secure connection:

```
MongoNetworkError: SSL handshake failed
```

```
error:14094418:SSL routines:ssl3_read_bytes:tlsv1 alert unknown ca
```

## Common Causes

- The server uses a self-signed certificate not trusted by the client
- The CA certificate is missing from the client's trust store
- TLS protocol version mismatch (server requires TLS 1.2, client uses 1.0)
- Certificate has expired
- The `--tls` flag is not passed to `mongosh`
- Certificate Common Name (CN) or SAN does not match the hostname
- Cipher suite is not supported by either side
- The PEM key file and certificate file are mismatched

## How to Fix

### 1. Enable TLS on the server

```yaml
# /etc/mongod.conf
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

### 2. Connect with the proper CA certificate

```bash
mongosh \
  --tls \
  --tlsCAFile /etc/ssl/ca.pem \
  --host mongo.example.com \
  --port 27017
```

### 3. Verify the certificate

```bash
openssl s_client -connect mongo.example.com:27017 -CAfile /etc/ssl/ca.pem
openssl x509 -in /etc/ssl/mongodb.pem -text -noout
```

### 4. Ensure certificate matches the hostname

```bash
openssl x509 -in /etc/ssl/mongodb.pem -noout -text | grep -A2 "Subject Alternative Name"
```

The SAN must include the hostname used in the connection string.

### 5. Use allowInvalidHostnames for testing only

```javascript
const client = new MongoClient(uri, {
  tls: true,
  tlsCAFile: '/etc/ssl/ca.pem',
  tlsAllowInvalidHostnames: true  // Not for production!
});
```

## Examples

```bash
# Generate a self-signed certificate for testing
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Combine into PEM for MongoDB
cat key.pem cert.pem > /etc/ssl/mongodb.pem

# Test TLS connection
mongosh --tls --tlsCAFile /etc/ssl/ca.pem --host mongo.example.com

# Verify the cipher suite being used
openssl s_client -connect mongo.example.com:27017 -tls1_2
```"""
    ),
    (
        "mongodb-replica-set-connection-string",
        "MongoDB Replica Set Connection String Error",
        "Fix replica set connection string issues in MongoDB",
        r"""## MongoDB Replica Set Connection String Error

When connecting to a replica set with an incorrect connection string, you may see:

```
MongoTopologyClosedError: Topology was destroyed
```

```
MongoServerSelectionError: No replica set primary found
```

## Common Causes

- The connection string does not include all replica set members
- The replica set name in the connection string is wrong
- Using a direct connection (`directConnection=true`) when you need replica set mode
- The replica set has not been initialized yet
- The members listed in the connection string are unreachable
- The client driver version is incompatible with the replica set configuration

## How to Fix

### 1. Use the correct connection string format

```
mongodb://user:password@mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0
```

### 2. Include the replica set name

```javascript
const client = new MongoClient(
  'mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0&authSource=admin'
);
```

### 3. Use the seedlist (SRV) format

```
mongodb+srv://user:password@mongo.example.com/?replicaSet=rs0
```

### 4. Verify replica set status

```javascript
rs.status()
rs.conf()
rs.isMaster()
```

### 5. Ensure all members are running

```bash
# On each member
mongosh --port 27017 --eval "rs.status().members.forEach(m => print(m.name, m.stateStr))"
```

## Examples

```bash
# Connect to the replica set
mongosh "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0"

# Check replica set status
mongosh --eval "rs.status()"

# Initialize replica set (if not yet initialized)
mongosh --eval "rs.initiate({_id:'rs0', members:[{_id:0, host:'mongo1:27017'},{_id:1, host:'mongo2:27017'},{_id:2, host:'mongo3:27017'}]})"

# Verify the replica set configuration
mongosh --eval "rs.conf()"
```"""
    ),
    (
        "mongodb-topology-closed",
        "MongoDB Topology Closed Error",
        "Fix MongoDB topology closed or destroyed errors",
        r"""## MongoDB Topology Closed Error

When the driver's topology is closed or destroyed, operations fail:

```
MongoTopologyClosedError: Topology was destroyed
```

```
MongoExpiredSessionError: Cannot use a session that has ended
```

## Common Causes

- The client was closed before operations completed
- A replica set failover occurred and the topology was not refreshed
- The server closed the connection due to an admin command (e.g., shutdown)
- The connection pool was closed during a graceful shutdown
- Network interruption caused the topology to be destroyed
- The `close()` method was called prematurely

## How to Fix

### 1. Do not close the client prematurely

```javascript
// Wrong: closing immediately
const client = new MongoClient(uri);
await client.close();

// Right: keep the client open for the application lifecycle
const client = new MongoClient(uri);
await client.connect();
// ... perform operations ...
// close only during application shutdown
```

### 2. Add retry logic for transient errors

```javascript
async function withRetry(fn, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await fn();
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}

// Usage
await withRetry(() => db.collection('users').findOne({ _id: id }));
```

### 3. Listen for topology events

```javascript
client.on('topologyClosed', () => {
  console.warn('Topology closed - attempting reconnect');
});

client.on('serverDescriptionChanged', (event) => {
  console.log('Server changed:', event.newDescription.address, event.newDescription.rtt);
});
```

### 4. Use unified topology (Node.js driver 4+)

In Node.js driver 4.0+, the unified topology is the default. Ensure you are not using legacy topology settings.

## Examples

```bash
# Check if the server is shutting down
grep -i "shutdown\|close\|shutdownInProgress" /var/log/mongodb/mongod.log

# Verify the client is connecting properly
mongosh --eval "db.runCommand({connectionStatus:1})"

# Monitor topology with server status
mongosh --eval "JSON.stringify(db.serverStatus().connections, null, 2)"
```"""
    ),
    (
        "mongodb-network-timeout",
        "MongoDB Network Timeout Error",
        "Fix MongoDB network timeout errors during operations",
        r"""## MongoDB Network Timeout Error

A network timeout occurs when a socket operation does not complete in time:

```
MongoNetworkError: connection 5 to mongo.example.com:27017 timed out
```

```
MongoNetworkError: Socket was unexpectedly closed
```

## Common Causes

- The server is under heavy load and cannot respond in time
- A long-running operation blocks the socket
- Network congestion between client and server
- The default socket timeout is too short for the workload
- Firewall is rate-limiting or dropping connections
- The server is performing a long compaction or checkpoint

## How to Fix

### 1. Increase the socket timeout

```javascript
const client = new MongoClient(uri, {
  socketTimeoutMS: 120000,   // 2 minutes
  connectTimeoutMS: 15000,
  serverSelectionTimeoutMS: 30000
});
```

### 2. Break large operations into smaller batches

```javascript
// Instead of inserting 1M documents at once
const batchSize = 1000;
for (let i = 0; i < documents.length; i += batchSize) {
  const batch = documents.slice(i, i + batchSize);
  await collection.insertMany(batch);
}
```

### 3. Optimize queries causing long-running operations

```javascript
// Add indexes to prevent full collection scans
db.users.createIndex({ email: 1 });

// Use .explain() to check query plans
db.users.find({ email: "test@example.com" }).explain("executionStats");
```

### 4. Monitor server health

```bash
# Check for slow operations
grep "Slow query" /var/log/mongodb/mongod.log | tail -20

# Check server status
mongosh --eval "db.serverStatus()"
```

## Examples

```bash
# Test with an extended timeout
mongosh --eval "db.runCommand({ping:1})" --socketTimeoutMS 60000

# Check for network issues
mtr mongo.example.com

# Monitor current operations
mongosh --eval "db.currentOp()"

# Kill long-running operations
mongosh --eval "db.killOp(<opId>)"
```"""
    ),
    (
        "mongodb-server-selection-timeout",
        "MongoDB Server Selection Timeout Error",
        "Fix MongoDB server selection timeout when no server is available",
        r"""## MongoDB Server Selection Timeout Error

The server selection timeout means no suitable server was found within the timeout window:

```
MongoServerSelectionError: Server selection timed out after 30000 ms
```

In a replica set context:

```
MongoServerSelectionError: No suitable server found
```

## Common Causes

- All members of the replica set are down
- The client cannot reach any member due to network issues
- Read preference settings exclude all available servers
- The replica set is in a split-brain state with no majority
- Max staleness settings are too restrictive
- The server is in maintenance mode or shutting down

## How to Fix

### 1. Increase server selection timeout

```javascript
const client = new MongoClient(uri, {
  serverSelectionTimeoutMS: 60000
});
```

### 2. Verify replica set members are running

```bash
for host in mongo1 mongo2 mongo3; do
  echo "Checking $host..."
  ssh $host "systemctl is-active mongod"
done
```

### 3. Check read preference settings

```javascript
// Ensure read preference allows reading from available members
const client = new MongoClient(uri, {
  readPreference: 'secondaryPreferred'
});
```

### 4. Verify maxStalenessSeconds

```javascript
// Don't set too restrictive a staleness value
const options = {
  readPreference: new ReadPreference('secondary', { maxStalenessSeconds: 120 })
};
```

## Examples

```bash
# Check which members are available
mongosh --eval "rs.status().members.forEach(m => print(m.name, m.stateStr, m.health))"

# Test connection to each member individually
mongosh --host mongo1 --eval "db.runCommand({ping:1})"
mongosh --host mongo2 --eval "db.runCommand({ping:1})"

# Check the replica set configuration
mongosh --eval "rs.conf().members.forEach(m => print(m.host, m.priority, m.votes))"
```"""
    ),
    # ============================================================
    # 2. CRUD ERRORS
    # ============================================================
    (
        "mongodb-duplicate-key-e11000",
        "MongoDB Duplicate Key Error E11000",
        "Fix MongoDB E11000 duplicate key error on insert or update",
        r"""## MongoDB Duplicate Key Error (E11000)

The E11000 error occurs when an insert or update attempts to create a duplicate value for a unique index:

```
MongoServerError: E11000 duplicate key error collection: mydb.users index: email_1 dup key: { email: "test@example.com" }
```

## Common Causes

- Inserting a document with a value that already exists in a unique-indexed field
- Updating a field to a value that violates a unique constraint
- Race condition: two concurrent inserts with the same unique value
- The unique index was created after duplicate documents already existed
- The `_id` field is being set manually and conflicts with an existing document

## How to Fix

### 1. Use upsert to handle duplicates gracefully

```javascript
// Instead of insertOne, use updateOne with upsert
await db.users.updateOne(
  { email: "test@example.com" },
  { $setOnInsert: { name: "John", createdAt: new Date() } },
  { upsert: true }
);
```

### 2. Use try-catch with error code

```javascript
try {
  await db.users.insertOne({ email: "test@example.com", name: "John" });
} catch (err) {
  if (err.code === 11000) {
    console.log("Duplicate key - document may already exist");
    // Update instead
    await db.users.updateOne(
      { email: "test@example.com" },
      { $set: { name: "John" } }
    );
  } else {
    throw err;
  }
}
```

### 3. Drop duplicates before creating unique index

```javascript
// Find duplicates
db.users.aggregate([
  { $group: { _id: "$email", dups: { $addToSet: "$_id" }, count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } }
]);

// Remove duplicates (keep the first one)
db.users.aggregate([
  { $group: { _id: "$email", dups: { $addToSet: "$_id" }, count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } }
]).forEach(doc => {
  doc.dups.shift();
  db.users.deleteMany({ _id: { $in: doc.dups } });
});

// Now create the unique index
db.users.createIndex({ email: 1 }, { unique: true });
```

### 4. Use bulkWrite with ordered:false

```javascript
const ops = documents.map(doc => ({
  updateOne: {
    filter: { email: doc.email },
    update: { $setOnInsert: doc },
    upsert: true
  }
}));
await db.users.bulkWrite(ops, { ordered: false });
```

## Examples

```bash
# Check existing unique indexes
mongosh --eval "db.users.getIndexes().filter(i => i.unique)"

# Insert a document and then try a duplicate
mongosh --eval '
  db.test.drop();
  db.test.createIndex({email:1},{unique:true});
  db.test.insertOne({email:"a@b.com"});
  try { db.test.insertOne({email:"a@b.com"}); } catch(e) { print(e); }
'

# Use findAndModify for atomic upsert
mongosh --eval '
  db.test.findAndModify({
    query: {email:"a@b.com"},
    update: {$setOnInsert:{name:"Alice"}},
    upsert: true
  });
'
```"""
    ),
    (
        "mongodb-write-concern-timeout",
        "MongoDB Write Concern Timeout",
        "Fix write concern timeout errors during write operations",
        r"""## MongoDB Write Concern Timeout Error

A write concern timeout occurs when the server does not satisfy the write concern within the specified time:

```
MongoServerError: operation exceeded time limit for write concern
```

```
WriteConcernError: operation timed out, write concern: { w: "majority", wtimeout: 5000 }
```

## Common Causes

- The `wtimeout` value is too low for current network/server conditions
- A replica set member is slow to acknowledge writes
- The majority is not available (replica set degraded)
- Network latency between the primary and secondary members
- The server is under heavy write load

## How to Fix

### 1. Increase the wtimeout value

```javascript
await db.users.insertOne(
  { name: "John" },
  { writeConcern: { w: "majority", wtimeout: 30000 } }  // 30 seconds
);
```

### 2. Use a less strict write concern for non-critical writes

```javascript
// Less strict: wait for primary only
await db.logs.insertMany(docs, { writeConcern: { w: 1 } });

// Or fire-and-forget (not recommended for critical data)
await db.logs.insertMany(docs, { writeConcern: { w: 0 } });
```

### 3. Set a global write concern

```javascript
db.adminCommand({
  setDefaultWriteConcern: { w: "majority", wtimeout: 30000 }
});
```

### 4. Check replica set health

```javascript
rs.status().members.forEach(m => {
  print(m.name, m.stateStr, m.optimeDate, m.lastHeartbeat);
});
```

## Examples

```bash
# Check current write concern settings
mongosh --eval "db.adminCommand({getDefaultWriteConcern:1})"

# Insert with specific write concern
mongosh --eval '
  db.test.insertOne(
    { data: "test" },
    { writeConcern: { w: "majority", wtimeout: 5000, j: true } }
  )
'

# Monitor replica set lag (cause of write concern timeouts)
mongosh --eval '
  rs.status().members.filter(m => m.stateStr === "SECONDARY").forEach(m => {
    print(m.name, "lag:", (rs.status().date - m.optimeDate) + "ms");
  })
'
```"""
    ),
    (
        "mongodb-write-concern-majority",
        "MongoDB Write Concern Majority Unreachable",
        "Fix write concern majority errors when majority cannot be reached",
        r"""## MongoDB Write Concern Majority Unreachable

When write concern `w: "majority"` cannot be satisfied:

```
WriteConcernError: Not enough data-bearing nodes (1/3) to satisfy write concern majority
```

## Common Causes

- More than half of the replica set members are down
- A network partition prevents the primary from reaching a majority
- Members are in recovery state and not yet synchronized
- The replica set was reconfigured with fewer data-bearing members
- An arbiter is included but does not count toward majority

## How to Fix

### 1. Ensure enough members are online

```javascript
// Check replica set status
rs.status().members.forEach(m => {
  print(m.name, m.stateStr, m.health);
});
```

### 2. Restart downed members

```bash
ssh mongo2 "sudo systemctl start mongod"
ssh mongo3 "sudo systemctl start mongod"
```

### 3. Temporarily use a lower write concern

```javascript
// If you must write and cannot restore the majority
await db.users.insertOne(
  { name: "test" },
  { writeConcern: { w: 1, wtimeout: 5000 } }
);
```

### 4. Check for network partitions

```bash
# From the primary
ping mongo2
ping mongo3
traceroute mongo2
```

## Examples

```bash
# Check how many members are in the replica set
mongosh --eval "rs.status().members.length"

# Check the replica set config for voting members
mongosh --eval "rs.conf().members.map(m => ({host: m.host, votes: m.votes}))"

# Force a member to rejoin (if healthy)
mongosh --eval "rs.syncFrom('mongo1:27017')" --host mongo2
```"""
    ),
    (
        "mongodb-document-too-large-bson",
        "MongoDB Document Too Large BSON Error",
        "Fix document too large error exceeding BSON size limit",
        r"""## MongoDB Document Too Large (BSON) Error

When a document exceeds the maximum BSON document size (16 MB):

```
MongoServerError: Object too large (2147483648 bytes), max size: 16777216
```

```
BSONError: BSONObj size: 2147483648 is invalid. Size must be between 0 and 1679360057
```

## Common Causes

- Storing large binary data (images, files) directly in the document
- Accumulation of array elements pushing the document over 16 MB
- An update operator (`$set`) accidentally sets a value to a very large object
- GridFS was not used for file storage
- Logging or debug fields containing excessive data

## How to Fix

### 1. Use GridFS for large files

```javascript
const { GridFSBucket } = require('mongodb');
const bucket = new GridFSBucket(db);

// Upload
const uploadStream = bucket.openUploadStream('largefile.bin');
fs.createReadStream('largefile.bin').pipe(uploadStream);

// Download
const downloadStream = bucket.openDownloadStreamByName('largefile.bin');
downloadStream.pipe(fs.createWriteStream('output.bin'));
```

### 2. Break large arrays into subdocuments or separate collections

```javascript
// Instead of storing all comments in one document
// collection: posts (has post metadata)
// collection: comments (references post _id)
```

### 3. Validate document size before insert

```javascript
function checkDocSize(doc) {
  const size = BSON.serialize(doc).byteLength;
  if (size > 16 * 1024 * 1024) {
    throw new Error(`Document too large: ${size} bytes (max: 16MB)`);
  }
  return true;
}
```

### 4. Use compression to reduce size

```javascript
await db.collection('logs').insertOne({
  data: compressData(largeObject)  // Use zlib or similar
});
```

## Examples

```bash
# Check the size of a document
mongosh --eval '
  let doc = db.mycol.findOne();
  printjson(BSON.serialize(doc).byteLength);
'

# Check current collection storage stats
mongosh --eval "db.mycol.stats()"

# Convert a document to GridFS using mongofiles
mongofiles --db=mydb put largefile.bin

# Check maximum BSON object size
mongosh --eval "db.runCommand({getParameter:1, maxBsonObjectSize:1})"
```"""
    ),
    (
        "mongodb-invalid-bson",
        "MongoDB Invalid BSON Error",
        "Fix invalid BSON errors when inserting or updating documents",
        r"""## MongoDB Invalid BSON Error

Invalid BSON data causes operations to fail:

```
MongoServerError: Invalid BSON: cannot decode element, type: 0
```

```
BSONError: Input must be a valid BSON document
```

## Common Causes

- Binary data was corrupted during transmission
- An embedded document contains null bytes or invalid UTF-8 characters
- The client driver generated malformed BSON
- Data was manually edited in a binary format
- A field contains a JavaScript function (`$where`) with invalid syntax
- Date values are out of the representable range

## How to Fix

### 1. Validate documents before insertion

```javascript
const bson = require('bson');

function validateBSON(doc) {
  try {
    bson.serialize(doc);
    return true;
  } catch (e) {
    console.error('Invalid BSON:', e.message);
    return false;
  }
}
```

### 2. Sanitize string fields

```javascript
function sanitizeString(str) {
  // Remove null bytes and invalid characters
  return str.replace(/\x00/g, '').replace(/[\x00-\x08\x0B\x0C\x0E-\x1F]/g, '');
}
```

### 3. Use proper BSON types instead of raw objects

```javascript
// Instead of passing raw Date strings
const doc = {
  createdAt: new Date(),           // Correct
};
```

### 4. Check for data corruption in existing documents

```javascript
db.myCollection.find().forEach(doc => {
  try {
    bson.serialize(doc);
  } catch (e) {
    print("Corrupted doc _id:", doc._id);
  }
});
```

## Examples

```bash
# Validate all documents in a collection
mongosh --eval '
  let errors = 0;
  db.mycol.find().forEach(doc => {
    try { bson.serialize(doc); }
    catch(e) { errors++; print("Bad doc:", doc._id); }
  });
  print("Total errors:", errors);
'

# Check collection integrity
mongosh --eval "db.mycol.validate({full: true})"

# Export and re-import to fix corruption
mongoexport --db mydb --collection mycol --out backup.json
mongoimport --db mydb --collection mycol --file backup.json
```"""
    ),
    (
        "mongodb-path-collision",
        "MongoDB Path Collision Error",
        "Fix path collision errors when creating index or update",
        r"""## MongoDB Path Collision Error

Path collision occurs when an update operation tries to create both a field and a subfield:

```
ServerError: Cannot create field 'a' in element {a: {b: 1}} : Path collision
```

```
The field 'a.b' cannot be mixed with a field of the same name in a dot path
```

## Common Causes

- An update tries to set both `a` and `a.b` simultaneously
- A `$set` operation conflicts with an existing field path
- Creating an index where one path is a prefix of another (e.g., `a` and `a.b`)
- Merging documents with conflicting field structures

## How to Fix

### 1. Restructure your update operations

```javascript
// Wrong: path collision
await db.users.updateOne(
  { _id: 1 },
  { $set: { address: { street: "Main St" }, "address.city": "NYC" } }
);

// Correct: set the full subdocument
await db.users.updateOne(
  { _id: 1 },
  { $set: { address: { street: "Main St", city: "NYC" } } }
);
```

### 2. Restructure index fields

```javascript
// Wrong: path collision in index
db.users.createIndex({ "address": 1, "address.city": 1 });

// Correct: use only the more specific path
db.users.createIndex({ "address.city": 1 });
```

### 3. Use separate update operations

```javascript
// If you need to set multiple levels, do it sequentially
await db.users.updateOne({ _id: 1 }, { $set: { address: { street: "Main St" } } });
await db.users.updateOne({ _id: 1 }, { $set: { "address.city": "NYC" } });
```

### 4. Review the document structure

```javascript
// Use $mergeObjects for merging subdocuments
await db.users.updateOne(
  { _id: 1 },
  { $set: { address: { $mergeObjects: ["$address", { city: "NYC" }] } } }
);
```

## Examples

```bash
# Demonstrate path collision
mongosh --eval '
  db.test.drop();
  db.test.insertOne({a: {b: 1}});
  try {
    db.test.updateOne({}, {$set: {a:1, "a.b":2}});
  } catch(e) { print(e.message); }
'

# Fix: restructure the update
mongosh --eval '
  db.test.updateOne({}, {$set: {a: {b: 2, c: 3}}});
  printjson(db.test.findOne());
'
```"""
    ),
    (
        "mongodb-update-validation-error",
        "MongoDB Update Validation Error",
        "Fix MongoDB update validation errors on documents",
        r"""## MongoDB Update Validation Error

Update validation errors occur when an update operation violates schema validation rules:

```
MongoServerError: Document failed validation
```

```
WriteError: Document failed validation
{ index: 0, code: 121, errmsg: 'Document failed validation' }
```

## Common Causes

- The update produces a document that violates a `$jsonSchema` validation rule
- The update tries to set a field to a value outside the allowed range
- Required fields are being removed or set to null
- The document no longer matches the collection validator after the update
- A `$rename` operation causes a required field to become missing

## How to Fix

### 1. Review the collection validator

```javascript
db.getCollectionInfos({ name: "myCollection" })[0].options.validator
```

### 2. Check what the update would produce

```javascript
// Run a find with the same filter to see affected documents
const docs = await db.myCollection.find({ _id: 1 }).toArray();
console.log("Before:", docs[0]);
```

### 3. Use validationAction: "warn" during development

```javascript
db.createCollection("myCollection", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string" }
      }
    }
  },
  validationAction: "warn"  // Log warnings but allow the operation
});
```

### 4. Relax the validator temporarily

```javascript
db.runCommand({
  collMod: "myCollection",
  validationLevel: "moderate"  // Only validate new documents and updates to existing valid documents
});
```

## Examples

```bash
# View the current validator
mongosh --eval "db.getCollectionInfos({name:'users'})[0].options.validator"

# Test an update that violates validation
mongosh --eval '
  db.users.updateOne({_id:1}, {$set:{age:-5}});
'

# Temporarily disable validation
mongosh --eval '
  db.runCommand({collMod:"users", validationLevel:"off"});
  db.users.updateOne({_id:1}, {$set:{age:-5}});
  db.runCommand({collMod:"users", validationLevel:"strict"});
'
```"""
    ),
    (
        "mongodb-array-filters-error",
        "MongoDB Array Filters Error",
        "Fix array filters errors in update operations",
        r"""## MongoDB Array Filters Error

Array filter errors occur when the `arrayFilters` parameter is misconfigured:

```
MongoServerError: No array filter found for identifier 'grades'
```

```
MongoServerError: arrayFilters invalid at grades.$[<ref>]
```

## Common Causes

- The array filter identifier does not match any variable in the update
- The filter syntax is incorrect (missing `$` or wrong path)
- The array field does not exist in the document
- Multiple array filters conflict with each other
- The filter condition is invalid BSON

## How to Fix

### 1. Use the correct array filter syntax

```javascript
// Update all elements in the 'grades' array where score < 60
await db.students.updateMany(
  {},
  { $set: { "grades.$[elem].status": "fail" } },
  {
    arrayFilters: [
      { "elem.score": { $lt: 60 } }
    ]
  }
);
```

### 2. Use the positional identifier correctly

```javascript
// The identifier after $[ must match the one in arrayFilters
await db.students.updateMany(
  {},
  { $set: { "grades.$[elem].passed": true } },
  {
    arrayFilters: [
      { "elem.score": { $gte: 70 } }  // "elem" must match $[elem]
    ]
  }
);
```

### 3. Handle nested arrays

```javascript
await db.students.updateMany(
  {},
  { $set: { "grades.$[outer].subgrades.$[inner].curve": 5 } },
  {
    arrayFilters: [
      { "outer.semester": "fall" },
      { "inner.type": "quiz" }
    ]
  }
);
```

### 4. Verify the field exists

```javascript
db.students.find({ grades: { $exists: true, $type: "array" } }).count();
```

## Examples

```bash
# Set up test data
mongosh --eval '
  db.students.drop();
  db.students.insertMany([
    {name:"Alice", grades:[{score:85, subject:"math"},{score:55, subject:"science"}]},
    {name:"Bob", grades:[{score:45, subject:"math"},{score:92, subject:"science"}]}
  ]);
'

# Update elements matching a condition
mongosh --eval '
  db.students.updateMany(
    {},
    {$set: {"grades.$[g].status": "review"}},
    {arrayFilters: [{"g.score": {$lt: 60}}]}
  );
  printjson(db.students.find().toArray());
'
```"""
    ),
    (
        "mongodb-positional-operator-error",
        "MongoDB Positional Operator Error",
        "Fix positional operator $ errors in update operations",
        r"""## MongoDB Positional Operator Error

The positional operator `$` fails with various errors:

```
MongoServerError: The positional operator did not find the match needed from the query document
```

```
MongoServerError: Updating the path 'grades.$' would create a conflict at 'grades'
```

## Common Causes

- The query filter does not match any element in the array
- Using `$` on a field that is not an array
- Using `$` with `$set` on a nested field incorrectly
- The array is empty
- Using multiple positional operators without `$[<identifier>]`

## How to Fix

### 1. Ensure the query matches an array element

```javascript
// The query must match the element you want to update
await db.students.updateOne(
  { "grades.score": { $lt: 60 } },  // Must match an element
  { $set: { "grades.$.status": "fail" } }
);
```

### 2. Use arrayFilters for multiple elements

```javascript
// To update ALL matching elements, use arrayFilters
await db.students.updateMany(
  {},
  { $set: { "grades.$[elem].status": "fail" } },
  { arrayFilters: [{ "elem.score": { $lt: 60 } }] }
);
```

### 3. Use `$[<identifier>]` for positional updates of nested arrays

```javascript
await db.students.updateOne(
  { "grades.score": 55 },
  { $set: { "grades.$[g].curve": 10 } },
  { arrayFilters: [{ "g.score": { $lt: 60 } }] }
);
```

### 4. Handle missing or empty arrays

```javascript
const doc = await db.students.findOne({ _id: 1 });
if (doc && doc.grades && doc.grades.length > 0) {
  // Safe to use positional operator
}
```

## Examples

```bash
# Set up test data
mongosh --eval '
  db.scores.drop();
  db.scores.insertOne({student:"Alice", scores:[85,92,45,78]});
'

# Update the first element matching a condition
mongosh --eval '
  db.scores.updateOne(
    {"scores": {$lt: 60}},
    {$set: {"scores.$": 60}}
  );
  printjson(db.scores.findOne());
'
```"""
    ),
    (
        "mongodb-bulk-write-error",
        "MongoDB Bulk Write Error",
        "Fix MongoDB bulkWrite operation errors",
        r"""## MongoDB Bulk Write Error

Bulk write operations can fail for various reasons:

```
BulkWriteError: write error at index 0
```

```
MongoBulkWriteError: E11000 duplicate key error
```

## Common Causes

- One or more operations in the batch violate a unique constraint
- A document in the batch is too large
- The batch exceeds the maximum bulk write size (100,000 operations)
- Write concern errors on one or more operations
- Mixed operation types cause conflicts

## How to Fix

### 1. Handle errors per-operation with ordered:false

```javascript
try {
  const result = await db.users.bulkWrite([
    { insertOne: { document: { _id: 1, name: "Alice" } } },
    { insertOne: { document: { _id: 1, name: "Duplicate" } } },
    { insertOne: { document: { _id: 2, name: "Bob" } } }
  ], { ordered: false });

  console.log("Inserted:", result.insertedCount);
  console.log("Errors:", result.writeErrors);
} catch (err) {
  console.error("Bulk write error:", err.message);
}
```

### 2. Process errors from the result object

```javascript
const result = await db.users.bulkWrite(operations, { ordered: false });
if (result.writeErrors && result.writeErrors.length > 0) {
  result.writeErrors.forEach(err => {
    console.error("Index:", err.index, "Error:", err.errmsg);
  });
}
```

### 3. Split large batches into smaller chunks

```javascript
const CHUNK_SIZE = 1000;
for (let i = 0; i < operations.length; i += CHUNK_SIZE) {
  const chunk = operations.slice(i, i + CHUNK_SIZE);
  await db.users.bulkWrite(chunk, { ordered: false });
}
```

### 4. Use upsert to avoid duplicate key errors

```javascript
await db.users.bulkWrite(
  users.map(user => ({
    updateOne: {
      filter: { email: user.email },
      update: { $set: user },
      upsert: true
    }
  })),
  { ordered: false }
);
```

## Examples

```bash
# Test bulk write with mixed operations
mongosh --eval '
  db.test.drop();
  let ops = [];
  for (let i = 0; i < 100; i++) {
    ops.push({insertOne: {document: {i, val: Math.random()}}});
  }
  let result = db.test.bulkWrite(ops, {ordered:false});
  printjson({inserted: result.insertedCount, errors: result.writeErrors?.length || 0});
'
```"""
    ),
    (
        "mongodb-findandmodify-error",
        "MongoDB findAndModify Error",
        "Fix findAndModify errors including upsert and returnDocument issues",
        r"""## MongoDB findAndModify Error

The `findAndModify` command can fail with several errors:

```
MongoServerError: After applying the update, the (immutable) field '_id' was found to have been altered
```

```
MongoServerError: findAndModify failed: write conflict
```

## Common Causes

- Attempting to modify the `_id` field
- The query matches multiple documents (only one is modified)
- Write conflict in a multi-statement transaction
- The update returns a value that conflicts with a unique index
- `new: true` (or `returnDocument: "AFTER"`) not specified when needed

## How to Fix

### 1. Never modify the _id field

```javascript
// Wrong
await db.users.findOneAndUpdate(
  { _id: 1 },
  { $set: { _id: 2, name: "Bob" } }  // Error: cannot modify _id
);

// Correct
await db.users.findOneAndUpdate(
  { _id: 1 },
  { $set: { name: "Bob" } }
);
```

### 2. Use returnDocument option

```javascript
const result = await db.users.findOneAndUpdate(
  { name: "Alice" },
  { $inc: { score: 10 } },
  { returnDocument: "after" }  // Returns the modified document
);
console.log(result.value);
```

### 3. Handle upsert with findAndModify

```javascript
const result = await db.counters.findOneAndUpdate(
  { _id: "orderId" },
  { $inc: { seq: 1 } },
  { upsert: true, returnDocument: "after" }
);
```

### 4. Avoid write conflicts in transactions

```javascript
const session = client.startSession();
try {
  session.startTransaction({ readConcern: { level: "snapshot" } });
  await db.users.findOneAndUpdate({ _id: 1 }, { $inc: { balance: -10 } }, { session });
  await session.commitTransaction();
} catch (err) {
  await session.abortTransaction();
} finally {
  session.endSession();
}
```

## Examples

```bash
# Atomic increment with findAndModify
mongosh --eval '
  let result = db.counters.findOneAndUpdate(
    {_id: "seq"},
    {$inc: {value: 1}},
    {upsert: true, returnDocument: "after"}
  );
  print("New value:", result.value);
'

# Delete and return a document
mongosh --eval '
  let removed = db.queue.findOneAndDelete(
    {status: "pending"},
    {sort: {created: 1}}
  );
  printjson(removed);
'
```"""
    ),
    # ============================================================
    # 3. INDEX ERRORS
    # ============================================================
    (
        "mongodb-index-build-failed",
        "MongoDB Index Build Failed",
        "Fix MongoDB index build failures and build process errors",
        r"""## MongoDB Index Build Failed Error

Index builds can fail for several reasons:

```
MongoServerError: Index build failed: operation was interrupted
```

```
MongoServerError: Error persisting index spec...
```

## Common Causes

- The index build was interrupted (e.g., server restart, stepdown)
- Not enough memory for the in-memory index build
- The index specification is invalid (duplicate field, bad collation)
- The collection is too large and the build exceeds the timeout
- A conflicting index already exists
- The server is in read-only mode

## How to Fix

### 1. Build indexes during low-traffic periods

```javascript
db.users.createIndex({ email: 1 }, { background: true });
```

### 2. Use the 4.2+ non-blocking index build

MongoDB 4.2+ builds indexes without blocking reads/writes by default. Ensure you are on 4.2+.

### 3. Check for sufficient resources

```bash
# Check available memory
free -h

# Check disk space
df -h /var/lib/mongodb

# Check for I/O bottleneck
iostat -x 1 5
```

### 4. Build in rolling fashion for replica sets

```bash
# Step 1: Build on secondary (with rs.stepDown)
mongosh --host mongo2 --eval "db.users.createIndex({email:1})"

# Step 2: Build on the other secondary
mongosh --host mongo3 --eval "db.users.createIndex({email:1})"

# Step 3: Step down primary, build on new secondary
```

### 5. Verify the index specification

```javascript
// Check existing indexes to avoid conflicts
db.users.getIndexes();

// Drop the index and recreate
db.users.dropIndex("email_1");
db.users.createIndex({ email: 1 }, { unique: true });
```

## Examples

```bash
# Monitor ongoing index builds
mongosh --eval "db.currentOp({desc: /index build/})"

# Check index build progress (MongoDB 4.2+)
mongosh --eval "db.adminCommand({getCurrentIndexBuilds:1})"

# Kill a stuck index build
mongosh --eval "db.adminCommand({killOp: <opId>})"
```"""
    ),
    (
        "mongodb-index-too-large",
        "MongoDB Index Too Large Error",
        "Fix MongoDB index size limit and too large index errors",
        r"""## MongoDB Index Too Large Error

An index can exceed the maximum key size or the available memory:

```
MongoServerError: Error: key too large to index (10485770 bytes)
```

```
MongoServerError: WiredTiger cannot find the file to compact
```

## Common Causes

- A text index includes very long text fields
- An indexed array field has too many elements
- The index key exceeds the WiredTiger key limit
- Insufficient RAM to hold the index
- Too many indexes on a collection (32 index limit)

## How to Fix

### 1. Limit the index key size with prefix

```javascript
// For text indexes, limit the indexed fields
db.articles.createIndex({ title: "text", content: "text" }, {
  weights: { title: 10, content: 5 },
  default_language: "english"
});
```

### 2. Use partial indexes for selective indexing

```javascript
// Only index documents where status is "active"
db.orders.createIndex(
  { status: 1 },
  { partialFilterExpression: { status: "active" } }
);
```

### 3. Drop unused indexes

```javascript
// List all indexes
db.users.getIndexes();

// Drop a specific index
db.users.dropIndex("unusedIndex_1");
```

### 4. Reduce indexed field sizes

```javascript
// Instead of indexing a large string, hash it
db.users.createIndex({ emailHash: 1 });
```

## Examples

```bash
# Check total index size for a collection
mongosh --eval "db.users.totalIndexSize()"

# Check index sizes individually
mongosh --eval '
  db.users.getIndexes().forEach(idx => {
    let stats = db.users.stats().indexSizes[idx.name];
    print(idx.name, ":", stats, "bytes");
  });
'

# Check WiredTiger cache usage
mongosh --eval "db.serverStatus().wiredTiger.cache"
```"""
    ),
    (
        "mongodb-index-not-found",
        "MongoDB Index Not Found Error",
        "Fix MongoDB index not found or missing index errors",
        r"""## MongoDB Index Not Found Error

Operations may fail when an expected index does not exist:

```
MongoServerError: error processing query: ... No query solutions
```

```
Error: plan executor error: Unknown error
```

## Common Causes

- The index was dropped or never created
- The index name was misspelled in a hint
- The collection was recreated without indexes
- The query references a field that has no index and no valid query plan
- Index builds failed silently

## How to Fix

### 1. List existing indexes

```javascript
db.users.getIndexes();
```

### 2. Create the missing index

```javascript
db.users.createIndex({ email: 1 }, { unique: true });
```

### 3. Use hint to specify the index

```javascript
db.users.find({ email: "test@example.com" }).hint("email_1");
```

### 4. Recreate indexes from index definitions

```javascript
const indexes = db.users.getIndexes();
indexes.forEach(idx => {
  if (idx.name !== "_id_") {
    const keys = {};
    for (let key in idx.key) {
      keys[key] = idx.key[key];
    }
    const opts = {};
    if (idx.unique) opts.unique = true;
    if (idx.sparse) opts.sparse = true;
    db.users.createIndex(keys, opts);
  }
});
```

## Examples

```bash
# Check indexes on a collection
mongosh --eval "db.users.getIndexes().forEach(i => printjson(i))"

# Verify a specific index exists
mongosh --eval "print(db.users.getIndexes().some(i => i.name === 'email_1'))"

# Create indexes from a template
mongosh --eval '
  [{email:1},{name:1},{createdAt:-1}].forEach(spec => {
    db.users.createIndex(spec);
    print("Created index:", JSON.stringify(spec));
  });
'
```"""
    ),
    (
        "mongodb-unique-constraint-violation",
        "MongoDB Unique Constraint Violation",
        "Fix MongoDB unique constraint violations on index fields",
        r"""## MongoDB Unique Constraint Violation

A unique constraint violation occurs when an insert or update creates duplicate values:

```
WriteError: E11000 duplicate key error collection: db.users index: username_1 dup key: { username: "admin" }
```

## Common Causes

- Inserting a document with a duplicate value in a unique-indexed field
- Updating a field to match an existing value in another document
- Compound unique index allows duplicate partial values but not full combination
- Race conditions in concurrent inserts
- The unique index was created on a collection with existing duplicates

## How to Fix

### 1. Check for existing duplicates before inserting

```javascript
const existing = await db.users.findOne({ username: "admin" });
if (existing) {
  console.log("User already exists:", existing._id);
} else {
  await db.users.insertOne({ username: "admin", name: "Administrator" });
}
```

### 2. Use upsert with $setOnInsert

```javascript
await db.users.updateOne(
  { username: "admin" },
  { $setOnInsert: { name: "Administrator", createdAt: new Date() } },
  { upsert: true }
);
```

### 3. Create a partial unique index for soft-deleted documents

```javascript
db.users.createIndex(
  { email: 1 },
  {
    unique: true,
    partialFilterExpression: { deleted: { $ne: true } }
  }
);
```

### 4. Handle compound unique constraints

```javascript
// Compound unique: the combination of fields must be unique
db.bookings.createIndex(
  { resourceId: 1, date: 1 },
  { unique: true }
);
```

## Examples

```bash
# Find all duplicate values
mongosh --eval '
  db.users.aggregate([
    {$group: {_id: "$email", count: {$sum: 1}, ids: {$addToSet: "$_id"}}},
    {$match: {count: {$gt: 1}}}
  ]).toArray();
'

# Create a unique index with sparse option
mongosh --eval '
  db.users.createIndex({email:1}, {unique: true, sparse: true});
'
```"""
    ),
    (
        "mongodb-compound-index-ordering",
        "MongoDB Compound Index Ordering Error",
        "Fix compound index field ordering issues in MongoDB",
        r"""## MongoDB Compound Index Ordering Error

Incorrect field ordering in compound indexes leads to inefficient queries:

```
MongoServerError: error processing query: ... Unable to execute query: no index available
```

## Common Causes

- The query fields do not match the index prefix order
- Equality fields appear after range fields in the index
- The index order (ascending/descending) does not match sort requirements
- Missing prefix fields in the query
- Mixed ascending and descending fields in compound sort

## How to Fix

### 1. Put equality fields first, then sort, then range

```javascript
// Query: { status: "active", age: {$gt: 25} } sorted by { createdAt: -1 }
// Good index order: status (equality), createdAt (sort), age (range)
db.users.createIndex({ status: 1, createdAt: -1, age: 1 });
```

### 2. Match the index order with query filter

```javascript
// For query: { a: 1, b: 1, c: {$gt: 5} }
db.collection.createIndex({ a: 1, b: 1, c: 1 });
```

### 3. Use explain() to verify index usage

```javascript
db.users.find({ status: "active", age: {$gt: 25} })
  .sort({ createdAt: -1 })
  .explain("executionStats");
```

### 4. Handle sort with mixed directions

```javascript
// If you need to sort by { a: 1, b: -1 }, create the index with matching directions
db.collection.createIndex({ a: 1, b: -1 });
```

## Examples

```bash
# Compare query plans with different indexes
mongosh --eval '
  db.test.drop();
  for (let i = 0; i < 10000; i++) {
    db.test.insertOne({a: i%100, b: i%10, c: i, d: "val"+i});
  }
  db.test.createIndex({a:1,b:1,c:1});
  print("Index 1 totalKeysExamined:");
  printjson(db.test.find({a:1,b:1,c:{$gt:5}}).sort({c:1}).explain("executionStats").executionStats.totalKeysExamined);
'
```"""
    ),
    (
        "mongodb-text-index-error",
        "MongoDB Text Index Error",
        "Fix MongoDB full text index creation and query errors",
        r"""## MongoDB Text Index Error

Text index operations can fail with several errors:

```
MongoServerError: bad query: Bad Value ... text index
```

```
MongoServerError: Only non-compound, non-array, non-geo fields can have a TTL index
```

## Common Causes

- Only one text index is allowed per collection
- The text index field is too large
- Text search is combined with an unsupported aggregation stage
- The search language is not supported
- Duplicate text index names
- The query uses a text index with an incompatible sort

## How to Fix

### 1. Only create one text index per collection

```javascript
// If you need to search multiple fields, combine them into one text index
db.articles.createIndex({ title: "text", content: "text", tags: "text" });

// Drop an existing text index before creating a new one
db.articles.dropIndex("title_text");
```

### 2. Use weights to prioritize fields

```javascript
db.articles.createIndex(
  { title: "text", content: "text" },
  { weights: { title: 10, content: 5 } }
);
```

### 3. Use language-specific text indexes

```javascript
db.articles.createIndex(
  { title: "text", content: "text" },
  { default_language: "english", language_override: "lang" }
);
```

### 4. Combine text search with aggregation correctly

```javascript
db.articles.aggregate([
  { $match: { $text: { $search: "mongodb" } } },
  { $project: { title: 1, score: { $meta: "textScore" } } },
  { $sort: { score: { $meta: "textScore" } } }
]);
```

## Examples

```bash
# Create a comprehensive text index
mongosh --eval '
  db.articles.drop();
  db.articles.createIndex({title:"text", content:"text", tags:"text"}, {weights:{title:10,content:5,tags:1}});
  db.articles.insertMany([
    {title:"MongoDB Guide", content:"Learn MongoDB basics", tags:["database","nosql"]},
    {title:"Advanced Queries", content:"Complex MongoDB queries", tags:["database","queries"]}
  ]);
  printjson(db.articles.find({$text:{$search:"MongoDB queries"}}).toArray());
'
```"""
    ),
    (
        "mongodb-ttl-index-error",
        "MongoDB TTL Index Error",
        "Fix MongoDB TTL index creation and expiration errors",
        r"""## MongoDB TTL Index Error

TTL indexes may not work as expected:

```
MongoServerError: Only non-compound, non-array, non-geo fields can have a TTL index
```

TTL indexes that exist but do not delete documents are a common issue.

## Common Causes

- The TTL index is on a compound index (not allowed)
- The field is an array (not allowed for TTL)
- The field does not contain a Date type value
- The TTL monitor has not run yet (runs every 60 seconds)
- The indexed field is a string instead of a Date
- The TTL index was created on `_id` (not supported)

## How to Fix

### 1. Ensure the TTL field contains Date objects

```javascript
// Correct
await db.sessions.insertOne({
  sessionId: "abc123",
  createdAt: new Date()  // Date object, not string
});

// Wrong
await db.sessions.insertOne({
  sessionId: "abc123",
  createdAt: "2024-01-15T00:00:00Z"  // String, not Date
});
```

### 2. Create TTL index on a single non-array field

```javascript
// Correct
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 });

// Wrong: compound index
db.sessions.createIndex({ createdAt: 1, userId: 1 }, { expireAfterSeconds: 3600 });
```

### 3. Wait for the TTL monitor

The TTL monitor runs every 60 seconds. Be patient.

### 4. Use expireAfterSeconds: 0 for immediate expiration

```javascript
db.logs.createIndex({ expireAt: 1 }, { expireAfterSeconds: 0 });
```

## Examples

```bash
# Set up a TTL collection
mongosh --eval '
  db.sessions.drop();
  db.sessions.createIndex({createdAt:1}, {expireAfterSeconds: 10});
  db.sessions.insertOne({data:"temp", createdAt: new Date()});
  print("Document inserted. Waiting for TTL monitor...");
'

# Check TTL index configuration
mongosh --eval '
  db.sessions.getIndexes().forEach(i => {
    if (i.expireAfterSeconds !== undefined) {
      print(i.name, "TTL:", i.expireAfterSeconds, "seconds");
    }
  });
'
```"""
    ),
    (
        "mongodb-sparse-index-error",
        "MongoDB Sparse Index Exception",
        "Fix MongoDB sparse index issues and missing documents",
        r"""## MongoDB Sparse Index Exception

Sparse indexes exclude documents that do not have the indexed field:

```
// Queries using sparse indexes may return fewer results than expected
```

## Common Causes

- A query uses a sparse index but documents without the field are excluded
- The sparse index does not contain all documents in the collection
- A unique sparse index allows multiple documents without the field
- An aggregation pipeline uses the sparse index and misses documents

## How to Fix

### 1. Understand sparse vs non-sparse behavior

```javascript
// Sparse: only documents with 'email' field are indexed
db.users.createIndex({ email: 1 }, { sparse: true });

// Non-sparse (default): all documents are indexed
// Documents without 'email' have null indexed
db.users.createIndex({ email: 1 });
```

### 2. Use partialFilterExpression instead of sparse

```javascript
db.users.createIndex(
  { email: 1 },
  {
    partialFilterExpression: {
      email: { $exists: true, $ne: null }
    }
  }
);
```

### 3. Be aware of unique sparse index behavior

```javascript
// Multiple documents WITHOUT the field are allowed
db.users.createIndex({ email: 1 }, { unique: true, sparse: true });

// These are all allowed:
db.users.insertOne({ name: "Alice" });           // No email
db.users.insertOne({ name: "Bob" });             // No email
db.users.insertOne({ name: "Charlie", email: "c@test.com" });
```

### 4. Use hint to avoid sparse index when needed

```javascript
db.users.find({ email: { $exists: false } }).hint("_id_");
```

## Examples

```bash
# Demonstrate sparse index behavior
mongosh --eval '
  db.test.drop();
  db.test.createIndex({email:1}, {sparse:true});
  db.test.insertMany([{name:"A"},{name:"B"},{name:"C",email:"c@test.com"}]);
  print("Documents with email:", db.test.countDocuments({email:{$exists:true}}));
  print("Documents without email:", db.test.countDocuments({email:{$exists:false}}));
  print("All documents:", db.test.countDocuments());
'
```"""
    ),
    (
        "mongodb-geospatial-index-error",
        "MongoDB Geospatial Index Error",
        "Fix MongoDB geospatial index creation and query errors",
        r"""## MongoDB Geospatial Index Error

Geospatial operations fail with various errors:

```
MongoServerError: can't use legacy geo queries (use 2d index): ...
```

```
MongoServerError: longitude must be between -180 and 180, got: 200
```

## Common Causes

- The location data has invalid coordinates (e.g., longitude > 180)
- The wrong index type is used (`2d` vs `2dsphere`)
- Query operators do not match the index type
- The coordinate pair is in the wrong order (lat/lng vs lng/lat)
- The field contains non-GeoJSON data

## How to Fix

### 1. Use the correct index type for your data

```javascript
// For GeoJSON data (recommended)
db.places.createIndex({ location: "2dsphere" });

// For legacy coordinate pairs (flat 2D space)
db.places.createIndex({ location: "2d" });
```

### 2. Store location as GeoJSON

```javascript
await db.places.insertOne({
  name: "Central Park",
  location: {
    type: "Point",
    coordinates: [-73.97, 40.78]  // [longitude, latitude]
  }
});
```

### 3. Validate coordinates

```javascript
function validateGeoJSON(doc) {
  if (doc.coordinates[0] < -180 || doc.coordinates[0] > 180) {
    throw new Error("Invalid longitude: " + doc.coordinates[0]);
  }
  if (doc.coordinates[1] < -90 || doc.coordinates[1] > 90) {
    throw new Error("Invalid latitude: " + doc.coordinates[1]);
  }
}
```

### 4. Use the correct query operators

```javascript
// For 2dsphere index
db.places.find({
  location: {
    $geoWithin: {
      $centerSphere: [[-73.97, 40.78], 1 / 6378.1]  // 1km radius
    }
  }
});
```

## Examples

```bash
# Create a geospatial collection
mongosh --eval '
  db.places.drop();
  db.places.createIndex({location: "2dsphere"});
  db.places.insertMany([
    {name:"Times Square", location:{type:"Point", coordinates:[-73.9857, 40.7580]}},
    {name:"Central Park", location:{type:"Point", coordinates:[-73.9654, 40.7829]}},
    {name:"Brooklyn Bridge", location:{type:"Point", coordinates:[-73.9969, 40.7061]}}
  ]);
  let near = db.places.find({
    location: {$near: {$geometry:{type:"Point",coordinates:[-73.97,40.78]}, $maxDistance: 5000}}
  }).toArray();
  print("Nearby places:", near.map(p => p.name));
'
```"""
    ),
    (
        "mongodb-hidden-index",
        "MongoDB Hidden Index Error",
        "Fix MongoDB hidden index issues and queries ignoring indexes",
        r"""## MongoDB Hidden Index Error

Hidden indexes are not used by the query planner:

```
// Queries may perform collection scans instead of using the hidden index
```

## Common Causes

- An index was marked hidden during testing and not unhidden
- The query planner does not consider hidden indexes for query plans
- Performance degrades because the query falls back to a collection scan
- The index was hidden via `collMod` and forgotten

## How to Fix

### 1. Check if any indexes are hidden

```javascript
db.users.getIndexes().forEach(idx => {
  if (idx.hidden) {
    print("HIDDEN:", idx.name);
  }
});
```

### 2. Unhide an index

```javascript
db.runCommand({
  collMod: "users",
  index: {
    name: "email_1",
    hidden: false
  }
});
```

### 3. Use hidden indexes for testing before making them visible

```javascript
// Create an index as hidden first
db.users.createIndex({ email: 1 }, { hidden: true });

// Test that it works as expected
db.users.find({ email: "test@example.com" }).explain("executionStats");

// Unhide when ready
db.runCommand({ collMod: "users", index: { name: "email_1", hidden: false } });
```

### 4. Verify the query is using the correct index

```javascript
db.users.find({ email: "test@example.com" }).explain("executionStats");
// Check which index was used
// If the query does a COLLSCAN, check if the index is hidden
```

## Examples

```bash
# Find all hidden indexes
mongosh --eval '
  db.users.getIndexes().forEach(i => {
    if (i.hidden) print("Hidden:", i.name, JSON.stringify(i.key));
  });
'

# Create a hidden index, test, then unhide
mongosh --eval '
  db.users.createIndex({email:1}, {hidden:true});
  let plan = db.users.find({email:"test@test.com"}).explain("executionStats");
  print("Index used:", plan.executionStats.stage);
  db.runCommand({collMod:"users", index:{name:"email_1", hidden:false}});
'
```"""
    ),
    # ============================================================
    # 4. AGGREGATION ERRORS
    # ============================================================
    (
        "mongodb-lookup-size-limit",
        "MongoDB $lookup Size Limit Error",
        "Fix MongoDB $lookup aggregation pipeline size limit errors",
        r"""## MongoDB $lookup Size Limit Error

The `$lookup` stage has limitations that can cause errors:

```
MongoServerError: $lookup containing an expression cannot be applied to a constant
```

```
MongoServerError: $lookup with pipeline may not specify 'let' without a pipeline
```

## Common Causes

- Using `$lookup` with a `localField` that does not exist
- The foreign collection is very large and the lookup exceeds memory
- Using `$lookup` with `let` variables but no pipeline
- Referencing a system collection in `$lookup`
- The `foreignField` does not exist in the foreign collection
- Nested `$lookup` depth exceeds 4 levels (pre-MongoDB 5.0)

## How to Fix

### 1. Use the simple `$lookup` syntax correctly

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "product"
    }
  }
]);
```

### 2. Use pipeline-based `$lookup` for complex joins

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      let: { productId: "$productId" },
      pipeline: [
        { $match: { $expr: { $eq: ["$_id", "$$productId"] } } },
        { $project: { name: 1, price: 1 } }
      ],
      as: "product"
    }
  }
]);
```

### 3. Add indexes on the foreign collection

```javascript
db.products.createIndex({ _id: 1 });
db.orders.createIndex({ customerId: 1 });
```

### 4. Limit the result size with $unwind and $limit

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "product"
    }
  },
  { $unwind: "$product" },
  { $limit: 100 }
]);
```

## Examples

```bash
# Set up test data
mongosh --eval '
  db.orders.drop(); db.products.drop();
  db.products.insertMany([{_id:1,name:"Widget"},{_id:2,name:"Gadget"}]);
  db.orders.insertMany([{productId:1,qty:5},{productId:2,qty:3},{productId:1,qty:10}]);
'

# Simple lookup
mongosh --eval '
  let result = db.orders.aggregate([
    {$lookup:{from:"products",localField:"productId",foreignField:"_id",as:"product"}},
    {$unwind:"$product"},
    {$project:{orderQty:"$qty",productName:"$product.name"}}
  ]).toArray();
  printjson(result);
'
```"""
    ),
    (
        "mongodb-group-memory-limit",
        "MongoDB $group Memory Limit Exceeded",
        "Fix MongoDB aggregation $group exceeds memory limit errors",
        r"""## MongoDB $group Memory Limit Exceeded

The `$group` stage has a default memory limit of 100 MB:

```
$group stage exceeded memory limit of 100 MB
```

## Common Causes

- The grouping key has too many unique values
- The accumulator produces large result sets
- The collection has high cardinality on the grouping field
- No `$sort` or `$match` was applied before `$group` to reduce the dataset

## How to Fix

### 1. Allow disk spill with `allowDiskUse`

```javascript
db.sales.aggregate([
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
], { allowDiskUse: true });
```

### 2. Reduce the dataset before grouping

```javascript
db.sales.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
]);
```

### 3. Use `$bucket` or `$bucketAuto` for large cardinality

```javascript
db.sales.aggregate([
  {
    $bucket: {
      groupBy: "$amount",
      boundaries: [0, 100, 500, 1000, Infinity],
      default: "Other",
      output: { count: { $sum: 1 }, total: { $sum: "$amount" } }
    }
  }
]);
```

## Examples

```bash
# Generate test data
mongosh --eval '
  db.sales.drop();
  let ops = [];
  for (let i = 0; i < 100000; i++) {
    ops.push({category:["A","B","C","D","E"][i%5], amount: Math.random()*1000});
  }
  db.sales.insertMany(ops);
'

# Use allowDiskUse for large aggregations
mongosh --eval '
  let result = db.sales.aggregate([
    {$group:{_id:"$category", total:{$sum:"$amount"}, count:{$sum:1}}}
  ], {allowDiskUse: true}).toArray();
  printjson(result);
'
```"""
    ),
    (
        "mongodb-facet-memory-limit",
        "MongoDB $facet Memory Limit Error",
        "Fix MongoDB $facet aggregation pipeline memory limit errors",
        r"""## MongoDB $facet Memory Limit Error

The `$facet` stage has a memory limit of 100 MB per sub-pipeline:

```
$facet stage exceeded memory limit of 100 MB
```

## Common Causes

- One or more sub-pipelines produce more than 100 MB of data
- The sub-pipeline uses $group or $sortByCount on a large dataset
- No $limit is applied in sub-pipelines
- The input to $facet is too large

## How to Fix

### 1. Add $limit to each sub-pipeline

```javascript
db.products.aggregate([
  {
    $facet: {
      "topByPrice": [
        { $sort: { price: -1 } },
        { $limit: 10 },
        { $project: { name: 1, price: 1 } }
      ],
      "topByRating": [
        { $sort: { rating: -1 } },
        { $limit: 10 },
        { $project: { name: 1, rating: 1 } }
      ],
      "totalCount": [
        { $count: "count" }
      ]
    }
  }
]);
```

### 2. Reduce input before $facet

```javascript
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $facet: {
    "topPriced": [{ $sort: { price: -1 } }, { $limit: 10 }],
    "avgPrice": [{ $group: { _id: null, avg: { $avg: "$price" } } }]
  }}
]);
```

### 3. Use allowDiskUse

```javascript
db.products.aggregate([
  { $facet: { ... } }
], { allowDiskUse: true });
```

## Examples

```bash
# Demonstrate $facet with limits
mongosh --eval '
  db.products.drop();
  let products = [];
  for (let i = 0; i < 50000; i++) {
    products.push({name:"P"+i, category:["A","B","C"][i%3], price:Math.random()*100, rating:Math.random()*5});
  }
  db.products.insertMany(products);

  let result = db.products.aggregate([
    {$facet:{
      byCategory:[{$group:{_id:"$category",count:{$sum:1}}}],
      priceStats:[{$group:{_id:null,avg:{$avg:"$price"},max:{$max:"$price"}}}],
      topRated:[{$sort:{rating:-1}},{$limit:5},{$project:{name:1,rating:1}}]
    }}
  ]).toArray();
  printjson(result[0]);
'
```"""
    ),
    (
        "mongodb-accumulator-error",
        "MongoDB Aggregation Accumulator Error",
        "Fix MongoDB accumulator errors in aggregation pipeline",
        r"""## MongoDB Aggregation Accumulator Error

Accumulator errors occur in `$group` or `$setWindowFields`:

```
MongoServerError: Accumulator $sum: args must be numeric
```

```
MongoServerError: $avg requires numeric or array values
```

## Common Causes

- Non-numeric values passed to `$sum` or `$avg`
- `$push` or `$addToSet` used on a field that is null or undefined
- Mixed types in an accumulator (string + number)
- The accumulator receives an empty array when `$first` or `$last` is needed

## How to Fix

### 1. Ensure numeric types for numeric accumulators

```javascript
db.sales.aggregate([
  {
    $group: {
      _id: "$category",
      total: { $sum: "$amount" }  // 'amount' must be numeric
    }
  }
]);

// Use $convert to ensure numeric type
db.sales.aggregate([
  { $addFields: { amountNum: { $convert: { input: "$amount", to: "double", onError: 0 } } } },
  { $group: { _id: "$category", total: { $sum: "$amountNum" } } }
]);
```

### 2. Filter null values before accumulation

```javascript
db.users.aggregate([
  { $match: { score: { $exists: true, $ne: null, $type: "number" } } },
  { $group: { _id: "$department", avgScore: { $avg: "$score" } } }
]);
```

### 3. Use $cond for conditional accumulation

```javascript
db.orders.aggregate([
  {
    $group: {
      _id: "$status",
      count: { $sum: 1 },
      premiumCount: {
        $sum: { $cond: [{ $eq: ["$type", "premium"] }, 1, 0] }
      }
    }
  }
]);
```

## Examples

```bash
# Demonstrate accumulator type errors
mongosh --eval '
  db.data.drop();
  db.data.insertMany([{v:10},{v:20},{v:"thirty"},{v:40}]);
  try {
    db.data.aggregate([{$group:{_id:null, total:{$sum:"$v"}}}]);
  } catch(e) { print("Error:", e.message); }
'

# Fix: filter non-numeric values
mongosh --eval '
  let result = db.data.aggregate([
    {$match:{v:{$type:"number"}}},
    {$group:{_id:null, total:{$sum:"$v"}, avg:{$avg:"$v"}}}
  ]).toArray();
  printjson(result);
'
```"""
    ),
    (
        "mongodb-sort-memory-limit",
        "MongoDB $sort Memory Limit Exceeded",
        "Fix MongoDB $sort exceeds memory limit errors in aggregation",
        r"""## MongoDB $sort Memory Limit Exceeded

The `$sort` stage has a default memory limit of 100 MB:

```
$sort stage exceeded memory limit of 100 MB
```

## Common Causes

- Sorting a large result set without a preceding $match or $limit
- Sorting on a field with high cardinality
- The pipeline produces more than 100 MB before sorting
- The sort is not covered by an index

## How to Fix

### 1. Use allowDiskUse

```javascript
db.largeCollection.aggregate([
  { $sort: { createdAt: -1 } }
], { allowDiskUse: true });
```

### 2. Reduce data before sorting

```javascript
db.largeCollection.aggregate([
  { $match: { status: "active" } },
  { $limit: 1000 },
  { $sort: { createdAt: -1 } }
]);
```

### 3. Use $sort with $limit (optimized in MongoDB 4.4+)

```javascript
// MongoDB optimizes $sort + $limit to use less memory
db.largeCollection.aggregate([
  { $sort: { score: -1 } },
  { $limit: 100 }
]);
```

### 4. Create an index to support the sort

```javascript
db.largeCollection.createIndex({ createdAt: -1 });
```

## Examples

```bash
# Check if allowDiskUse is needed
mongosh --eval '
  let result = db.logs.aggregate([
    {$sort:{timestamp:-1}},
    {$limit:10}
  ], {allowDiskUse: true}).explain("executionStats");
  print("Sort usage:", result.stages ? "in-memory" : "index");
'

# Optimize with $sort + $limit
mongosh --eval '
  db.logs.aggregate([
    {$sort:{timestamp:-1}},
    {$limit:10}
  ], {allowDiskUse:true}).toArray();
'
```"""
    ),
    (
        "mongodb-project-field-mismatch",
        "MongoDB $project Field Mismatch Error",
        "Fix MongoDB $project aggregation stage field errors",
        r"""## MongoDB $project Field Mismatch Error

The `$project` stage can produce unexpected errors:

```
MongoServerError: $project with inclusion and exclusion cannot coexist
```

```
Cannot create field 'x' in element {_id: ...}
```

## Common Causes

- Mixing inclusion (1) and exclusion (0) in the same $project stage
- Referencing a field that does not exist
- Trying to project `_id` as 0 without explicit exclusion
- Using a field path that conflicts with an existing field

## How to Fix

### 1. Use only inclusion OR exclusion, not both

```javascript
// Wrong: mixing inclusion and exclusion
db.users.aggregate([
  { $project: { name: 1, email: 0 } }  // Error!
]);

// Correct: inclusion only
db.users.aggregate([
  { $project: { name: 1, email: 1 } }
]);
```

### 2. Exclude _id explicitly when using inclusion

```javascript
db.users.aggregate([
  { $project: { _id: 0, name: 1, email: 1 } }
]);
```

### 3. Use $addFields instead of $project for computed fields

```javascript
db.users.aggregate([
  { $addFields: { fullName: { $concat: ["$firstName", " ", "$lastName"] } } }
]);
```

### 4. Use $replaceRoot or $replaceWith for complete restructuring

```javascript
db.users.aggregate([
  { $replaceRoot: { newRoot: { name: "$name", email: "$email" } } }
]);
```

## Examples

```bash
# Demonstrate inclusion/exclusion error
mongosh --eval '
  db.test.drop();
  db.test.insertOne({name:"Alice",age:30,email:"a@test.com"});
  try {
    db.test.aggregate([{$project:{name:1,email:0}}]);
  } catch(e) { print("Error:", e.message); }
'

# Fix: use only inclusion
mongosh --eval '
  let result = db.test.aggregate([{$project:{_id:0,name:1,age:1}}]).toArray();
  printjson(result);
'
```"""
    ),
    (
        "mongodb-unwind-array-error",
        "MongoDB $unwind Array Error",
        "Fix MongoDB $unwind aggregation array errors",
        r"""## MongoDB $unwind Array Error

The `$unwind` stage fails when the input field is not an array:

```
MongoServerError: $unwind requires that the value of 'path' must be an array
```

```
Cannot unwind non-array field 'tags'
```

## Common Causes

- The field being unwound does not exist in some documents
- The field is not an array type (it is a string or object)
- Using `$unwind` on a nested field without first projecting it
- The array is empty, causing the document to be excluded
- Missing `preserveNullAndEmptyArrays` when nulls are expected

## How to Fix

### 1. Ensure the field is an array before unwinding

```javascript
db.articles.aggregate([
  { $match: { tags: { $type: "array" } } },
  { $unwind: "$tags" }
]);
```

### 2. Use preserveNullAndEmptyArrays

```javascript
db.articles.aggregate([
  {
    $unwind: {
      path: "$tags",
      preserveNullAndEmptyArrays: true
    }
  }
]);
```

### 3. Convert non-array fields to arrays first

```javascript
db.articles.aggregate([
  {
    $addFields: {
      tags: {
        $cond: {
          if: { $eq: [{ $type: "$tags" }, "array"] },
          then: "$tags",
          else: ["$tags"]
        }
      }
    }
  },
  { $unwind: "$tags" }
]);
```

## Examples

```bash
# Demonstrate unwind with missing arrays
mongosh --eval '
  db.posts.drop();
  db.posts.insertMany([
    {title:"Post1", tags:["mongo","db"]},
    {title:"Post2", tags:"single-tag"},
    {title:"Post3"}
  ]);

  try {
    db.posts.aggregate([{$unwind:"$tags"}]);
  } catch(e) { print("Error:", e.message); }

  let result = db.posts.aggregate([
    {$match:{tags:{$type:"array"}}},
    {$unwind:"$tags"},
    {$group:{_id:"$tags", count:{$sum:1}}}
  ]).toArray();
  printjson(result);
'
```"""
    ),
    (
        "mongodb-bucket-boundaries-error",
        "MongoDB $bucket Boundaries Error",
        "Fix MongoDB $bucket aggregation boundary errors",
        r"""## MongoDB $bucket Boundaries Error

The `$bucket` stage fails with boundary errors:

```
MongoServerError: $bucket boundaries must be monotonically increasing
```

```
MongoServerError: $bucket requires boundaries to be comparable
```

## Common Causes

- Boundaries are not in ascending order
- Boundary values are of mixed types (string and number)
- The default bucket range does not cover all documents
- Boundaries have duplicate values

## How to Fix

### 1. Provide monotonically increasing boundaries

```javascript
db.sales.aggregate([
  {
    $bucket: {
      groupBy: "$amount",
      boundaries: [0, 50, 100, 500, 1000],
      default: "Other",
      output: { count: { $sum: 1 } }
    }
  }
]);
```

### 2. Use consistent types for boundaries

```javascript
// Correct: all numeric
boundaries: [0, 50, 100, 500, 1000]
```

### 3. Use $bucketAuto for automatic boundaries

```javascript
db.sales.aggregate([
  {
    $bucketAuto: {
      groupBy: "$amount",
      buckets: 4,
      output: { count: { $sum: 1 }, avgAmount: { $avg: "$amount" } }
    }
  }
]);
```

## Examples

```bash
# Set up test data
mongosh --eval '
  db.scores.drop();
  db.scores.insertMany([{s:10},{s:25},{s:45},{s:70},{s:85},{s:95}]);

  let result = db.scores.aggregate([
    {$bucket:{
      groupBy:"$s",
      boundaries:[0,30,60,80,100],
      default:"Other",
      output:{count:{$sum:1},values:{$push:"$s"}}
    }}
  ]).toArray();
  printjson(result);
'
```"""
    ),
    (
        "mongodb-geonear-syntax-error",
        "MongoDB $geoNear Syntax Error",
        "Fix MongoDB $geoNear aggregation stage syntax errors",
        r"""## MongoDB $geoNear Syntax Error

The `$geoNear` stage has strict syntax requirements:

```
MongoServerError: $geoNear requires that 'near' is a GeoJSON point
```

```
MongoServerError: $geoNear requires 'distanceField' to be specified
```

## Common Causes

- Missing required fields (`near`, `distanceField`)
- The `near` value is not a valid GeoJSON point
- Using `$geoNear` without a `2dsphere` index
- Mixing `maxDistance` and `minDistance` incorrectly
- The `key` field references a non-indexed field

## How to Fix

### 1. Include all required fields

```javascript
db.places.aggregate([
  {
    $geoNear: {
      near: { type: "Point", coordinates: [-73.97, 40.78] },
      distanceField: "distance",
      maxDistance: 5000,
      query: { type: "park" },
      spherical: true
    }
  }
]);
```

### 2. Ensure a 2dsphere index exists

```javascript
db.places.createIndex({ location: "2dsphere" });
```

### 3. Use the correct distanceField output

```javascript
db.places.aggregate([
  {
    $geoNear: {
      near: { type: "Point", coordinates: [-73.97, 40.78] },
      distanceField: "distFromCenter",
      maxDistance: 10000,
      spherical: true
    }
  },
  { $sort: { distFromCenter: 1 } },
  { $limit: 10 }
]);
```

## Examples

```bash
# Create geospatial collection with correct setup
mongosh --eval '
  db.places.drop();
  db.places.createIndex({location:"2dsphere"});
  db.places.insertMany([
    {name:"Library", location:{type:"Point",coordinates:[-73.97,40.78]}, type:"building"},
    {name:"Park", location:{type:"Point",coordinates:[-73.96,40.79]}, type:"park"},
    {name:"Cafe", location:{type:"Point",coordinates:[-73.98,40.77]}, type:"restaurant"}
  ]);

  let result = db.places.aggregate([
    {$geoNear:{
      near:{type:"Point", coordinates:[-73.97,40.78]},
      distanceField:"distance",
      maxDistance:2000,
      spherical:true,
      query:{type:"park"}
    }}
  ]).toArray();
  printjson(result);
'
```"""
    ),
    (
        "mongodb-aggregation-timeout",
        "MongoDB Aggregation Pipeline Timeout",
        "Fix MongoDB aggregation timeout errors",
        r"""## MongoDB Aggregation Pipeline Timeout

Aggregation pipelines can timeout on large collections:

```
MongoServerError: operation exceeded time limit
```

```
MongoServerError: aggregation timed out
```

## Common Causes

- The pipeline is processing too many documents
- Multiple stages without index support
- The pipeline runs during peak hours
- No `$match` or `$limit` early in the pipeline
- The pipeline uses expensive stages like `$lookup` on large collections

## How to Fix

### 1. Optimize pipeline stage order

```javascript
// Good: filter early
db.sales.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $match: { status: "completed" } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
]);
```

### 2. Use allowDiskUse for large datasets

```javascript
db.sales.aggregate([...pipeline], { allowDiskUse: true });
```

### 3. Add indexes to support $match stages

```javascript
db.sales.createIndex({ date: 1 });
db.sales.createIndex({ status: 1 });
```

### 4. Use $limit early in the pipeline

```javascript
db.sales.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $limit: 10000 },
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
]);
```

## Examples

```bash
# Test aggregation performance
mongosh --eval '
  let start = Date.now();
  let result = db.sales.aggregate([
    {$match:{date:{$gte:new Date("2024-01-01")}}},
    {$group:{_id:"$category",total:{$sum:"$amount"}}},
    {$sort:{total:-1}}
  ], {allowDiskUse:true}).toArray();
  print("Aggregation took:", Date.now()-start, "ms");
  print("Results:", result.length);
'
```"""
    ),
    # ============================================================
    # 5. REPLICA SET ERRORS
    # ============================================================
    (
        "mongodb-no-primary",
        "MongoDB No Primary Available",
        "Fix MongoDB replica set no primary available errors",
        r"""## MongoDB No Primary Available Error

```
MongoServerError: not primary and secondaryOk=false
```

```
MongoServerSelectionError: No replica set primary available
```

## Common Causes

- The replica set is in the process of electing a new primary
- All eligible nodes are down or unreachable
- A network partition has isolated the primary
- The primary has stepped down
- There are not enough voting members to elect a primary

## How to Fix

### 1. Check replica set status

```javascript
rs.status()
rs.isMaster()
```

### 2. Wait for election to complete

Elections typically take 10-15 seconds. Wait and retry.

### 3. Read from secondaries if allowed

```javascript
const client = new MongoClient(uri, {
  readPreference: 'secondaryPreferred'
});
```

Or with mongosh:

```bash
mongosh --readPreference secondaryPreferred
```

### 4. Check network connectivity between members

```bash
mongosh --eval "rs.status().members.forEach(m => print(m.name, m.stateStr, m.optimeDate))"
```

## Examples

```bash
# Check who is primary
mongosh --eval "rs.isMaster().primary"

# Check member states
mongosh --eval '
  rs.status().members.forEach(m => {
    print(m.name, m.stateStr, "votes:", m.votes, "priority:", m.priority);
  });
'

# Read from secondary
mongosh --readPreference secondaryPreferred --eval "db.users.find().limit(5).toArray()"
```"""
    ),
    (
        "mongodb-stale-secondary",
        "MongoDB Stale Secondary Error",
        "Fix MongoDB stale secondary errors during reads",
        r"""## MongoDB Stale Secondary Error

A stale secondary has fallen too far behind the primary:

```
MongoServerError: command secondaryAllowed : stale
```

## Common Causes

- The secondary cannot keep up with the primary's write volume
- Network latency between primary and secondary
- The secondary is performing heavy read operations
- The oplog is too small to retain the necessary operations
- The secondary was down for too long and needs to resync

## How to Fix

### 1. Check replication lag

```javascript
rs.printReplicationInfo()    // Primary's oplog
rs.printSecondaryReplicationInfo()  // Secondary's lag
```

### 2. Increase the oplog size

```bash
mongosh --eval '
  db.adminCommand({
    resizeOplog: 1,
    size: 10240  // 10 GB
  });
'
```

### 3. Reduce read load on secondaries

```javascript
const client = new MongoClient(uri, {
  readPreference: 'primary'
});
```

### 4. Monitor and fix replication lag

```bash
mongosh --eval '
  let primary = rs.printReplicationInfo();
  let secondary = rs.printSecondaryReplicationInfo();
'
```

### 5. Resync a severely lagging secondary

```bash
# On the lagging secondary
mongosh --eval "db.adminCommand({resync: 1})"
```

## Examples

```bash
# Check replication status
mongosh --eval "rs.printReplicationInfo()"
mongosh --eval "rs.printSecondaryReplicationInfo()"

# Check oplog size and usage
mongosh --eval '
  let stats = db.replicationInfo();
  print("Oplog size:", stats.logSizeMB, "MB");
  print("Used:", stats.usedMB, "MB");
  print("Time window:", stats.tFirst, "to", stats.tLast);
'
```"""
    ),
    (
        "mongodb-replication-lag",
        "MongoDB Replication Lag Error",
        "Fix MongoDB replication lag issues between primary and secondary",
        r"""## MongoDB Replication Lag Error

Replication lag is the delay between the primary and secondary:

```
// Primary optime: 2024-01-15T12:00:00Z
// Secondary optime: 2024-01-15T11:50:00Z
// Lag: 10 minutes
```

## Common Causes

- Insufficient network bandwidth between replica set members
- The secondary is under heavy read load
- Write volume exceeds the secondary's replication capacity
- Disk I/O bottleneck on the secondary
- Large operations causing lag
- The oplog is too small

## How to Fix

### 1. Monitor lag continuously

```javascript
rs.status().members.filter(m => m.stateStr === "SECONDARY").forEach(m => {
  const lag = rs.status().date - m.optimeDate;
  print(m.name, "lag:", lag + "ms");
});
```

### 2. Increase oplog size

```javascript
db.adminCommand({ resizeOplog: 1, size: 10240 });
```

### 3. Optimize secondary performance

```bash
# Ensure the secondary has good I/O
iostat -x 1 5

# Check WiredTiger cache pressure
mongosh --eval "db.serverStatus().wiredTiger.cache"
```

### 4. Reduce primary write volume

- Use bulk operations instead of individual inserts
- Batch writes to reduce oplog entries
- Consider sharding for write scaling

## Examples

```bash
# Create a lag monitoring script
mongosh --eval '
  setInterval(() => {
    let status = rs.status();
    status.members.filter(m => m.stateStr === "SECONDARY").forEach(m => {
      let lag = status.date - m.optimeDate;
      let status = lag > 10000 ? "WARNING" : "OK";
      print(`[${status}] ${m.name}: lag ${lag}ms`);
    });
  }, 5000);
'
```"""
    ),
    (
        "mongodb-replsetinitiate-failure",
        "MongoDB replSetInitiate Failure",
        "Fix MongoDB replica set initialization errors",
        r"""## MongoDB replSetInitiate Failure

```
MongoServerError: replSetInitiate quorum check failed
```

```
MongoServerError: members are already initialized
```

## Common Causes

- The replica set is already initialized
- Members in the config are not reachable
- The initiate command was run on a non-empty data directory
- Member hostnames cannot be resolved
- Not enough members can be reached to form a quorum

## How to Fix

### 1. Check if the set is already initialized

```javascript
rs.status()
```

### 2. Verify all members are reachable

```bash
mongosh --host mongo1 --port 27017 --eval "db.adminCommand({ping:1})"
mongosh --host mongo2 --port 27017 --eval "db.adminCommand({ping:1})"
mongosh --host mongo3 --port 27017 --eval "db.adminCommand({ping:1})"
```

### 3. Use rs.initiate() with the correct config

```javascript
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017", priority: 2 },
    { _id: 1, host: "mongo2:27017", priority: 1 },
    { _id: 2, host: "mongo3:27017", priority: 1 }
  ]
});
```

### 4. Ensure the data directory is empty on new members

```bash
sudo systemctl stop mongod
sudo rm -rf /var/lib/mongodb/*
sudo systemctl start mongod
```

## Examples

```bash
# Check replica set status
mongosh --eval "rs.status()"

# Force re-initiation
mongosh --eval '
  rs.reconfig({
    _id: "rs0",
    members: [
      {_id:0, host:"mongo1:27017"},
      {_id:1, host:"mongo2:27017"},
      {_id:2, host:"mongo3:27017"}
    ]
  }, {force: true});
'
```"""
    ),
    (
        "mongodb-replsetreconfig-unsafe",
        "MongoDB replSetReconfig Not Safe",
        "Fix MongoDB replica set reconfiguration safety issues",
        r"""## MongoDB replSetReconfig Not Safe Error

```
MongoServerError: Reconfig would remove a voting member that has data
```

```
MongoServerError: only one voting member at a time may be removed
```

## Common Causes

- Attempting to remove a member with votes and data simultaneously
- Removing too many voting members at once
- The new configuration would leave less than 3 voting members
- Changing the `_id` of an existing member

## How to Fix

### 1. Use { force: true } cautiously

```javascript
// Safe reconfiguration (requires majority)
rs.reconfig(newConfig);

// Force reconfiguration (only from one member, bypasses checks)
rs.reconfig(newConfig, { force: true });
```

### 2. Remove members one at a time

```javascript
rs.remove("mongo4:27017");
// Wait for stability, then remove another if needed
rs.remove("mongo5:27017");
```

### 3. Verify the new config is valid before applying

```javascript
const config = rs.conf();
config.members = config.members.filter(m => m.host !== "mongo4:27017");
rs.reconfig(config);
```

## Examples

```bash
# View current configuration
mongosh --eval "printjson(rs.conf())"

# Safely add a member
mongosh --eval '
  let config = rs.conf();
  config.members.push({_id:3, host:"mongo4:27017", priority:0.5});
  rs.reconfig(config);
'
```"""
    ),
    (
        "mongodb-vote-count-error",
        "MongoDB Replica Set Vote Count Error",
        "Fix MongoDB replica set voting member count errors",
        r"""## MongoDB Replica Set Vote Count Error

```
MongoServerError: ReplSet cfg has members that cast 2 votes, which is invalid
```

## Common Causes

- More than 7 voting members in the replica set
- A member has more than 1 vote configured
- The number of voting members is even

## How to Fix

### 1. Limit voting members to 7 or fewer

```javascript
rs.reconfig({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017", votes: 1 },
    { _id: 1, host: "mongo2:27017", votes: 1 },
    { _id: 2, host: "mongo3:27017", votes: 1 },
    { _id: 3, host: "mongo4:27017", votes: 0 }
  ]
});
```

### 2. Ensure an odd number of voting members

```javascript
// Use an arbiter for even-numbered setups
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" },
    { _id: 3, host: "mongo4:27017" },
    { _id: 4, host: "arbiter:27017", arbiterOnly: true }
  ]
});
```

### 3. Check current vote configuration

```javascript
rs.conf().members.forEach(m => {
  print(m.host, "votes:", m.votes, "priority:", m.priority);
});
```

## Examples

```bash
# Check voting members
mongosh --eval '
  rs.conf().members.forEach(m => {
    print(m.host, "votes:", m.votes);
  });
'

# Change a member to non-voting
mongosh --eval '
  let config = rs.conf();
  config.members[3].votes = 0;
  rs.reconfig(config);
'
```"""
    ),
    (
        "mongodb-election-timeout",
        "MongoDB Election Timeout Error",
        "Fix MongoDB replica set election timeout issues",
        r"""## MongoDB Election Timeout Error

```
MongoServerError: ELECTION FAILED
```

```
rsMember is in state PRIMARY but heartbeat says DOWN
```

## Common Causes

- Network latency between replica set members exceeds the election timeout
- The `electionTimeoutMillis` is too low
- Members cannot reach each other due to firewall rules
- Clock skew between members
- Too many members are down

## How to Fix

### 1. Increase the election timeout

```javascript
rs.reconfig({
  _id: "rs0",
  settings: {
    electionTimeoutMillis: 30000  // Default is 10000 (10 seconds)
  }
});
```

### 2. Ensure network connectivity between all members

```bash
ping mongo2
ping mongo3
sudo iptables -L -n | grep 27017
```

### 3. Synchronize clocks

```bash
sudo ntpdate pool.ntp.org
# Or use chrony
sudo chronyc makestep
```

## Examples

```bash
# Check election-related settings
mongosh --eval '
  let config = rs.conf();
  print("Election timeout:", config.settings.electionTimeoutMillis, "ms");
  print("Members:", config.members.length);
'

# Update election timeout
mongosh --eval '
  rs.reconfig({
    _id: "rs0",
    settings: { electionTimeoutMillis: 30000 },
    members: rs.conf().members
  });
'
```"""
    ),
    (
        "mongodb-downstream-member-error",
        "MongoDB Downstream Member Error",
        "Fix MongoDB replica set downstream member communication errors",
        r"""## MongoDB Downstream Member Error

```
ReplSet info: member mongo2:27017 is now in state DOWN
```

```
MongoServerError: member is not reachable
```

## Common Causes

- The downstream member has crashed or been shut down
- Network connectivity is lost between members
- The member's data directory is corrupted
- Disk full on the downstream member
- Firewall rules changed

## How to Fix

### 1. Check the member's status

```bash
ssh mongo2 "sudo systemctl status mongod"
ssh mongo2 "df -h"
ssh mongo2 "free -h"
```

### 2. Restart the member

```bash
ssh mongo2 "sudo systemctl restart mongod"
```

### 3. Check for corruption

```bash
ssh mongo2 "mongosh --eval 'db.adminCommand({repairDatabase: 1})'"
```

### 4. Monitor heartbeat status

```javascript
rs.status().members.forEach(m => {
  print(m.name, m.stateStr, "lastHeartbeat:", m.lastHeartbeat);
});
```

## Examples

```bash
# Check member connectivity
mongosh --eval '
  rs.status().members.forEach(m => {
    print(m.name, m.stateStr, "health:", m.health,
          "lastHeartbeat:", m.lastHeartbeat);
  });
'
```"""
    ),
    (
        "mongodb-rollback-error",
        "MongoDB Rollback Error",
        "Fix MongoDB replica set rollback errors",
        r"""## MongoDB Rollback Error

```
MongoServerError: rollback is needed
```

## Common Causes

- The primary was isolated and writes went to a different node
- The old primary rejoins and must roll back uncommitted changes
- Network partition caused split-brain
- The oplog on the new primary does not contain the old primary's writes

## How to Fix

### 1. Prevent unnecessary rollbacks

- Use `w: "majority"` write concern for critical writes
- This ensures writes are on a majority of members before acknowledging

### 2. Check rollback data

```bash
# Look for rollback files
ls -la /var/lib/mongodb/*.bson

# Rollback files are saved in the data directory
mongodump --db local --collection rollback
```

### 3. Apply rollback data manually

```bash
sudo systemctl stop mongod
mongorestore --db local --collection <collection> /var/lib/mongodb/rollback/<file>.bson
sudo systemctl start mongod
```

### 4. Monitor for rollback events

```javascript
db.serverStatus().repl
```

```bash
grep -i "rollback" /var/log/mongodb/mongod.log
```

## Examples

```bash
# Check for rollback files
find /var/log/mongodb/ -name "*.bson" -o -name "rollback" 2>/dev/null

# Monitor rollback status
mongosh --eval '
  let status = db.serverStatus().repl;
  print("Replication state:", status.ismaster);
  print("Sync source:", status.syncSourceHost);
'

# Check oplog freshness
mongosh --eval "rs.printReplicationInfo()"
```"""
    ),
    (
        "mongodb-heartbeat-timeout",
        "MongoDB Heartbeat Timeout Error",
        "Fix MongoDB replica set heartbeat timeout issues",
        r"""## MongoDB Heartbeat Timeout Error

```
heartbeat to mongo2:27017 timed out
```

```
MongoServerError: Heartbeat to mongo3:27017 failed
```

## Common Causes

- Network latency between members is too high
- The member is overloaded and cannot respond to heartbeats
- Firewall or network device is dropping heartbeat packets
- The member is performing a long-running operation
- DNS resolution is slow

## How to Fix

### 1. Increase heartbeat intervals

```javascript
rs.reconfig({
  _id: "rs0",
  settings: {
    heartbeatPeriodMillis: 5000,
    electionTimeoutMillis: 30000
  }
});
```

### 2. Optimize network between members

```bash
ping -c 10 mongo2
ping -c 10 mongo3
mtr mongo2
```

### 3. Reduce load on heartbeat targets

```bash
ssh mongo2 "iostat -x 1 5"
ssh mongo2 "top -bn1 | head -20"
```

### 4. Verify firewall rules

```bash
sudo iptables -L -n
```

## Examples

```bash
# Check heartbeat status
mongosh --eval '
  rs.status().members.forEach(m => {
    let lastHB = m.lastHeartbeat ? new Date() - m.lastHeartbeat : "N/A";
    print(m.name, "lastHeartbeat:", lastHB, "ms ago");
  });
'
```"""
    ),
    # ============================================================
    # 6. SHARDING ERRORS
    # ============================================================
    (
        "mongodb-no-shard-key",
        "MongoDB No Shard Key Error",
        "Fix MongoDB missing shard key errors for sharded collections",
        r"""## MongoDB No Shard Key Error

```
MongoServerError: no shard key found in query
```

```
No shard key exists in the query: { }
```

## Common Causes

- The collection is sharded but the query does not include the shard key
- The shard key field was misspelled in the query
- The insert/update operation does not include the shard key

## How to Fix

### 1. Include the shard key in all queries

```javascript
// If the collection is sharded on { userId: 1 }
db.orders.find({ userId: 123, status: "shipped" });  // Correct
db.orders.find({ status: "shipped" });  // Missing shard key
```

### 2. Use scatter-gather queries when shard key is unknown

```javascript
db.orders.find({ status: "shipped" }).comment("scatter-gather");
```

### 3. Shard the collection with a proper key

```javascript
sh.shardCollection("mydb.orders", { userId: 1 });
```

## Examples

```bash
# Check shard distribution
mongosh --eval "sh.status()"

# Check which shard a document lives on
mongosh --eval '
  db.orders.find({userId:123}).explain().shards
'
```"""
    ),
    (
        "mongodb-shard-key-not-indexed",
        "MongoDB Shard Key Not Indexed Error",
        "Fix MongoDB shard key must be indexed errors",
        r"""## MongoDB Shard Key Not Indexed Error

```
MongoServerError: shard key must be an indexed field
```

```
Please create an index that starts with the shard key
```

## Common Causes

- The shard key field is not indexed
- The index on the shard key was dropped

## How to Fix

### 1. Create the required index

```javascript
db.orders.createIndex({ userId: 1 });
sh.shardCollection("mydb.orders", { userId: 1 });
```

### 2. For hashed shard keys

```javascript
db.orders.createIndex({ userId: "hashed" });
sh.shardCollection("mydb.orders", { userId: "hashed" });
```

### 3. For compound shard keys

```javascript
db.orders.createIndex({ customerId: 1, orderId: 1 });
sh.shardCollection("mydb.orders", { customerId: 1, orderId: 1 });
```

## Examples

```bash
# Check current indexes before sharding
mongosh --eval "db.orders.getIndexes()"

# Create the index and shard
mongosh --eval '
  db.orders.createIndex({userId:1});
  sh.shardCollection("mydb.orders", {userId:1});
  print("Collection sharded successfully");
'
```"""
    ),
    (
        "mongodb-shard-not-found",
        "MongoDB Shard Not Found Error",
        "Fix MongoDB shard not found errors in sharded cluster",
        r"""## MongoDB Shard Not Found Error

```
MongoServerError: shard <shard_name> was not found
```

## Common Causes

- The shard was removed from the cluster
- The config servers have stale data
- The shard name in the connection string is wrong
- The shard was never added to the cluster

## How to Fix

### 1. Add the shard to the cluster

```javascript
sh.addShard("shard1/mongo-shard1:27017");
```

### 2. Check current shards

```javascript
sh.status()
// or
db.adminCommand({ listShards: 1 })
```

### 3. Verify the config server is healthy

```bash
mongosh --host config1:27017 --eval "db.adminCommand({listShards:1})"
```

## Examples

```bash
# List all shards in the cluster
mongosh --eval "sh.status()"

# Add a new shard
mongosh --eval 'sh.addShard("shard2/mongo-shard2:27017")'

# Check which shard a collection is on
mongosh --eval "db.orders.getShardDistribution()"
```"""
    ),
    (
        "mongodb-balancer-error",
        "MongoDB Balancer Error",
        "Fix MongoDB balancer errors in sharded cluster",
        r"""## MongoDB Balancer Error

```
Balancer failed to run
```

```
MongoServerError: balancer did not start
```

## Common Causes

- The balancer is not enabled
- The config servers are not accessible
- Chunk migration failed and the balancer stopped
- The balancer lock is stale

## How to Fix

### 1. Check balancer status

```javascript
sh.getBalancerState()
sh.isBalancerRunning()
```

### 2. Enable the balancer

```javascript
sh.startBalancer()
```

### 3. Check the balancer lock

```javascript
use config
db.locks.find({ _id: "balancer" })
```

### 4. Disable and re-enable the balancer

```javascript
sh.stopBalancer()
// Wait a few seconds
sh.startBalancer()
```

## Examples

```bash
# Check balancer status
mongosh --eval '
  print("Balancer state:", sh.getBalancerState());
  print("Running:", sh.isBalancerRunning());
'

# Start the balancer
mongosh --eval 'sh.startBalancer()'

# Check chunk distribution
mongosh --eval 'sh.status({showBalancer: true})'
```"""
    ),
    (
        "mongodb-chunk-migration-failure",
        "MongoDB Chunk Migration Failure",
        "Fix MongoDB chunk migration errors in sharded cluster",
        r"""## MongoDB Chunk Migration Failure

```
Migration failed for chunk ...
```

```
chunk migration failed: write conflict
```

## Common Causes

- The destination shard does not have enough resources
- Network connectivity between shards is lost
- The chunk is too large to migrate
- Write conflicts during migration
- The balancer lock was lost

## How to Fix

### 1. Check chunk sizes

```javascript
sh.status()
```

### 2. Split large chunks manually

```javascript
sh.splitAt("mydb.orders", { userId: 500 });
```

### 3. Check shard disk space

```bash
ssh shard1 "df -h /var/lib/mongodb"
ssh shard2 "df -h /var/lib/mongodb"
```

### 4. Move chunks manually

```javascript
sh.moveChunk("mydb.orders", { userId: 100 }, "shard2");
```

## Examples

```bash
# Check chunk distribution
mongosh --eval "sh.status()"

# Split a chunk manually
mongosh --eval 'sh.splitAt("mydb.orders", {userId:1000})'

# Move a specific chunk
mongosh --eval 'sh.moveChunk("mydb.orders", {userId:500}, "shard2")'
```"""
    ),
    (
        "mongodb-shard-too-large",
        "MongoDB Shard Too Large Error",
        "Fix MongoDB shard too large or unbalanced shard errors",
        r"""## MongoDB Shard Too Large Error

A shard becomes too large when it has significantly more data than others:

```
// Shard1: 500GB, Shard2: 50GB - unbalanced
```

## Common Causes

- The shard key has low cardinality
- Chunk splits are not happening correctly
- The balancer cannot move chunks efficiently
- Hot spots in the data distribution

## How to Fix

### 1. Choose a better shard key

```javascript
// Bad shard key with low cardinality
sh.shardCollection("mydb.orders", { country: 1 });

// Better: higher cardinality key
sh.shardCollection("mydb.orders", { userId: 1 });
```

### 2. Use a hashed shard key for even distribution

```javascript
sh.shardCollection("mydb.orders", { userId: "hashed" });
```

### 3. Check current distribution

```javascript
sh.getShardDistribution()
```

### 4. Split and move chunks manually

```javascript
sh.splitAt("mydb.orders", { userId: 500 });
sh.moveChunk("mydb.orders", { userId: 250 }, "shard2");
```

## Examples

```bash
# Check shard distribution
mongosh --eval "sh.getShardDistribution()"

# Find the shard with most data
mongosh --eval '
  let dist = sh.getShardDistribution();
  Object.keys(dist).forEach(shard => {
    print(shard, "data:", dist[shard].data, "docs:", dist[shard].docs);
  });
'
```"""
    ),
    (
        "mongodb-jumbo-chunk",
        "MongoDB Jumbo Chunk Error",
        "Fix MongoDB jumbo chunk errors in sharded cluster",
        r"""## MongoDB Jumbo Chunk Error

A jumbo chunk cannot be moved because it exceeds the chunk size limit:

```
chunk is jumbo: moveChunk failed
```

## Common Causes

- The chunk size exceeds the configured chunkSize (default 64 MB)
- The shard key has low cardinality
- The balancer cannot split the chunk further

## How to Fix

### 1. Check for jumbo chunks

```javascript
sh.status({ verbose: 1 })
```

### 2. Split the jumbo chunk

```javascript
sh.splitAt("mydb.orders", { userId: 500 })
```

### 3. Increase chunk size

```javascript
use config
db.settings.updateOne(
  { _id: "chunksize" },
  { $set: { value: 128 } },
  { upsert: true }
);
```

## Examples

```bash
# Find jumbo chunks
mongosh --eval '
  db.chunks.find({ns:"mydb.orders"}).forEach(chunk => {
    let size = chunk.jumbo ? "JUMBO" : "normal";
    print(size, JSON.stringify(chunk.min), "->", JSON.stringify(chunk.max));
  });
'

# Update chunk size
mongosh --eval '
  use config;
  db.settings.updateOne({_id:"chunksize"}, {$set:{value:128}}, {upsert:true});
  print("Chunk size updated to 128 MB");
'
```"""
    ),
    (
        "mongodb-zone-mismatch",
        "MongoDB Zone Mismatch Error",
        "Fix MongoDB zone sharding configuration errors",
        r"""## MongoDB Zone Mismatch Error

Zone sharding errors occur when zone ranges do not match the shard key:

```
MongoServerError: zone range does not match the shard key
```

## Common Causes

- The zone range boundaries do not align with the shard key type
- The shard is not assigned to the correct zone
- The zone tag does not exist
- The range is overlapping with another zone

## How to Fix

### 1. Verify zone configuration

```javascript
sh.status()
```

### 2. Add a shard to a zone

```javascript
sh.addShardTag("shard1", "US-EAST")
sh.addShardTag("shard2", "US-WEST")
```

### 3. Define zone ranges

```javascript
sh.updateZoneKeyRange("mydb.users", { region: "east" }, { region: "east;" }, "US-EAST")
```

### 4. Ensure ranges do not overlap

```javascript
// Check existing zone ranges
use config
db.tags.find()
```

## Examples

```bash
# Set up zone sharding
mongosh --eval '
  // Add tags to shards
  sh.addShardTag("shard1", "US-EAST")
  sh.addShardTag("shard2", "US-WEST")

  // Define zone ranges
  sh.updateZoneKeyRange("mydb.users", {zip:{$gte:"01000",$lt:"30000"}}, "US-EAST")
  sh.updateZoneKeyRange("mydb.users", {zip:{$gte:"90000",$lt:"99999"}}, "US-WEST")

  sh.status()
'
```"""
    ),
    (
        "mongodb-shard-key-range-error",
        "MongoDB Shard Key Range Error",
        "Fix MongoDB shard key range errors in queries",
        r"""## MongoDB Shard Key Range Error

```
MongoServerError: bad shard key pattern: not a valid prefix of compound shard key
```

```
shard key range not supported
```

## Common Causes

- The query filter on the shard key is invalid
- The range query on a hashed shard key is not supported
- The shard key pattern does not match the expected format

## How to Fix

### 1. Use equality or range on prefix of shard key

```javascript
// For shard key { a: 1, b: 1 }
db.coll.find({ a: 1 })             // Works (prefix)
db.coll.find({ a: 1, b: 1 })      // Works (full key)
db.coll.find({ b: 1 })             // Missing prefix 'a'
```

### 2. For hashed shard keys, use equality only

```javascript
// For hashed shard key { userId: "hashed" }
db.orders.find({ userId: 123 })    // Works (equality)
db.orders.find({ userId: { $gt: 100 } })  // Does NOT work
```

### 3. Use targeted queries with the shard key

```javascript
db.orders.find({ userId: 123, status: "shipped" })
```

## Examples

```bash
# Check shard key type
mongosh --eval '
  let stats = db.orders.stats();
  print("Shard key:", JSON.stringify(stats.shardKey));
'

# Verify query uses shard key
mongosh --eval '
  db.orders.find({userId:123}).explain().executionStats
'
```"""
    ),
    (
        "mongodb-mongos-connection-error",
        "MongoDB mongos Connection Error",
        "Fix MongoDB mongos router connection errors",
        r"""## MongoDB mongos Connection Error

```
MongoServerError: could not find mongos in config servers
```

```
MongoServerError: mongos instance not found
```

## Common Causes

- The mongos process is not running
- The config servers are unreachable from mongos
- The mongos was started with incorrect config server addresses
- Network issues between mongos and config servers
- The mongos process crashed

## How to Fix

### 1. Start or restart mongos

```bash
mongos --configdb configRS/config1:27017,config2:27017,config3:27017 --bind_ip 0.0.0.0 --port 27017
```

### 2. Check mongos logs

```bash
tail -100 /var/log/mongodb/mongos.log
```

### 3. Verify config server connectivity from mongos

```bash
mongosh --host config1:27017 --eval "db.adminCommand({ping:1})"
```

### 4. Check mongos status

```javascript
sh.status()
```

## Examples

```bash
# Start mongos as a service
sudo systemctl start mongos

# Check if mongos is running
ps aux | grep mongos

# Verify connection to config servers
mongosh --host mongos --eval "sh.status()"
```"""
    ),
    # ============================================================
    # 7. TRANSACTION ERRORS
    # ============================================================
    (
        "mongodb-unknown-transaction",
        "MongoDB Unknown Transaction Error",
        "Fix MongoDB unknown transaction errors",
        r"""## MongoDB Unknown Transaction Error

```
MongoServerError: unknown transaction
```

```
MongoServerError: no transaction started
```

## Common Causes

- The transaction was already committed or aborted
- The session ID is invalid
- The transaction was started on a different session
- The session timed out
- The transaction was started on a different connection

## How to Fix

### 1. Start a new transaction

```javascript
const session = client.startSession();
session.startTransaction();
// ... operations ...
await session.commitTransaction();
session.endSession();
```

### 2. Check for active transactions

```javascript
db.currentOp({ "active": true, "desc": /transaction/ })
```

### 3. Handle session reuse properly

```javascript
const session = client.startSession();
try {
  await session.startTransaction();
  await db.users.updateOne({ _id: 1 }, { $inc: { balance: -10 } }, { session });
  await session.commitTransaction();
} catch (err) {
  await session.abortTransaction();
  throw err;
} finally {
  session.endSession();
}
```

## Examples

```bash
# Check current transactions
mongosh --eval "db.currentOp({desc: /transaction/})"

# Check for prepared transactions
mongosh --eval "db.adminCommand({currentOp: true, desc: /prepared/})"
```"""
    ),
    (
        "mongodb-transaction-too-large",
        "MongoDB Transaction Too Large Error",
        "Fix MongoDB transaction exceeds size limits",
        r"""## MongoDB Transaction Too Large Error

```
MongoServerError: oplog is too large for this transaction
```

```
Transaction too large, cannot fit in memory
```

## Common Causes

- Too many write operations in a single transaction
- Writing large documents in a transaction
- The oplog cannot accommodate the transaction's operations
- Multiple collections with large writes in one transaction

## How to Fix

### 1. Break large transactions into smaller ones

```javascript
// Instead of one large transaction
const BATCH_SIZE = 100;
for (let i = 0; i < documents.length; i += BATCH_SIZE) {
  const session = client.startSession();
  await session.startTransaction();
  for (const doc of documents.slice(i, i + BATCH_SIZE)) {
    await db.users.updateOne({ _id: doc._id }, { $set: doc }, { session });
  }
  await session.commitTransaction();
  session.endSession();
}
```

### 2. Use write concern at transaction level

```javascript
await session.commitTransaction({ writeConcern: { w: "majority" } });
```

### 3. Reduce document sizes in transactions

```javascript
// Only update necessary fields
await db.users.updateOne({ _id: 1 }, { $set: { balance: newBalance } }, { session });
// Instead of replacing the entire document
```

## Examples

```bash
# Check transaction size limits
mongosh --eval "db.adminCommand({getParameter:1, transactionLifetimeLimitSeconds:1})"

# Monitor active transactions
mongosh --eval "db.currentOp({desc: /transaction/})"
```"""
    ),
    (
        "mongodb-transaction-timed-out",
        "MongoDB Transaction Timed Out",
        "Fix MongoDB transaction timeout errors",
        r"""## MongoDB Transaction Timed Out Error

```
MongoServerError: transaction timeout
```

```
TransactionAborted: transaction timed out after 60 seconds
```

## Common Causes

- The transaction ran longer than the default lifetime (60 seconds)
- Lock contention caused the transaction to wait too long
- Network delays between operations
- Deadlock detected in multi-document transactions

## How to Fix

### 1. Increase transaction lifetime

```javascript
db.adminCommand({
  setParameter: 1,
  transactionLifetimeLimitSeconds: 120  // 2 minutes
});
```

### 2. Keep transactions short

```javascript
// Do reads outside the transaction, then start transaction for writes only
const user = await db.users.findOne({ _id: 1 });
// ... processing ...
const session = client.startSession();
await session.startTransaction();
await db.users.updateOne({ _id: 1 }, { $set: { balance: newBalance } }, { session });
await db.accounts.updateOne({ _id: "checking" }, { $inc: { total: -10 } }, { session });
await session.commitTransaction();
session.endSession();
```

### 3. Add retry logic for transient transaction errors

```javascript
async function runTransactionWithRetry(fn) {
  while (true) {
    const session = client.startSession();
    try {
      await session.startTransaction();
      await fn(session);
      await session.commitTransaction();
      return;
    } catch (err) {
      if (err.errorLabels && err.errorLabels.includes("TransientTransactionError")) {
        continue; // Retry
      }
      await session.abortTransaction();
      throw err;
    } finally {
      session.endSession();
    }
  }
}
```

## Examples

```bash
# Check transaction timeout settings
mongosh --eval "db.adminCommand({getParameter:1, transactionLifetimeLimitSeconds:1})"

# Monitor transaction performance
mongosh --eval "db.currentOp({active: true, desc: /transaction/})"
```"""
    ),
    (
        "mongodb-no-active-transaction",
        "MongoDB No Active Transaction",
        "Fix MongoDB no active transaction errors",
        r"""## MongoDB No Active Transaction Error

```
MongoServerError: no active transaction to commit
```

```
MongoServerError: cannot commit in a transaction without starting one
```

## Common Causes

- Trying to commit without starting a transaction
- The transaction was already committed or aborted
- The session was ended before commit
- The session timed out and the transaction was aborted

## How to Fix

### 1. Always start a transaction before committing

```javascript
const session = client.startSession();
await session.startTransaction();  // Must start first
// ... operations ...
await session.commitTransaction();  // Then commit
session.endSession();
```

### 2. Check session state before operations

```javascript
if (session.inTransaction()) {
  await session.commitTransaction();
} else {
  console.log("No active transaction");
}
```

### 3. Handle errors properly

```javascript
try {
  await session.startTransaction();
  await db.users.updateOne({ _id: 1 }, { $set: { balance: 90 } }, { session });
  await session.commitTransaction();
} catch (err) {
  // If commit fails, the transaction may already be aborted
  if (!err.message.includes("cannot commit")) {
    await session.abortTransaction();
  }
} finally {
  session.endSession();
}
```

## Examples

```bash
# Test transaction lifecycle
mongosh --eval '
  const session = db.getMongo().startSession();
  session.startTransaction();
  db.test.insertOne({a:1}, {session});
  session.commitTransaction();
  print("Transaction committed successfully");
  session.endSession();
'
```"""
    ),
    (
        "mongodb-write-conflict-transaction",
        "MongoDB Write Conflict Error",
        "Fix MongoDB write conflict errors in transactions",
        r"""## MongoDB Write Conflict Error

```
MongoServerError: WriteConflict error: this operation cannot be performed because a storage engine-level conflict is preventing it
```

## Common Causes

- Two concurrent transactions modifying the same document
- A non-transactional write conflicts with a transactional write
- The storage engine detected a conflict between operations
- An operation in a snapshot transaction modified data changed by another transaction

## How to Fix

### 1. Retry on write conflicts (TransientTransactionError)

```javascript
const session = client.startSession();
while (true) {
  try {
    await session.startTransaction();
    await db.users.updateOne({ _id: 1 }, { $inc: { balance: -10 } }, { session });
    await db.accounts.updateOne({ _id: 1 }, { $inc: { balance: 10 } }, { session });
    await session.commitTransaction();
    break;
  } catch (err) {
    if (err.hasErrorLabel("TransientTransactionError")) {
      await session.abortTransaction();
      continue;
    }
    throw err;
  }
}
session.endSession();
```

### 2. Use optimistic concurrency with version fields

```javascript
const doc = await db.users.findOne({ _id: 1 });
const session = client.startSession();
await session.startTransaction();
await db.users.updateOne(
  { _id: 1, version: doc.version },
  { $set: { balance: doc.balance - 10 }, $inc: { version: 1 } },
  { session }
);
await session.commitTransaction();
session.endSession();
```

### 3. Reduce transaction scope

```javascript
// Only include writes that must be atomic in the transaction
// Do reads outside the transaction
```

## Examples

```bash
# Monitor write conflicts
mongosh --eval "db.serverStatus().locks"

# Check for conflicts
mongosh --eval "db.currentOp({active: true, desc: /update/})"
```"""
    ),
    (
        "mongodb-prepared-transaction",
        "MongoDB Prepared Transaction Error",
        "Fix MongoDB prepared transaction errors",
        r"""## MongoDB Prepared Transaction Error

```
MongoServerError: cannot prepare transaction in a different session
```

```
Transaction has already been prepared
```

## Common Causes

- The transaction was prepared on a different session
- Trying to prepare an already prepared transaction
- The prepared transaction was rolled back by the server
- Session migration failed during failover

## How to Fix

### 1. Use the same session for prepare and commit

```javascript
const session = client.startSession();
await session.startTransaction();
// ... operations ...
await session.commitTransaction({ prepareCommit: true });  // Prepare
// Later, on the same session
await session.commitTransaction();  // Commit
session.endSession();
```

### 2. Handle prepared transaction recovery after failover

```javascript
// After a failover, the server will roll back prepared transactions
// Check server logs for recovery information
```

### 3. Set transaction lifetime appropriately

```javascript
db.adminCommand({
  setParameter: 1,
  transactionLifetimeLimitSeconds: 120
});
```

## Examples

```bash
# Check for prepared transactions
mongosh --eval "db.adminCommand({currentOp: true, desc: /prepared/})"

# Check transaction recovery
grep -i "prepared transaction" /var/log/mongodb/mongod.log | tail -10
```"""
    ),
    (
        "mongodb-transaction-aborted",
        "MongoDB Transaction Aborted",
        "Fix MongoDB transaction aborted errors",
        r"""## MongoDB Transaction Aborted Error

```
MongoServerError: transaction aborted
```

```
TransactionAborted: caused by TransientTransactionError
```

## Common Causes

- A transient error occurred (network issue, replica set election)
- The transaction timed out
- An operation in the transaction failed
- Write conflict detected
- The server rolled back the transaction

## How to Fix

### 1. Implement retry logic

```javascript
async function executeWithRetry(operation, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    const session = client.startSession();
    try {
      await session.startTransaction();
      await operation(session);
      await session.commitTransaction();
      return { success: true };
    } catch (err) {
      await session.abortTransaction();
      if (err.hasErrorLabel("TransientTransactionError") && attempt < maxRetries - 1) {
        continue;
      }
      throw err;
    } finally {
      session.endSession();
    }
  }
}
```

### 2. Use commitTransaction with retryable write concern

```javascript
await session.commitTransaction({
  writeConcern: { w: "majority", wtimeout: 10000 },
  retryWrites: true
});
```

### 3. Check for error labels

```javascript
try {
  await session.commitTransaction();
} catch (err) {
  if (err.hasErrorLabel("TransientTransactionError")) {
    // Safe to retry the entire transaction
  } else if (err.hasErrorLabel("UnknownTransactionCommitResult")) {
    // Commit may have succeeded, check server state
  }
}
```

## Examples

```bash
# Monitor transaction aborts
mongosh --eval "db.serverStatus().metrics.transactions"

# Check for failed transactions
mongosh --eval "db.currentOp({active: true, desc: /transaction/})"
```"""
    ),
    (
        "mongodb-snapshot-unavailable",
        "MongoDB Snapshot Unavailable Error",
        "Fix MongoDB snapshot unavailable errors in transactions",
        r"""## MongoDB Snapshot Unavailable Error

```
MongoServerError: SnapshotUnavailable
```

```
MongoServerError: cannot provide snapshot when timestamp is too old
```

## Common Causes

- The oplog has rolled over and the required snapshot timestamp is no longer available
- The transaction ran for too long and the snapshot is stale
- The oplog size is too small for the workload

## How to Fix

### 1. Increase the oplog size

```javascript
db.adminCommand({ resizeOplog: 1, size: 10240 });  // 10 GB
```

### 2. Keep transactions short

```javascript
// Read needed data first, then start transaction
const docs = await db.users.find({ status: "active" }).toArray();
// Process outside transaction
const processed = docs.map(d => processDoc(d));
// Start transaction only for writes
const session = client.startSession();
await session.startTransaction();
for (const doc of processed) {
  await db.users.updateOne({ _id: doc._id }, { $set: doc }, { session });
}
await session.commitTransaction();
session.endSession();
```

### 3. Use `startAtOperationTime` carefully

```javascript
// Don't start transactions too far in the past
const session = client.startSession({
  snapshot: { readConcern: { level: "snapshot" } }
});
```

## Examples

```bash
# Check oplog window
mongosh --eval "rs.printReplicationInfo()"

# Check if snapshot timestamp is available
mongosh --eval "db.adminCommand({getOptime: 1})"
```"""
    ),
    (
        "mongodb-retryable-write-error",
        "MongoDB Retryable Write Error",
        "Fix MongoDB retryable write errors",
        r"""## MongoDB Retryable Write Error

```
MongoServerError: RetryableWriteError
```

```
MongoNetworkError: connection pool was cleared
```

## Common Causes

- The primary stepped down during a write operation
- Network timeout caused the write to be interrupted
- The server accepted the write but the acknowledgment was lost
- The driver retried the write on a new primary

## How to Fix

### 1. Ensure retryWrites is enabled

```javascript
const client = new MongoClient(uri, {
  retryWrites: true,  // Default in modern drivers
  retryReads: true
});
```

### 2. Handle retryable write errors in code

```javascript
try {
  await db.users.updateOne({ _id: 1 }, { $inc: { counter: 1 } });
} catch (err) {
  if (err.hasErrorLabel("RetryableWriteError")) {
    // The driver should have retried automatically
    // If it still fails, manually retry
    await db.users.updateOne({ _id: 1 }, { $inc: { counter: 1 } });
  }
}
```

### 3. Use write concern with retryable writes

```javascript
await db.users.insertOne(
  { name: "test" },
  { writeConcern: { w: "majority" } }
);
```

### 4. Check for connection pool issues

```javascript
db.serverStatus().connections
```

## Examples

```bash
# Check retryable writes configuration
mongosh --eval "db.adminCommand({getParameter:1, retryableWritesEnabled:1})"

# Monitor connection pool
mongosh --eval "db.serverStatus().connections"

# Test a retryable write
mongosh --eval '
  db.test.drop();
  db.test.insertOne({a:1});
  print("Write succeeded");
'
```"""
    ),
    # ============================================================
    # 8. SECURITY/AUTHORIZATION ERRORS
    # ============================================================
    (
        "mongodb-user-not-found",
        "MongoDB User Not Found Error",
        "Fix MongoDB user not found errors during authentication",
        r"""## MongoDB User Not Found Error

```
MongoServerError: User "myuser" not found
```

```
MongoServerError: auth failed, user not found
```

## Common Causes

- The username does not exist in the specified authSource database
- The user was created in a different database
- The authSource parameter is wrong
- The user was dropped

## How to Fix

### 1. Check which users exist

```javascript
use admin
db.getUsers()
```

### 2. Check a specific user

```javascript
use admin
db.getUser("myuser")
```

### 3. Verify the authSource in the connection string

```
mongodb://myuser:password@localhost:27017/mydb?authSource=admin
```

### 4. Create the user if it does not exist

```javascript
use admin
db.createUser({
  user: "myuser",
  pwd: "securePassword!",
  roles: [{ role: "readWrite", db: "mydb" }]
});
```

## Examples

```bash
# List all users in admin database
mongosh --eval "use admin; db.getUsers()"

# Check user in a specific database
mongosh --eval "use mydb; db.getUsers()"

# Verify user authentication
mongosh --username myuser --password securePassword! --authenticationDatabase admin
```"""
    ),
    (
        "mongodb-role-not-found",
        "MongoDB Role Not Found Error",
        "Fix MongoDB role not found errors when granting privileges",
        r"""## MongoDB Role Not Found Error

```
MongoServerError: role "customRole" not found
```

## Common Causes

- The role name is misspelled
- The role does not exist in the specified database
- A built-in role was referenced in the wrong database
- Custom roles must be created before being assigned

## How to Fix

### 1. List available roles

```javascript
db.getRoles({ showBuiltinRoles: true })
```

### 2. List roles in a specific database

```javascript
use mydb
db.getRoles()
```

### 3. Create a custom role

```javascript
use admin
db.createRole({
  role: "customReadRole",
  privileges: [
    { resource: { db: "mydb", collection: "" }, actions: ["find"] }
  ],
  roles: []
});
```

### 4. Use built-in roles correctly

```javascript
// Built-in roles: read, readWrite, dbAdmin, userAdmin, clusterAdmin, etc.
db.createUser({
  user: "myuser",
  pwd: "password",
  roles: [
    { role: "readWrite", db: "mydb" },
    { role: "dbAdmin", db: "mydb" }
  ]
});
```

## Examples

```bash
# List all roles
mongosh --eval "db.getRoles({showBuiltinRoles: true})"

# List roles in a database
mongosh --eval "use mydb; db.getRoles()"

# Create a custom role
mongosh --eval '
  use admin;
  db.createRole({
    role: "customMonitor",
    privileges: [{resource:{db:"",collection:""},actions:["serverStatus","connPoolStats"]}],
    roles: []
  });
'
```"""
    ),
    (
        "mongodb-unauthorized-command",
        "MongoDB Unauthorized to Execute Command",
        "Fix MongoDB unauthorized command execution errors",
        r"""## MongoDB Unauthorized to Execute Command

```
MongoServerError: not authorized on admin to execute command { serverStatus: 1 }
```

```
MongoServerError: command <command> not allowed
```

## Common Causes

- The user does not have the required role to execute the command
- The command requires admin-level privileges
- The user's role does not include the necessary action
- The command was executed on the wrong database

## How to Fix

### 1. Grant the required role

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "read", db: "admin" },
  { role: "clusterMonitor", db: "admin" }
]);
```

### 2. Create a user with proper privileges

```javascript
use admin
db.createUser({
  user: "monitor",
  pwd: "password",
  roles: [
    { role: "clusterMonitor", db: "admin" },
    { role: "read", db: "mydb" }
  ]
});
```

### 3. Use built-in roles for common tasks

```javascript
// clusterMonitor: for serverStatus, connPoolStats, etc.
// read: for querying data
// readWrite: for insert, update, delete operations
// dbAdmin: for index creation, validate, etc.
// userAdmin: for user management
```

### 4. Check the user's current roles

```javascript
use admin
db.getUser("myuser")
```

## Examples

```bash
# Check user roles
mongosh --eval "use admin; db.getUser('myuser')"

# Grant a role
mongosh --eval 'use admin; db.grantRolesToUser("myuser", [{role:"clusterMonitor",db:"admin"}])'

# Test a command
mongosh --username myuser --password password --authenticationDatabase admin --eval "db.adminCommand({serverStatus:1})"
```"""
    ),
    (
        "mongodb-scram-authentication-error",
        "MongoDB SCRAM Authentication Error",
        "Fix MongoDB SCRAM authentication mechanism errors",
        r"""## MongoDB SCRAM Authentication Error

```
MongoServerError: SCRAM authentication failed
```

```
MongoServerError: Authentication failed. SCRAM conversation invalid
```

## Common Causes

- Password was changed between authentication attempts
- The SCRAM mechanism version mismatch
- The salt or iteration count in the stored credentials is corrupt
- Client and server support different SCRAM versions

## How to Fix

### 1. Specify the authentication mechanism explicitly

```
mongodb://user:password@localhost:27017/mydb?authMechanism=SCRAM-SHA-256
```

### 2. Reset the user credentials

```javascript
use admin
db.changeUserPassword("myuser", "newSecurePassword!")
```

### 3. Drop and recreate the user

```javascript
use admin
db.dropUser("myuser")
db.createUser({
  user: "myuser",
  pwd: "newPassword!",
  roles: [{ role: "readWrite", db: "mydb" }],
  mechanisms: ["SCRAM-SHA-256"]  // Specify mechanism
});
```

### 4. Check server authentication settings

```yaml
# /etc/mongod.conf
security:
  authorization: enabled
  authenticationMechanisms: SCRAM-SHA-256
```

## Examples

```bash
# Test SCRAM-SHA-256 authentication
mongosh --authenticationMechanism SCRAM-SHA-256 \
  --username myuser --password mypassword \
  --authenticationDatabase admin

# Check stored credentials
mongosh --eval "use admin; db.system.users.findOne({user:'myuser'})"

# Change password
mongosh --eval "use admin; db.changeUserPassword('myuser', 'newPass123!')"
```"""
    ),
    (
        "mongodb-atlas-ip-whitelist",
        "MongoDB Atlas IP Whitelist Error",
        "Fix MongoDB Atlas IP whitelist connection errors",
        r"""## MongoDB Atlas IP Whitelist Error

```
MongoServerError: Cannot connect to MongoDB Atlas
```

```
IP address is not whitelisted in the Atlas IP whitelist
```

## Common Causes

- The client IP address is not in the Atlas whitelist
- The IP address changed (dynamic IP)
- The Atlas project has no IP whitelist entries
- The whitelist entry is incorrect (wrong IP or CIDR)

## How to Fix

### 1. Add the client IP to the Atlas whitelist

1. Go to Atlas dashboard -> Network Access
2. Click "Add IP Address"
3. Enter the client IP or select "Allow Access from Anywhere" (0.0.0.0/0) for development

### 2. Use the Atlas API to add IPs

```bash
curl --user "publicKey:privateKey" \
  --data '{"ipAddress":"203.0.113.50","comment":"Office IP"}' \
  --header "Content-Type: application/json" \
  https://cloud.mongodb.com/api/atlas/v1.0/groups/<projectId>/whitelist
```

### 3. Check current whitelist

```bash
curl --user "publicKey:privateKey" \
  https://cloud.mongodb.com/api/atlas/v1.0/groups/<projectId>/whitelist
```

### 4. Use VPC peering for private connectivity

For production, use VPC peering instead of IP whitelisting.

## Examples

```bash
# Get current IP
curl https://api.ipify.org

# Add current IP to Atlas whitelist
curl --user "publicKey:privateKey" \
  --data "{\"ipAddress\":\"$(curl -s https://api.ipify.org)\",\"comment\":\"Current IP\"}" \
  --header "Content-Type: application/json" \
  https://cloud.mongodb.com/api/atlas/v1.0/groups/<projectId>/whitelist
```"""
    ),
    (
        "mongodb-x509-authentication-error",
        "MongoDB x509 Authentication Error",
        "Fix MongoDB x509 certificate authentication errors",
        r"""## MongoDB x509 Authentication Error

```
MongoServerError: x509 authentication failed
```

```
No matching subject found in client certificate
```

## Common Causes

- The certificate CN (Common Name) does not match the MongoDB username
- The CA certificate is not trusted by the server
- The certificate has expired
- The certificate is not in PEM format
- The certificate does not have the required key usage

## How to Fix

### 1. Create a MongoDB user matching the certificate CN

```javascript
use $external
db.createUser({
  user: "CN=myuser,OU=Engineering,O=MyCompany",
  roles: [{ role: "readWrite", db: "mydb" }],
  mechanisms: ["X.509"]
});
```

### 2. Configure the server to use x509

```yaml
# /etc/mongod.conf
security:
  authorization: enabled
  clusterAuthMode: x509
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

### 3. Connect with x509 authentication

```bash
mongosh \
  --tls \
  --tlsCertificateKeyFile /etc/ssl/client.pem \
  --tlsCAFile /etc/ssl/ca.pem \
  --authenticationMechanism MONGODB-X509 \
  --authenticationDatabase '$external' \
  --username "CN=myuser,OU=Engineering,O=MyCompany"
```

### 4. Verify the certificate

```bash
openssl x509 -in client.pem -noout -subject
```

## Examples

```bash
# Create client certificate
openssl req -new -x509 -days 365 -nodes \
  -out client.pem -keyout client-key.pem \
  -subj "/CN=myuser/OU=Engineering/O=MyCompany"

# Test x509 authentication
mongosh --tls \
  --tlsCertificateKeyFile client.pem \
  --tlsCAFile ca.pem \
  --authenticationMechanism MONGODB-X509 \
  --authenticationDatabase '$external'
```"""
    ),
    (
        "mongodb-ldap-auth-error",
        "MongoDB LDAP Auth Error",
        "Fix MongoDB LDAP authentication errors",
        r"""## MongoDB LDAP Auth Error

```
MongoServerError: sasl library error: -13
```

```
LDAP authentication failed
```

## Common Causes

- LDAP server is unreachable from the MongoDB server
- The bind DN or password is incorrect
- The LDAP search filter is misconfigured
- The user's LDAP group is not mapped to a MongoDB role
- TLS is required but not configured
- The SASL library is not installed on the MongoDB server

## How to Fix

### 1. Verify LDAP connectivity

```bash
ldapsearch -H ldap://ldap.example.com -D "cn=admin,dc=example,dc=com" -W -b "dc=example,dc=com"
```

### 2. Configure LDAP in mongod.conf

```yaml
security:
  authorization: enabled
  ldap:
    servers: "ldap.example.com"
    transportSecurity: tls
    timeoutMS: 5000
    userToDNMapping:
      - match: "(.+)"
        substitution: "cn={0},ou=users,dc=example,dc=com"
    authz:
      queryTemplate: "ou=groups,dc=example,dc=com??one?(member={0})"
```

### 3. Map LDAP groups to MongoDB roles

```javascript
use admin
db.createRole({
  role: "ldapReader",
  privileges: [],
  roles: ["read"]
});
```

### 4. Test LDAP authentication

```bash
mongosh --authenticationMechanism PLAIN \
  --username "cn=myuser,ou=users,dc=example,dc=com" \
  --password "ldapPassword" \
  --authenticationDatabase '$external'
```

## Examples

```bash
# Test LDAP bind
ldapsearch -H ldap://ldap.example.com \
  -D "cn=myuser,ou=users,dc=example,dc=com" \
  -W -b "ou=users,dc=example,dc=com" "(cn=myuser)"

# Check MongoDB LDAP configuration
mongosh --eval "db.adminCommand({getParameter:1, ldapServers:1})"
```"""
    ),
    (
        "mongodb-authorization-failure",
        "MongoDB Authorization Failure",
        "Fix MongoDB authorization failures on operations",
        r"""## MongoDB Authorization Failure

```
MongoServerError: not authorized on mydb to execute command { insert: "users" }
```

## Common Causes

- The user does not have the required role for the operation
- The role was granted on a different database
- The user's role was revoked
- The operation requires a more privileged role

## How to Fix

### 1. Check the user's current roles

```javascript
use admin
db.getUser("myuser")
```

### 2. Grant the appropriate role

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "readWrite", db: "mydb" }
]);
```

### 3. Use dbAdmin for index operations

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "dbAdmin", db: "mydb" }
]);
```

### 4. Grant cluster-level permissions for admin commands

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "clusterAdmin", db: "admin" }
]);
```

## Examples

```bash
# Check user authorization
mongosh --eval "use admin; db.getUser('myuser')"

# Grant readWrite role
mongosh --eval 'use admin; db.grantRolesToUser("myuser", [{role:"readWrite",db:"mydb"}])'

# Test authorization
mongosh --username myuser --password password --authenticationDatabase admin \
  --eval "db.mydb.users.insertOne({name:'test'})"
```"""
    ),
    (
        "mongodb-privilege-check-error",
        "MongoDB Privilege Check Error",
        "Fix MongoDB insufficient privileges errors",
        r"""## MongoDB Privilege Check Error

```
MongoServerError: not enough privileges for <action>
```

## Common Causes

- The user's role does not include the required privilege
- The privilege scope is too narrow (wrong database or collection)
- Custom privileges were not properly configured
- Built-in roles do not include the specific action required

## How to Fix

### 1. Check role privileges

```javascript
db.getRoles({ showPrivileges: true })
// or for a specific role
db.getRole("customRole", { showPrivileges: true })
```

### 2. Create a role with specific privileges

```javascript
use admin
db.createRole({
  role: "dataPipeline",
  privileges: [
    {
      resource: { db: "mydb", collection: "logs" },
      actions: ["find", "insert", "update"]
    },
    {
      resource: { db: "mydb", collection: "archive" },
      actions: ["find", "insert"]
    }
  ],
  roles: []
});
```

### 3. Grant the role to a user

```javascript
db.grantRolesToUser("myuser", [
  { role: "dataPipeline", db: "admin" }
]);
```

### 4. Verify privileges

```javascript
db.getUser("myuser", { showPrivileges: true })
```

## Examples

```bash
# Check custom role privileges
mongosh --eval "use admin; db.getRole('dataPipeline', {showPrivileges:true})"

# List all privileges for a user
mongosh --eval "use admin; db.getUser('myuser', {showPrivileges:true})"

# Create a role with specific collection access
mongosh --eval '
  use admin;
  db.createRole({
    role: "readOnlyAudit",
    privileges: [{
      resource: {db:"audit", collection:""},
      actions: ["find","listCollections","listIndexes"]
    }],
    roles: []
  });
'
```"""
    ),
    (
        "mongodb-password-change-error",
        "MongoDB Password Change Error",
        "Fix MongoDB password change errors",
        r"""## MongoDB Password Change Error

```
MongoServerError: Could not update user
```

```
MongoServerError: password change failed
```

## Common Causes

- The old password is incorrect
- The user does not have permission to change passwords
- The new password does not meet the password validation policy
- The user was created with SCRAM-SHA-1 and the server requires SCRAM-SHA-256

## How to Fix

### 1. Change password using changeUserPassword

```javascript
use admin
db.changeUserPassword("myuser", "newSecurePassword123!")
```

### 2. Update user with new password and roles

```javascript
use admin
db.updateUser("myuser", {
  pwd: "newSecurePassword123!",
  roles: [{ role: "readWrite", db: "mydb" }]
});
```

### 3. Reset password as admin

```javascript
use admin
// Connect as admin user first
db.changeUserPassword("targetUser", "resetPassword!")
```

### 4. Check password validation policy

```javascript
db.adminCommand({ getParameter: 1, passwordDigestor: 1 })
```

## Examples

```bash
# Change password
mongosh --eval "use admin; db.changeUserPassword('myuser', 'newPass123!')"

# Verify user after password change
mongosh --eval "use admin; db.getUser('myuser')"

# Test new password
mongosh --username myuser --password newPass123! --authenticationDatabase admin \
  --eval "db.runCommand({connectionStatus:1})"
```"""
    ),
    # ============================================================
    # 9. PERFORMANCE/RESOURCE ERRORS
    # ============================================================
    (
        "mongodb-open-cursor-limit",
        "MongoDB Open Cursor Limit Error",
        "Fix MongoDB too many open cursors errors",
        r"""## MongoDB Open Cursor Limit Error

```
MongoServerError: too many open cursors
```

```
MongoServerError: number of open cursors exceeds limit
```

## Common Causes

- Cursors are not being closed after use
- The application creates many cursors without consuming results
- Batch size is too small, creating too many cursors
- Long-running cursors accumulate

## How to Fix

### 1. Close cursors when done

```javascript
const cursor = db.users.find({ status: "active" });
try {
  while (await cursor.hasNext()) {
    const doc = await cursor.next();
    // process document
  }
} finally {
  await cursor.close();
}
```

### 2. Increase the cursor limit (temporary)

```javascript
db.adminCommand({ setParameter: 1, cursorTimeoutMillis: 600000 });
```

### 3. Use batchSize to reduce open cursors

```javascript
const cursor = db.users.find().batchSize(1000);
```

### 4. Check current cursor count

```javascript
db.serverStatus().metrics.cursor
```

## Examples

```bash
# Check open cursors
mongosh --eval "db.serverStatus().metrics.cursor"

# Set cursor timeout
mongosh --eval "db.adminCommand({setParameter:1, cursorTimeoutMillis:300000})"

# Kill stale cursors
mongosh --eval "db.adminCommand({killCursors: 'users', cursors: []})"
```"""
    ),
    (
        "mongodb-cursor-not-found",
        "MongoDB Cursor Not Found Error",
        "Fix MongoDB cursor not found errors",
        r"""## MongoDB Cursor Not Found Error

```
MongoServerError: cursor id not found on server
```

```
MongoServerError: cursor not found (cursor may have timed out)
```

## Common Causes

- The cursor timed out (default 10 minutes of inactivity)
- The server was restarted, destroying all cursors
- The cursor was killed by the server due to resource pressure
- The client tried to use a cursor after a network reconnection

## How to Fix

### 1. Increase the cursor timeout

```javascript
db.adminCommand({ setParameter: 1, cursorTimeoutMillis: 600000 });  // 10 minutes
```

### 2. Use tailable cursors for capped collections

```javascript
const cursor = db.logs.find().sort({ $natural: -1 }).tailable();
```

### 3. Implement retry logic for cursor operations

```javascript
async function iterateCursorWithRetry(collection, query) {
  let cursor = collection.find(query);
  try {
    while (await cursor.hasNext()) {
      const doc = await cursor.next();
      // process
    }
  } catch (err) {
    if (err.message.includes("cursor not found")) {
      // Restart from where we left off if possible
      cursor = collection.find(query);
      // Continue iteration
    }
  }
}
```

### 4. Use noCursorTimeout to prevent automatic closing

```javascript
const cursor = db.users.find().noCursorTimeout();
// Remember to close manually when done
```

## Examples

```bash
# Check cursor statistics
mongosh --eval "db.serverStatus().metrics.cursor"

# List open cursors
mongosh --eval "db.adminCommand({listCommands:1}).commands | grep cursor"

# Create a noCursorTimeout cursor
mongosh --eval '
  db.test.find().noCursorTimeout();
  print("Cursor will not timeout");
'
```"""
    ),
    (
        "mongodb-operation-timed-out",
        "MongoDB Operation Timed Out Error",
        "Fix MongoDB operation timeout errors",
        r"""## MongoDB Operation Timed Out Error

```
MongoServerError: operation exceeded time limit
```

```
MongoNetworkError: operation timed out
```

## Common Causes

- The operation is too large or complex
- The server is under heavy load
- No indexes are available for the query
- The operation is waiting for a lock
- Network latency is high

## How to Fix

### 1. Set maxTimeMS on operations

```javascript
db.users.find({ status: "active" }).maxTimeMS(5000);
db.users.aggregate([...]).maxTimeMS(30000);
```

### 2. Optimize the query

```javascript
// Use explain to find bottlenecks
db.users.find({ email: "test@example.com" }).explain("executionStats");

// Add appropriate indexes
db.users.createIndex({ email: 1 });
```

### 3. Kill long-running operations

```javascript
db.currentOp({ active: true, secs_running: { $gt: 60 } })
```

```javascript
db.killOp(<opId>)
```

### 4. Break large operations into smaller ones

```javascript
// Instead of one large aggregation
db.largeCollection.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
], { maxTimeMS: 10000 });
```

## Examples

```bash
# Check long-running operations
mongosh --eval "db.currentOp({active:true, secs_running:{$gt:30}})"

# Kill an operation
mongosh --eval "db.killOp(<opId>)"

# Set maxTimeMS on a find
mongosh --eval "db.users.find({}).maxTimeMS(5000).toArray()"
```"""
    ),
    (
        "mongodb-too-many-connections",
        "MongoDB Too Many Connections Error",
        "Fix MongoDB connection limit exceeded errors",
        r"""## MongoDB Too Many Connections Error

```
MongoServerError: Connection pool was cleared
```

```
MongoServerError: too many connections
```

## Common Causes

- The connection pool size is too small for the workload
- Connections are not being released back to the pool
- Each request creates a new client instance
- The maxIncomingConnections setting is too low

## How to Fix

### 1. Increase max incoming connections

```yaml
# /etc/mongod.conf
net:
  maxIncomingConnections: 5000
```

### 2. Reuse the client instance

```javascript
// Wrong: creating a new client for each operation
async function getUser(id) {
  const client = new MongoClient(uri);
  await client.connect();
  const db = client.db("mydb");
  const result = await db.users.findOne({ _id: id });
  await client.close();
  return result;
}

// Right: reuse a single client
const client = new MongoClient(uri);
await client.connect();

async function getUser(id) {
  return client.db("mydb").users.findOne({ _id: id });
}
```

### 3. Configure connection pool size

```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 100,
  minPoolSize: 10,
  maxIdleTimeMS: 30000
});
```

### 4. Monitor connection usage

```javascript
db.serverStatus().connections
```

## Examples

```bash
# Check current connections
mongosh --eval "db.serverStatus().connections"

# Check connection pool stats
mongosh --eval "db.serverStatus().network"

# Increase max connections
mongosh --eval "db.adminCommand({setParameter:1, maxIncomingConnections:5000})"
```"""
    ),
    (
        "mongodb-no-free-disk-space",
        "MongoDB No Free Disk Space Error",
        "Fix MongoDB out of disk space errors",
        r"""## MongoDB No Free Disk Space Error

```
MongoServerError: Insufficient free disk space
```

```
WiredTiger error: No space left on device
```

## Common Causes

- The data directory is full
- The journal directory is full
- The log directory is full
- Large uncleaned temp files
- The oplog has grown too large

## How to Fix

### 1. Check disk usage

```bash
df -h /var/lib/mongodb
df -h /var/log/mongodb
```

### 2. Clean up old files

```bash
# Remove old logs
sudo find /var/log/mongodb -name "*.log.*" -mtime +30 -delete

# Compact the database
mongosh --eval "db.runCommand({compact: 'users'})"
```

### 3. Move data to a larger disk

```bash
# Stop MongoDB
sudo systemctl stop mongod

# Move data directory
sudo rsync -av /var/lib/mongodb /new/path/mongodb

# Update mongod.conf
# net:
#   dbPath: /new/path/mongodb

# Start MongoDB
sudo systemctl start mongod
```

### 4. Enable WiredTiger compression

```javascript
db.runCommand({
  collMod: "users",
  storageEngine: { wiredTiger: { configString: "block_compressor=snappy" } }
});
```

## Examples

```bash
# Check disk usage
df -h

# Check data directory size
du -sh /var/lib/mongodb

# Check for large files
find /var/lib/mongodb -size +1G -ls
```"""
    ),
    (
        "mongodb-msync-failed",
        "MongoDB msync Failed Error",
        "Fix MongoDB msync and disk sync failures",
        r"""## MongoDB msync Failed Error

```
WiredTiger error: msync: Input/output error
```

```
WiredTiger error: fsync: Input/output error
```

## Common Causes

- The disk has hardware errors
- The filesystem is corrupted
- The disk is full
- I/O controller errors
- The journal files are corrupted

## How to Fix

### 1. Check disk health

```bash
sudo smartctl -a /dev/sda
dmesg | grep -i error
```

### 2. Check filesystem integrity

```bash
sudo fsck /dev/sda1
```

### 3. Repair the database

```bash
# Stop MongoDB first
sudo systemctl stop mongod

# Run mongod with --repair
sudo mongod --repair --dbpath /var/lib/mongodb

# Start MongoDB
sudo systemctl start mongod
```

### 4. Replace the disk if hardware failure is detected

```bash
# Check for I/O errors
dmesg | tail -50
smartctl -l error /dev/sda
```

## Examples

```bash
# Check disk errors
dmesg | grep -i "error\|fail\|bad"

# Check smart status
sudo smartctl -H /dev/sda

# Check filesystem
sudo fsck -n /dev/sda1
```"""
    ),
    (
        "mongodb-page-fault-spike",
        "MongoDB Page Fault Spike Error",
        "Fix MongoDB excessive page fault errors",
        r"""## MongoDB Page Fault Spike Error

Page faults occur when MongoDB accesses data not in memory:

```
// Detected via monitoring
// page_faults: 15000 (high)
```

## Common Causes

- Working set exceeds available RAM
- The storage engine needs more memory for caching
- Large sequential scans evict hot data
- Too many collections with indexes not fitting in memory

## How to Fix

### 1. Monitor page faults

```javascript
db.serverStatus().extra_info.pageFaults
```

### 2. Increase RAM

The working set should fit in RAM for optimal performance.

### 3. Create indexes to reduce full collection scans

```javascript
db.users.createIndex({ email: 1 });  // Prevents full scan
```

### 4. Use the storage engine cache size

```yaml
# /etc/mongod.conf
storage:
  wiredTiger:
    engineConfig:
      cacheSizeGB: 4  # Set to ~60% of available RAM
```

### 5. Monitor WiredTiger cache usage

```javascript
db.serverStatus().wiredTiger.cache
```

## Examples

```bash
# Check page faults
mongosh --eval "db.serverStatus().extra_info.pageFaults"

# Check cache usage
mongosh --eval "db.serverStatus().wiredTiger.cache"

# Check memory usage
free -h
```"""
    ),
    (
        "mongodb-working-set-exceeded",
        "MongoDB Working Set Exceeded Error",
        "Fix MongoDB working set size exceeded errors",
        r"""## MongoDB Working Set Exceeded Error

```
// Working set size exceeds available memory
// This causes performance degradation
```

## Common Causes

- The frequently accessed data exceeds available RAM
- Large collections with random access patterns
- Indexes are too large to fit in memory
- Inefficient queries causing full collection scans

## How to Fix

### 1. Monitor the working set size

```javascript
db.serverStatus().wiredTiger.cache
```

### 2. Increase the WiredTiger cache size

```yaml
# /etc/mongod.conf
storage:
  wiredTiger:
    engineConfig:
      cacheSizeGB: 8  # Adjust based on available RAM
```

### 3. Optimize query patterns

```javascript
// Use covered queries to reduce data loading
db.users.find({ email: "test@example.com" }, { _id: 0, email: 1 });
```

### 4. Shard the collection to distribute the working set

```javascript
sh.shardCollection("mydb.largeCollection", { userId: 1 });
```

### 5. Use compression

```yaml
storage:
  wiredTiger:
    collectionConfig:
      blockCompressor: snappy
```

## Examples

```bash
# Check cache usage
mongosh --eval "db.serverStatus().wiredTiger.cache"

# Check which collections are largest
mongosh --eval '
  db.getCollectionNames().forEach(coll => {
    let stats = db[coll].stats();
    print(coll, ":", (stats.size / 1024 / 1024).toFixed(2), "MB");
  });
'

# Check index sizes
mongosh --eval '
  db.getCollectionNames().forEach(coll => {
    let stats = db[coll].stats();
    print(coll, "indexSize:", (stats.totalIndexSize / 1024 / 1024).toFixed(2), "MB");
  });
'
```"""
    ),
    (
        "mongodb-wiredtiger-cache-full",
        "MongoDB WiredTiger Cache Full Error",
        "Fix MongoDB WiredTiger cache full and eviction errors",
        r"""## MongoDB WiredTiger Cache Full Error

```
WiredTiger error: cache eviction thread timed out
```

```
Cache capacity: 95% full
```

## Common Causes

- The cache is at or near capacity
- Heavy write load causing cache pressure
- Large documents evicting other useful pages
- Insufficient RAM for the working set

## How to Fix

### 1. Monitor cache usage

```javascript
db.serverStatus().wiredTiger.cache
```

Key metrics:
- `bytes currently in the cache`: current usage
- `maximum bytes configured`: max cache size
- `tracked dirty bytes in the cache`: dirty data waiting to be written

### 2. Adjust cache size

```yaml
# /etc/mongod.conf
storage:
  wiredTiger:
    engineConfig:
      cacheSizeGB: 4  # Set to ~60% of available RAM
```

### 3. Reduce write pressure

- Use bulk writes instead of individual inserts
- Reduce the frequency of writes
- Use write concern `{ w: 1 }` for non-critical writes

### 4. Check for large operations

```javascript
db.currentOp({ active: true, secs_running: { $gt: 10 } })
```

## Examples

```bash
# Check cache stats
mongosh --eval "db.serverStatus().wiredTiger.cache"

# Check eviction activity
mongosh --eval "db.serverStatus().wiredTiger.cache['eviction server candidate cache hit count']"

# Check dirty cache
mongosh --eval "db.serverStatus().wiredTiger.cache['tracked dirty bytes in the cache']"
```"""
    ),
    # ============================================================
    # 10. MISCELLANEOUS ERRORS
    # ============================================================
    (
        "mongodb-oplog-too-small",
        "MongoDB Oplog Too Small Error",
        "Fix MongoDB oplog too small errors",
        r"""## MongoDB Oplog Too Small Error

```
// Secondary cannot keep up because the oplog is too small
// Oplog window: 24 hours (insufficient for the workload)
```

## Common Causes

- The oplog size is too small for the write volume
- The secondary was down for too long and the required operations rolled off the oplog
- Heavy write operations fill the oplog quickly

## How to Fix

### 1. Check the current oplog size

```javascript
rs.printReplicationInfo()
```

### 2. Increase the oplog size

```javascript
db.adminCommand({
  resizeOplog: 1,
  size: 10240  // 10 GB
});
```

### 3. Monitor oplog window

```javascript
let primaryLog = rs.printReplicationInfo();
let secondaryLog = rs.printSecondaryReplicationInfo();
```

### 4. Reduce oplog usage

- Use bulk operations instead of individual writes
- Reduce the amount of data written
- Use `w: 1` write concern for non-critical writes

## Examples

```bash
# Check oplog size and window
mongosh --eval "rs.printReplicationInfo()"
mongosh --eval "rs.printSecondaryReplicationInfo()"

# Check oplog stats
mongosh --eval "db.printReplicationInfo()"

# Resize oplog
mongosh --eval "db.adminCommand({resizeOplog: 1, size: 20480})"
```"""
    ),
    (
        "mongodb-oplog-full",
        "MongoDB Oplog Full Error",
        "Fix MongoDB oplog full errors causing replication to stop",
        r"""## MongoDB Oplog Full Error

```
// Oplog is full, secondary cannot catch up
// Replication has stopped
```

## Common Causes

- The write volume exceeds the oplog capacity
- The secondary was down and needs more oplog data than available
- The oplog size was not configured appropriately

## How to Fix

### 1. Check oplog usage

```javascript
rs.printReplicationInfo()
// Output shows the time range covered by the oplog
```

### 2. Resize the oplog

```javascript
// On the primary
db.adminCommand({ resizeOplog: 1, size: 10240 });  // 10 GB
```

### 3. Force a resync on the secondary

```bash
# If the secondary is too far behind
mongosh --eval "db.adminCommand({resync: 1})" --host secondary
```

### 4. Monitor oplog usage regularly

```javascript
// Check oplog stats
db.getReplicationInfo()
```

## Examples

```bash
# Check oplog coverage
mongosh --eval "rs.printReplicationInfo()"

# Check secondary lag
mongosh --eval "rs.printSecondaryReplicationInfo()"

# Get detailed oplog stats
mongosh --eval "db.getReplicationInfo()"

# Monitor continuously
watch -n 10 "mongosh --quiet --eval 'rs.printReplicationInfo()'"
```"""
    ),
    (
        "mongodb-feature-compatibility-version",
        "MongoDB Feature Compatibility Version Error",
        "Fix MongoDB feature compatibility version errors",
        r"""## MongoDB Feature Compatibility Version Error

```
MongoServerError: The featureCompatibilityVersion must be set to 4.4 or earlier
```

```
featureCompatibilityVersion is not compatible with this server version
```

## Common Causes

- The FCV was not updated after a MongoDB upgrade
- The FCV is set to a version newer than the server supports
- Mixed-version replica set members

## How to Fix

### 1. Check the current FCV

```javascript
db.adminCommand({ getParameter: 1, featureCompatibilityVersion: 1 })
```

### 2. Update the FCV after upgrade

```javascript
// After upgrading all members to 5.0
db.adminCommand({ setFeatureCompatibilityVersion: "5.0" })
```

### 3. Downgrade FCV before rolling back

```javascript
// Before downgrading, ensure all members support the target version
db.adminCommand({ setFeatureCompatibilityVersion: "4.4" })
```

### 4. Verify all members are on the same version

```javascript
db.adminCommand({ buildInfo: 1 }).version
```

## Examples

```bash
# Check current FCV
mongosh --eval "db.adminCommand({getParameter:1, featureCompatibilityVersion:1})"

# Update FCV
mongosh --eval "db.adminCommand({setFeatureCompatibilityVersion:'5.0'})"

# Check server version
mongosh --eval "db.adminCommand({buildInfo:1}).version"
```"""
    ),
    (
        "mongodb-unknown-operator",
        "MongoDB Unknown Operator Error",
        "Fix MongoDB unknown operator errors in queries",
        r"""## MongoDB Unknown Operator Error

```
MongoServerError: Unrecognized pipeline stage name: '$invalidStage'
```

```
unknown operator: $invalid
```

## Common Causes

- The operator name is misspelled
- The operator is from a newer version of MongoDB
- The operator is used in the wrong context (e.g., aggregation operator in find)
- The operator does not exist

## How to Fix

### 1. Check the operator spelling

```javascript
// Correct
db.users.find({ age: { $gte: 18 } })

// Wrong
db.users.find({ age: { $great: 18 } })
```

### 2. Use the correct operator for the context

```javascript
// Aggregation operators
db.users.aggregate([
  { $match: { age: { $gte: 18 } } },
  { $group: { _id: "$city", count: { $sum: 1 } } }
])

// Find operators
db.users.find({ age: { $gte: 18 }, city: "NYC" })
```

### 3. Check MongoDB version for supported operators

```javascript
db.adminCommand({ buildInfo: 1 }).version
```

## Examples

```bash
# Test operator syntax
mongosh --eval '
  try {
    db.test.find({field: {$invalid: 1}});
  } catch(e) { print("Error:", e.message); }
'

# List aggregation stages
mongosh --eval "db.adminCommand({listCommands:1}).commands | grep aggregate"
```"""
    ),
    (
        "mongodb-query-not-covered",
        "MongoDB Query Not Covered Error",
        "Fix MongoDB query not covered by index errors",
        r"""## MongoDB Query Not Covered Error

```
// Performance issue: query requires fetching documents from disk
// planSummary: COLLSCAN
```

## Common Causes

- The query does not use any index
- The query requires a fetch stage to retrieve documents
- The index does not cover all fields in the query
- No index exists for the query fields

## How to Fix

### 1. Create a compound index that covers the query

```javascript
// For query: { status: "active", email: 1 }
db.users.createIndex({ status: 1, email: 1 });

// For covered query: include all fields in the index
db.users.find({ status: "active" }, { _id: 0, status: 1, email: 1 });
```

### 2. Use explain to check query plans

```javascript
db.users.find({ status: "active" }).explain("executionStats")
```

### 3. Create a partial index for selective queries

```javascript
db.users.createIndex(
  { status: 1 },
  { partialFilterExpression: { status: "active" } }
);
```

### 4. Use projection to match index

```javascript
// If index is { status: 1, email: 1 }
db.users.find({ status: "active" }, { _id: 0, status: 1, email: 1 });
```

## Examples

```bash
# Check query plan
mongosh --eval "db.users.find({status:'active'}).explain('executionStats')"

# Check for COLLSCAN
mongosh --eval '
  db.users.find({status:"active"}).explain("executionStats").executionStats.stage
'

# Create a covering index
mongosh --eval '
  db.users.createIndex({status:1, email:1});
  let plan = db.users.find({status:"active"},{_id:0,status:1,email:1}).explain("executionStats");
  print("Stage:", plan.executionStats.stage);
'
```"""
    ),
    (
        "mongodb-regex-parse-error",
        "MongoDB Regex Parse Error",
        "Fix MongoDB regular expression parse errors",
        r"""## MongoDB Regex Parse Error

```
MongoServerError: syntax error in regular expression
```

```
MongoServerError: invalid regex
```

## Common Causes

- The regex pattern contains invalid syntax
- Special characters are not properly escaped
- The regex options are invalid
- The regex is too complex

## How to Fix

### 1. Validate the regex pattern

```javascript
// Correct regex
db.users.find({ name: { $regex: "^John" } })

// Wrong: unescaped special characters
db.users.find({ name: { $regex: "[invalid" } })  // Missing closing bracket
```

### 2. Use $options for case-insensitive matching

```javascript
db.users.find({ name: { $regex: "^john", $options: "i" } })
```

### 3. Escape special characters

```javascript
// Escape dots, asterisks, and other regex special characters
const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
db.users.find({ name: { $regex: escaped } });
```

### 4. Use text search instead of regex when possible

```javascript
// Instead of regex
db.users.find({ name: { $regex: /keyword/i } })

// Use text search
db.users.createIndex({ name: "text" })
db.users.find({ $text: { $search: "keyword" } })
```

## Examples

```bash
# Test regex syntax
mongosh --eval '
  try {
    db.test.find({field: {$regex: "[invalid"}});
  } catch(e) { print("Error:", e.message); }
'

# Test valid regex
mongosh --eval '
  db.test.find({field: {$regex: "^test", $options: "i"}}).toArray();
'
```"""
    ),
    (
        "mongodb-collmod-failed",
        "MongoDB collMod Failed Error",
        "Fix MongoDB collMod (collection modification) errors",
        r"""## MongoDB collMod Failed Error

```
MongoServerError: can't have two validation documents for the same collection
```

```
MongoServerError: collection already has index with that name
```

## Common Causes

- The collMod command is malformed
- The collection does not exist
- The index or validator to modify does not exist
- Conflicting options are provided

## How to Fix

### 1. Verify the collection exists

```javascript
db.getCollectionInfos({ name: "myCollection" })
```

### 2. Use collMod correctly

```javascript
// Change validation level
db.runCommand({
  collMod: "myCollection",
  validationLevel: "moderate"
});

// Change validation action
db.runCommand({
  collMod: "myCollection",
  validationAction: "warn"
});

// Update validator
db.runCommand({
  collMod: "myCollection",
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name"],
      properties: {
        name: { bsonType: "string" }
      }
    }
  }
});
```

### 3. Hide an index with collMod

```javascript
db.runCommand({
  collMod: "myCollection",
  index: {
    name: "email_1",
    hidden: true
  }
});
```

## Examples

```bash
# Change validation level
mongosh --eval 'db.runCommand({collMod:"users", validationLevel:"moderate"})'

# Change validation action
mongosh --eval 'db.runCommand({collMod:"users", validationAction:"warn"})'

# Hide an index
mongosh --eval 'db.runCommand({collMod:"users", index:{name:"email_1", hidden:true}})'
```"""
    ),
    (
        "mongodb-createcollection-failed",
        "MongoDB createCollection Failed Error",
        "Fix MongoDB createCollection errors",
        r"""## MongoDB createCollection Failed Error

```
MongoServerError: a collection 'mydb.users' already exists
```

```
MongoServerError: invalid collection name
```

## Common Causes

- The collection already exists
- The collection name contains invalid characters
- The collection name is too long
- The capped collection options are invalid
- The validator schema is malformed

## How to Fix

### 1. Check if the collection exists

```javascript
db.getCollectionInfos({ name: "users" })
```

### 2. Use createCollection with options

```javascript
// Create a capped collection
db.createCollection("logs", {
  capped: true,
  size: 1024 * 1024 * 100,  // 100 MB
  max: 100000
});

// Create with validator
db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "email"],
      properties: {
        name: { bsonType: "string" },
        email: { bsonType: "string" }
      }
    }
  }
});
```

### 3. Drop and recreate if needed

```javascript
db.users.drop();
db.createCollection("users");
```

### 4. Use a valid collection name

```javascript
// Valid: alphanumeric, underscores, dots (not starting with system.)
db.createCollection("my_collection");
db.createCollection("logs.2024");

// Invalid
db.createCollection("$invalid");
db.createCollection("system.users");  // Reserved
```

## Examples

```bash
# Check existing collections
mongosh --eval "db.getCollectionInfos().map(c => c.name)"

# Create a capped collection
mongosh --eval '
  db.createCollection("logs", {
    capped: true,
    size: 1024*1024*100,
    max: 100000
  });
  print("Capped collection created");
'
```"""
    ),
    (
        "mongodb-rename-collection-error",
        "MongoDB Rename Collection Error",
        "Fix MongoDB renameCollection errors",
        r"""## MongoDB Rename Collection Error

```
MongoServerError: can't rename to different database
```

```
MongoServerError: collection name already exists
```

## Common Causes

- Renaming to a different database is not allowed with renameCollection
- The target collection name already exists
- The collection name is invalid
- The user does not have the required privileges

## How to Fix

### 1. Use renameCollection on the same database

```javascript
db.adminCommand({
  renameCollection: "mydb.oldName",
  to: "mydb.newName"
});
```

### 2. Drop the target collection first if it exists

```javascript
db.targetCollection.drop();
db.adminCommand({
  renameCollection: "mydb.source",
  to: "mydb.target"
});
```

### 3. For cross-database renames, use copy and drop

```javascript
// Copy to new database
db.source.find().forEach(doc => {
  db.getSiblingDB("targetDB").target.insert(doc);
});

// Verify the copy
print("Source count:", db.source.countDocuments());
print("Target count:", db.getSiblingDB("targetDB").target.countDocuments());

// Drop the source
db.source.drop();
```

### 4. Ensure proper privileges

```javascript
// The user needs dbAdmin or restore role
use admin
db.grantRolesToUser("myuser", [{ role: "dbAdmin", db: "mydb" }]);
```

## Examples

```bash
# Rename a collection
mongosh --eval 'db.adminCommand({renameCollection:"mydb.old", to:"mydb.new"})'

# Cross-database copy and rename
mongosh --eval '
  db.source.find().forEach(doc => {
    db.getSiblingDB("targetDB").target.insert(doc);
  });
  db.source.drop();
  print("Collection moved successfully");
'
```"""
    ),
    (
        "mongodb-drop-database-failed",
        "MongoDB Drop Database Failed Error",
        "Fix MongoDB dropDatabase errors",
        r"""## MongoDB Drop Database Failed Error

```
MongoServerError: not authorized to drop database
```

```
MongoServerError: cannot drop database while session is active
```

## Common Causes

- The user does not have the required privileges to drop a database
- There are active sessions using the database
- The database does not exist
- The database is a system database (admin, local, config)

## How to Fix

### 1. Grant the required role

```javascript
use admin
db.grantRolesToUser("myuser", [
  { role: "dbOwner", db: "mydb" }
]);
```

### 2. Drop the database correctly

```javascript
use mydb
db.dropDatabase()
```

### 3. Ensure no active sessions

```javascript
// Check for active operations
db.currentOp({ ns: /mydb/ })

// Kill operations if needed
db.killOp(<opId>)
```

### 4. Never drop system databases

```javascript
// These databases should never be dropped:
// - admin
// - local
// - config
```

## Examples

```bash
# Check current databases
mongosh --eval "db.adminCommand({listDatabases:1}).databases.map(d => d.name)"

# Drop a database
mongosh --eval 'use mydb; db.dropDatabase();'

# Verify the database is dropped
mongosh --eval "db.adminCommand({listDatabases:1}).databases.map(d => d.name)"
```"""
    ),
]

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        continue
    content = make_page(title, desc, body)
    path = os.path.join(BASE, f"{slug}.md")
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {len(PAGES) - count}")
