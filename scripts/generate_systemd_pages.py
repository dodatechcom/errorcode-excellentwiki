#!/usr/bin/env python3
"""Generate systemd error pages"""
import os, sys

EXISTING = {f.replace('.md', '') for f in os.listdir('/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/systemd/') if f.endswith('.md')}

PAGES = [
    # ── Category 1: Unit file errors ──
    ("unit-file-syntax-error", "systemd unit file syntax error",
     "Fix systemd unit file syntax errors. Resolve parse failures in .service, .socket, .timer, and .target unit files.",
     """$ sudo systemctl daemon-reload
Failed to reload daemon: Unit file contains a syntax error: /etc/systemd/system/myapp.service:3: Failed to parse service type 'simplee'.

systemd cannot parse the unit file because it contains a syntax error. This prevents the unit from being loaded.""",
     """Common Causes:
- Typo in a directive name (e.g., `Type=simplee` instead of `Type=simple`)
- Missing `=` sign after a directive
- Unknown or deprecated directive
- Invalid value for a known directive
- Encoding issues (BOM, non-UTF-8 characters)""",
     """How to Fix:
```bash
# Check unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Reload after fixing
sudo systemctl daemon-reload

# View the specific line with the error
sudo systemd-analyze verify /etc/systemd/system/myapp.service 2>&1
```

Example of a corrected unit file:
```ini
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/myapp
Restart=on-failure

[Install]
WantedBy=multi-user.target
```"""),

    ("missing-unit-section", "systemd missing [Unit] section",
     "Fix systemd missing [Unit] section in unit files. Resolve unit loading failures when the [Unit] section is absent.",
     """Failed to start myapp.service: Unit myapp.service has a bad unit file setting.

Unit file is missing the [Unit] section which is required for proper dependency ordering.""",
     """Common Causes:
- Unit file was manually edited and the [Unit] section header was removed
- Unit file was auto-generated without the [Unit] section
- File format corruption""",
     """How to Fix:
```bash
# Verify the unit file has all required sections
grep -n '^\[Unit\]\|^\[Service\]\|^\[Install\]' /etc/systemd/system/myapp.service

# Edit and add the missing section
sudo systemctl edit myapp --force
```

Example unit file with all sections:
```ini
[Unit]
Description=My Application
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/myapp

[Install]
WantedBy=multi-user.target
```"""),

    ("missing-service-section", "systemd missing [Service] section",
     "Fix systemd missing [Service] section in service unit files. Resolve unit loading failures for services.",
     """Failed to start myapp.service: Unit file lacks [Service] section.

Service unit files require a [Service] section to define how the service runs.""",
     """Common Causes:
- Unit file was created without the [Service] section
- Incorrect file extension (e.g., .target instead of .service)
- File was truncated during editing""",
     """How to Fix:
```bash
# Check the file content
cat /etc/systemd/system/myapp.service

# Create or fix the unit file
sudo systemctl edit myapp --force
```

Minimal service unit:
```ini
[Unit]
Description=My Application

[Service]
Type=simple
ExecStart=/usr/bin/myapp

[Install]
WantedBy=multi-user.target
```"""),

    ("execstart-not-defined", "systemd ExecStart not defined",
     "Fix systemd ExecStart not defined errors. Resolve service start failures when ExecStart is missing from the unit file.",
     """Failed to start myapp.service: Unit myapp.service has a bad unit file setting.

For service unit files of Type=simple, ExecStart= must be set.""",
     """Common Causes:
- ExecStart directive is missing from the [Service] section
- The unit file is for a oneshot service without ExecStart
- The directive was commented out accidentally""",
     """How to Fix:
```bash
# Check if ExecStart is defined
grep ExecStart /etc/systemd/system/myapp.service

# Edit the unit file to add ExecStart
sudo systemctl edit myapp --force
```

Example with ExecStart:
```ini
[Service]
Type=simple
ExecStart=/usr/bin/myapp --config /etc/myapp/config.yml
WorkingDirectory=/opt/myapp
```"""),

    ("execstop-not-defined", "systemd ExecStop not defined",
     "Fix systemd ExecStop not defined warnings. Resolve graceful shutdown issues when ExecStop is missing.",
     """Warning: myapp.service: ExecStop= is not set. Using default stop signal.

Without ExecStop, systemd sends SIGTERM by default. Custom stop behavior requires an explicit ExecStop.""",
     """Common Causes:
- ExecStop was not set and default SIGTERM is insufficient
- Application needs a specific shutdown command
- Service requires cleanup before stopping""",
     """How to Fix:
```bash
# Add ExecStop to the unit file
sudo systemctl edit myapp
```

Example with ExecStop:
```ini
[Service]
Type=simple
ExecStart=/usr/bin/myapp
ExecStop=/usr/bin/myapp --stop
KillSignal=SIGTERM
TimeoutStopSec=30
```"""),

    ("type-not-set", "systemd Type not set in service",
     "Fix systemd Type not set errors. Resolve service configuration warnings when ServiceType is not specified.",
     """Warning: myapp.service: Unit type not specified, defaulting to 'simple'.

While systemd defaults to Type=simple, explicitly setting it avoids ambiguity.""",
     """Common Causes:
- Type= directive is missing from [Service] section
- Service was created without specifying the type
- Type was accidentally removed during editing""",
     """How to Fix:
```bash
# Add Type= to the service unit
sudo systemctl edit myapp --force
```

Common types:
```ini
[Service]
# For foreground processes:
Type=simple

# For services that fork to background:
Type=forking

# For one-shot commands:
Type=oneshot

# For D-Bus activated services:
Type=dbus

# For services with notify support:
Type=notify
```"""),

    ("user-group-not-found", "systemd User or Group not found",
     "Fix systemd User/Group not found errors. Resolve service start failures when the specified user or group does not exist.",
     """Failed to start myapp.service: Unable to run service as user 'myappuser': No such process

User 'myappuser' specified in the unit file does not exist on this system.""",
     """Common Causes:
- The user or group specified in User= or Group= does not exist
- The user was deleted but the service unit still references it
- Typo in the username or groupname""",
     """How to Fix:
```bash
# Check if the user exists
id myappuser

# Create the user if missing
sudo useradd -r -s /usr/sbin/nologin myappuser

# Create the group if missing
sudo groupadd myappgroup

# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart myapp
```"""),

    ("workingdirectory-not-found", "systemd WorkingDirectory not found",
     "Fix systemd WorkingDirectory not found errors. Resolve service start failures when the working directory is missing.",
     """Failed to start myapp.service: Working directory '/opt/myapp' not found.

The directory specified by WorkingDirectory= does not exist.""",
     """Common Causes:
- The directory was deleted or moved
- Typo in the path
- The directory has not been created yet
- NFS or remote mount not available""",
     """How to Fix:
```bash
# Check if the directory exists
ls -la /opt/myapp

# Create the directory
sudo mkdir -p /opt/myapp
sudo chown myappuser:myappuser /opt/myapp

# Verify unit file
sudo systemd-analyze verify /etc/systemd/system/myapp.service
```"""),

    ("environmentfile-not-found", "systemd EnvironmentFile not found",
     "Fix systemd EnvironmentFile not found errors. Resolve service start failures when the environment file is missing.",
     """Failed to start myapp.service: EnvironmentFile not found: /etc/sysconfig/myapp

The environment file specified in EnvironmentFile= does not exist.""",
     """Common Causes:
- The environment file was deleted or never created
- Package uninstall removed the file
- Path typo in EnvironmentFile= directive
- Conditional file with `-` prefix not working as expected""",
     """How to Fix:
```bash
# Check if the file exists
ls -la /etc/sysconfig/myapp

# Create the environment file
sudo tee /etc/sysconfig/myapp <<'EOF'
DATABASE_URL=postgresql://localhost/mydb
APP_ENV=production
EOF

# Use dash prefix for optional files
# EnvironmentFile=-/etc/sysconfig/myapp
```"""),

    ("pidfile-not-writable", "systemd PIDFile not writable",
     "Fix systemd PIDFile not writable errors. Resolve service failures when systemd cannot write the PID file.",
     """Failed to start myapp.service: PID file '/run/myapp.pid' not writable (Permission denied).

systemd cannot write the PID file to the specified location.""",
     """Common Causes:
- The service runs as a non-root user without write permission to the PID directory
- /run directory permissions are incorrect
- SELinux or AppArmor blocking access
- The PID file path points to a read-only filesystem""",
     """How to Fix:
```bash
# Check directory permissions
ls -la /run/

# Create a dedicated runtime directory
sudo mkdir -p /run/myapp
sudo chown myappuser:myappuser /run/myapp

# Or use RuntimeDirectory in the unit file
# [Service]
# RuntimeDirectory=myapp
# User=myappuser
```"""),

    ("restart-always-loop", "systemd Restart=always loop",
     "Fix systemd Restart=always loop. Resolve service restart loops where a service continuously crashes and restarts.",
     """myapp.service: Service entered restart loop with 5 restarts in 10 seconds. Stopping.

The service keeps crashing and systemd has hit the start rate limit.""",
     """Common Causes:
- The application has a fatal error on startup
- Missing dependencies or configuration
- Incorrect ExecStart path or arguments
- Port conflict preventing startup""",
     """How to Fix:
```bash
# Check recent logs
journalctl -u myapp -n 50 --no-pager

# Check restart rate limits
systemctl show myapp | grep -E 'StartLimit|RestartSec'

# Temporarily disable restart to debug
sudo systemctl edit myapp
# Add:
# [Service]
# Restart=on-failure
# StartLimitIntervalSec=600
# StartLimitBurst=5

# Fix the underlying issue
sudo myapp --test-config
```"""),

    ("timeout-startsec-too-low", "systemd TimeoutStartSec too low",
     "Fix systemd TimeoutStartSec too low errors. Resolve service start timeouts when the timeout is insufficient.",
     """myapp.service: Startup time limited to 10.000000s. Service startup timed out.

The service did not signal readiness within TimeoutStartSec.""",
     """Common Causes:
- TimeoutStartSec is set too low for the application's startup time
- Application is slow to start due to database migrations or heavy initialization
- Service uses Type=notify but does not call sd_notify(READY=1)""",
     """How to Fix:
```bash
# Increase the timeout
sudo systemctl edit myapp
```

```ini
[Service]
Type=notify
ExecStart=/usr/bin/myapp
TimeoutStartSec=300
NotifyAccess=main
```

```bash
# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart myapp
```"""),

    ("timeout-stopsec-too-low", "systemd TimeoutStopSec too low",
     "Fix systemd TimeoutStopSec too low errors. Resolve service stop timeouts when the grace period is insufficient.",
     """myapp.service: Stopping too quick, skipping ExecStop. Service stop request timed out.

The service did not stop within the configured TimeoutStopSec.""",
     """Common Causes:
- TimeoutStopSec is too low for the application's shutdown time
- Application does not handle SIGTERM properly
- Application is waiting for in-flight requests to complete""",
     """How to Fix:
```bash
# Increase the timeout
sudo systemctl edit myapp
```

```ini
[Service]
ExecStart=/usr/bin/myapp
ExecStop=/bin/kill -TERM $MAINPID
TimeoutStopSec=120
KillMode=mixed
```"""),

    ("limitnofile-too-low", "systemd LimitNOFILE too low",
     "Fix systemd LimitNOFILE too low errors. Resolve service failures when the open file descriptor limit is insufficient.",
     """myapp.service: Failed to adjust resource limits: Too many open files

The LimitNOFILE value is too low for the application.""",
     """Common Causes:
- Default LimitNOFILE is 1024 which is too low for high-concurrency apps
- Application opens many connections or file descriptors
- The system-wide limit (ulimit -n) is lower than the configured value""",
     """How to Fix:
```bash
# Check current limits
systemctl show myapp | grep LimitNOFILE
cat /proc/$(pidof myapp)/limits | grep "Max open files"

# Increase in the unit file
sudo systemctl edit myapp
```

```ini
[Service]
ExecStart=/usr/bin/myapp
LimitNOFILE=65536
LimitNPROC=65536
```

```bash
# Also set system-wide
echo "fs.file-max = 2097152" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```"""),

    ("nice-level-invalid", "systemd Nice level invalid",
     "Fix systemd Nice level invalid errors. Resolve service start failures when the Nice priority is out of range.",
     """myapp.service: Nice level -20 is not valid: Invalid argument

The Nice= value is outside the valid range (-20 to 19).""",
     """Common Causes:
- Nice value is outside the range -20 to 19
- Non-root user trying to set negative nice values
- Syntax error in the Nice= directive""",
     """How to Fix:
```bash
# Nice values must be between -20 (highest priority) and 19 (lowest priority)
sudo systemctl edit myapp
```

```ini
[Service]
ExecStart=/usr/bin/myapp
Nice=10
```"""),

    # ── Category 2: Service start/stop errors ──
    ("unit-failed-to-start", "systemd unit failed to start",
     "Fix systemd unit failed to start errors. Resolve service start failures with status inspection and debugging.",
     """Failed to start myapp.service: Unit myapp.service failed.

A requested service unit failed to start.""",
     """Common Causes:
- ExecStart command returns a non-zero exit code
- Missing executable or incorrect path
- Permission denied on the executable
- Missing shared libraries or runtime dependencies""",
     """How to Fix:
```bash
# Check service status
systemctl status myapp.service

# View detailed logs
journalctl -u myapp.service -n 100 --no-pager

# Verify the unit file
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Check if the executable exists
ls -la /usr/bin/myapp
```"""),

    ("start-request-repeated-too-quickly", "systemd start request repeated too quickly",
     "Fix systemd start request repeated too quickly errors. Resolve service restart rate limiting.",
     """myapp.service: Start request repeated too quickly.

The service was restarted too many times in a short period.""",
     """Common Causes:
- Service crashes immediately after starting
- StartLimitBurst and StartLimitIntervalSec are too restrictive
- Underlying issue causing rapid restarts""",
     """How to Fix:
```bash
# Check restart limits
systemctl show myapp | grep StartLimit

# Temporarily reset the failure counter
sudo systemctl reset-failed myapp

# Adjust limits in the unit file
sudo systemctl edit myapp
```

```ini
[Service]
Restart=on-failure
RestartSec=10
StartLimitIntervalSec=300
StartLimitBurst=5
```"""),

    ("start-limit-hit", "systemd start-limit-hit",
     "Fix systemd start-limit-hit errors. Resolve service activation blocked by start rate limits.",
     """myapp.service: Start request repeated too quickly, refusing to start.

The service hit its start rate limit and is refusing to start.""",
     """Common Causes:
- Service has failed too many times within the interval
- StartLimitBurst has been exhausted
- Underlying issue causing repeated failures""",
     """How to Fix:
```bash
# Reset the failed state
sudo systemctl reset-failed myapp

# Check what went wrong
journalctl -u myapp -n 50 --no-pager

# Increase limits if appropriate
sudo systemctl edit myapp
```

```ini
[Service]
StartLimitIntervalSec=600
StartLimitBurst=10
Restart=on-failure
RestartSec=5
```"""),

    ("unit-is-masked", "systemd unit is masked",
     "Fix systemd unit is masked errors. Resolve service start failures caused by masked units.",
     """Failed to start myapp.service: Unit myapp.service is masked.

The unit file is masked, preventing it from being started.""",
     """Common Causes:
- Unit was intentionally masked by an administrator
- Another package masked the unit as a conflict resolution
- Unit was masked during a previous disable operation""",
     """How to Fix:
```bash
# Check if masked
systemctl is-enabled myapp
ls -la /etc/systemd/system/myapp.service

# Unmask the unit
sudo systemctl unmask myapp

# Enable and start
sudo systemctl enable myapp
sudo systemctl start myapp
```"""),

    ("unit-not-found", "systemd unit not found",
     "Fix systemd unit not found errors. Resolve service command failures when the unit does not exist.",
     """Failed to start myapp.service: Unit myapp.service not found.

The specified unit does not exist.""",
     """Common Causes:
- The unit file has not been created or installed
- Typo in the unit name
- Unit file is in a location not scanned by systemd
- The package providing the unit is not installed""",
     """How to Fix:
```bash
# Search for the unit
systemctl list-unit-files | grep myapp
find /etc/systemd /lib/systemd -name "myapp*" 2>/dev/null

# Create the unit file
sudo tee /etc/systemd/system/myapp.service <<'EOF'
[Unit]
Description=My Application

[Service]
Type=simple
ExecStart=/usr/bin/myapp

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start myapp
```"""),

    ("refused-to-start", "systemd refused to start",
     "Fix systemd refused to start errors. Resolve service start refusals due to configuration issues.",
     """myapp.service: Refused to start, not enough resources.

systemd refused to start the service due to resource constraints.""",
     """Common Causes:
- Insufficient memory or CPU resources
- CGroup resource limits reached
- systemd-logind resource control blocking the service
- Too many processes already running under the service's slice""",
     """How to Fix:
```bash
# Check resource usage
systemctl status myapp
systemd-cgtop

# Check memory limits
systemctl show myapp | grep Memory

# Increase resource limits
sudo systemctl edit myapp
```

```ini
[Service]
MemoryMax=2G
CPUQuota=200%
TasksMax=4096
```"""),

    ("enter-failed-state", "systemd unit enter failed state",
     "Fix systemd unit enter failed state. Resolve services stuck in a failed state.",
     """myapp.service: Entered failed state.

The service process exited with a failure and the unit is now in a failed state.""",
     """Common Causes:
- Application crashed or exited with non-zero code
- ExecStartPre or ExecStartPost command failed
- Service could not bind to its required port
- Configuration file error causing immediate exit""",
     """How to Fix:
```bash
# Check the failure reason
systemctl status myapp
journalctl -u myapp -n 50 --no-pager

# Reset and restart
sudo systemctl reset-failed myapp
sudo systemctl start myapp

# If persistent, check configuration
cat /etc/myapp/config.yml
```"""),

    ("exit-code-1", "systemd service exit code 1",
     "Fix systemd service exit code 1. Resolve service failures where the main process exits with error code 1.",
     """myapp.service: Main process exited, code=exited, status=1/FAILURE

The service's main process exited with a generic error code.""",
     """Common Causes:
- Application configuration error
- Missing or invalid command-line arguments
- Unhandled exception in the application
- Missing environment variables""",
     """How to Fix:
```bash
# View the error output
journalctl -u myapp -n 100 --no-pager

# Test the command manually
sudo -u myappuser /usr/bin/myapp --config /etc/myapp/config.yml

# Check for configuration errors
/usr/bin/myapp --validate-config
```"""),

    ("main-process-exited", "systemd main process exited",
     "Fix systemd main process exited errors. Resolve unexpected service termination when the main process stops.",
     """myapp.service: Main process exited, code=exited, status=15/SIGTERM

The main process of the service was terminated unexpectedly.""",
     """Common Causes:
- Process received a signal (SIGTERM, SIGKILL, etc.)
- OOM killer terminated the process
- Application crashed due to a bug
- The process was stopped by another service""",
     """How to Fix:
```bash
# Check if OOM killed
dmesg | grep -i oom | tail -5
journalctl -u myapp -n 50 --no-pager

# Increase memory limits if OOM
sudo systemctl edit myapp
```

```ini
[Service]
MemoryMax=4G
MemoryHigh=3G
OOMPolicy=continue
```"""),

    ("service-not-active", "systemd service not active",
     "Fix systemd service not active errors. Resolve issues where a service is not in the active state.",
     """myapp.service: Unit is not active.

The service is not currently running.""",
     """Common Causes:
- Service was never started
- Service crashed and was not set to restart
- Service was manually stopped
- Dependency failure prevented start""",
     """How to Fix:
```bash
# Check service state
systemctl is-active myapp
systemctl status myapp

# Start the service
sudo systemctl start myapp

# Enable on boot
sudo systemctl enable myapp

# Check why it failed
journalctl -u myapp -n 50 --no-pager
```"""),

    ("stop-not-allowed", "systemd stop not allowed",
     "Fix systemd stop not allowed errors. Resolve service stop failures when the stop operation is prohibited.",
     """Failed to stop myapp.service: Operation not permitted.

The service cannot be stopped due to policy restrictions.""",
     """Common Causes:
- SELinux policy preventing the stop operation
- Polkit authorization not granted
- Service is protected by a unit file policy
- The user lacks sufficient privileges""",
     """How to Fix:
```bash
# Use sudo
sudo systemctl stop myapp

# Check SELinux audit logs
sudo ausearch -m avc -ts recent

# Check polkit rules
pkaction --verbose --action-id org.freedesktop.systemd1.manage-units
```"""),

    ("reload-not-supported", "systemd reload not supported",
     "Fix systemd reload not supported errors. Resolve reload failures for services without ExecReload.",
     """Failed to reload myapp.service: Service does not support reload operation.

No ExecReload= is defined for this service.""",
     """Common Causes:
- ExecReload is not defined in the unit file
- Service uses Type=simple without ExecReload
- Application does not support config reload""",
     """How to Fix:
```bash
# Check if ExecReload is defined
grep ExecReload /etc/systemd/system/myapp.service

# Add ExecReload to the unit
sudo systemctl edit myapp
```

```ini
[Service]
Type=simple
ExecStart=/usr/bin/myapp --config /etc/myapp/config.yml
ExecReload=/bin/kill -HUP $MAINPID
```"""),

    ("restart-rate-limited", "systemd restart rate limited",
     "Fix systemd restart rate limited errors. Resolve service restart throttling issues.",
     """myapp.service: Restart rate limited. Deferring.

systemd is deferring the restart due to rate limiting.""",
     """Common Causes:
- Too many restart attempts in a short time
- RestartSec is too low combined with high restart frequency
- Service keeps failing and accumulating restart credits""",
     """How to Fix:
```bash
# Check restart configuration
systemctl show myapp | grep -E 'Restart|RestartSec'

# Increase restart interval
sudo systemctl edit myapp
```

```ini
[Service]
Restart=on-failure
RestartSec=30
StartLimitIntervalSec=600
StartLimitBurst=3
```"""),

    ("control-process-exited", "systemd control process exited",
     "Fix systemd control process exited errors. Resolve failures in ExecStartPre, ExecStartPost, ExecStop, or ExecReload.",
     """myapp.service: Control process exited, code=exited, status=1/FAILURE

A control process (ExecStartPre, ExecStartPost, ExecStop, ExecReload) failed.""",
     """Common Causes:
- ExecStartPre command failed (e.g., config validation)
- ExecStartPost command failed (e.g., registration with load balancer)
- ExecStop cleanup command failed
- Script used in ExecStart* is not executable or has errors""",
     """How to Fix:
```bash
# Identify which control process failed
journalctl -u myapp -n 50 --no-pager

# Test the command manually
/usr/libexec/myapp-pre-start.sh

# Ensure scripts are executable
chmod +x /usr/libexec/myapp-pre-start.sh

# Check exit code of the specific command
echo $?
```"""),

    ("status-timeout", "systemd status timeout",
     "Fix systemd status timeout errors. Resolve service status check timeouts when the manager is overloaded.",
     """A dependency job for myapp.service/start was run, but it failed.

systemd timed out waiting for the service status.""",
     """Common Causes:
- systemd is overloaded with too many parallel operations
- D-Bus communication timeout
- The service's status check is taking too long
- System is under heavy load""",
     """How to Fix:
```bash
# Check system load
uptime
systemd-analyze

# Increase D-Bus timeout (system-wide)
# In /etc/systemd/system.conf:
# DefaultTimeoutStartSec=90s

# Or for specific service
sudo systemctl edit myapp
```

```ini
[Service]
TimeoutStartSec=300
```"""),

    # ── Category 3: Dependency errors ──
    ("dependency-failed", "systemd dependency failed",
     "Fix systemd dependency failed errors. Resolve service start failures caused by dependent unit failures.",
     """myapp.service: Dependency failed.
A start job for unit myapp.service has failed with result 'dependency'.

The service could not start because a required dependency failed.""",
     """Common Causes:
- A RequiredBy= or Wants= dependency unit failed to start
- An After= dependency did not start in time
- The dependency unit is masked or not installed""",
     """How to Fix:
```bash
# Check dependency tree
systemctl list-dependencies myapp

# Identify which dependency failed
systemctl status myapp

# Check failed units
systemctl --failed

# Start the failed dependency
sudo systemctl start <dependency-unit>
```"""),

    ("ordering-cycle-detected", "systemd ordering cycle detected",
     "Fix systemd ordering cycle detected errors. Resolve circular dependency ordering issues.",
     """myapp.service: Found ordering cycle. Breaking.

systemd detected a circular ordering dependency between units.""",
     """Common Causes:
- Circular After= or Before= dependencies between units
- Service A requires B which requires A
- Conflicting After= and Before= directives""",
     """How to Fix:
```bash
# Analyze the dependency graph
systemd-analyze dot myapp.service | dot -Tsvg > deps.svg

# Check ordering dependencies
systemctl list-dependencies --all myapp

# Remove circular dependencies by using Wants= instead of Requires=
# or by removing redundant After= directives
```"""),

    ("breaking-ordering-cycle", "systemd breaking ordering cycle",
     "Fix systemd breaking ordering cycle. Resolve systemd automatic cycle breaking and reconfigure dependencies.",
     """systemd[1]: myapp.service: Breaking ordering cycle by removing myapp.service->network-online.target After= dependency.

systemd automatically broke a dependency cycle.""",
     """Common Causes:
- Circular dependency between services
- Incorrect use of After= and Requires=
- Too many cross-referencing dependency chains""",
     """How to Fix:
```bash
# Find the cycle
systemd-analyze dot myapp.service | dot -Tsvg > cycle.svg

# Simplify dependencies
sudo systemctl edit myapp
```

```ini
[Unit]
Description=My Application
After=network-online.target
Wants=network-online.target
# Remove conflicting Before= or Requires= that create cycles
```"""),

    ("required-by-stopped", "systemd required by stopped unit",
     "Fix systemd required by stopped unit. Resolve service start issues when a RequiredBy= target or service is stopped.",
     """myapp.service is required by some-unit.service, which is stopped.

Starting myapp may not be useful as its consumer is not running.""",
     """Common Causes:
- The unit listing myapp as RequiredBy= is not running
- The requiring unit was manually stopped
- The dependency graph is inverted""",
     """How to Fix:
```bash
# Check which units require myapp
systemctl list-dependencies --reverse myapp

# Start the requiring unit if needed
sudo systemctl start some-unit

# Or adjust dependencies
sudo systemctl edit myapp
```"""),

    ("wanted-by-not-found", "systemd WantedBy not found",
     "Fix systemd WantedBy not found errors. Resolve service enable failures when the WantedBy target does not exist.",
     """Failed to enable myapp.service: Unit file WantedBy target not found.

The target specified in WantedBy= does not exist.""",
     """Common Causes:
- Target name typo in WantedBy=
- Required target package not installed
- Custom target not created""",
     """How to Fix:
```bash
# List available targets
systemctl list-unit-files --type=target

# Common targets: multi-user.target, graphical.target, network-online.target

# Edit the unit file
sudo systemctl edit myapp --force
```

```ini
[Install]
WantedBy=multi-user.target
```"""),

    ("after-dependency-not-met", "systemd After dependency not met",
     "Fix systemd After dependency not met. Resolve service ordering failures when After= dependencies are not satisfied.",
     """myapp.service: After dependency network-online.target was not started.

The service requires network-online.target to be started first.""",
     """Common Causes:
- The After= dependency unit is not enabled or not installed
- The dependency unit failed to start
- Incorrect ordering dependency""",
     """How to Fix:
```bash
# Check if the dependency is enabled
systemctl is-enabled network-online.target

# Enable the dependency
sudo systemctl enable network-online.target

# Use Wants= along with After= for soft dependencies
sudo systemctl edit myapp
```

```ini
[Unit]
After=network-online.target
Wants=network-online.target
```"""),

    ("before-dependency-conflict", "systemd Before dependency conflict",
     "Fix systemd Before dependency conflict. Resolve ordering conflicts between units with conflicting Before= directives.",
     """Conflicting Before= and After= directives detected between myapp.service and other.service.

One unit cannot be both before and after another.""",
     """Common Causes:
- Two units have conflicting Before= and After= references to each other
- Circular Before=/After= chain
- Incorrect dependency configuration""",
     """How to Fix:
```bash
# Find conflicting dependencies
systemd-analyze dot myapp.service | dot -Tsvg > deps.svg

# Remove one of the conflicting directives
sudo systemctl edit myapp
```"""),

    ("requires-not-started", "systemd Requires not started",
     "Fix systemd Requires not started. Resolve service failures when a Required dependency fails to start.",
     """myapp.service: Requires=database.service was not started.

The service requires database.service which is not running.""",
     """Common Causes:
- The required unit failed to start
- The required unit is masked
- The required unit is not installed
- Dependency is too strict for the use case""",
     """How to Fix:
```bash
# Check the required unit
systemctl status database.service

# Start it manually
sudo systemctl start database.service

# Consider using Wants= instead of Requires= for optional dependencies
sudo systemctl edit myapp
```

```ini
[Unit]
Wants=database.service
After=database.service
```"""),

    ("wants-ignored", "systemd Wants ignored",
     "Fix systemd Wants ignored. Resolve situations where Wants= dependencies are silently skipped.",
     """myapp.service: Wants=optional-service.service ignored.

The Wants= dependency was not started because the unit does not exist.""",
     """Common Causes:
- The wanted unit does not exist on the system
- The unit file for the dependency is not installed
- Silent failure is expected behavior for Wants=""",
     """How to Fix:
```bash
# Wants= is optional by design - no error if missing
# To make it required, use Requires= instead

# Check if the wanted unit exists
systemctl list-unit-files | grep optional-service

# To install it
sudo apt install <package-providing-the-unit>
```"""),

    ("bindsto-failed", "systemd BindsTo failed",
     "Fix systemd BindsTo failed. Resolve service failures when a BindsTo= dependency stops or fails.",
     """myapp.service: BindsTo=parent.service failed. Stopping myapp.

The bound parent service stopped, so this service is also stopping.""",
     """Common Causes:
- The BindsTo= unit stopped unexpectedly
- The bound service was manually stopped
- Network dependency lost""",
     """How to Fix:
```bash
# Check the bound service
systemctl status parent.service

# BindsTo= is strict - if parent stops, this stops too
# Consider using Wants= or After= for looser coupling

# Restart the bound service
sudo systemctl restart parent.service
```"""),

    ("partof-not-followed", "systemd PartOf not followed",
     "Fix systemd PartOf not followed. Resolve issues where PartOf= stop/restart is not propagated.",
     """When stopping parent.service, myapp.service was expected to be stopped but was not.

PartOf= was not correctly configured.""",
     """Common Causes:
- PartOf= points to a non-existent unit
- The dependent unit was masked
- systemd did not propagate the stop signal""",
     """How to Fix:
```bash
# Verify PartOf= target exists
systemctl list-unit-files | grep parent.service

# PartOf= only propagates stop and restart, not start
sudo systemctl edit myapp
```

```ini
[Unit]
PartOf=parent.service
```"""),

    ("onfailure-not-triggered", "systemd OnFailure not triggered",
     "Fix systemd OnFailure not triggered. Resolve issues where failure handlers are not executed.",
     """myapp.service failed but the OnFailure= handler was not triggered.

The OnFailure= dependency was not activated on service failure.""",
     """Common Causes:
- OnFailure= target or service does not exist
- The failure handler unit file is missing
- The service reached a different failure mode than expected""",
     """How to Fix:
```bash
# Verify OnFailure= target exists
systemctl list-unit-files | grep failure-handler

# Create the handler if missing
sudo tee /etc/systemd/system/failure-handler.service <<'EOF'
[Unit]
Description=Failure Handler
After=myapp.service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/notify-failure.sh

[Install]
WantedBy=multi-user.target
EOF

# Update the main service
sudo systemctl edit myapp
```

```ini
[Unit]
OnFailure=failure-handler.service
```"""),

    ("conflicts-conflict", "systemd Conflicts conflict",
     "Fix systemd Conflicts conflict. Resolve mutual exclusion conflicts between units.",
     """Conflicting units detected: myapp.service and other-service.service

Two units with Conflicts= cannot run simultaneously.""",
     """Common Causes:
- Two units both declare Conflicts= with each other
- A unit was configured to conflict with an essential service
- Package installation created conflicting unit files""",
     """How to Fix:
```bash
# Check conflicts
systemctl show myapp | grep Conflicts

# Stop the conflicting service
sudo systemctl stop other-service

# Remove the Conflicts= directive if both should run
sudo systemctl edit myapp --full
```"""),

    ("service-ordering-circular", "systemd service ordering circular",
     "Fix systemd service ordering circular dependency. Resolve circular ordering chains between multiple services.",
     """Found circular ordering dependency between myapp.service, backend.service, and database.service.

systemd cannot determine the start order.""",
     """Common Causes:
- Chain of After= directives forming a circle
- A -> B -> C -> A dependency chain
- Multiple services depending on each other for ordering""",
     """How to Fix:
```bash
# Visualize the dependency graph
systemd-analyze dot myapp.service backend.service database.service | dot -Tsvg > circular.svg

# Break the cycle by removing one After= directive
# Use Wants= for non-critical ordering
sudo systemctl edit myapp
```

```ini
[Unit]
After=network-online.target
Wants=database.service
# Remove After=backend.service if it creates a cycle
```"""),

    # ── Category 4: Socket/activation errors ──
    ("socket-unit-failed", "systemd socket unit failed",
     "Fix systemd socket unit failed errors. Resolve socket activation failures.",
     """myapp.socket: Failed to listen on sockets: Address already in use.

The socket unit failed to bind to the configured address and port.""",
     """Common Causes:
- Port is already in use by another process
- Another socket unit is using the same port
- Insufficient privileges to bind to privileged ports (<1024)
- Socket address format is invalid""",
     """How to Fix:
```bash
# Check what is using the port
sudo ss -tlnp | grep :8080

# Find conflicting socket units
systemctl list-units --type=socket

# Kill the conflicting process or change the port
sudo systemctl edit myapp.socket
```

```ini
[Socket]
ListenStream=8081
```"""),

    ("socket-bind-failed", "systemd socket bind failed",
     "Fix systemd socket bind failed errors. Resolve socket binding failures during activation.",
     """myapp.socket: Failed to bind to [::]:80: Permission denied

systemd cannot bind the socket to the specified address.""",
     """Common Causes:
- Binding to privileged port without root
- SELinux blocking the bind
- IPv6 not available or disabled
- Address format is invalid""",
     """How to Fix:
```bash
# For privileged ports, ensure the socket has appropriate capabilities
sudo systemctl edit myapp.socket
```

```ini
[Socket]
ListenStream=8080
# Or use capabilities
# AmbientCapabilities=CAP_NET_BIND_SERVICE

# Check SELinux
sudo ausearch -m avc -ts recent
```"""),

    ("port-already-in-use", "systemd port already in use",
     "Fix systemd port already in use errors. Resolve socket and service port conflicts.",
     """myapp.socket: Address already in use

Port 8080 is already bound by another process.""",
     """Common Causes:
- Another service or process is using the port
- The socket was not properly closed after a crash
- TIME_WAIT state on the port
- Duplicate socket units configured""",
     """How to Fix:
```bash
# Find the process using the port
sudo ss -tlnp | grep :8080
sudo lsof -i :8080

# Stop the conflicting service
sudo systemctl stop other-service

# Or restart the socket
sudo systemctl restart myapp.socket
```"""),

    ("socket-not-found", "systemd socket not found",
     "Fix systemd socket not found errors. Resolve socket activation failures when the socket unit is missing.",
     """Failed to activate myapp.service via socket: Socket unit myapp.socket not found.

The socket unit referenced by the service does not exist.""",
     """Common Causes:
- The socket unit file was deleted
- The socket unit was not installed
- Typo in the socket name in the service unit""",
     """How to Fix:
```bash
# Create the socket unit
sudo tee /etc/systemd/system/myapp.socket <<'EOF'
[Unit]
Description=My App Socket

[Socket]
ListenStream=8080

[Install]
WantedBy=sockets.target
EOF

sudo systemctl daemon-reload
sudo systemctl start myapp.socket
```"""),

    ("socket-activated-too-slowly", "systemd socket activated too slowly",
     "Fix systemd socket activated too slowly. Resolve slow socket activation causing connection timeouts.",
     """myapp.service: Socket activation timed out. Connection refused.

The service did not start quickly enough to accept the incoming connection.""",
     """Common Causes:
- Service startup is too slow for socket activation
- Accept=no is used incorrectly
- Service has heavy initialization that delays readiness""",
     """How to Fix:
```bash
# Optimize service startup
sudo systemctl edit myapp.service
```

```ini
[Service]
Type=notify
ExecStart=/usr/bin/myapp
TimeoutStartSec=30
# Use Accept=yes for per-connection instances
# Or use Type=simple with fast startup
```"""),

    ("accept-false-not-allowed", "systemd Accept=false not allowed",
     "Fix systemd Accept=false not allowed. Resolve socket unit configuration errors for Accept directive.",
     """myapp.socket: Accept=false not valid for this socket type.

The Accept= directive is not compatible with the configured socket type.""",
     """Common Causes:
- Accept= is used with datagram or special socket types
- Accept= is only valid for stream sockets
- Misconfiguration of socket activation""",
     """How to Fix:
```bash
# Accept= only works with ListenStream=
# For datagram sockets, use Accept=no (default)
sudo systemctl edit myapp.socket
```

```ini
[Socket]
# For stream sockets:
ListenStream=8080
Accept=yes

# For datagram sockets:
# ListenDatagram=8080
# Accept=no
```"""),

    ("listenstream-invalid", "systemd ListenStream invalid",
     "Fix systemd ListenStream invalid errors. Resolve socket unit ListenStream configuration errors.",
     """myapp.socket: Invalid ListenStream address: [::]:abc

The ListenStream= value has an invalid address or port format.""",
     """Common Causes:
- Invalid port number (non-numeric or out of range)
- Malformed IPv6 address
- Missing port specification
- Using a path that doesn't start with /""",
     """How to Fix:
```bash
# Valid ListenStream formats:
# ListenStream=8080           (port on all interfaces)
# ListenStream=127.0.0.1:8080 (specific IPv4)
# ListenStream=[::]:8080      (all IPv6 interfaces)
# ListenStream=/run/myapp.sock (Unix socket)

sudo systemctl edit myapp.socket
```

```ini
[Socket]
ListenStream=8080
```"""),

    ("listen-datagram-error", "systemd ListenDatagram error",
     "Fix systemd ListenDatagram errors. Resolve datagram socket configuration issues.",
     """myapp.socket: Failed to create datagram socket: Invalid argument

The datagram socket could not be created with the specified configuration.""",
     """Common Causes:
- Invalid address format for datagram socket
- Port is out of range
- IPv6 datagram socket requires specific configuration
- Kernel does not support the requested socket type""",
     """How to Fix:
```bash
# Check the socket configuration
systemd-analyze verify myapp.socket

# Valid ListenDatagram format
sudo systemctl edit myapp.socket
```

```ini
[Socket]
ListenDatagram=8080
```"""),

    ("listenfifo-error", "systemd ListenFIFO error",
     "Fix systemd ListenFIFO errors. Resolve FIFO/pipe socket configuration issues.",
     """myapp.socket: Failed to open FIFO: No such file or directory

The FIFO path specified in ListenFIFO= does not exist.""",
     """Common Causes:
- The FIFO path does not exist
- The FIFO was not created with mkfifo
- Directory permissions prevent FIFO creation
- SELinux blocking FIFO access""",
     """How to Fix:
```bash
# Create the FIFO manually
sudo mkfifo /run/myapp/fifo
sudo chown myappuser:myappuser /run/myapp/fifo

# Or let systemd create it with RuntimeDirectory
sudo systemctl edit myapp.socket
```

```ini
[Socket]
ListenFIFO=/run/myapp/fifo
RuntimeDirectory=myapp
```"""),

    ("socketgroup-not-found", "systemd SocketGroup not found",
     "Fix systemd SocketGroup not found errors. Resolve socket group ownership issues.",
     """myapp.socket: SocketGroup 'appgroup' not found.

The group specified in SocketGroup= does not exist.""",
     """Common Causes:
- The group specified in SocketGroup= does not exist
- Group was deleted but socket unit still references it
- Typo in the group name""",
     """How to Fix:
```bash
# Check if the group exists
getent group appgroup

# Create the group if missing
sudo groupadd appgroup

# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart myapp.socket
```"""),

    ("service-not-socket-activatable", "systemd service not socket-activatable",
     "Fix systemd service not socket-activatable. Resolve socket activation failures when the service cannot be started via socket.",
     """myapp.service: Not socket-activatable: missing Accept= or Type=notify.

The service is not configured for socket activation.""",
     """Common Causes:
- Service does not use Type=notify or Type=simple
- Service does not call sd_notify(READY=1)
- Accept= is not properly configured in the socket unit
- Application does not support systemd socket activation""",
     """How to Fix:
```bash
# Ensure the service supports socket activation
sudo systemctl edit myapp.service
```

```ini
[Service]
Type=notify
ExecStart=/usr/bin/myapp
NotifyAccess=main
```"""),

    ("trigger-limit-exceeded", "systemd socket trigger limit exceeded",
     "Fix systemd socket trigger limit exceeded. Resolve socket activation rate limiting.",
     """myapp.socket: Trigger limit hit. Refusing to activate service.

The socket unit has been triggered too many times.""",
     """Common Causes:
- Too many connections arriving in a short time
- Service is not starting fast enough to handle connections
- Rate limiting is too restrictive""",
     """How to Fix:
```bash
# Check socket trigger limits
systemctl show myapp.socket | grep TriggerLimit

# Increase the trigger limit
sudo systemctl edit myapp.socket
```

```ini
[Socket]
TriggerLimitIntervalSec=60
TriggerLimitBurst=1000
```"""),

    ("socket-stopped-unexpectedly", "systemd socket stopped unexpectedly",
     "Fix systemd socket stopped unexpectedly. Resolve socket unit unexpected stop issues.",
     """myapp.socket: Stopped (but not bound) too quickly.

The socket unit stopped before it could accept connections.""",
     """Common Causes:
- Socket unit was stopped by another service
- System shutdown or restart interrupted the socket
- Socket configuration error causing immediate stop
- Conflicts= directive with another unit""",
     """How to Fix:
```bash
# Check socket status
systemctl status myapp.socket

# Restart the socket
sudo systemctl restart myapp.socket

# Check for conflicts
systemctl show myapp.socket | grep Conflicts

# Ensure socket is enabled
sudo systemctl enable myapp.socket
```"""),

    # ── Category 5: Timer unit errors ──
    ("timer-not-active", "systemd timer not active",
     "Fix systemd timer not active errors. Resolve timer units that are not triggering their associated services.",
     """myapp.timer: Timer is not active.

The timer unit is not in the active state and is not scheduling runs.""",
     """Common Causes:
- Timer unit is not enabled
- Timer was stopped or failed
- Timer configuration has invalid calendar or monotonic value
- The associated service does not exist""",
     """How to Fix:
```bash
# Check timer status
systemctl status myapp.timer

# Enable and start the timer
sudo systemctl enable myapp.timer
sudo systemctl start myapp.timer

# List all active timers
systemctl list-timers --all

# Check the timer configuration
systemctl cat myapp.timer
```"""),

    ("oncalendar-parse-error", "systemd OnCalendar parse error",
     "Fix systemd OnCalendar parse error. Resolve timer configuration failures with invalid calendar expressions.",
     """myapp.timer: Failed to parse OnCalendar= expression: 'daily 2:30': Invalid format

The OnCalendar= value has invalid syntax.""",
     """Common Causes:
- Invalid calendar expression format
- Missing or incorrect time specification
- Unsupported calendar keywords
- Locale-related parsing issues""",
     """How to Fix:
```bash
# Valid OnCalendar= formats:
# OnCalendar=daily
# OnCalendar=*-*-* 02:30:00
# OnCalendar=Mon *-*-* 09:00:00
# OnCalendar=monthly
# OnCalendar=weekly
# OnCalendar=yearly

# Test calendar expression
systemd-analyze calendar 'daily' --iterations=3

# Edit the timer
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
```"""),

    ("onbootsec-too-short", "systemd OnBootSec too short",
     "Fix systemd OnBootSec too short. Resolve timer issues where the boot delay is insufficient.",
     """myapp.timer: OnBootSec=10s is too short. Minimum is 1ms.

The OnBootSec= value is below the minimum allowed.""",
     """Common Causes:
- OnBootSec= set to a value below 1ms
- Value is negative or zero
- Value format is incorrect""",
     """How to Fix:
```bash
# Valid OnBootSec= formats:
# OnBootSec=30s    (30 seconds after boot)
# OnBootSec=5min   (5 minutes after boot)
# OnBootSec=1h     (1 hour after boot)

sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnBootSec=5min
OnUnitActiveSec=1h
```"""),

    ("onunitactivesec-not-set", "systemd OnUnitActiveSec not set",
     "Fix systemd OnUnitActiveSec not set warnings. Resolve timer issues with missing repeat intervals.",
     """myapp.timer: Neither OnCalendar= nor OnUnitActiveSec= is set.

The timer has no way to determine when to fire next.""",
     """Common Causes:
- Timer unit file has no scheduling directive
- Only OnBootSec= is set without a recurring trigger
- Timer was misconfigured""",
     """How to Fix:
```bash
# Add a scheduling directive
sudo systemctl edit myapp.timer
```

```ini
[Timer]
# For one-shot after boot:
OnBootSec=5min

# For recurring:
OnUnitActiveSec=1h

# For calendar-based:
OnCalendar=*-*-* 02:00:00
```"""),

    ("persistent-not-set", "systemd Persistent not set",
     "Fix systemd Persistent not set warnings. Resolve timer issues where missed runs are not captured.",
     """myapp.timer: Persistent= not set. Missed runs will not be captured.

The timer will not run missed executions if the system was off.""",
     """Common Causes:
- Persistent= is not set in the timer unit
- System was off during a scheduled timer run
- Timer does not catch up on missed triggers""",
     """How to Fix:
```bash
# Enable persistent mode
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnCalendar=daily
Persistent=true
```"""),

    ("accuracysec-too-high", "systemd AccuracySec too high",
     "Fix systemd AccuracySec too high. Resolve timer accuracy issues causing delayed execution.",
     """myapp.timer: AccuracySec=1d is very high. Timer may not fire on time.

The timer accuracy window is too large.""",
     """Common Causes:
- AccuracySec= set to a very large value
- Timer fires much later than expected
- Default AccuracySec=1min may be overridden""",
     """How to Fix:
```bash
# Set appropriate accuracy
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnCalendar=*-*-* 02:00:00
AccuracySec=1s
```"""),

    ("randomizeddelaysec-conflict", "systemd RandomizedDelaySec conflict",
     "Fix systemd RandomizedDelaySec conflict. Resolve timer issues with incompatible delay settings.",
     """myapp.timer: RandomizedDelaySec=3600 conflicts with OnUnitActiveSec=60.

Randomized delay exceeds the interval.""",
     """Common Causes:
- RandomizedDelaySec= is larger than the timer interval
- Delay would cause the next trigger before the previous completes
- OnUnitActiveSec= is too short for the random delay""",
     """How to Fix:
```bash
# Adjust RandomizedDelaySec to be less than the interval
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnUnitActiveSec=1h
RandomizedDelaySec=5min
```"""),

    ("fixedrandomdelay-error", "systemd FixedRandomDelay error",
     "Fix systemd FixedRandomDelay error. Resolve timer fixed random delay configuration issues.",
     """myapp.timer: FixedRandomDelay= requires RandomizedDelaySec= to be set.

FixedRandomDelay without RandomizedDelaySec is invalid.""",
     """Common Causes:
- FixedRandomDelay=true is set without RandomizedDelaySec=
- RandomizedDelaySec= is set to 0""",
     """How to Fix:
```bash
# Set both RandomizedDelaySec and FixedRandomDelay
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnCalendar=daily
RandomizedDelaySec=15min
FixedRandomDelay=true
```"""),

    ("timer-not-triggering", "systemd timer not triggering",
     "Fix systemd timer not triggering. Resolve timer units that are active but not starting their service.",
     """myapp.timer: Timer is active but myapp.service has not been started.

The timer is running but not triggering its associated service.""",
     """Common Causes:
- The associated service unit name does not match the timer name
- Timer is configured but the OnCalendar= expression has not yet matched
- The service unit is masked or has a dependency failure""",
     """How to Fix:
```bash
# Verify timer-service name match
systemctl list-timers

# Check what the timer will start
systemctl list-dependencies myapp.timer

# Test the calendar expression
systemd-analyze calendar 'daily' --iterations=5

# Manually trigger the service
sudo systemctl start myapp.service
```"""),

    ("unit-not-found-for-timer", "systemd unit not found for timer",
     "Fix systemd unit not found for timer. Resolve timer failures when the associated service does not exist.",
     """myapp.timer: Unit myapp.service not found.

The service unit that the timer is supposed to start does not exist.""",
     """Common Causes:
- The service unit file was deleted
- The service unit was never created
- Timer and service names do not match""",
     """How to Fix:
```bash
# Check the timer configuration
systemctl cat myapp.timer

# Create the missing service unit
sudo tee /etc/systemd/system/myapp.service <<'EOF'
[Unit]
Description=My App Timer Job

[Service]
Type=oneshot
ExecStart=/usr/bin/myapp --run-job

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
```"""),

    ("monotonic-timer-error", "systemd monotonic timer error",
     "Fix systemd monotonic timer error. Resolve OnActiveSec, OnBootSec, or OnUnitActiveSec configuration issues.",
     """myapp.timer: Invalid monotonic timer value: -10s.

Monotonic timer values must be positive.""",
     """Common Causes:
- Negative value specified for a monotonic timer
- Invalid time format (e.g., missing unit suffix)
- Value is 0 or negative""",
     """How to Fix:
```bash
# Valid monotonic timer values are positive
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnActiveSec=10min
OnBootSec=5min
OnUnitActiveSec=1h
OnUnitInactiveSec=30min
```"""),

    ("calendar-timer-error", "systemd calendar timer error",
     "Fix systemd calendar timer error. Resolve OnCalendar expression parsing and scheduling issues.",
     """myapp.timer: OnCalendar= expression 'every day at 2:30' could not be parsed.

The calendar expression is not in a recognized format.""",
     """Common Causes:
- Human-readable expressions are not supported
- Time format must follow systemd calendar syntax
- Missing year or date component""",
     """How to Fix:
```bash
# Use systemd calendar format
systemd-analyze calendar 'Mon *-*-* 09:00:00' --iterations=3

# Common formats:
# daily          → *-*-* 00:00:00
# hourly         → *-*-* *:00:00
# Mon 09:00      → Mon *-*-* 09:00:00
# 1st of month   → *-*-01 00:00:00

sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnCalendar=*-*-* 02:30:00
```"""),

    ("timer-overlaps-missed", "systemd timer overlaps missed",
     "Fix systemd timer overlaps missed. Resolve timer execution gaps when runs overlap.",
     """myapp.timer: Missed scheduled run. Timer interval too short.

The timer could not complete the previous run before the next one was due.""",
     """Common Causes:
- Timer interval is shorter than the service execution time
- OnUnitActiveSec is too short
- System was under heavy load during the timer run""",
     """How to Fix:
```bash
# Increase the timer interval
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnUnitActiveSec=2h
# Ensure this is longer than the service typically takes
```"""),

    # ── Category 6: Mount/automount errors ──
    ("mount-unit-failed", "systemd mount unit failed",
     "Fix systemd mount unit failed errors. Resolve mount unit failures during system startup or manual mounting.",
     """mnt-data.mount: Mount process exited, code=exited, status=32/FAILURE

The mount operation failed with exit code 32.""",
     """Common Causes:
- The device specified in What= does not exist
- Filesystem type in Type= is not supported
- Mount point directory does not exist
- Device is busy or already mounted""",
     """How to Fix:
```bash
# Check mount unit status
systemctl status mnt-data.mount

# Check the device
lsblk

# Create mount point if missing
sudo mkdir -p /mnt/data

# Test mount manually
sudo mount /dev/sdb1 /mnt/data
```"""),

    ("mount-not-found", "systemd mount unit not found",
     "Fix systemd mount unit not found errors. Resolve mount failures when the mount unit is missing.",
     """Failed to mount mnt-data.mount: Unit mnt-data.mount not found.

The mount unit file does not exist.""",
     """Common Causes:
- Mount unit file was not created
- Unit file was deleted
- The mount was configured in /etc/fstab but not converted to a systemd mount""",
     """How to Fix:
```bash
# Check if the mount is in fstab
grep /mnt/data /etc/fstab

# Create the mount unit
sudo tee /etc/systemd/system/mnt-data.mount <<'EOF'
[Unit]
Description=Data Mount
After=blockdev@dev-disk-by\\x2duuid-XXXX.target

[Mount]
What=/dev/sdb1
Where=/mnt/data
Type=ext4
Options=defaults

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable mnt-data.mount
sudo systemctl start mnt-data.mount
```"""),

    ("what-not-set", "systemd What= not set in mount unit",
     "Fix systemd What= not set errors. Resolve mount unit configuration errors when the device path is missing.",
     """mnt-data.mount: What= is not set. Mount unit requires a device.

The What= directive is required in the [Mount] section.""",
     """Common Causes:
- What= directive is missing from the mount unit
- Unit file was created without specifying the device
- The device path was removed accidentally""",
     """How to Fix:
```bash
# Edit the mount unit to add What=
sudo systemctl edit mnt-data.mount --force
```

```ini
[Mount]
What=/dev/sdb1
Where=/mnt/data
Type=ext4
```"""),

    ("where-not-found", "systemd Where= path not found",
     "Fix systemd Where= path not found errors. Resolve mount failures when the mount point directory is missing.",
     """mnt-data.mount: Where= path '/mnt/data' does not exist.

The mount point directory does not exist.""",
     """Common Causes:
- The mount point directory was deleted
- Directory permissions are incorrect
- Path was created with incorrect case""",
     """How to Fix:
```bash
# Create the mount point directory
sudo mkdir -p /mnt/data
sudo chmod 755 /mnt/data

# Verify
ls -la /mnt/data

# Reload and start
sudo systemctl daemon-reload
sudo systemctl start mnt-data.mount
```"""),

    ("fstab-conversion-error", "systemd fstab conversion error",
     "Fix systemd fstab conversion error. Resolve issues where /etc/fstab entries cannot be converted to systemd mount units.",
     """Failed to add mount: /etc/fstab contains invalid entry for /mnt/data.

systemd could not parse the fstab entry.""",
     """Common Causes:
- Malformed fstab entry
- Missing fields in the fstab line
- Invalid options in the fstab mount
- UUID or device path not found""",
     """How to Fix:
```bash
# Check the fstab entry
cat /etc/fstab

# Valid fstab format:
# <device>  <mount>  <type>  <options>  <dump>  <pass>

# Example:
# UUID=xxxx-xxxx  /mnt/data  ext4  defaults  0  2

# Verify with systemd
sudo systemd-analyze verify /mnt-data.mount
```"""),

    ("automount-not-working", "systemd automount not working",
     "Fix systemd automount not working. Resolve automount units that do not trigger on access.",
     """mnt-data.automount: Automount not triggered when accessing /mnt/data.

The automount unit is not mounting on demand.""",
     """Common Causes:
- Automount unit is not enabled
- The associated mount unit has errors
- Directory access is happening through a cached path
- The automount unit file is not properly configured""",
     """How to Fix:
```bash
# Check automount status
systemctl status mnt-data.automount

# Enable and start
sudo systemctl enable mnt-data.automount
sudo systemctl start mnt-data.automount

# Test by accessing the mount point
ls /mnt/data
```"""),

    ("automount-timeout", "systemd automount timeout",
     "Fix systemd automount timeout. Resolve automount units that time out during mounting.",
     """mnt-data.automount: Mounting timed out. Killing mount process.

The automount took too long to complete the mount.""",
     """Common Causes:
- Network mount is slow to respond
- Device is slow to initialize
- Timeout is too short for the mount type
- NFS or SMB server is unreachable""",
     """How to Fix:
```bash
# Increase the timeout
sudo systemctl edit mnt-data.automount
```

```ini
[Automount]
Where=/mnt/data
TimeoutIdleSec=120
```"""),

    ("unit-dependency-on-mount", "systemd unit dependency on mount",
     "Fix systemd unit dependency on mount. Resolve service failures when dependent mount units fail.",
     """myapp.service: Failed to start because dependent mount mnt-data.mount failed.

The service depends on a mount that could not be established.""",
     """Common Causes:
- Mount unit failed before the service started
- Service has RequiresMountsFor= or Requires= pointing to a failed mount
- Mount dependency chain is broken""",
     """How to Fix:
```bash
# Check the mount status
systemctl status mnt-data.mount

# Ensure mount is started before the service
sudo systemctl edit myapp
```

```ini
[Unit]
Requires=mnt-data.mount
After=mnt-data.mount
```"""),

    ("network-mount-timeout", "systemd network mount timeout",
     "Fix systemd network mount timeout. Resolve mount failures for network filesystems (NFS, CIFS).",
     """mnt-nfs.mount: Mount timed out. Network server is not responding.

The network mount could not be completed within the timeout.""",
     """Common Causes:
- NFS server is unreachable
- Network interface is not ready when mount is attempted
- Firewall blocking NFS/CIFS ports
- DNS resolution failed for the server hostname""",
     """How to Fix:
```bash
# Ensure network is ready before mount
sudo systemctl edit mnt-nfs.mount
```

```ini
[Unit]
After=network-online.target
Wants=network-online.target

[Mount]
What=nfs-server:/export
Where=/mnt/nfs
Type=nfs
Options=soft,timeo=10,retrans=3
```"""),

    ("nfs-mount-failed", "systemd NFS mount failed",
     "Fix systemd NFS mount failed. Resolve NFS mount failures from systemd mount units.",
     """mnt-nfs.mount: Mount failed: mount.nfs: No route to host

The NFS mount could not connect to the NFS server.""",
     """Common Causes:
- NFS server is down or unreachable
- NFS export does not exist
- Client IP is not authorized in exports file
- NFS version mismatch""",
     """How to Fix:
```bash
# Test NFS connectivity
showmount -e nfs-server

# Check NFS service
rpcinfo -p nfs-server

# Test mount manually
sudo mount -t nfs nfs-server:/export /mnt/nfs

# Check firewall
sudo firewall-cmd --list-services | grep nfs
```"""),

    ("smb-mount-credential", "systemd SMB mount credential error",
     "Fix systemd SMB mount credential error. Resolve CIFS/SMB mount failures due to authentication issues.",
     """mnt-smb.mount: Mount failed: mount error(13): Permission denied

The SMB mount failed due to credential issues.""",
     """Common Causes:
- Incorrect username or password
- Credential file has wrong permissions
- SMB share requires domain authentication
- SMB protocol version mismatch""",
     """How to Fix:
```bash
# Create credential file
sudo tee /etc/samba/credentials <<'EOF'
username=myuser
password=mypassword
domain=MYDOMAIN
EOF
sudo chmod 600 /etc/samba/credentials

# Update mount unit
sudo systemctl edit mnt-smb.mount
```

```ini
[Mount]
What=//server/share
Where=/mnt/smb
Type=cifs
Options=credentials=/etc/samba/credentials,vers=3.0
```"""),

    ("filesystem-not-recognized", "systemd filesystem not recognized",
     "Fix systemd filesystem not recognized. Resolve mount failures when systemd cannot identify the filesystem type.",
     """mnt-data.mount: Failed to identify file system: No such file system.

systemd cannot determine the filesystem type.""",
     """Common Causes:
- Filesystem type kernel module is not loaded
- The filesystem type name is misspelled
- The device does not contain a valid filesystem
- Required userspace tools are not installed""",
     """How to Fix:
```bash
# Check the filesystem
blkid /dev/sdb1

# Load the kernel module (for exotic filesystems)
sudo modprobe <filesystem-module>

# Install required tools
sudo apt install <filesystem-tools-package>
```"""),

    ("mount-point-not-empty", "systemd mount point not empty",
     "Fix systemd mount point not empty. Resolve mount failures when the mount directory contains existing files.",
     """mnt-data.mount: Mount point /mnt/data is not empty. Mounting anyway.

Warning: Files in the mount point will be hidden.""",
     """Common Causes:
- Files exist in the mount point directory
- Previous mount left residual files
- Mount was not cleanly unmounted""",
     """How to Fix:
```bash
# Check mount point contents
ls -la /mnt/data

# Backup and clean the mount point
sudo mv /mnt/data/* /tmp/backup/
sudo systemctl restart mnt-data.mount

# Or use x-systemd.requires for cleanup
```"""),

    ("bind-mount-error", "systemd bind mount error",
     "Fix systemd bind mount error. Resolve bind mount failures in systemd mount units.",
     """mnt-link.mount: Bind mount failed: No such file or directory

The source directory for the bind mount does not exist.""",
     """Common Causes:
- Source directory for bind mount does not exist
- Target directory does not exist
- SELinux blocking the bind mount
- Source is a file but target expects a directory""",
     """How to Fix:
```bash
# Check source directory
ls -la /opt/myapp/data

# Create directories if missing
sudo mkdir -p /opt/myapp/data
sudo mkdir -p /mnt/data

# Update mount unit with Options=bind
sudo systemctl edit mnt-link.mount
```

```ini
[Mount]
What=/opt/myapp/data
Where=/mnt/data
Type=none
Options=bind
```"""),

    # ── Category 7: Target/runlevel errors ──
    ("target-not-found", "systemd target not found",
     "Fix systemd target not found errors. Resolve failures when referencing a non-existent target.",
     """Failed to isolate myapp.target: Unit myapp.target not found.

The specified target does not exist.""",
     """Common Causes:
- Target unit file does not exist
- Typo in the target name
- Target was deleted but still referenced
- Package providing the target is not installed""",
     """How to Fix:
```bash
# List available targets
systemctl list-unit-files --type=target

# Create a custom target
sudo tee /etc/systemd/system/myapp.target <<'EOF'
[Unit]
Description=My App Target
Requires=multi-user.target
After=multi-user.target
AllowIsolate=yes

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
```"""),

    ("multi-user-target-failed", "systemd multi-user.target failed",
     "Fix systemd multi-user.target failed. Resolve boot failures where multi-user.target cannot be reached.",
     """multi-user.target: Failed to start. System not reaching multi-user mode.

The system failed to reach the multi-user.target during boot.""",
     """Common Causes:
- A required service in multi-user.target failed
- Network configuration error
- Filesystem mount failure
- Critical service dependency not met""",
     """How to Fix:
```bash
# Check which services failed
systemctl --failed

# Check multi-user.target dependencies
systemctl list-dependencies multi-user.target

# Boot into rescue mode for debugging
sudo systemctl isolate rescue.target

# Check logs
journalctl -b -p err
```"""),

    ("graphical-target-failed", "systemd graphical.target failed",
     "Fix systemd graphical.target failed. Resolve desktop boot failures when graphical.target cannot be reached.",
     """graphical.target: Failed to start. Display manager not starting.

The system could not reach the graphical.target.""",
     """Common Causes:
- Display manager (GDM, SDDM, LightDM) failed to start
- GPU driver issues
- X11 or Wayland configuration error
- Missing graphical dependencies""",
     """How to Fix:
```bash
# Check display manager status
systemctl status gdm
systemctl status sddm

# Switch to text mode
sudo systemctl isolate multi-user.target

# Check X11 logs
cat /var/log/Xorg.0.log

# Reinstall display manager
sudo apt reinstall gdm3
```"""),

    ("default-target-not-set", "systemd default target not set",
     "Fix systemd default target not set. Resolve boot issues when the system does not know which target to reach.",
     """No default target set. System cannot determine boot target.

The default.target symlink is missing or broken.""",
     """Common Causes:
- /etc/systemd/system/default.target symlink is missing
- Symlink points to a non-existent target
- System was installed without a default target""",
     """How to Fix:
```bash
# Check current default target
systemctl get-default

# Set the default target
sudo systemctl set-default multi-user.target
# or for graphical desktop:
sudo systemctl set-default graphical.target

# Verify the symlink
ls -la /etc/systemd/system/default.target
```"""),

    ("rescue-target-entered", "systemd rescue.target entered",
     "Fix systemd rescue.target entered. Resolve systems stuck in rescue mode during boot.",
     """The system has entered rescue mode. Some services failed to start.

Emergency mode with limited services is active.""",
     """Common Causes:
- Critical services failed during boot
- Root filesystem mount failure
- Filesystem corruption
- Incorrect fstab entry""",
     """How to Fix:
```bash
# Check failed services
systemctl --failed

# Check filesystem
fsck /dev/sda1

# Fix fstab
nano /etc/fstab

# Exit rescue mode
exit
```"""),

    ("emergency-target-active", "systemd emergency.target active",
     "Fix systemd emergency.target active. Resolve systems stuck in emergency mode.",
     """The system has entered emergency mode. Only root filesystem mounted.

The system is in emergency mode with minimal services.""",
     """Common Causes:
- Root filesystem is read-only
- Filesystem corruption
- Critical kernel module missing
- Wrong root device in bootloader""",
     """How to Fix:
```bash
# Remount root filesystem as read-write
mount -o remount,rw /

# Check and repair filesystem
fsck /dev/sda1

# Check fstab
cat /etc/fstab

# Fix bootloader configuration
```"""),

    ("isolate-failed", "systemd isolate failed",
     "Fix systemd isolate failed. Resolve target isolation failures when switching between targets.",
     """Failed to isolate myapp.target: Transaction is destructive.

systemd refused to isolate the target because it would stop critical services.""",
     """Common Causes:
- Isolate would require stopping essential services
- AllowIsolate=yes is not set on the target
- Conflicting dependencies prevent isolation
- Target requires services that are stopped""",
     """How to Fix:
```bash
# Set AllowIsolate on the target
sudo systemctl edit myapp.target
```

```ini
[Unit]
AllowIsolate=yes
```

```bash
# Or force isolate (use with caution)
sudo systemctl isolate --force myapp.target
```"""),

    ("conflict-with-other-target", "systemd conflict with other target",
     "Fix systemd conflict with other target. Resolve target conflicts preventing simultaneous activation.",
     """Conflicting targets: myapp.target conflicts with graphical.target.

Two targets with Conflicts= cannot be active simultaneously.""",
     """Common Causes:
- Two targets have Conflicts= pointing at each other
- Target isolation is prevented by conflicting dependencies
- System cannot run in two modes at once""",
     """How to Fix:
```bash
# Check target conflicts
systemctl show myapp.target | grep Conflicts

# Remove the conflict if both should be available
sudo systemctl edit myapp.target --full
```"""),

    ("sysinit-target-timeout", "systemd sysinit.target timeout",
     "Fix systemd sysinit.target timeout. Resolve boot delays when sysinit.target takes too long.",
     """sysinit.target: Job sysinit.target/start timed out.

The system initialization target did not complete in time.""",
     """Common Causes:
- Hardware initialization is slow
- Filesystem check (fsck) is taking too long
- Module loading is slow
- Device probing timeout""",
     """How to Fix:
```bash
# Check what is blocking sysinit.target
systemd-analyze blame

# Increase the timeout
sudo systemctl edit sysinit.target
```

```ini
[Service]
TimeoutStartSec=300
```

# Or speed up boot:
```bash
# Disable unnecessary services
sudo systemctl mask <service>

# Skip fsck if not needed
sudo tune2fs -c 0 /dev/sda1
```"""),

    ("basic-target-not-reached", "systemd basic.target not reached",
     "Fix systemd basic.target not reached. Resolve boot failures when basic.target cannot be started.",
     """basic.target: Failed to start. Boot process incomplete.

The basic.target (system startup complete) could not be reached.""",
     """Common Causes:
- A dependency of basic.target failed
- Socket units failed to start
- Timer units failed
- Slice or scope creation failed""",
     """How to Fix:
```bash
# Check which basic.target deps failed
systemctl list-dependencies basic.target

# Check failed units
systemctl --failed

# Analyze boot time
systemd-analyze blame

# Check specific failures
journalctl -b -u <failed-unit>
```"""),

    ("local-fs-target-failed", "systemd local-fs.target failed",
     "Fix systemd local-fs.target failed. Resolve boot failures when local filesystem mounts fail.",
     """local-fs.target: Failed to start. Local filesystems not mounted.

One or more local filesystem mounts failed during boot.""",
     """Common Causes:
- /etc/fstab contains invalid entries
- Device specified in fstab does not exist
- Filesystem corruption requires fsck
- Mount point directory missing""",
     """How to Fix:
```bash
# Check mount failures
systemctl --failed | grep mount

# Verify fstab
cat /etc/fstab
sudo systemd-analyze verify local-fs.target

# Boot to rescue mode and fix
sudo systemctl isolate rescue.target

# Run fsck
fsck /dev/sda1
```"""),

    ("network-target-not-ready", "systemd network.target not ready",
     "Fix systemd network.target not ready. Resolve service startup failures when network is not yet available.",
     """myapp.service: Network is not yet configured. Starting anyway.

The service started before network.target was reached.""",
     """Common Causes:
- Service starts before network is configured
- After=network.target is missing or not effective
- Network configuration is slow
- Service does not wait for network-online.target""",
     """How to Fix:
```bash
# Use network-online.target instead of network.target
sudo systemctl edit myapp
```

```ini
[Unit]
After=network-online.target
Wants=network-online.target
```"""),

    ("time-sync-target-timeout", "systemd time-sync.target timeout",
     "Fix systemd time-sync.target timeout. Resolve boot delays when time synchronization takes too long.",
     """time-sync.target: Job timed out. NTP synchronization not complete.

The system could not synchronize time within the allowed timeout.""",
     """Common Causes:
- NTP server is unreachable
- systemd-timesyncd is not configured
- Network not available for time sync
- Firewall blocking NTP traffic""",
     """How to Fix:
```bash
# Check time sync status
timedatectl status

# Configure NTP
sudo timedatectl set-ntp true

# Check timesyncd
systemctl status systemd-timesyncd

# Set NTP server
sudo tee /etc/systemd/timesyncd.conf <<'EOF'
[Time]
NTP=pool.ntp.org
FallbackNTP=0.pool.ntp.org 1.pool.ntp.org
EOF

sudo systemctl restart systemd-timesyncd
```"""),

    # ── Category 8: Journal/log errors ──
    ("journal-corrupt", "systemd journal corrupt",
     "Fix systemd journal corrupt errors. Resolve journal corruption causing log reading failures.",
     """Journal file /var/log/journal/... is corrupt, ignoring file.

The journal file is corrupted and cannot be read.""",
     """Common Causes:
- System crash or power loss during journal write
- Disk full during journal write
- Journal file format incompatibility after upgrade
- Storage=volatile with unexpected shutdown""",
     """How to Fix:
```bash
# Check journal health
journalctl --disk-usage

# Vacuum corrupt journal files
sudo journalctl --vacuum-files=1

# Remove all journal files (loses logs)
sudo rm /var/log/journal/*/*.journal*

# Restart journald
sudo systemctl restart systemd-journald
```"""),

    ("journal-file-too-large", "systemd journal file too large",
     "Fix systemd journal file too large. Resolve disk space issues caused by large journal files.",
     """Journal file /var/log/journal/... is too large (2.5G). Consider using SystemMaxUse.

The journal has consumed excessive disk space.""",
     """Common Causes:
- SystemMaxUse or SystemMaxFileSize not configured
- No journal vacuum policy set
- High-volume logging services""",
     """How to Fix:
```bash
# Check current journal size
journalctl --disk-usage

# Vacuum old entries
sudo journalctl --vacuum-size=500M

# Configure size limits
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
SystemMaxUse=1G
SystemMaxFileSize=100M
MaxRetentionSec=30day
MaxFileSec=7day
EOF

sudo systemctl restart systemd-journald
```"""),

    ("journal-disk-full", "systemd journal disk full",
     "Fix systemd journal disk full. Resolve situations where the journal has consumed all available disk space.",
     """No space left on device. Journal cannot write new entries.

The disk is full and the journal cannot create new files.""",
     """Common Causes:
- Journal size limits not configured
- Disk partition is too small for logging
- Other data consuming disk space
- Log rotation not working""",
     """How to Fix:
```bash
# Emergency: vacuum journal immediately
sudo journalctl --vacuum-size=100M

# Check disk usage
df -h /var/log

# Remove old journal files
sudo find /var/log/journal -name "*.journal" -mtime +7 -delete

# Configure permanent limits
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
SystemMaxUse=500M
RuntimeMaxUse=200M
EOF

sudo systemctl restart systemd-journald
```"""),

    ("journal-vacuum-failed", "systemd journal vacuum failed",
     "Fix systemd journal vacuum failed. Resolve journal cleanup failures preventing disk space recovery.",
     """Failed to vacuum journal: Permission denied

The journal vacuum operation could not complete.""",
     """Common Causes:
- Insufficient privileges (not root)
- Journal files are owned by a different user
- Filesystem is read-only
- Journal is in volatile storage with special permissions""",
     """How to Fix:
```bash
# Use sudo
sudo journalctl --vacuum-size=500M

# Or vacuum by time
sudo journalctl --vacuum-time=30d

# Or vacuum by files
sudo journalctl --vacuum-files=5
```"""),

    ("journal-rotate-error", "systemd journal rotate error",
     "Fix systemd journal rotate error. Resolve journal file rotation failures.",
     """Failed to rotate journal files: No space left on device

The journal could not create new files during rotation.""",
     """Common Causes:
- Disk is full
- Journal directory permissions incorrect
- Inode exhaustion
- Filesystem quota reached""",
     """How to Fix:
```bash
# Free disk space first
sudo journalctl --vacuum-size=100M

# Check inode usage
df -i /var/log

# Fix permissions
sudo chown -R systemd-journal:systemd-journal /var/log/journal
sudo chmod 755 /var/log/journal
```"""),

    ("journalctl-no-entries", "systemd journalctl -u no entries",
     "Fix systemd journalctl -u no entries. Resolve missing log entries when using journalctl with service filter.",
     """-- No entries --

No journal entries found for the specified unit.""",
     """Common Causes:
- Service has not logged anything
- Service is not using journald for logging
- Log level is too low to capture entries
- Journal storage is set to volatile and was cleared""",
     """How to Fix:
```bash
# Check if the unit exists
systemctl status myapp

# Check all logs (not just this unit)
journalctl -n 50

# Verify journald is running
systemctl status systemd-journald

# Check storage configuration
cat /etc/systemd/journald.conf
```"""),

    ("journal-export-failed", "systemd journal export failed",
     "Fix systemd journal export failed. Resolve journal data export failures.",
     """Failed to export journal: Protocol error

The journal export operation encountered a protocol error.""",
     """Common Causes:
- Journal file corruption
- Insufficient disk space for export
- Incompatible journal format version
- Permission issues on output file""",
     """How to Fix:
```bash
# Export to a different location
journalctl -o export > /tmp/journal-export.txt

# Or output as JSON
journalctl -o json-pretty > /tmp/journal.json

# Check journal integrity first
journalctl --verify
```"""),

    ("systemd-journald-not-running", "systemd-journald not running",
     "Fix systemd-journald not running. Resolve logging failures when the journal daemon is not active.",
     """systemd-journald.service: Service is not running.

The journald daemon that manages system logs is not active.""",
     """Common Causes:
- journald was stopped or crashed
- Configuration error preventing startup
- Disk full preventing journald from running
- Corrupted journal files""",
     """How to Fix:
```bash
# Check journald status
systemctl status systemd-journald

# Restart it
sudo systemctl start systemd-journald

# Check logs for why it stopped
journalctl -u systemd-journald

# Fix configuration
sudo systemd-analyze verify systemd-journald
```"""),

    ("persistent-journal-not-enabled", "systemd persistent journal not enabled",
     "Fix systemd persistent journal not enabled. Resolve log persistence issues across reboots.",
     """Logs are not being persisted across reboots. Journal is volatile only.

The persistent journal storage is not configured.""",
     """Common Causes:
- /var/log/journal directory does not exist
- Storage=volatile is configured
- journald.conf has Storage=none
- Missing systemd-journal persistence configuration""",
     """How to Fix:
```bash
# Create persistent journal directory
sudo mkdir -p /var/log/journal

# Configure persistent storage
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
Storage=persistent
SystemMaxUse=1G
MaxRetentionSec=90day
EOF

sudo systemctl restart systemd-journald
```"""),

    ("journal-namespace-error", "systemd journal namespace error",
     "Fix systemd journal namespace error. Resolve journal namespace configuration issues.",
     """Failed to open journal namespace 'myapp': No such file or directory.

The journal namespace does not exist.""",
     """Common Causes:
- Journal namespace directory does not exist
- Namespace was not created by the service
- The journal@namespace service is not running
- Storage path misconfiguration""",
     """How to Fix:
```bash
# Create the namespace directory
sudo mkdir -p /var/log/journal/$(cat /etc/machine-id).myapp

# Check namespace journal
journalctl --namespace=myapp

# Restart journald
sudo systemctl restart systemd-journald
```"""),

    ("journal-size-limit-exceeded", "systemd journal size limit exceeded",
     "Fix systemd journal size limit exceeded. Resolve journal storage quota violations.",
     """Journal size limit exceeded. Oldest entries will be removed.

The journal has exceeded its configured size limit.""",
     """Common Causes:
- SystemMaxUse is configured but too low
- High log volume from services
- Logging at debug level increases volume""",
     """How to Fix:
```bash
# Check current size and limits
journalctl --disk-usage
grep -v '^#' /etc/systemd/journald.conf | grep -v '^$'

# Increase the limit
sudo tee -a /etc/systemd/journald.conf <<'EOF'
[Journal]
SystemMaxUse=2G
EOF

sudo systemctl restart systemd-journald
```"""),

    ("journal-acl-error", "systemd journal ACL error",
     "Fix systemd journal ACL error. Resolve journal access control issues preventing log reading.",
     """Failed to access journal: Permission denied. Access denied by journal ACL.

You do not have permission to read the journal entries.""",
     """Common Causes:
- User is not in the systemd-journal group
- ACL permissions on journal files are restrictive
- SELinux blocking journal access
- Journal was created with strict permissions""",
     """How to Fix:
```bash
# Add user to systemd-journal group
sudo usermod -a -G systemd-journal $USER

# Fix ACL on journal directory
sudo setfacl -R -m g:systemd-journal:rx /var/log/journal

# Check SELinux
sudo ausearch -m avc -ts recent
```"""),

    ("syslog-forwarding-failed", "systemd syslog forwarding failed",
     "Fix systemd syslog forwarding failed. Resolve remote syslog forwarding issues from journald.",
     """Failed to forward journal entries to remote syslog server: Connection refused

journald cannot forward logs to the remote syslog server.""",
     """Common Causes:
- Remote syslog server is unreachable
- ForwardToSyslog=yes is set but rsyslog is not running
- Network firewall blocking syslog port (514)
- rsyslog configuration error""",
     """How to Fix:
```bash
# Check rsyslog status
systemctl status rsyslog

# Configure journald forwarding
sudo tee /etc/systemd/journald.conf <<'EOF'
[Journal]
ForwardToSyslog=yes
ForwardToSyslogSocket=yes
EOF

sudo systemctl restart systemd-journald

# Or use rsyslog to read journald
sudo tee /etc/rsyslog.d/journald.conf <<'EOF'
module(load="imjournal")
input(type="imjournal")
EOF
```"""),

    # ── Category 9: Resource control errors ──
    ("cgroup-not-found", "systemd cgroup not found",
     "Fix systemd cgroup not found errors. Resolve service failures when cgroup hierarchy is missing.",
     """myapp.service: Failed to create cgroup: No such file or directory

systemd could not create or find the cgroup for this service.""",
     """Common Causes:
- cgroup filesystem is not mounted
- cgroup v1 vs v2 incompatibility
- Kernel does not support the requested cgroup controller
- cgroup hierarchy is corrupted""",
     """How to Fix:
```bash
# Check cgroup mount
mount | grep cgroup

# For cgroup v2
sudo mkdir -p /sys/fs/cgroup/system.slice/myapp.service

# Or remount cgroups
sudo systemctl daemon-reexec
```"""),

    ("cgroup-write-failed", "systemd cgroup write failed",
     "Fix systemd cgroup write failed. Resolve resource control failures when cgroup cannot be configured.",
     """myapp.service: Failed to write to cgroup: Permission denied

systemd cannot write resource control values to the cgroup.""",
     """Common Causes:
- Insufficient privileges to write cgroup values
- cgroup filesystem is read-only
- Resource limits exceed system capabilities
- Kernel cgroup support is disabled""",
     """How to Fix:
```bash
# Check cgroup permissions
ls -la /sys/fs/cgroup/system.slice/myapp.service/

# Ensure running as root
sudo systemctl start myapp

# Check kernel cgroup support
grep cgroup /proc/filesystems
```"""),

    ("memory-limit-exceeded", "systemd memory limit exceeded",
     "Fix systemd memory limit exceeded. Resolve OOM kills when service memory limits are too low.",
     """myapp.service: Memory limit exceeded. Process killed by OOM.

The service exceeded its configured MemoryMax and was killed.""",
     """Common Causes:
- MemoryMax is set too low for the application
- Memory leak in the application
- Insufficient system memory
- MemoryHigh threshold being hit continuously""",
     """How to Fix:
```bash
# Check memory usage
systemctl status myapp
systemd-cgtop

# Increase memory limit
sudo systemctl edit myapp
```

```ini
[Service]
MemoryMax=4G
MemoryHigh=3G
MemorySwapMax=2G
```"""),

    ("cpuquota-too-low", "systemd CPUQuota too low",
     "Fix systemd CPUQuota too low. Resolve service performance issues when CPU quota is insufficient.",
     """myapp.service: CPU quota too low. Service is severely throttled.

The CPUQuota= value is limiting CPU usage too aggressively.""",
     """Common Causes:
- CPUQuota= is set too low (e.g., 10%)
- Application requires more CPU than allocated
- CPUQuota format is invalid""",
     """How to Fix:
```bash
# Check current quota
systemctl show myapp | grep CPUQuota

# Increase the quota
sudo systemctl edit myapp
```

```ini
[Service]
CPUQuota=200%
# Or use CPUWeight for proportional scheduling
CPUWeight=100
```"""),

    ("ioweight-invalid", "systemd IOWeight invalid",
     "Fix systemd IOWeight invalid. Resolve IO scheduling configuration errors.",
     """myapp.service: Invalid IOWeight value: 2000. Valid range: 1-10000.

The IOWeight= value is outside the valid range.""",
     """Common Causes:
- IOWeight value is outside 1-10000
- IOWeight= is not supported by the current IO controller
- cgroup v2 IO controller not available""",
     """How to Fix:
```bash
# Valid IOWeight range: 1-10000 (default: 100)
sudo systemctl edit myapp
```

```ini
[Service]
IOWeight=500
# Or use IOReadBandwidthMax for bandwidth limiting
IOReadBandwidthMax=/dev/sda 50M
```"""),

    ("tasksmax-too-low", "systemd TasksMax too low",
     "Fix systemd TasksMax too low. Resolve service failures when the task limit is insufficient.",
     """myapp.service: TasksMax too low. Cannot fork new processes.

The service has hit its TasksMax= limit.""",
     """Common Causes:
- TasksMax= is set too low
- Application forks many worker processes
- Default TasksMax from systemd.conf is too restrictive
- System-wide pids.max limit reached""",
     """How to Fix:
```bash
# Check current limit
systemctl show myapp | grep TasksMax

# Increase the limit
sudo systemctl edit myapp
```

```ini
[Service]
TasksMax=65536
```"""),

    ("blockioweight-deprecated", "systemd BlockIOWeight deprecated",
     "Fix systemd BlockIOWeight deprecated. Resolve deprecation warnings for legacy IO control directives.",
     """myapp.service: BlockIOWeight= is deprecated. Use IOWeight= instead.

The BlockIOWeight= directive is no longer supported.""",
     """Common Causes:
- Using legacy cgroup v1 BlockIO directives on a cgroup v2 system
- Unit file was written for an older systemd version
- Deprecated directive not updated""",
     """How to Fix:
```bash
# Replace deprecated directives
# BlockIOWeight= → IOWeight=
# BlockIOReadBandwidthMax= → IOReadBandwidthMax=
# BlockIOWriteBandwidthMax= → IOWriteBandwidthMax=

sudo systemctl edit myapp
```

```ini
[Service]
IOWeight=500
```"""),

    ("cpuaccounting-not-enabled", "systemd CPUAccounting not enabled",
     "Fix systemd CPUAccounting not enabled. Resolve missing CPU usage statistics for services.",
     """CPU usage statistics are not available for myapp.service.

CPUAccounting= is not enabled for this service.""",
     """Common Causes:
- CPUAccounting=no is set explicitly
- cgroup CPU controller not available
- systemd compiled without CPU accounting support""",
     """How to Fix:
```bash
# Enable CPU accounting
sudo systemctl edit myapp
```

```ini
[Service]
CPUAccounting=yes
CPUQuota=100%
```"""),

    ("memory-accounting-not-available", "systemd memory accounting not available",
     "Fix systemd memory accounting not available. Resolve missing memory usage statistics.",
     """Memory usage statistics are not available for myapp.service.

MemoryAccounting is not supported for this service.""",
     """Common Causes:
- MemoryAccounting=no is set
- cgroup memory controller not available
- Kernel compiled without memory cgroup support""",
     """How to Fix:
```bash
# Enable memory accounting
sudo systemctl edit myapp
```

```ini
[Service]
MemoryAccounting=yes
MemoryMax=2G
```"""),

    ("io-accounting-disabled", "systemd IO accounting disabled",
     "Fix systemd IO accounting disabled. Resolve missing disk IO statistics for services.",
     """IO usage statistics are not available for myapp.service.

IOAccounting= is not enabled for this service.""",
     """Common Causes:
- IOAccounting=no is set
- cgroup IO controller not available
- IO accounting requires cgroup v2""",
     """How to Fix:
```bash
# Enable IO accounting (requires cgroup v2)
sudo systemctl edit myapp
```

```ini
[Service]
IOAccounting=yes
IOWeight=100
```"""),

    ("cgroup-v1-vs-v2-conflict", "systemd cgroup v1 vs v2 conflict",
     "Fix systemd cgroup v1 vs v2 conflict. Resolve incompatible cgroup controller issues between v1 and v2.",
     """The system is using mixed cgroup v1 and v2. Resource control may not work correctly.

cgroup v1 and v2 controllers are conflicting.""",
     """Common Causes:
- System booted with unified cgroup hierarchy but some services expect v1
- Container runtime using different cgroup version
- Kernel boot parameter enables mixed mode""",
     """How to Fix:
```bash
# Check cgroup version
stat -fc %T /sys/fs/cgroup/

# For pure cgroup v2, add to kernel cmdline:
# systemd.unified_cgroup_hierarchy=1

# Check current cgroup mount
mount | grep cgroup
```"""),

    ("oom-kill-by-systemd-oomd", "systemd OOM killed by systemd-oomd",
     "Fix systemd OOM kill by systemd-oomd. Resolve services killed by the systemd OOM daemon.",
     """myapp.service: Killed by systemd-oomd due to memory pressure.

systemd-oomd killed the service because system memory pressure was too high.""",
     """Common Causes:
- System is under heavy memory pressure
- Memory limits are too generous for the workload
- systemd-oomd is aggressively killing processes
- ManagedOOMMemoryPressure is set to kill""",
     """How to Fix:
```bash
# Check oomd status
systemctl status systemd-oomd

# Adjust oomd settings
sudo systemctl edit systemd-oomd
```

```ini
[Service]
ManagedOOMMemoryPressure=kill
ManagedOOMSwap=kill
```"""),

    ("memory-pressure-action", "systemd memory pressure action",
     "Fix systemd memory pressure action. Resolve unexpected behavior from MemoryPressureAction settings.",
     """myapp.service: MemoryPressureAction=kill triggered. Service terminated.

The service was killed due to memory pressure events.""",
     """Common Causes:
- MemoryPressureAction is set to 'kill'
- System is under sustained memory pressure
- Service does not handle memory pressure gracefully
- Action threshold is too sensitive""",
     """How to Fix:
```bash
# Change the action to 'none' or 'log'
sudo systemctl edit myapp
```

```ini
[Service]
MemoryPressureAction=log
# Options: none, log, kill, watch
```"""),

    # ── Category 10: Network/connectivity errors ──
    ("network-online-target-timeout", "systemd network-online.target timeout",
     "Fix systemd network-online.target timeout. Resolve boot delays when waiting for network availability.",
     """network-online.target: Job timed out. Network not ready within timeout.

The network did not become available within the expected time.""",
     """Common Causes:
- Network interface is slow to get an IP address
- DHCP server is unreachable
- NetworkManager or systemd-networkd not configured
- Waiting for a specific interface that does not exist""",
     """How to Fix:
```bash
# Check network status
systemctl status NetworkManager
# or
systemctl status systemd-networkd

# Configure network wait
sudo systemctl edit network-online.target
```

```ini
[Unit]
DefaultTimeoutStartSec=120
```

```bash
# For systemd-networkd, check configuration
networkctl status
```"""),

    ("network-not-ready-for-service", "systemd network not ready for service",
     "Fix systemd network not ready for service. Resolve service failures that depend on network availability.",
     """myapp.service: Network not ready. Starting anyway and may fail.

The service started before the network was available.""",
     """Common Causes:
- Service does not wait for network-online.target
- After= and Wants= for network targets are missing
- Network interface is not configured""",
     """How to Fix:
```bash
# Add network dependency
sudo systemctl edit myapp
```

```ini
[Unit]
After=network-online.target
Wants=network-online.target
```"""),

    ("dhcp-failed", "systemd DHCP failed",
     "Fix systemd DHCP failed. Resolve DHCP client failures with systemd-networkd.",
     """eth0: DHCP lease failed. Could not obtain IP address.

The DHCP client could not obtain an IP address.""",
     """Common Causes:
- DHCP server is unreachable
- Network cable is disconnected
- Network interface is down
- Firewall blocking DHCP traffic""",
     """How to Fix:
```bash
# Check network status
networkctl status eth0

# Request DHCP lease manually
sudo networkctl renew eth0

# Check DHCP configuration
cat /etc/systemd/network/10-eth0.network

# Restart networkd
sudo systemctl restart systemd-networkd
```"""),

    ("dns-resolution-failed", "systemd DNS resolution failed",
     "Fix systemd DNS resolution failed. Resolve DNS lookup failures with systemd-resolved.",
     """myapp.service: DNS resolution failed: Name or service not known

The system cannot resolve domain names.""",
     """Common Causes:
- systemd-resolved is not running
- DNS servers are not configured
- /etc/resolv.conf is missing or incorrect
- DNS over TLS configuration error""",
     """How to Fix:
```bash
# Check resolved status
systemctl status systemd-resolved

# Check DNS configuration
resolvectl status

# Configure DNS
sudo tee /etc/systemd/resolved.conf <<'EOF'
[Resolve]
DNS=8.8.8.8 8.8.4.4
FallbackDNS=1.1.1.1
DNSOverTLS=opportunistic
EOF

sudo systemctl restart systemd-resolved

# Link resolv.conf
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```"""),

    ("systemd-networkd-error", "systemd-networkd error",
     "Fix systemd-networkd error. Resolve network configuration failures with the systemd-networkd daemon.",
     """systemd-networkd.service: Failed to start. Network not configured.

The systemd-networkd service failed to start.""",
     """Common Causes:
- Network configuration files have errors
- Missing or invalid .network files
- Interface naming conflict
- systemd-networkd is not enabled""",
     """How to Fix:
```bash
# Check networkd status
systemctl status systemd-networkd

# Check network configuration
ls /etc/systemd/network/
networkctl status

# Restart networkd
sudo systemctl restart systemd-networkd

# Check logs
journalctl -u systemd-networkd -n 50
```"""),

    ("link-not-ready", "systemd link not ready",
     "Fix systemd link not ready. Resolve network link state issues with systemd-networkd.",
     """eth0: Link is not ready. Waiting for carrier.

The network link is down or waiting for carrier signal.""",
     """Common Causes:
- Physical cable is disconnected
- Network interface is administratively down
- Switch port is disabled
- Driver issue with the NIC""",
     """How to Fix:
```bash
# Check link status
networkctl status eth0

# Bring link up
sudo ip link set eth0 up

# Check physical connection
ethtool eth0

# Restart networkd
sudo systemctl restart systemd-networkd
```"""),

    ("addressfamily-not-set", "systemd AddressFamily not set",
     "Fix systemd AddressFamily not set. Resolve network configuration issues with missing address family specification.",
     """eth0.network: AddressFamily= not set. Defaults to inet+inet6.

AddressFamily was not explicitly specified in network configuration.""",
     """Common Causes:
- AddressFamily= is not specified in .network file
- Service expects IPv4 only but IPv6 is being used
- Dual-stack issues causing unexpected behavior""",
     """How to Fix:
```bash
# Specify AddressFamily in network config
sudo tee /etc/systemd/network/10-eth0.network <<'EOF'
[Match]
Name=eth0

[Network]
AddressFamily=inet
DHCP=yes
EOF

sudo systemctl restart systemd-networkd
```"""),

    ("ip-forwarding-not-enabled", "systemd IP forwarding not enabled",
     "Fix systemd IP forwarding not enabled. Resolve routing issues when IP forwarding is disabled.",
     """IP forwarding is not enabled. Routing between interfaces will not work.

The kernel IP forwarding is disabled.""",
     """Common Causes:
- net.ipv4.ip_forward is set to 0
- systemd-networkd did not enable forwarding
- Firewall rules blocking forwarded traffic""",
     """How to Fix:
```bash
# Enable IP forwarding
echo "net.ipv4.ip_forward = 1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Or enable in network config
sudo tee /etc/systemd/network/forwarding.network <<'EOF'
[Match]
Name=*

[Network]
IPForward=yes
EOF

sudo systemctl restart systemd-networkd
```"""),

    ("bridged-network-fail", "systemd bridged network fail",
     "Fix systemd bridged network fail. Resolve bridge network creation and configuration failures.",
     """br0: Failed to create bridge. Operation not supported.

The bridge interface could not be created.""",
     """Common Causes:
- Bridge kernel module is not loaded
- Insufficient privileges
- Interface is already a slave of another bridge
- Kernel does not support bridge functionality""",
     """How to Fix:
```bash
# Load bridge module
sudo modprobe bridge

# Create bridge via networkd
sudo tee /etc/systemd/network/20-br0.netdev <<'EOF'
[NetDev]
Name=br0
Kind=bridge
EOF

sudo systemctl restart systemd-networkd
```"""),

    ("wireguard-systemd-integration", "systemd WireGuard integration error",
     "Fix systemd WireGuard integration error. Resolve WireGuard tunnel issues with systemd-networkd.",
     """wg0: WireGuard tunnel failed to start. Interface not configured.

The WireGuard interface failed to initialize.""",
     """Common Causes:
- WireGuard kernel module not loaded
- Missing WireGuard configuration
- Private key is invalid or missing
- Peer configuration error""",
     """How to Fix:
```bash
# Load WireGuard module
sudo modprobe wireguard

# Check WireGuard status
sudo wg show

# Configure via systemd-networkd
sudo tee /etc/systemd/network/30-wg0.netdev <<'EOF'
[NetDev]
Name=wg0
Kind=wireguard

[WireGuard]
PrivateKey=<your-private-key>
ListenPort=51820

[WireGuardPeer]
PublicKey=<peer-public-key>
Endpoint=peer.example.com:51820
AllowedIPs=0.0.0.0/0
EOF

sudo systemctl restart systemd-networkd
```"""),

    ("nss-resolve-not-available", "systemd nss-resolve not available",
     "Fix systemd nss-resolve not available. Resolve name resolution failures when nss-resolve module is missing.",
     """Name lookup using nss-resolve failed. Module not found.

The nss_resolve module is not available for name resolution.""",
     """Common Causes:
- libnss_resolve is not installed
- /etc/nsswitch.conf does not include resolve
- systemd-resolved is not installed
- NSS configuration is incorrect""",
     """How to Fix:
```bash
# Install systemd-resolved
sudo apt install systemd-resolved

# Check nsswitch.conf
grep hosts /etc/nsswitch.conf

# Ensure resolve is in the hosts line
# hosts: files resolve dns

# Restart resolved
sudo systemctl restart systemd-resolved
```"""),

    ("resolved-stub-listener-conflict", "systemd resolved stub listener conflict",
     "Fix systemd resolved stub listener conflict. Resolve DNS listener port conflicts with systemd-resolved.",
     """systemd-resolved: Failed to listen on stub DNS listener: Address already in use

Another process is using port 53.""",
     """Common Causes:
- dnsmasq or another DNS server is using port 53
- Multiple instances of systemd-resolved
- dnsmasq is not stopped before enabling resolved""",
     """How to Fix:
```bash
# Find what is using port 53
sudo ss -ulnp | grep :53

# Stop conflicting DNS servers
sudo systemctl stop dnsmasq
sudo systemctl disable dnsmasq

# Enable and start resolved
sudo systemctl enable systemd-resolved
sudo systemctl start systemd-resolved
```"""),

    ("timesyncd-ntp-failure", "systemd timesyncd NTP failure",
     "Fix systemd timesyncd NTP failure. Resolve time synchronization failures with systemd-timesyncd.",
     """systemd-timesyncd.service: NTP synchronization failed. No server found.

The timesyncd daemon could not synchronize time.""",
     """Common Causes:
- NTP servers are not configured or unreachable
- Network is not available
- Firewall blocking NTP traffic (port 123)
- DNS resolution failing for NTP servers""",
     """How to Fix:
```bash
# Check timesyncd status
timedatectl status

# Configure NTP servers
sudo tee /etc/systemd/timesyncd.conf <<'EOF'
[Time]
NTP=0.pool.ntp.org 1.pool.ntp.org 2.pool.ntp.org
FallbackNTP=3.pool.ntp.org 4.pool.ntp.org
RootDistanceMaxSec=5
PollIntervalMinSec=32
PollIntervalMaxSec=2048
EOF

sudo systemctl restart systemd-timesyncd
timedatectl set-ntp true
```"""),

    # ── Category 11: Security/hardening errors ──
    ("protectsystem-conflict", "systemd ProtectSystem conflict",
     "Fix systemd ProtectSystem conflict. Resolve service startup failures caused by conflicting ProtectSystem directives.",
     """myapp.service: ProtectSystem=strict conflicts with writable paths.

The service cannot write to directories that are protected.""",
     """Common Causes:
- ProtectSystem=strict makes / and /usr read-only
- Application needs to write to protected directories
- ProtectSystem=full makes /etc and /usr read-only
- Conflicting with ExecStart paths""",
     """How to Fix:
```bash
# Use TemporaryFileSystem for writable paths
sudo systemctl edit myapp
```

```ini
[Service]
ProtectSystem=strict
ReadWritePaths=/var/lib/myapp /var/log/myapp
TemporaryFileSystem=/var/lib/myapp:ro
```"""),

    ("protecthome-not-found", "systemd ProtectHome not found",
     "Fix systemd ProtectHome not found. Resolve service failures when ProtectHome blocks access to /home.",
     """myapp.service: Cannot access /home. Protected by ProtectHome=yes.

The service is blocked from accessing /home.""",
     """Common Causes:
- ProtectHome=yes makes /home inaccessible
- Application needs to read from /home
- User files are in /home and service needs access""",
     """How to Fix:
```bash
# If the service needs access to /home
sudo systemctl edit myapp
```

```ini
[Service]
ProtectHome=no
# Or use specific paths:
# BindReadOnlyPaths=/home/myapp/config /home/myapp/config
```"""),

    ("private-tmp-not-writable", "systemd PrivateTmp not writable",
     "Fix systemd PrivateTmp not writable. Resolve service failures when /tmp is private and not writable.",
     """myapp.service: Cannot write to /tmp. PrivateTmp=yes may be preventing access.

The service cannot write to its private /tmp.""",
     """Common Causes:
- PrivateTmp=yes creates a private /tmp but with restricted permissions
- Application expects shared /tmp
- /tmp is full or has wrong permissions""",
     """How to Fix:
```bash
# Check private /tmp permissions
ls -la /tmp/private/myapp.service

# Or disable PrivateTmp
sudo systemctl edit myapp
```

```ini
[Service]
PrivateTmp=no
```"""),

    ("nonewprivileges-blocked", "systemd NoNewPrivileges blocked",
     "Fix systemd NoNewPrivileges blocked. Resolve service failures when NoNewPrivileges prevents privilege escalation.",
     """myapp.service: setuid() failed. NoNewPrivileges=yes is set.

The service cannot gain new privileges.""",
     """Common Causes:
- NoNewPrivileges=yes prevents setuid/setgid
- Application requires setuid binaries
- Sudo is not allowed within the service
- Kernel feature not supported""",
     """How to Fix:
```bash
# If the service legitimately needs new privileges
sudo systemctl edit myapp
```

```ini
[Service]
NoNewPrivileges=no
# Note: This reduces security. Only use if absolutely necessary.
```"""),

    ("capabilityboundingset-too-restrictive", "systemd CapabilityBoundingSet too restrictive",
     "Fix systemd CapabilityBoundingSet too restrictive. Resolve service failures when capabilities are stripped.",
     """myapp.service: Operation not permitted. Missing capability: CAP_NET_BIND_SERVICE.

The service lacks the required Linux capability.""",
     """Common Causes:
- CapabilityBoundingSet does not include needed capabilities
- Service needs to bind to privileged ports
- Service needs to change process priorities
- Too many capabilities were removed""",
     """How to Fix:
```bash
# Add required capabilities
sudo systemctl edit myapp
```

```ini
[Service]
CapabilityBoundingSet=CAP_NET_BIND_SERVICE CAP_SYS_ADMIN
AmbientCapabilities=CAP_NET_BIND_SERVICE
```"""),

    ("syscallfilter-blocked", "systemd SystemCallFilter blocked",
     "Fix systemd SystemCallFilter blocked. Resolve service failures when system calls are blocked.",
     """myapp.service: System call 'mount' blocked by SystemCallFilter.

The service tried to use a blocked system call.""",
     """Common Causes:
- SystemCallFilter=~@mount blocks mount-related calls
- Application requires blocked system calls
- Filter is too restrictive for the workload""",
     """How to Fix:
```bash
# Remove the restrictive filter
sudo systemctl edit myapp
```

```ini
[Service]
# Remove SystemCallFilter or use a less restrictive one
SystemCallFilter=@system-service
# Or whitelist specific calls:
# SystemCallFilter=~@mount
```"""),

    ("restrictaddressfamilies-too-strict", "systemd RestrictAddressFamilies too strict",
     "Fix systemd RestrictAddressFamilies too strict. Resolve networking failures when address families are restricted.",
     """myapp.service: socket() failed: EAFNOSUPPORT. Address family not allowed.

The service cannot create sockets of the required address family.""",
     """Common Causes:
- RestrictAddressFamilies does not include AF_INET
- Service needs AF_NETLINK for certain operations
- D-Bus requires AF_UNIX""",
     """How to Fix:
```bash
# Allow required address families
sudo systemctl edit myapp
```

```ini
[Service]
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX AF_NETLINK
```"""),

    ("protectkernelmodules-denied", "systemd ProtectKernelModules denied",
     "Fix systemd ProtectKernelModules denied. Resolve service failures when module loading is blocked.",
     """myapp.service: modprobe failed. ProtectKernelModules=yes prevents loading.

The service cannot load kernel modules.""",
     """Common Causes:
- ProtectKernelModules=yes blocks modprobe
- Application needs to load kernel modules
- Hardware drivers require module loading""",
     """How to Fix:
```bash
# Disable ProtectKernelModules if needed
sudo systemctl edit myapp
```

```ini
[Service]
ProtectKernelModules=no
```"""),

    ("memorydenywriteexecute-error", "systemd MemoryDenyWriteExecute error",
     "Fix systemd MemoryDenyWriteExecute error. Resolve JIT compilation and code generation failures.",
     """myapp.service: mmap(PROT_WRITE|PROT_EXEC) failed. MemoryDenyWriteExecute=yes blocks W^X.

The service cannot create writable-executable memory mappings.""",
     """Common Causes:
- MemoryDenyWriteExecute=yes prevents W^X pages
- JIT compilers (V8, LuaJIT) need executable memory
- JIT is used for dynamic code generation""",
     """How to Fix:
```bash
# Allow JIT compilation
sudo systemctl edit myapp
```

```ini
[Service]
MemoryDenyWriteExecute=no
```"""),

    ("lockpersonality-not-supported", "systemd LockPersonality not supported",
     "Fix systemd LockPersonality not supported. Resolve service failures on systems without personality locking.",
     """myapp.service: LockPersonality=yes is not supported on this kernel.

The kernel does not support the personality system call.""",
     """Common Causes:
- Kernel was compiled without CONFIG_EXPERT
- LockPersonality requires specific kernel support
- Container environment blocking the syscall""",
     """How to Fix:
```bash
# Remove LockPersonality if not needed
sudo systemctl edit myapp
```

```ini
[Service]
# Remove LockPersonality=yes
```"""),

    ("privatedevices-mount-fail", "systemd PrivateDevices mount fail",
     "Fix systemd PrivateDevices mount fail. Resolve service failures when /dev is private and causes mount issues.",
     """myapp.service: Failed to create private /dev. Mount failed.

The service cannot create its private /dev namespace.""",
     """Common Causes:
- PrivateDevices=yes requires root
- /devtmpfs is not available
- Container environment prevents mount namespace
- Insufficient kernel support""",
     """How to Fix:
```bash
# Check if the service runs as root
sudo systemctl edit myapp

# If root is required, ensure correct settings
```

```ini
[Service]
PrivateDevices=yes
# Or disable if not needed:
# PrivateDevices=no
```"""),

    ("protectcontrolgroups-error", "systemd ProtectControlGroups error",
     "Fix systemd ProtectControlGroups error. Resolve service failures when cgroup hierarchy access is blocked.",
     """myapp.service: Cannot access cgroup hierarchy. ProtectControlGroups=yes is set.

The service is blocked from accessing /sys/fs/cgroup.""",
     """Common Causes:
- ProtectControlGroups=yes makes cgroup filesystem read-only
- Application needs to create cgroups (e.g., container runtimes)
- Monitoring tools need cgroup access""",
     """How to Fix:
```bash
# Allow cgroup access if needed
sudo systemctl edit myapp
```

```ini
[Service]
ProtectControlGroups=no
# Or use specific paths:
# BindReadOnlyPaths=/sys/fs/cgroup /sys/fs/cgroup
```"""),

    # ── Category 12: User session errors ──
    ("systemd-user-failed", "systemd --user failed",
     "Fix systemd --user failed. Resolve user session manager failures.",
     """Failed to start user@1000.service: User session manager not starting.

The per-user systemd instance failed to start.""",
     """ Common Causes:
- XDG_RUNTIME_DIR is not set
- D-Bus session bus is not available
- User service directory does not exist
- systemd-logind is not running""",
     """How to Fix:
```bash
# Check user session
systemctl --user status

# Check logind
systemctl status systemd-logind

# Ensure XDG_RUNTIME_DIR is set
echo $XDG_RUNTIME_DIR

# Create runtime directory if missing
sudo mkdir -p /run/user/1000
sudo chown 1000:1000 /run/user/1000
```"""),

    ("user-service-not-started", "systemd user service not started",
     "Fix systemd user service not started. Resolve per-user service startup failures.",
     """myapp.service: User service failed to start. User session not active.

The user service could not start in the user session.""",
     """Common Causes:
- User has not logged in yet
- User service is not enabled
- Lingering is not enabled for the user
- systemd --user instance is not running""",
     """How to Fix:
```bash
# Enable lingering for the user
sudo loginctl enable-linger myuser

# Enable the user service
systemctl --user enable myapp

# Start it
systemctl --user start myapp

# Check status
systemctl --user status myapp
```"""),

    ("lingering-disabled", "systemd lingering disabled",
     "Fix systemd lingering disabled. Resolve user service failures when lingering is not enabled.",
     """User services cannot start without a login session. Lingering is disabled.

The user needs lingering enabled to run services without an active session.""",
     """Common Causes:
- Lingering is not enabled for the user
- User services need to run without a login session
- loginctl has not been configured for lingering""",
     """How to Fix:
```bash
# Enable lingering
sudo loginctl enable-linger myuser

# Verify
ls /var/lib/systemd/linger/
ls /var/lib/systemd/linger/myuser

# List lingering users
loginctl list-users
```"""),

    ("logind-session-error", "systemd-logind session error",
     "Fix systemd-logind session error. Resolve user session tracking and management issues.",
     """systemd-logind.service: Session tracking failed. Too many sessions.

The logind service cannot track additional sessions.""",
     """Common Causes:
- Too many concurrent sessions
- Session tracking limit reached
- logind configuration is too restrictive
- Resource exhaustion in logind""",
     """How to Fix:
```bash
# Check active sessions
loginctl list-sessions

# Kill stale sessions
loginctl kill-session <session-id>

# Configure limits
sudo tee /etc/systemd/logind.conf <<'EOF'
[Login]
KillUserProcesses=yes
HandleLidSwitch=suspend
StopIdleSessionSec=1800
EOF

sudo systemctl restart systemd-logind
```"""),

    ("xdg-runtime-dir-not-set", "systemd XDG_RUNTIME_DIR not set",
     "Fix systemd XDG_RUNTIME_DIR not set. Resolve user service failures when the runtime directory is missing.",
     """XDG_RUNTIME_DIR is not set. User services cannot start.

The XDG runtime directory environment variable is missing.""",
     """Common Causes:
- User session does not set XDG_RUNTIME_DIR
- Runtime directory was not created
- systemd-logind did not set up the session
- SSH session without X forwarding""",
     """How to Fix:
```bash
# Check if logind is running
systemctl status systemd-logind

# Manually set XDG_RUNTIME_DIR
export XDG_RUNTIME_DIR=/run/user/$(id -u)

# Ensure lingering is enabled
sudo loginctl enable-linger $USER

# Create the directory
sudo mkdir -p /run/user/$(id -u)
sudo chown $(id -u):$(id -u) /run/user/$(id -u)
```"""),

    ("dbus-connection-failed", "systemd D-Bus connection failed",
     "Fix systemd D-Bus connection failed. Resolve communication failures between services and systemd.",
     """Failed to connect to D-Bus system bus: Connection refused

The service cannot communicate with systemd via D-Bus.""",
     """Common Causes:
- D-Bus daemon is not running
- D-Bus socket is not accessible
- Service does not have D-Bus permissions
- D-Bus policy file is misconfigured""",
     """How to Fix:
```bash
# Check D-Bus status
systemctl status dbus

# Restart D-Bus
sudo systemctl restart dbus

# Check D-Bus socket
ls -la /run/dbus/system_bus_socket

# Verify D-Bus configuration
ls /etc/dbus-1/system.d/
```"""),

    ("user-manager-crashed", "systemd user manager crashed",
     "Fix systemd user manager crashed. Resolve per-user systemd instance crash and recovery.",
     """user@1000.service: User manager process crashed. Restarting.

The user-level systemd manager crashed unexpectedly.""",
     """Common Causes:
- A user service crashed the user manager
- Memory exhaustion in user session
- D-Bus connection lost
- Corrupted user state files""",
     """How to Fix:
```bash
# Check user service status
systemctl --user status

# Check user manager logs
journalctl --user -u myapp -n 50

# Reset user state
systemctl --user daemon-reexec

# Kill and restart user manager
systemctl --user stop myapp
systemctl --user start myapp
```"""),

    ("user-unit-not-found", "systemd user unit not found",
     "Fix systemd user unit not found. Resolve user service command failures when the unit does not exist.",
     """Failed to start myapp.service: Unit myapp.service not found for user.

The user-level unit does not exist.""",
     """Common Causes:
- User unit file was not installed in ~/.config/systemd/user/
- Unit file is in the wrong location
- Unit was deleted
- User service was not enabled""",
     """How to Fix:
```bash
# Check user unit files
ls ~/.config/systemd/user/

# Create the unit file
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/myapp.service <<'EOF'
[Unit]
Description=My User App

[Service]
ExecStart=/usr/bin/myapp

[Install]
WantedBy=default.target
EOF

# Reload and enable
systemctl --user daemon-reload
systemctl --user enable myapp
systemctl --user start myapp
```"""),

    ("user-session-scope", "systemd user session scope",
     "Fix systemd user session scope. Resolve user session scope issues affecting service management.",
     """Failed to create user session scope: No space for session

The user session scope could not be created.""",
     """Common Causes:
- Too many user sessions active
- System resource limits reached
- systemd-logind session tracking issue
- Memory limits for user slices reached""",
     """How to Fix:
```bash
# Check user slice resource usage
systemd-cgtop | grep user

# Increase user slice limits
sudo systemctl edit user-1000.slice
```

```ini
[Slice]
MemoryMax=4G
TasksMax=4096
```"""),

    ("systemd-logind-not-active", "systemd-logind not active",
     "Fix systemd-logind not active. Resolve user session management failures when logind is not running.",
     """systemd-logind.service: Service is not running.

The logind service that manages user sessions is not active.""",
     """Common Causes:
- logind was stopped or crashed
- D-Bus issues preventing logind startup
- Configuration error in logind.conf
- Missing dependencies for logind""",
     """How to Fix:
```bash
# Check logind status
systemctl status systemd-logind

# Start logind
sudo systemctl start systemd-logind

# Check logs
journalctl -u systemd-logind -n 50

# Fix configuration
sudo systemd-analyze verify systemd-logind
```"""),

    ("multi-seat-error", "systemd multi-seat error",
     "Fix systemd multi-seat error. Resolve multi-seat display and session management issues.",
     """systemd-logind: Failed to create seat seat0. Multi-seat not supported.

The system cannot set up multi-seat configuration.""",
     """Common Causes:
- Display hardware not recognized for seat assignment
- logind cannot enumerate displays
- Missing udev rules for seat assignment
- VT (virtual terminal) configuration issue""",
     """How to Fix:
```bash
# Check available seats
loginctl seat-status seat0

# List seats
loginctl list-seats

# Create custom seat assignment
sudo tee /etc/udev/rules.d/99-seat.rules <<'EOF'
ACTION=="add", KERNEL=="card0", TAG+="seat"
EOF

sudo udevadm control --reload-rules
```"""),

    ("user-slice-not-created", "systemd user slice not created",
     "Fix systemd user slice not created. Resolve user resource management failures when slices are missing.",
     """user-1000.slice: Slice not created. Resource limits not applied.

The user slice was not created by systemd-logind.""",
     """Common Causes:
- systemd-logind did not create the slice
- Slice configuration has errors
- Resource limits exceed system capabilities
- Missing kernel resource control support""",
     """How to Fix:
```bash
# Check if slice exists
systemctl status user-1000.slice

# Create the slice manually
sudo tee /etc/systemd/system/user-1000.slice <<'EOF'
[Unit]
Description=User Slice for UID 1000

[Slice]
CPUQuota=100%
MemoryMax=4G
TasksMax=4096

[Install]
WantedBy=slices.target
EOF

sudo systemctl daemon-reload
sudo systemctl start user-1000.slice
```"""),

    ("desktop-environment-integration", "systemd desktop environment integration error",
     "Fix systemd desktop environment integration error. Resolve issues where desktop environments fail to integrate with systemd.",
     """Failed to start display manager: systemd-user-sessions.target not reached.

The desktop environment cannot start due to systemd integration issues.""",
     """Common Causes:
- systemd-user-sessions.target is not activated
- Display manager does not depend on user sessions
- graphical.target dependencies are not met
- User session is not properly initialized""",
     """How to Fix:
```bash
# Check graphical target dependencies
systemctl list-dependencies graphical.target

# Ensure user sessions target is active
systemctl status systemd-user-sessions.target

# Check display manager
systemctl status gdm
systemctl status sddm

# Set graphical target as default
sudo systemctl set-default graphical.target
```"""),
]

def make_page(title, desc, body, causes, fix):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["systemd"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        'weight: 5',
        '---',
        '',
        f'# {title}',
        '',
        '## Error Description',
        '',
        body,
        '',
        '## Common Causes',
        '',
        causes,
        '',
        '## How to Fix',
        '',
        fix,
        '',
        '## Examples',
        '',
        '```bash',
        '# Check systemd version',
        'systemctl --version',
        '',
        '# Verify unit file syntax',
        'sudo systemd-analyze verify /etc/systemd/system/myapp.service',
        '',
        '# Analyze system boot',
        'systemd-analyze blame',
        '',
        '# List failed units',
        'systemctl --failed',
        '',
        '# View service logs',
        'journalctl -u myapp -n 50 --no-pager',
        '```',
    ]
    return '\n'.join(lines)

count = 0
skipped = 0
for slug, title, desc, body, causes, fix in PAGES:
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        skipped += 1
        continue
    content = make_page(title, desc, body, causes, fix)
    path = f"/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/systemd/{slug}.md"
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {skipped}")
print(f"Total pages defined: {len(PAGES)}")
