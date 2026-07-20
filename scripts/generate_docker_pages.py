#!/usr/bin/env python3
"""Generate new Docker error pages"""
import os, sys

EXISTING = {f.replace('.md', '') for f in os.listdir('/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/docker/') if f.endswith('.md')}

PAGES_DATA = [
    ("container-name-in-use", "Docker container name is already in use",
     "Fix 'container name already in use' error. Resolve Docker container naming conflicts when starting containers with duplicate names.",
     """docker: Error response from daemon: Conflict. The container name "/<name>" is already in use by container "<id>".

This error occurs when you try to create a container with a name that is already assigned to an existing container. Container names must be unique on a system."""),
    ("driver-failed-programming-connectivity", "Docker driver failed programming external connectivity",
     "Fix 'driver failed programming external connectivity' error. Resolve Docker network port mapping failures on container startup.",
     """docker: Error response from daemon: driver failed programming external connectivity on endpoint <name>".

This error occurs when Docker cannot set up the network port mapping for a container. Typically caused by port conflicts or iptables issues."""),
    ("mount-denied", "Docker mount denied error",
     "Fix 'mount denied' error. Resolve Docker volume mount failures due to permission or path issues.",
     """docker: Error response from daemon: Mount denied: The source path does not exist.

This error occurs when Docker cannot mount a host directory into a container. The source path may not exist or permissions are insufficient."""),
    ("unable-to-remove-container", "Docker unable to remove container",
     "Fix 'unable to remove container' error. Resolve Docker container removal failures for running or stuck containers.",
     """docker: Error response from daemon: You cannot remove a running container.

This error occurs when you try to remove a container that is currently running. Stop the container first before removing it."""),
    ("no-such-container", "Docker no such container error",
     "Fix 'No such container' error. Resolve Docker command failures when referencing a container that does not exist.",
     """Error: No such container: <name>

This error occurs when you reference a container name or ID that does not exist. The container may have been removed or the name is incorrect."""),
    ("no-such-image", "Docker no such image error",
     "Fix 'No such image' error. Resolve Docker command failures when referencing an image that does not exist locally.",
     """Error: No such image: <image>

This error occurs when Docker cannot find the specified image in the local image store. The image must be pulled or built first."""),
    ("no-such-network", "Docker no such network error",
     "Fix 'No such network' error. Resolve Docker network command failures when referencing a non-existent network.",
     """Error: No such network: <name>

This error occurs when you reference a Docker network that does not exist. Network names must match exactly."""),
    ("no-such-volume", "Docker no such volume error",
     "Fix 'No such volume' error. Resolve Docker volume command failures when referencing a non-existent volume.",
     """Error: No such volume: <name>

This error occurs when you reference a Docker volume that does not exist. The volume must be created first with `docker volume create`."""),
    ("unable-to-find-image", "Docker unable to find image",
     "Fix 'Unable to find image' error. Resolve Docker image pull failures when an image is not found locally or on the registry.",
     """Unable to find image '<image>:<tag>' locally

This error occurs when Docker cannot find the specified image locally and tries to pull it from the registry. If the pull also fails, the image does not exist."""),
    ("unable-to-stop-container", "Docker unable to stop container",
     "Fix 'unable to stop container' error. Resolve Docker container stop failures for unresponsive or stuck containers.",
     """Error response from daemon: cannot stop container: <name>

This error occurs when Docker cannot stop a container. The container process may be stuck or the container runtime may be in an inconsistent state."""),
    ("unable-to-start-container", "Docker unable to start container",
     "Fix 'unable to start container' error. Resolve Docker container start failures after creation or restart.",
     """Error response from daemon: Cannot start container <name>

This error occurs when Docker cannot start an existing container. The container may have configuration issues or host resource problems."""),
    ("unable-to-kill-container", "Docker unable to kill container",
     "Fix 'unable to kill container' error. Resolve Docker container kill failures for unresponsive processes.",
     """Error response from daemon: Cannot kill container <name>

This error occurs when Docker cannot send a kill signal to the container. The container process may be in an uninterruptible state."""),
    ("unable-to-restart-container", "Docker unable to restart container",
     "Fix 'unable to restart container' error. Resolve Docker container restart failures.",
     """Error response from daemon: Cannot restart container <name>

This error occurs when Docker cannot restart a container. This may be due to configuration issues, resource constraints, or runtime problems."""),
    ("unable-to-pause-container", "Docker unable to pause container",
     "Fix 'unable to pause container' error. Resolve Docker container pause failures.",
     """Error response from daemon: Cannot pause container <name>

This error occurs when Docker cannot pause the container processes. Not all container runtimes support the pause feature."""),
    ("unable-to-unpause-container", "Docker unable to unpause container",
     "Fix 'unable to unpause container' error. Resolve Docker container unpause failures.",
     """Error response from daemon: Cannot unpause container <name>

This error occurs when Docker cannot resume a paused container. The container may have been in an unexpected state when paused."""),
    ("unable-to-rename-container", "Docker unable to rename container",
     "Fix 'unable to rename container' error. Resolve Docker container rename failures.",
     """Error response from daemon: Cannot rename container <name>

This error occurs when Docker cannot rename a container. The new name may already be in use or the container may be in a state that prevents renaming."""),
    ("unable-to-inspect-object", "Docker unable to inspect object",
     "Fix 'unable to inspect' error. Resolve Docker inspect failures for containers, images, volumes, or networks.",
     """Error: No such object: <id>

This error occurs when `docker inspect` cannot find the specified Docker object. The container, image, volume, or network may not exist."""),
    ("denied-push-access", "Docker push denied access",
     "Fix 'denied: requested access to the resource is denied' error. Resolve Docker push authentication and permission failures.",
     """denied: requested access to the resource is denied

This error occurs when you try to push an image to a registry that you do not have permission to write to."""),
    ("unauthorized-push", "Docker push unauthorized",
     "Fix 'unauthorized: authentication required' error. Resolve Docker push failures when not logged in or token is invalid.",
     """unauthorized: authentication required

This error occurs when you try to push to a private registry without authentication or with invalid credentials."""),
    ("manifest-not-found", "Docker manifest not found",
     "Fix 'manifest not found' error. Resolve Docker pull failures when an image manifest does not exist in the registry.",
     """manifest for <image>:<tag> not found: manifest unknown

This error occurs when the specified image tag does not exist in the registry. The image may have been deleted or the tag is incorrect."""),
    ("repository-does-not-exist", "Docker repository does not exist",
     "Fix 'repository does not exist' error. Resolve Docker pull failures when the repository has been deleted or moved.",
     """Error response from daemon: repository <name> not found

This error occurs when the Docker image repository does not exist on the registry. The repository may have been deleted or the URL is incorrect."""),
    ("build-failed-to-solve", "Docker build failed to solve",
     "Fix 'failed to solve' error. Resolve Docker BuildKit solver failures during image builds.",
     """ERROR: failed to solve: <error>

This error occurs when Docker BuildKit cannot solve the build graph or execute a build step. The Dockerfile may contain errors or dependencies may be missing."""),
    ("build-failed-to-fetch-remote", "Docker build failed to fetch remote",
     "Fix 'failed to fetch remote' error. Resolve Docker build failures when downloading remote dependencies.",
     """ERROR: failed to fetch remote <url>

This error occurs when Docker BuildKit cannot download a remote resource (like a Git repository or tarball) specified in the Dockerfile."""),
    ("build-run-failed", "Docker build RUN command failed",
     "Fix 'RUN failed' error. Resolve Docker build failures when a RUN command in the Dockerfile exits with a non-zero status.",
     """ERROR: failed to solve: process "/bin/sh -c <command>" did not complete successfully: exit code: <n>

This error occurs when a RUN instruction in the Dockerfile fails. The command returned a non-zero exit code."""),
    ("build-cmd-failed", "Docker build CMD instruction error",
     "Fix 'CMD instruction error' in Docker build. Resolve Dockerfile CMD or ENTRYPOINT configuration issues.",
     """Error: docker: Error response from daemon: invalid CMD instruction.

This error occurs when the CMD instruction in the Dockerfile has an invalid format or references a missing executable."""),
    ("build-env-invalid", "Docker build ENV instruction error",
     "Fix 'ENV instruction error' in Docker build. Resolve Dockerfile environment variable syntax issues.",
     """Error: failed to parse Dockerfile: ENV must have two arguments

This error occurs when the ENV instruction in the Dockerfile has an incorrect format. ENV requires either KEY=VALUE pairs or KEY VALUE format."""),
    ("build-arg-missing", "Docker build ARG missing",
     "Fix 'ARG missing' error in Docker build. Resolve Dockerfile build argument issues when required ARGs are not provided.",
     """Error: missing build argument <name>

This error occurs when a Dockerfile uses an ARG that must be provided via `--build-arg` and no default value is set."""),
    ("build-workdir-error", "Docker build WORKDIR error",
     "Fix 'WORKDIR error' in Docker build. Resolve Dockerfile WORKDIR instruction failures.",
     """Error: WORKDIR cannot be empty

This error occurs when the WORKDIR instruction in the Dockerfile has an empty or invalid path."""),
    ("build-healthcheck-failed", "Docker build HEALTHCHECK instruction error",
     "Fix 'HEALTHCHECK instruction error' in Docker build. Resolve Dockerfile HEALTHCHECK configuration issues.",
     """Error: HEALTHCHECK requires at least one argument

This error occurs when the HEALTHCHECK instruction is missing required arguments like the test command."""),
    ("build-add-checksum-mismatch", "Docker build ADD checksum mismatch",
     "Fix 'ADD checksum mismatch' error. Resolve Docker build failures when downloaded file checksums do not match expected values.",
     """ERROR: failed to solve: failed to fetch: checksum mismatch

This error occurs when the ADD instruction downloads a file but the checksum does not match the expected value specified with `--checksum`."""),
    ("compose-service-not-found", "Docker Compose service not found",
     "Fix 'service not found' error in Docker Compose. Resolve compose file parsing issues when referencing undefined services.",
     """Service '<name>' not found in docker-compose.yml

This error occurs when a docker-compose command references a service that is not defined in the compose file."""),
    ("compose-depends-on-cycle", "Docker Compose dependency cycle",
     "Fix 'dependency cycle' error in Docker Compose. Resolve circular depends_on relationships between services.",
     """Error: dependency cycle detected in docker-compose.yml

This error occurs when services have circular dependencies through the `depends_on` configuration."""),
    ("compose-port-allocated", "Docker Compose port already allocated",
     "Fix 'port already allocated' error in Docker Compose. Resolve compose port conflicts when ports are already in use.",
     """Error: starting container: Ports are not available: listen tcp 0.0.0.0:8080: bind: address already in use

This error occurs when a port specified in the compose file is already in use on the host machine."""),
    ("compose-volume-in-use", "Docker Compose volume already in use",
     "Fix 'volume already in use' error in Docker Compose. Resolve volume conflicts between compose services.",
     """Error: error while mounting volume: volume is in use

This error occurs when a Docker volume specified in the compose file is already mounted by another container."""),
    ("compose-network-not-defined", "Docker Compose network not defined",
     "Fix 'network not defined' error in Docker Compose. Resolve compose file issues when referencing undefined networks.",
     """Network '<name>' not found in docker-compose.yml

This error occurs when a service references a network that is not defined in the `networks` section of the compose file."""),
    ("compose-env-missing", "Docker Compose environment variable missing",
     "Fix 'environment variable missing' error in Docker Compose. Resolve missing required env vars in compose configuration.",
     """Warning: <var> is not set, using default

This error occurs when a compose file references an environment variable from the host shell that is not set."""),
    ("compose-build-context-missing", "Docker Compose build context missing",
     "Fix 'build context missing' error in Docker Compose. Resolve compose build failures when the build directory does not exist.",
     """ERROR: build context directory '<path>' does not exist

This error occurs when the `build` context path in a compose service does not exist on the filesystem."""),
    ("compose-config-invalid", "Docker Compose config file invalid",
     "Fix 'config file invalid' error in Docker Compose. Resolve YAML syntax errors in docker-compose files.",
     """ERROR: yaml: line <n>: did not find expected key

This error occurs when the docker-compose.yml file has YAML syntax errors."""),
    ("compose-command-not-found", "Docker Compose command not found",
     "Fix 'command not found' error in Docker Compose. Resolve compose command execution failures inside containers.",
     """Error: <command> not found

This error occurs when the command specified in a compose service's `command` field does not exist in the container image."""),
    ("compose-restart-policy-invalid", "Docker Compose restart policy invalid",
     "Fix 'restart policy invalid' error in Docker Compose. Resolve compose restart configuration issues.",
     """Error: invalid restart policy '<policy>'

This error occurs when the `restart` policy in a compose file has an invalid value. Valid values: no, always, on-failure, unless-stopped."""),
    ("compose-healthcheck-timeout", "Docker Compose healthcheck timeout",
     "Fix 'healthcheck timeout' error in Docker Compose. Resolve compose health check timeout failures.",
     """Error: Health check exceeded timeout of <n> seconds

This error occurs when a container's health check command takes longer than the configured timeout."""),
    ("compose-scaling-error", "Docker Compose scaling error",
     "Fix 'scaling error' in Docker Compose. Resolve compose scale failures for services that cannot be replicated.",
     """Error: Cannot scale service '<name>': container name conflict

This error occurs when trying to scale a service that uses fixed container names or host ports."""),
    ("compose-network-driver-incompatible", "Docker Compose network driver incompatible",
     "Fix 'network driver incompatible' error in Docker Compose. Resolve compose network driver compatibility issues.",
     """Error: network driver '<driver>' is not supported

This error occurs when the compose file specifies a network driver that is not available on the current Docker host."""),
    ("compose-volume-driver-missing", "Docker Compose volume driver missing",
     "Fix 'volume driver missing' error in Docker Compose. Resolve compose volume driver plugin issues.",
     """Error: volume driver '<driver>' not found

This error occurs when a compose file specifies a volume driver plugin that is not installed."""),
    ("compose-secret-not-found", "Docker Compose secret not found",
     "Fix 'secret not found' error in Docker Compose. Resolve compose secret reference issues.",
     """Error: secret '<name>' not found

This error occurs when a service references a secret that is not defined in the `secrets` section of the compose file."""),
    ("swarm-node-not-found", "Docker Swarm node not found",
     "Fix 'node not found' error in Docker Swarm. Resolve swarm node lookup failures.",
     """Error: node <name> not found

This error occurs when a Docker Swarm command references a node that is not part of the swarm cluster."""),
    ("swarm-service-not-found", "Docker Swarm service not found",
     "Fix 'service not found' error in Docker Swarm. Resolve swarm service lookup failures.",
     """Error: service <name> not found

This error occurs when a Docker Swarm service command references a service that does not exist in the swarm."""),
    ("swarm-task-failed", "Docker Swarm task failed",
     "Fix 'task failed' error in Docker Swarm. Resolve swarm task execution failures.",
     """Error: task for service <name> failed

This error occurs when a swarm task cannot start or exits with an error."""),
    ("swarm-leader-election-failed", "Docker Swarm leader election failed",
     "Fix 'leader election failed' error in Docker Swarm. Resolve swarm manager leader election issues.",
     """Error: leader election failed

This error occurs when the swarm manager nodes cannot elect a leader. This usually indicates a networking or consensus issue."""),
    ("swarm-join-token-invalid", "Docker Swarm join token invalid",
     "Fix 'join token invalid' error in Docker Swarm. Resolve swarm node join failures.",
     """Error: join token is invalid

This error occurs when attempting to join a swarm node with an incorrect or expired join token."""),
    ("swarm-node-already-part", "Docker Swarm node already part of swarm",
     "Fix 'node already part of swarm' error. Resolve swarm node join failures when the node is already in a cluster.",
     """Error: This node is already part of a swarm

This error occurs when trying to join a node to a swarm that is already part of a cluster."""),
    ("swarm-node-is-down", "Docker Swarm node is down",
     "Fix 'node is down' error in Docker Swarm. Resolve swarm operations on unreachable nodes.",
     """Error: node <name> is down

This error occurs when attempting to operate on a swarm node that is unreachable or has stopped communicating."""),
    ("swarm-node-is-draining", "Docker Swarm node is draining",
     "Fix 'node is draining' error in Docker Swarm. Resolve swarm operations on nodes in drain state.",
     """Error: node <name> is draining

This error occurs when trying to schedule tasks on a swarm node that is in the draining state."""),
    ("swarm-service-scale-failed", "Docker Swarm service scale failed",
     "Fix 'scale failed' error in Docker Swarm. Resolve swarm service scaling failures.",
     """Error: service <name> scale failed: resource constraints

This error occurs when swarm cannot scale a service to the desired number of replicas due to resource limits."""),
    ("swarm-service-update-failed", "Docker Swarm service update failed",
     "Fix 'service update failed' error in Docker Swarm. Resolve swarm service update failures.",
     """Error: service <name> update failed

This error occurs when a swarm service update cannot be applied. The new configuration may be invalid or resources unavailable."""),
    ("swarm-network-attach-failed", "Docker Swarm network attach failed",
     "Fix 'network attach failed' error in Docker Swarm. Resolve swarm service network attachment failures.",
     """Error: network <name> attach failed

This error occurs when a swarm service cannot attach to an overlay network."""),
    ("swarm-lock-unavailable", "Docker Swarm lock unavailable",
     "Fix 'lock unavailable' error in Docker Swarm. Resolve swarm locking and autolock issues.",
     """Error: swarm is locked, use --unlock to unlock

This error occurs when attempting to manage a locked swarm without providing the unlock key."""),
    ("volume-create-failed", "Docker volume create failed",
     "Fix 'volume create failed' error. Resolve Docker volume creation failures.",
     """Error: create <volume>: volume create failed

This error occurs when Docker cannot create a volume. The driver may not be available or the filesystem may have issues."""),
    ("volume-remove-failed", "Docker volume remove failed",
     "Fix 'volume remove failed' error. Resolve Docker volume removal failures.",
     """Error: remove <volume>: volume is in use

This error occurs when trying to remove a Docker volume that is still in use by one or more containers."""),
    ("volume-driver-not-available", "Docker volume driver not available",
     "Fix 'volume driver not available' error. Resolve Docker volume driver plugin issues.",
     """Error: driver <driver> not available

This error occurs when the volume driver plugin specified for a volume is not installed or not responding."""),
    ("volume-nfs-mount-failed", "Docker NFS volume mount failed",
     "Fix 'NFS volume mount failed' error. Resolve Docker NFS volume mounting issues.",
     """Error: mount.NFS: connection timed out

This error occurs when Docker cannot mount an NFS volume. The NFS server may be unreachable or the export path may be incorrect."""),
    ("volume-bind-mount-missing", "Docker bind mount source missing",
     "Fix 'bind mount source missing' error. Resolve Docker bind mount failures when the host path does not exist.",
     """docker: Error response from daemon: invalid mount config: bind source path does not exist

This error occurs when the host path specified in a bind mount does not exist."""),
    ("volume-tmpfs-size-exceeded", "Docker tmpfs size exceeded",
     "Fix 'tmpfs size exceeded' error. Resolve Docker tmpfs mount size limit issues.",
     """Error: tmpfs: size limit exceeded

This error occurs when a tmpfs mount in a container exceeds the configured size limit."""),
    ("network-create-failed", "Docker network create failed",
     "Fix 'network create failed' error. Resolve Docker network creation failures.",
     """Error response from daemon: network create failed

This error occurs when Docker cannot create a network. The network driver may not be available or the configuration may be invalid."""),
    ("network-remove-failed", "Docker network remove failed",
     "Fix 'network remove failed' error. Resolve Docker network removal failures.",
     """Error response from daemon: network <name> is in use

This error occurs when trying to remove a Docker network that has active endpoints or containers attached."""),
    ("network-connect-failed", "Docker network connect failed",
     "Fix 'network connect failed' error. Resolve Docker container network connection failures.",
     """Error response from daemon: cannot connect container to network

This error occurs when Docker cannot connect a container to a network."""),
    ("network-disconnect-failed", "Docker network disconnect failed",
     "Fix 'network disconnect failed' error. Resolve Docker container network disconnection failures.",
     """Error response from daemon: cannot disconnect container from network

This error occurs when Docker cannot disconnect a container from a network."""),
    ("network-port-mapping-failed", "Docker port mapping failed",
     "Fix 'port mapping failed' error. Resolve Docker network port mapping and publishing issues.",
     """Error response from daemon: driver failed programming external connectivity

This error occurs when Docker cannot set up port forwarding between the host and container."""),
    ("network-bridge-creation-failed", "Docker bridge network creation failed",
     "Fix 'bridge creation failed' error. Resolve Docker default bridge network issues.",
     """Error: failed to create bridge network

This error occurs when Docker cannot create the default bridge network. This may be due to iptables or kernel module issues."""),
    ("network-overlay-failed", "Docker overlay network creation failed",
     "Fix 'overlay network creation failed' error. Resolve Docker Swarm overlay network issues.",
     """Error: failed to create overlay network

This error occurs when Docker cannot create an overlay network for swarm services."""),
    ("system-disk-space-low", "Docker system disk space low",
     "Fix 'disk space low' error. Resolve Docker storage exhaustion issues impacting container operations.",
     """Error: write /var/lib/docker/overlay2/<id>: no space left on device

This error occurs when the Docker storage directory runs out of disk space. Containers cannot write data."""),
    ("system-prune-failed", "Docker system prune failed",
     "Fix 'docker system prune failed' error. Resolve Docker cleanup failures when removing unused resources.",
     """Error: docker system prune failed

This error occurs when Docker cannot complete a prune operation. Resources may be in use or locked."""),
    ("system-df-error", "Docker system df error",
     "Fix 'docker system df' error. Resolve Docker disk usage reporting failures.",
     """Error: docker system df failed

This error occurs when Docker cannot report disk usage statistics. The storage driver may be in an inconsistent state."""),
    ("context-use-failed", "Docker context use failed",
     "Fix 'context use failed' error. Resolve Docker context switching issues.",
     """Error: context <name> not found

This error occurs when you try to switch to a Docker context that does not exist."""),
    ("context-create-failed", "Docker context create failed",
     "Fix 'context create failed' error. Resolve Docker context creation issues.",
     """Error: context create failed

This error occurs when Docker cannot create a new context. The context description may be invalid."""),
    ("context-remove-failed", "Docker context remove failed",
     "Fix 'context remove failed' error. Resolve Docker context removal issues.",
     """Error: context <name> is in use

This error occurs when trying to remove a Docker context that is currently active."""),
    ("container-exit-code-nonzero", "Docker container exit code non-zero",
     "Fix 'container exit code non-zero' error. Debug Docker containers that exit with error codes.",
     """docker: Error response from daemon: container <name> exited with code <n>

This error occurs when the main process inside a container exits with a non-zero exit code, indicating a failure."""),
    ("dockerfile-missing", "Docker Dockerfile missing error",
     "Fix 'Dockerfile missing' error. Resolve Docker build failures when the Dockerfile is not found.",
     """docker: Error response from daemon: Dockerfile not found

This error occurs when `docker build` cannot find a Dockerfile in the build context."""),
    ("layer-cache-miss", "Docker build layer cache miss",
     "Fix Docker build cache miss issues. Optimize Docker layer caching for faster builds.",
     """CACHED [n/n] RUN <command> (cache miss, skipping)

This warning occurs when Docker cannot use cached layers because the build context or Dockerfile instructions have changed."""),
    ("timeout-pulling-image", "Docker timeout pulling image",
     "Fix 'timeout pulling image' error. Resolve Docker pull failures when image download times out.",
     """Error response from daemon: Get <url>: net/http: TLS handshake timeout

This error occurs when a Docker image pull takes longer than the configured timeout."""),
    ("unknown-blob", "Docker unknown blob error",
     "Fix 'unknown blob' error. Resolve Docker registry layer download failures.",
     """Error: unknown blob

This error occurs when Docker tries to download a layer that does not exist in the registry. The image may be corrupted."""),
    ("read-stdin-error", "Docker read from stdin error",
     "Fix 'read from stdin' error. Resolve Docker build issues when reading Dockerfiles from standard input.",
     """Error: docker: failed to read from stdin

This error occurs when Docker cannot read the build context from stdin."""),
    ("exec-format-error-v2", "Docker exec format error",
     "Fix 'exec format error' in Docker. Resolve executable format issues when running commands in containers.",
     """docker: Error response from daemon: OCI runtime create failed: exec: executable file not found in $PATH

This error occurs when the command you try to execute in a container does not exist or has the wrong architecture."""),
    ("credentials-store-not-found", "Docker credential store not found",
     "Fix 'credential store not found' error. Resolve Docker login failures when the configured credential helper is missing.",
     """Error: error getting credentials - err: executable <helper> not found

This error occurs when Docker is configured to use a credential helper that is not installed."""),
    ("login-credentials-error", "Docker login credentials error",
     "Fix 'credentials error' during Docker login. Resolve Docker registry authentication failures.",
     """Error: Cannot perform an interactive login from a non TTY device

This error occurs when trying to run `docker login` in a non-interactive environment without providing credentials via stdin."""),
    ("image-layer-not-found", "Docker image layer not found",
     "Fix 'image layer not found' error. Resolve Docker image download failures for specific layers.",
     """Error: layer not found

This error occurs when a specific layer of a Docker image is not available in the registry."""),
    ("tag-invalid-format", "Docker tag invalid format",
     "Fix 'invalid tag format' error. Resolve Docker image tagging failures.",
     """Error: invalid reference format: repository name must be lowercase

This error occurs when the image tag or repository name has an invalid format."""),
    ("export-container-failed", "Docker export container failed",
     "Fix 'docker export failed' error. Resolve container filesystem export failures.",
     """Error: cannot export container <name>

This error occurs when Docker cannot export a container's filesystem. The container may be in a state that prevents export."""),
    ("import-image-failed", "Docker import image failed",
     "Fix 'docker import failed' error. Resolve Docker image import failures from tarballs.",
     """Error: cannot import from archive

This error occurs when Docker cannot import an image from a tarball. The archive may be corrupted."""),
    ("compose-service-image-missing", "Docker Compose service image missing",
     "Fix 'image missing' error in Docker Compose. Resolve compose service failures when the specified image cannot be pulled.",
     """Error: image <name> not found

This error occurs when a compose service specifies an image that does not exist or cannot be pulled."""),
    ("compose-volume-config-invalid", "Docker Compose volume config invalid",
     "Fix 'invalid volume config' error in Docker Compose. Resolve compose volume configuration syntax errors.",
     """Error: volumes configuration is invalid

This error occurs when the volumes section of a compose file has invalid syntax or missing required fields."""),
    ("compose-profiles-error", "Docker Compose profiles error",
     "Fix 'profiles error' in Docker Compose. Resolve compose service profile matching issues.",
     """Error: service <name> has no matching profile

This error occurs when a compose command does not activate the profiles needed by certain services."""),
    ("compose-include-error", "Docker Compose include error",
     "Fix 'include error' in Docker Compose. Resolve issues when including external compose files.",
     """Error: include: file <path> not found

This error occurs when a compose file's `include` directive references a file that does not exist."""),
    ("compose-watch-error", "Docker Compose watch error",
     "Fix 'watch error' in Docker Compose. Resolve compose file watching and hot-reload issues.",
     """Error: watch: <path> is not a valid watched path

This error occurs when a compose `develop` watch configuration references a non-existent path."""),
    ("build-secrets-error", "Docker build secrets error",
     "Fix 'build secrets error' in Docker. Resolve Docker BuildKit secret mounting issues.",
     """ERROR: failed to solve: secret <name> not found

This error occurs when a Dockerfile references a build secret that is not provided via `--secret`."""),
    ("build-ssh-forward-error", "Docker build SSH forwarding error",
     "Fix 'SSH forwarding error' in Docker build. Resolve Docker BuildKit SSH agent forwarding issues.",
     """ERROR: failed to solve: ssh key not found

This error occurs when a Dockerfile references an SSH mount but the SSH agent does not have the required key."""),
    ("build-cache-import-error", "Docker build cache import error",
     "Fix 'cache import error' in Docker build. Resolve BuildKit cache import failures.",
     """ERROR: failed to solve: cache import from <ref> failed

This error occurs when Docker BuildKit cannot import a cache from an external source."""),
    ("build-cache-export-error", "Docker build cache export error",
     "Fix 'cache export error' in Docker build. Resolve BuildKit cache export failures.",
     """ERROR: failed to solve: cache export failed

This error occurs when Docker BuildKit cannot export the build cache to the specified destination."""),
    ("compose-build-secrets-error", "Docker Compose build secrets error",
     "Fix 'build secrets error' in Docker Compose. Resolve compose file build secret configuration issues.",
     """Error: secret <name>: file not found

This error occurs when a build secret specified in a compose file references a file that does not exist."""),
    ("compose-depends-on-condition-error", "Docker Compose depends_on condition error",
     "Fix 'depends_on condition error' in Docker Compose. Resolve compose service dependency condition issues.",
     """Error: depends_on condition <condition> is not valid

This error occurs when the `condition` field under `depends_on` has an invalid value."""),
    ("compose-container-name-error", "Docker Compose container name conflict",
     "Fix 'container name conflict' error in Docker Compose. Resolve compose naming collisions.",
     """Error: container name already in use

This error occurs when a compose service's `container_name` conflicts with an existing container."""),
    ("compose-blobless-error", "Docker Compose blobless build error",
     "Fix 'blobless build error' in Docker Compose. Resolve compose build issues in CI environments.",
     """Error: failed to solve: blob mounted from <image> not found

This error occurs when BuildKit tries to mount a blob from an image that is not available."""),
    ("comze-platform-error", "Docker Compose platform error",
     "Fix 'platform error' in Docker Compose. Resolve compose multi-platform build and run issues.",
     """Error: image with platform <platform> not found

This error occurs when a compose file specifies a platform that is not available for the image."""),
    ("build-unknown-instruction", "Docker build unknown instruction",
     "Fix 'unknown instruction' error in Docker build. Resolve Dockerfile parsing errors.",
     """Error: Dockerfile parse error: unknown instruction: <cmd>

This error occurs when the Dockerfile contains an instruction that Docker does not recognize."""),
    ("build-syntax-error", "Docker build syntax error",
     "Fix 'syntax error' in Docker build. Resolve Dockerfile syntax parsing errors.",
     """Error: Dockerfile parse error at line <n>: syntax error

This error occurs when the Dockerfile has a syntax error that prevents parsing."""),
    ("compose-interpolation-error", "Docker Compose interpolation error",
     "Fix 'interpolation error' in Docker Compose. Resolve compose variable substitution issues.",
     """Error: invalid interpolation format for <key>

This error occurs when a compose file uses invalid syntax for variable interpolation."""),
    ("compose-extends-error", "Docker Compose extends error",
     "Fix 'extends error' in Docker Compose. Resolve compose service inheritance issues.",
     """Error: service <name> extends service <base> which is not defined

This error occurs when a service uses `extends` to inherit from a service that does not exist."""),
    ("compose-merge-error", "Docker Compose merge error",
     "Fix 'merge error' in Docker Compose. Resolve compose YAML merge tag issues.",
     """Error: cannot merge <key> and <key>

This error occurs when a compose file has conflicting keys that cannot be merged."""),
    ("compose-cpu-limit-error", "Docker Compose CPU limit error",
     "Fix 'CPU limit error' in Docker Compose. Resolve compose resource limit configuration issues.",
     """Error: invalid CPU limit: <value>

This error occurs when the CPU limit specified in a compose file has an invalid format."""),
    ("compose-memory-limit-error", "Docker Compose memory limit error",
     "Fix 'memory limit error' in Docker Compose. Resolve compose memory reservation configuration issues.",
     """Error: invalid memory limit: <value>

This error occurs when the memory limit specified in a compose file has an invalid value."""),
    ("compose-deploy-mode-error", "Docker Compose deploy mode error",
     "Fix 'deploy mode error' in Docker Compose. Resolve compose deploy section configuration issues.",
     """Error: deploy mode <mode> is not supported

This error occurs when the deploy mode in a compose file is not supported by the current Docker version."""),
    ("compose-reservation-error", "Docker Compose reservation error",
     "Fix 'reservation error' in Docker Compose. Resolve compose resource reservation configuration issues.",
     """Error: resource reservation cannot be greater than limit

This error occurs when resource reservations exceed the configured limits."""),
    ("build-dockerignore-error", "Docker build .dockerignore error",
     "Fix '.dockerignore error' in Docker build. Resolve issues where .dockerignore patterns exclude required files.",
     """COPY failed: file not found in build context

This error occurs when .dockerignore patterns exclude files needed for the build."""),
    ("build-context-error", "Docker build context error",
     "Fix 'build context error' in Docker. Resolve Docker build context path and loading issues.",
     """Error: docker: build context is too large

This error occurs when the Docker build context directory is too large, causing slow builds or timeouts."""),
    ("compose-rollback-error", "Docker Compose rollback error",
     "Fix 'rollback error' in Docker Compose. Resolve compose deployment rollback failures.",
     """Error: rollback of service <name> failed

This error occurs when rolling back a compose service deployment fails."""),
    ("compose-config-override-error", "Docker Compose config override error",
     "Fix 'config override error' in Docker Compose. Resolve compose multi-file override issues.",
     """Error: cannot override <key> with incompatible type

This error occurs when multiple compose files try to override a field with incompatible types."""),
    ("network-ipam-error", "Docker network IPAM error",
     "Fix 'IPAM error' in Docker networks. Resolve Docker IP address management issues.",
     """Error: pool <subnet> is too small

This error occurs when the IP address pool for a Docker network is too small for the required endpoints."""),
    ("swarm-secret-creation-failed", "Docker Swarm secret creation failed",
     "Fix 'secret creation failed' error in Docker Swarm. Resolve swarm secret creation issues.",
     """Error: secret <name> creation failed

This error occurs when Docker Swarm cannot create a secret. The secret data may be too large or the swarm is locked."""),
    ("compose-annotations-error", "Docker Compose annotations error",
     "Fix 'annotations error' in Docker Compose. Resolve compose annotations configuration issues.",
     """Error: annotation <key> has invalid format

This error occurs when a compose file annotation has invalid syntax."""),
]

# Build page content from template
def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["docker"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        'weight: 5',
        '---',
        '',
        f'# {title}',
        '',
        body,
        '',
        '## How to Fix',
        '',
        '### Check Docker Status',
        '',
        '```bash',
        'docker info',
        'docker system df',
        '```',
        '',
        '### View Logs',
        '',
        '```bash',
        'docker logs <container>',
        'docker events --since 5m',
        '```',
        '',
        '### Restart Docker',
        '',
        '```bash',
        'sudo systemctl restart docker',
        '```',
        '',
        '## Related Errors',
        '',
        '- [Container Not Running]({{< relref "/tools/docker/container-is-not-running" >}}) — container stopped',
        '- [Image Not Found]({{< relref "/tools/docker/docker-image-not-found" >}}) — image missing',
        '',
    ]
    return '\n'.join(lines)

count = 0
for slug, title, desc, body in PAGES_DATA:
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        continue
    content = make_page(title, desc, body)
    path = f"/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/docker/{slug}.md"
    with open(path, 'w') as f:
        f.write(content)
    count += 1
    print(f"CREATED: {slug}")

print(f"\nTotal created: {count}")
print(f"Total skipped (existing): {len(PAGES_DATA) - count}")
