---
title: "Solved JavaScript PM2 Error — How to Fix"
date: 2026-03-20T13:00:45+00:00
description: "Learn how to resolve JavaScript PM2 process manager errors, clustering, and configuration issues."
categories: ["javascript"]
keywords: ["pm2 error", "pm2 process", "pm2 cluster", "pm2 configuration", "pm2 logs"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

PM2 errors occur when the Node.js process manager fails to start, cluster, or manage application processes. Memory limits, port conflicts, and configuration errors are the most frequent causes.

Common causes include:
- Application crash loop due to startup errors
- Memory limit exceeded causing process restart
- Port already in use by another process
- Missing or incorrect ecosystem.config.js
- Log file permissions preventing writes

## Common Error Messages

```
[PM2] Starting /path/to/app.js
[PM2] Process has crashed (pid: 12345)
```

```
Error: listen EADDRINUSE: address already in use :::3000
```

```
[PM2] Spawning PM2 daemon with pm2_home=/root/.pm2
```

## How to Fix It

### 1. Configure PM2 Ecosystem File

Set up comprehensive PM2 configuration.

```javascript
// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: "api",
      script: "./dist/index.js",
      instances: "max",  // Use all CPU cores
      exec_mode: "cluster",
      autorestart: true,
      watch: false,
      max_memory_restart: "1G",
      env: {
        NODE_ENV: "development",
        PORT: 3000
      },
      env_production: {
        NODE_ENV: "production",
        PORT: 8080
      },
      error_file: "/var/log/pm2/api-error.log",
      out_file: "/var/log/pm2/api-out.log",
      merge_logs: true,
      log_date_format: "YYYY-MM-DD HH:mm:ss Z",
      kill_timeout: 5000,
      listen_timeout: 10000,
      max_restarts: 10,
      restart_delay: 5000
    },
    {
      name: "worker",
      script: "./dist/worker.js",
      instances: 2,
      exec_mode: "fork",
      autorestart: true,
      max_memory_restart: "500M"
    }
  ],
  deploy: {
    production: {
      user: "deploy",
      host: ["server1.example.com"],
      ref: "origin/main",
      repo: "git@github.com:user/repo.git",
      path: "/var/www/production",
      "post-deploy": "npm install && pm2 reload ecosystem.config.js --env production"
    }
  }
};
```

### 2. Handle Process Management

Start, monitor, and restart processes properly.

```bash
# Start application
pm2 start ecosystem.config.js --env production

# Start with specific name
pm2 start app.js --name "my-api"

# List all processes
pm2 list

# Monitor processes
pm2 monit

# View logs
pm2 logs api
pm2 logs api --lines 100
pm2 logs api --err

# Restart process
pm2 restart api

# Reload without downtime (cluster mode)
pm2 reload api

# Stop process
pm2 stop api

# Delete process
pm2 delete api

# Save current process list
pm2 save

# Restore saved processes
pm2 resurrect

# Startup script for auto-restart
pm2 startup
```

```javascript
// Graceful shutdown in app.js
process.on("SIGTERM", () => {
  console.log("SIGTERM received, shutting down gracefully");
  
  // Close database connections
  db.close(() => {
    process.exit(0);
  });
  
  // Force exit after timeout
  setTimeout(() => {
    process.exit(1);
  }, 10000);
});

// Handle cluster events
process.on("message", (msg) => {
  if (msg === "shutdown") {
    process.exit(0);
  }
});
```

### 3. Debug and Monitor Applications

Use PM2 tools for debugging and monitoring.

```bash
# Show detailed process info
pm2 show api

# View process metrics
pm2 monit

# Check PM2 daemon status
pm2 status

# View PM2 logs
pm2 logs --nostream

# Flush all logs
pm2 flush

# Reload PM2 configuration
pm2 reload ecosystem.config.js

# Update PM2
npm install pm2@latest -g
pm2 update
```

```javascript
// Programmatic PM2 usage
const pm2 = require("pm2");

pm2.connect((err) => {
  if (err) {
    console.error(err);
    process.exit(2);
  }
  
  pm2.start({
    script: "./dist/index.js",
    name: "api",
    instances: 4,
    exec_mode: "cluster",
    env: {
      NODE_ENV: "production"
    }
  }, (err, apps) => {
    if (err) {
      console.error(err);
    } else {
      console.log("Process started:", apps[0].name);
    }
    pm2.disconnect();
  });
});
```

## Common Scenarios

### Scenario 1: Docker with PM2

Run PM2 inside Docker containers:

```dockerfile
# Dockerfile
FROM node:18-alpine
RUN npm install -g pm2
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY dist ./dist
CMD ["pm2-runtime", "ecosystem.config.js", "--env", "production"]
```

```yaml
# docker-compose.yml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DB_HOST=db
    deploy:
      resources:
        limits:
          memory: 2G
```

### Scenario 2: Log Management

Configure log rotation and storage:

```javascript
// ecosystem.config.js
module.exports = {
  apps: [
    {
      name: "api",
      script: "./dist/index.js",
      log_date_format: "YYYY-MM-DD HH:mm:ss",
      error_file: "/var/log/pm2/error.log",
      out_file: "/var/log/pm2/output.log",
      merge_logs: true,
      log_type: "json"
    }
  ]
};
```

```bash
# Log rotation with logrotate
# /etc/logrotate.d/pm2
/var/log/pm2/*.log {
  daily
  missingok
  rotate 14
  compress
  delaycompress
  notifempty
  copytruncate
}
```

## Prevent It

- Use `pm2 start ecosystem.config.js` for reproducible process management
- Set `max_memory_restart` to prevent memory leaks from crashing the system
- Use `pm2 reload` instead of `pm2 restart` for zero-downtime deployments
- Run `pm2 save` and `pm2 startup` to persist process list across reboots
- Configure log rotation to prevent disk space exhaustion