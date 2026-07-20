#!/usr/bin/env python3
"""Generate 150+ Kubernetes error pages"""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/kubernetes'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["kubernetes"]',
        'error-types: ["scheduling-error", "pod-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
        '',
        '## Related Errors',
        '',
        '- [CrashLoopBackOff]({{< relref "/tools/kubernetes/crash-loop-back-off" >}})',
        '- [ImagePullBackOff]({{< relref "/tools/kubernetes/image-pull-back-off" >}})',
        '- [FailedScheduling]({{< relref "/tools/kubernetes/failed-scheduling" >}})',
    ]
    return '\n'.join(lines)

PAGES = [
    # ===== POD LIFECYCLE ERRORS =====
    ("image-pull-back-off", "ImagePullBackOff",
     "Fix Kubernetes ImagePullBackOff error. Resolve pod startup failures when the kubelet cannot pull the container image from the registry.",
     """## ImagePullBackOff

This error occurs when the kubelet cannot pull the container image for a pod. Kubernetes retries the pull with exponential backoff (BackOff), and the pod enters ImagePullBackOff while waiting.

### Common Causes

- Image name or tag is incorrect
- Image does not exist in the registry
- Registry requires authentication but no credentials are configured
- Network issues preventing access to the registry
- Image pull rate limits exceeded (Docker Hub, etc.)

### How to Fix

Verify the image name:
```bash
kubectl describe pod <pod-name> | grep -A5 "Failed to pull image"
```

Check the exact error:
```bash
kubectl get events --field-selector involvedObject.name=<pod-name>
```

Set image pull secrets:
```bash
kubectl create secret docker-registry regcred \\
  --docker-server=<registry> \\
  --docker-username=<user> \\
  --docker-password=<pass>
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"regcred"}]}'
```

### Examples

```bash
# Check which image is failing
kubectl describe pod my-app-7d4f9c7b6-abcde | grep -i "Failed to pull image"
#  Failed to pull image "my-app:latest": rpc error: code = NotFound

# Fix typo in deployment
kubectl set image deployment/my-app my-app=my-app:v1.0.0
```"""),

    ("err-image-pull", "ErrImagePull",
     "Fix Kubernetes ErrImagePull error. Resolve pod failures when the kubelet encounters an error pulling the container image.",
     """## ErrImagePull

This error occurs when the kubelet encounters an error while trying to pull the container image. Unlike ImagePullBackOff, this is a non-retriable error that requires immediate intervention.

### Common Causes

- Image repository does not exist
- Image tag is invalid
- Registry returned an error (permission denied, not found)
- Network timeout or DNS resolution failure
- Invalid image reference format

### How to Fix

Check the exact error message:
```bash
kubectl describe pod <pod-name> | grep -i "Error"
```

Use a fully qualified image reference:
```yaml
image: docker.io/library/nginx:1.25
```

Pull the image manually on a node:
```bash
crictl pull nginx:1.25
```

### Examples

```bash
# Common error: image doesn't exist
kubectl describe pod test-pod
#  Failed to pull image "nonexistent:v999": rpc error: code = NotFound

# Fix by correcting the image name
kubectl set image deployment/my-app my-app=nginx:1.25
```"""),

    ("crash-loop-back-off", "CrashLoopBackOff",
     "Fix Kubernetes CrashLoopBackOff error. Resolve pods that repeatedly crash and restart in an infinite loop.",
     """## CrashLoopBackOff

This error occurs when a pod crashes immediately after starting, and Kubernetes repeatedly restarts it. After each crash, the backoff delay increases exponentially (10s, 20s, 40s, 80s, up to 5 minutes).

### Common Causes

- Application error or unhandled exception in the container
- Missing environment variables or configuration
- Liveness probe failing and killing the container
- Resource limits too low (OOMKilled)
- Incorrect command or entrypoint
- Dependency service not available (database, API)

### How to Fix

View container logs (previous instance):
```bash
kubectl logs <pod-name> --previous
```

Check the exit code:
```bash
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[0].state.terminated.exitCode}'
```

Check resource limits:
```bash
kubectl describe pod <pod-name> | grep -A5 Limits
```

Check liveness probe:
```bash
kubectl describe pod <pod-name> | grep -A10 Liveness
```

### Examples

```bash
# View logs of crashed container
kubectl logs my-app-7d4f9c7b6-abcde --previous --tail=50

# Increase memory limit
kubectl set resources deployment/my-app --limits=memory=512Mi
```"""),

    ("oom-killed", "OOMKilled (Exit Code 137)",
     "Fix Kubernetes OOMKilled error. Resolve pods terminated for exceeding memory limits with exit code 137 (SIGKILL).",
     """## OOMKilled (Exit Code 137)

This error occurs when a container exceeds its memory limit and is killed by the Out-Of-Memory (OOM) killer. The exit code 137 (128 + 9 = SIGKILL) indicates the process was forcefully terminated.

### Common Causes

- Memory limit is set too low for the application
- Memory leak in the application
- Traffic spike causing higher memory usage
- Pod running on a node with insufficient memory
- No memory limits set (can be killed under node pressure)

### How to Fix

Check the termination reason:
```bash
kubectl describe pod <pod-name> | grep -i "OOM"
```

Check memory usage:
```bash
kubectl top pod <pod-name>
```

Increase memory limit:
```bash
kubectl set resources deployment/my-app --limits=memory=1Gi
```

### Examples

```bash
# Check if pod was OOMKilled
kubectl get pod my-app-7d4f9c7b6-abcde -o jsonpath='{.status.containerStatuses[0].state.terminated.reason}'
# OOMKilled

# Increase memory
kubectl set resources deployment/my-app --requests=memory=256Mi --limits=memory=512Mi
```"""),

    ("run-container-error", "RunContainerError",
     "Fix Kubernetes RunContainerError. Resolve pod failures when the container runtime cannot start the container after the image is pulled.",
     """## RunContainerError

This error occurs when the container runtime (containerd, CRI-O) cannot start the container after the image has been successfully pulled. The container fails before the application process begins.

### Common Causes

- Container command or entrypoint not found or invalid
- Working directory does not exist in the container
- Volume mount points to a non-existent or invalid path
- Container runtime configuration issue
- Invalid container permissions or security context

### How to Fix

Check the error description:
```bash
kubectl describe pod <pod-name> | grep -A10 "RunContainerError"
```

Verify the container command exists in the image:
```bash
kubectl run test --image=<image> -- ls /app/start.sh
```

Check volume mounts and paths:
```bash
kubectl describe pod <pod-name> | grep -A5 Mounts
```

### Examples

```bash
# Check exact error
kubectl describe pod my-app | grep -A5 "RunContainerError"
#  Error: container command '/app/start.sh' not found

# Fix by correcting command in deployment
kubectl edit deployment my-app
# Change command or entrypoint to match the image
```"""),

    ("container-creating", "ContainerCreating (Stuck)",
     "Fix Kubernetes pods stuck in ContainerCreating state. Resolve issues when pods remain in ContainerCreating status during startup.",
     """## ContainerCreating (Stuck)

This state means the pod has been scheduled to a node but the kubelet is still creating the container. While this is normal during startup, being stuck in this state for minutes indicates an underlying issue.

### Common Causes

- Image pull is slow (large image, slow registry, rate limited)
- Volume mount is pending (PVC not bound, NFS unreachable)
- Node resource pressure (CPU, memory, disk)
- Storage provisioning is slow (CSI driver, cloud volume attach)
- Network plugin (CNI) setup delays

### How to Fix

Check pod events:
```bash
kubectl describe pod <pod-name>
```

Check PVC binding:
```bash
kubectl get pvc
kubectl get pv
```

Check node conditions:
```bash
kubectl describe node <node-name>
```

### Examples

```bash
# Wait for pod with timeout
kubectl wait --for=condition=Ready pod/<pod-name> --timeout=300s

# Check pending PVC
kubectl get pvc
# my-claim    Pending
# Fix: ensure StorageClass exists and can provision volumes
```"""),

    ("init-error", "Init:Error",
     "Fix Kubernetes Init:Error. Resolve pod initialization container failures during startup.",
     """## Init:Error

This error occurs when an init container in the pod fails to complete successfully. Init containers run before application containers and must finish successfully for the pod to start.

### Common Causes

- Init container command or script fails
- Missing dependencies or configuration in init container
- Network connectivity issues during init
- Volume mount permissions in init container
- Resource limits too low for init container

### How to Fix

Check init container logs:
```bash
kubectl logs <pod-name> -c <init-container-name>
```

Check init container exit code:
```bash
kubectl get pod <pod-name> -o jsonpath='{.status.initContainerStatuses[0].state.terminated.exitCode}'
```

### Examples

```bash
# View init container logs
kubectl logs my-app-7d4f9c7b6-abcde -c init-mydb

# Check init status
kubectl get pod my-app -o wide
# my-app   0/1   Init:Error   0   2m
```"""),

    ("create-container-config-error", "CreateContainerConfigError",
     "Fix Kubernetes CreateContainerConfigError. Resolve pod failures when container configuration references ConfigMaps or Secrets that are missing.",
     """## CreateContainerConfigError

This error occurs when the kubelet cannot create the container because required configuration references do not exist or are invalid.

### Common Causes

- ConfigMap referenced in environment variables does not exist
- Secret referenced in environment variables does not exist
- ConfigMap key or Secret key does not exist
- ConfigMap or Secret is in a different namespace

### How to Fix

Check the exact error:
```bash
kubectl describe pod <pod-name> | grep -A5 "CreateContainerConfigError"
```

Verify ConfigMaps exist:
```bash
kubectl get configmap
kubectl get configmap <name> -o yaml
```

Verify Secrets exist:
```bash
kubectl get secret
kubectl get secret <name> -o yaml
```

### Examples

```bash
# Check for missing ConfigMap
kubectl describe pod my-app
#  Error: configmap "app-config" not found

# Fix
kubectl create configmap app-config --from-file=config.yaml
```"""),

    ("create-container-error", "CreateContainerError",
     "Fix Kubernetes CreateContainerError. Resolve pod failures when the container runtime cannot create the container due to configuration issues.",
     """## CreateContainerError

This error occurs when the container runtime cannot create the container due to configuration or resource issues after the image is pulled and config is resolved.

### Common Causes

- Invalid security context settings
- Root filesystem issues or overlay filesystem errors
- Container runtime (containerd/CRI-O) not functioning
- Node disk space exhausted
- Invalid container capabilities or seccomp profile

### How to Fix

Describe the pod for detailed error:
```bash
kubectl describe pod <pod-name>
```

Check node disk space:
```bash
kubectl debug node/<node-name> -- df -h
```

Check container runtime on the node:
```bash
kubectl get nodes -o wide
# SSH to node and check: systemctl status containerd
```

### Examples

```bash
# Check node disk pressure
kubectl describe node <node-name> | grep -i -A5 "Conditions"

# Free disk space on node
kubectl debug node/<node-name> -it --image=busybox -- df -h
```"""),

    ("invalid-image-name", "InvalidImageName",
     "Fix Kubernetes InvalidImageName error. Resolve pod failures when the container image name format is invalid.",
     """## InvalidImageName

This error occurs when the container image name or tag does not follow valid format rules. Kubernetes cannot parse the image reference.

### Common Causes

- Whitespace in the image name or tag
- Missing repository name or tag
- Invalid characters in the image reference
- Missing colon between image and tag
- Trailing slash or special characters

### How to Fix

Check the image in the pod spec:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].image}'
```

Verify the image format:
```yaml
# Valid formats
image: nginx
image: nginx:1.25
image: docker.io/library/nginx:1.25
image: myregistry.example.com/app:v1.0
```

### Examples

```bash
# Invalid formats
# image: nginx:   (empty tag)
# image: my-app:v1.0-beta 1  (space in tag)

# Fix by correcting the image reference
kubectl set image deployment/my-app my-app=nginx:1.25
```"""),

    ("image-inspect-error", "ImageInspectError",
     "Fix Kubernetes ImageInspectError. Resolve pod failures when the container runtime cannot inspect a pulled image's metadata.",
     """## ImageInspectError

This error occurs when the container runtime successfully pulls an image but cannot inspect or parse its metadata. The image manifest may be corrupted or incompatible.

### Common Causes

- Corrupted image manifest
- Image built for a different architecture
- Incompatible image format
- Registry returned a malformed image
- Disk I/O errors reading the image layers

### How to Fix

Try pulling the image manually on the node:
```bash
crictl pull <image>:<tag>
```

Re-pull the image:
```bash
kubectl delete pod <pod-name>
# New pod will be created by the controller
```

### Examples

```bash
# Check architecture mismatch
kubectl describe pod my-app | grep -i "ImageInspectError"
#  Error: image with reference my-app requires ARM64 but node is amd64

# Fix: use multi-arch image or specify correct architecture
```"""),

    ("err-image-never-pull", "ErrImageNeverPull",
     "Fix Kubernetes ErrImageNeverPull error. Resolve pod failures when imagePullPolicy is Never but the image does not exist locally on the node.",
     """## ErrImageNeverPull

This error occurs when the pod has `imagePullPolicy: Never` but the specified image does not exist on the node where the pod is scheduled.

### Common Causes

- `imagePullPolicy` set to `Never` in the pod spec
- Image was pre-loaded on some nodes but not on the scheduling node
- Image was removed by image garbage collection
- Deployment uses `Never` pull policy unintentionally

### How to Fix

Check the imagePullPolicy:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].imagePullPolicy}'
```

Change to a pull policy that will pull the image:
```yaml
imagePullPolicy: IfNotPresent
# or
imagePullPolicy: Always
```

### Examples

```bash
# Fix pull policy
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"containers":[{"name":"my-app","imagePullPolicy":"IfNotPresent"}]}}}}'
```"""),

    ("registry-unavailable", "RegistryUnavailable",
     "Fix Kubernetes RegistryUnavailable error. Resolve pod failures when the container image registry is unreachable from the node.",
     """## RegistryUnavailable

This error occurs when the kubelet cannot connect to the container image registry. The registry may be down, unreachable, or the connection may be blocked.

### Common Causes

- Registry service outage
- Network connectivity issues between node and registry
- Firewall or security group blocking outbound connections
- DNS resolution failure for registry hostname
- Proxy configuration missing or incorrect

### How to Fix

Test connectivity from a node:
```bash
kubectl run test --image=busybox -it --rm -- wget -S https://registry-1.docker.io/v2/
```

Check DNS resolution:
```bash
kubectl run test --image=busybox -it --rm -- nslookup registry-1.docker.io
```

Configure image pull secrets or proxy settings on the node.

### Examples

```bash
# Test registry connectivity
kubectl run test --image=busybox -it --rm -- wget -S https://registry-1.docker.io/v2/

# Configure containerd proxy
# Edit /etc/systemd/system/containerd.service.d/http-proxy.conf
# [Service]
# Environment="HTTP_PROXY=http://proxy:8080"
# Environment="HTTPS_PROXY=http://proxy:8080"
```"""),

    ("post-start-hook-error", "PostStartHookError",
     "Fix Kubernetes PostStartHookError. Resolve pod failures when the container postStart lifecycle hook fails during container startup.",
     """## PostStartHookError

This error occurs when the postStart lifecycle hook defined in the container spec fails. Kubernetes runs this hook immediately after creating the container, and a failure will terminate the container.

### Common Causes

- postStart command or script exits with non-zero
- HTTP postStart handler returns non-2xx status
- Handler touches dependent resources not yet available
- Incorrect handler configuration

### How to Fix

Describe the pod for hook errors:
```bash
kubectl describe pod <pod-name> | grep -A10 "postStart"
```

Check the handler configuration:
```yaml
lifecycle:
  postStart:
    exec:
      command: ["/bin/sh", "-c", "echo done > /tmp/startup"]
```

### Examples

```bash
# Check postStart error
kubectl describe pod my-app | grep -i "hook"
#  PostStartHookError: command '/scripts/init.sh' exited with 1

# Fix: correct the script or handle errors gracefully
kubectl edit deployment my-app
```"""),

    ("pre-stop-hook-error", "PreStopHookError",
     "Fix Kubernetes PreStopHookError. Resolve pod termination failures when the preStop lifecycle hook fails during graceful shutdown.",
     """## PreStopHookError

This error occurs when the preStop lifecycle hook fails during pod termination. Kubernetes still proceeds with termination but logs the error.

### Common Causes

- preStop command or script exits with non-zero
- HTTP handler returns non-2xx status
- Handler takes longer than the terminationGracePeriodSeconds
- Handler tries to access resources already being terminated

### How to Fix

Check the pod events:
```bash
kubectl describe pod <pod-name> | grep -A10 "preStop"
```

Increase terminationGracePeriodSeconds:
```yaml
terminationGracePeriodSeconds: 60
```

### Examples

```bash
# Check for preStop errors
kubectl describe pod my-app | grep -i -A3 "Unhealthy"

# Fix: increase grace period
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"terminationGracePeriodSeconds":60}}}}'
```"""),

    ("evicted", "Pod Evicted",
     "Fix Kubernetes pod eviction. Resolve pods that are evicted from nodes due to resource pressure or taints.",
     """## Pod Evicted

A pod enters the Evicted status when the kubelet evicts it from a node. This is a protection mechanism to reclaim resources for higher-priority workloads.

### Common Causes

- Node disk pressure (DiskPressure)
- Node memory pressure (MemoryPressure)
- Node PID pressure (PIDPressure)
- Node pressure condition resolved, but pods remain in evicted status
- Pod exceeded ephemeral storage limit
- Node became unreachable (NodeLost)

### How to Fix

Check the eviction reason:
```bash
kubectl get pod <pod-name> -o jsonpath='{.status.reason}'
```

List evicted pods:
```bash
kubectl get pods --field-selector=status.phase=Failed
```

Remove evicted pods:
```bash
kubectl delete pod <pod-name>
```

Clean up all evicted pods:
```bash
kubectl get pods --all-namespaces | grep Evicted | awk '{print $2 " -n " $1}' | xargs kubectl delete pod
```

### Examples

```bash
# Remove all evicted pods
kubectl get pods --all-namespaces | grep Evicted | while read ns pod rest; do kubectl delete pod -n $ns $pod; done
```"""),

    ("deadline-exceeded", "DeadlineExceeded (Job)",
     "Fix Kubernetes Job DeadlineExceeded error. Resolve jobs that exceed their activeDeadlineSeconds limit and are terminated.",
     """## DeadlineExceeded (Job)

This error occurs when a Kubernetes Job runs longer than the configured `activeDeadlineSeconds` limit. Kubernetes terminates the job and marks it as failed.

### Common Causes

- Job takes longer to complete than expected
- activeDeadlineSeconds is set too low
- Worker pods are stuck or hanging
- BackoffLimit exceeded for retries
- Dependent services are slow or unavailable

### How to Fix

Check job status:
```bash
kubectl describe job <job-name>
```

View logs of the failed pod:
```bash
kubectl logs job/<job-name>
```

Increase the deadline:
```yaml
spec:
  activeDeadlineSeconds: 3600
```

### Examples

```bash
# Delete and recreate job with longer deadline
kubectl delete job <job-name>
kubectl create job <job-name> --image=myapp
```"""),

    ("back-off-restarting", "BackOff (restarting failed container)",
     "Fix Kubernetes BackOff restart backoff delay. Resolve pods that fail to start and are delayed by exponential backoff between restart attempts.",
     """## BackOff

This status means Kubernetes is using exponential backoff between container restart attempts. The delay increases with each retry (10s, 20s, 40s, 80s, up to 5 minutes).

### Common Causes

- Application crashes immediately after start
- Configuration errors preventing application startup
- Missing dependencies at startup
- Resource limits causing immediate OOM

### How to Fix

Check the crash reason:
```bash
kubectl logs <pod-name> --previous
```

Check for configuration issues:
```bash
kubectl describe pod <pod-name>
```

Reset the backoff by deleting the pod:
```bash
kubectl delete pod <pod-name>
# The controller recreates it
```

### Examples

```bash
# View crash logs
kubectl logs my-app-7d4f9c7b6-abcde --previous --tail=50

# Delete pod to reset backoff (deployment recreates)
kubectl delete pod my-app-7d4f9c7b6-abcde
```"""),

    # ===== SCHEDULING ERRORS =====

    ("failed-scheduling", "FailedScheduling",
     "Fix Kubernetes FailedScheduling error. Resolve pods that cannot be scheduled to any node in the cluster.",
     """## FailedScheduling

This error occurs when the Kubernetes scheduler cannot find a suitable node to run the pod. The pod remains in Pending state.

### Common Causes

- Insufficient CPU or memory resources on any node
- Node selector or affinity rules cannot be satisfied
- Pod tolerations do not match node taints
- All nodes have resource pressure (DiskPressure, MemoryPressure)
- PVC not bound or does not exist
- Cluster autoscaler is provisioning new nodes (may be temporary)

### How to Fix

Check the scheduling error:
```bash
kubectl describe pod <pod-name> | grep -A5 "Events"
```

View node resource usage:
```bash
kubectl top nodes
```

Check for taints:
```bash
kubectl describe nodes | grep -i taint
```

### Examples

```bash
kubectl describe pod my-app
#  Events:
#    0/4 nodes are available: 2 Insufficient cpu, 2 Insufficient memory.

# Fix: reduce resource requests or add more nodes
```"""),

    ("insufficient-cpu", "Insufficient CPU",
     "Fix Kubernetes Insufficient CPU scheduling error. Resolve pods that cannot be scheduled because no node has enough available CPU.",
     """## Insufficient CPU

`0/4 nodes are available: 4 Insufficient cpu`

This scheduling error occurs when every node in the cluster has insufficient available CPU capacity to meet the pod's resource request.

### Common Causes

- Pod CPU request is set too high
- Cluster is at capacity with other workloads
- Node CPU requests are overallocated
- Too many pods running on the nodes

### How to Fix

Check node resources:
```bash
kubectl top nodes
```

Reduce CPU request in the pod spec:
```bash
kubectl set resources deployment/my-app --requests=cpu=200m --limits=cpu=500m
```

Add more nodes to the cluster.

### Examples

```bash
# Reduce CPU request
kubectl set resources deployment/my-app --requests=cpu=200m --limits=cpu=500m
```"""),

    ("insufficient-memory", "Insufficient Memory",
     "Fix Kubernetes Insufficient Memory scheduling error. Resolve pods that cannot be scheduled due to memory constraints on all nodes.",
     """## Insufficient Memory

`0/4 nodes are available: 4 Insufficient memory`

This scheduling error occurs when no node in the cluster has enough available memory to run the pod.

### Common Causes

- Pod memory request is too high
- Cluster memory is fully utilized by existing workloads
- Memory leak in other pods consuming excessive memory
- Nodes have memory pressure condition

### How to Fix

Check node memory usage:
```bash
kubectl top nodes
```

Reduce memory request:
```bash
kubectl set resources deployment/my-app --requests=memory=256Mi --limits=memory=512Mi
```

### Examples

```bash
# Reduce memory request
kubectl set resources deployment/my-app --requests=memory=256Mi --limits=memory=512Mi
```"""),

    ("insufficient-pods", "Insufficient Pods",
     "Fix Kubernetes Insufficient Pods scheduling error. Resolve pods that cannot be scheduled because nodes have reached their pod capacity limit.",
     """## Insufficient Pods

`0/4 nodes are available: 4 Insufficient Pods`

This scheduling error occurs when all nodes in the cluster have reached their maximum pod capacity (default 110 pods per node).

### Common Causes

- Default pod limit (110 pods per node) has been reached
- Large number of daemonset pods on each node
- Node has been configured with a low `--max-pods` limit
- Too many small sidecar containers

### How to Fix

Check pods per node:
```bash
kubectl get pods --all-namespaces -o wide | grep <node> | wc -l
```

Increase max pods per node (kubelet config):
```yaml
kubeletConfig:
  maxPods: 250
```

### Examples

```bash
# Count pods per node
kubectl get pods --all-namespaces -o wide | awk '{print $8}' | sort | uniq -c | sort -rn
```"""),

    ("taint-toleration", "Node had taints that the pod did not tolerate",
     "Fix Kubernetes taint and toleration scheduling errors. Resolve pods that cannot be scheduled due to node taints without matching tolerations.",
     """## Node Taints Not Tolerated

`0/4 nodes are available: 4 node(s) had untolerated taint`

This scheduling error occurs when all nodes have taints that the pod does not tolerate. Kubernetes uses taints and tolerations to control which pods can run on which nodes.

### Common Causes

- Node has a taint preventing general workload scheduling
- Pod is missing required tolerations
- Node was cordoned (tainted unschedulable)
- Workload intended for a different node pool
- Taint added for node maintenance

### How to Fix

List node taints:
```bash
kubectl describe nodes | grep -i taint
```

Add tolerations to the pod spec:
```yaml
tolerations:
- key: "dedicated"
  operator: "Equal"
  value: "gpu"
  effect: "NoSchedule"
```

Remove a taint:
```bash
kubectl taint nodes <node-name> key:NoSchedule-
```

### Examples

```bash
# Add toleration to deployment
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"tolerations":[{"key":"dedicated","operator":"Equal","value":"gpu","effect":"NoSchedule"}]}}}}'
```"""),

    ("node-selector-mismatch", "Node selector mismatch",
     "Fix Kubernetes nodeSelector scheduling error. Resolve pods that cannot be scheduled because no node has the required labels.",
     """## Node Selector Mismatch

`0/4 nodes are available: 4 node(s) didn't match node selector`

This scheduling error occurs when no node has the labels required by the pod's `nodeSelector`. The pod can only run on nodes with matching labels.

### Common Causes

- Node selector label does not exist on any node
- Node labels were removed or renamed
- Labels are case-sensitive
- Pod was deployed to wrong cluster

### How to Fix

Check node labels:
```bash
kubectl get nodes --show-labels
```

Add label to a node:
```bash
kubectl label nodes <node-name> <key>=<value>
```

### Examples

```bash
# Find nodes with specific label
kubectl get nodes -l disktype=ssd

# Label a node
kubectl label nodes node1 disktype=ssd
```"""),

    ("pod-affinity-mismatch", "Pod affinity or anti-affinity conflict",
     "Fix Kubernetes pod affinity scheduling errors. Resolve pods that cannot be scheduled due to pod affinity or anti-affinity rules.",
     """## Pod Affinity / Anti-Affinity Conflict

This scheduling error occurs when the pod's affinity or anti-affinity rules cannot be satisfied by the current state of the cluster.

### Common Causes

- Pod affinity requires pods on the same node but no node has matching pods
- Pod anti-affinity prevents co-location on all available nodes
- RequiredDuringScheduling rules that cannot be met
- TopologyKey mismatch with node labels

### How to Fix

Check pod affinity rules:
```bash
kubectl get pod <pod-name> -o yaml | grep -A20 affinity
```

Relax anti-affinity from required to preferred:
```yaml
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution: [...]
```

### Examples

```bash
# Check existing pods for anti-affinity conflicts
kubectl get pods -l app=myapp -o wide
```"""),

    ("topology-spread-constraints", "Topology spread constraints not met",
     "Fix Kubernetes topology spread constraint scheduling errors. Resolve pods that cannot be scheduled due to topology spread rules.",
     """## Topology Spread Constraints Not Met

This scheduling error occurs when the pod's topology spread constraints cannot be satisfied. Pods must be distributed across topology domains but no suitable domain is available.

### Common Causes

- Constraints are too strict for the cluster topology
- Not enough nodes to distribute the desired number of pods
- maxSkew is set too low
- Too few topology zones available

### How to Fix

Increase maxSkew to allow more imbalance:
```yaml
topologySpreadConstraints:
  - maxSkew: 5
```

Relax from required to preferred:
```yaml
whenUnsatisfiable: ScheduleAnyway
```

### Examples

```bash
# View node topology zones
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.labels.topology\.kubernetes\.io/zone}{"\n"}{end}'
```"""),

    # ===== KUBELET / NODE ERRORS =====

    ("node-not-ready", "NodeNotReady",
     "Fix Kubernetes NodeNotReady condition. Resolve nodes that become unhealthy and stop accepting pods.",
     """## NodeNotReady

A node enters the NotReady state when the kubelet fails to report its status to the control plane. After the `node-monitor-grace-period` (default 40s), the node is marked NotReady.

### Common Causes

- Kubelet service stopped or crashed
- Node is out of disk space (DiskPressure)
- Node is out of memory (MemoryPressure)
- Container runtime (containerd/CRI-O) is not responding
- Network connectivity issues between node and control plane
- Node rebooted or kernel panic

### How to Fix

Check node conditions:
```bash
kubectl describe node <node-name> | grep -A10 Conditions
```

SSH to the node and check kubelet:
```bash
systemctl status kubelet
journalctl -u kubelet --tail=50
```

Restart kubelet:
```bash
sudo systemctl restart kubelet
```

### Examples

```bash
# Check all node statuses
kubectl get nodes

# Detailed node diagnostics
kubectl describe node worker-1 | grep -A10 Conditions
# DiskPressure  True  ...
# Fix: free disk space on the node
```"""),

    ("kubelet-not-ready", "KubeletNotReady",
     "Fix Kubernetes KubeletNotReady error. Resolve issues where the kubelet cannot start or becomes unhealthy on a node.",
     """## KubeletNotReady

This error occurs when the kubelet on a node is running but not ready. The kubelet may be initializing, waiting for resources, or encountering configuration errors.

### Common Causes

- Kubelet cannot connect to the API server
- CNI plugin not configured or not working
- Container runtime not initialized
- Kubelet configuration is invalid
- TLS certificate issues

### How to Fix

SSH to the node and check kubelet:
```bash
sudo journalctl -u kubelet --no-pager --tail=100
```

Check kubelet configuration:
```bash
sudo cat /var/lib/kubelet/config.yaml
```

Restart kubelet:
```bash
sudo systemctl restart kubelet
```

### Examples

```bash
# Check kubelet for CNI errors
sudo journalctl -u kubelet | grep -i "cni"
#  Failed to initialize CNI: failed to load CNI config

# Fix: install CNI plugin binary and config
sudo cp /opt/cni/bin/<plugin> /opt/cni/bin/
```"""),

    ("disk-pressure", "DiskPressure",
     "Fix Kubernetes DiskPressure node condition. Resolve nodes that are under disk space pressure and may evict pods.",
     """## DiskPressure

A node enters DiskPressure state when the local disk usage exceeds the configured threshold (default 85% for image filesystem, 90% for node filesystem). Pods may be evicted to reclaim disk space.

### Common Causes

- Node disk is nearly full
- Excessive container logs filling disk
- Docker/containerd image cache consuming space
- Application writing large files to the node filesystem
- Not enough inodes available

### How to Fix

SSH to the node and check disk usage:
```bash
df -h
du -sh /var/log/
du -sh /var/lib/docker/
```

Clean up unused images:
```bash
docker image prune -a -f
# or with crictl
crictl rmi --prune
```

Configure log rotation in kubelet config:
```yaml
containerLogMaxSize: 10Mi
containerLogMaxFiles: 5
```

### Examples

```bash
# Check disk on node
ssh <node> df -h
# /dev/sda1   50G   48G   2G   96% /

# Remove unused Docker images
ssh <node> docker image prune -a -f
```"""),

    ("memory-pressure", "MemoryPressure",
     "Fix Kubernetes MemoryPressure node condition. Resolve nodes under memory pressure affecting pod scheduling and stability.",
     """## MemoryPressure

A node enters MemoryPressure when its available memory drops below the configured threshold (default 100Mi). The kubelet starts evicting lower-priority pods to reclaim memory.

### Common Causes

- Node memory is overcommitted
- Pods are using more memory than requested
- Memory leak in an application
- Burstable or BestEffort QoS pods consuming excess memory

### How to Fix

Check node memory:
```bash
kubectl top node <node-name>
free -m
```

Check which pods use the most memory:
```bash
kubectl top pods --all-namespaces --sort-by=memory | head -10
```

Set memory limits on problematic pods:
```bash
kubectl set resources deployment/<name> --limits=memory=256Mi
```

### Examples

```bash
# Top memory consumers
kubectl top pods --all-namespaces --sort-by=memory | head -10

# Add more memory or evict pods
kubectl drain <node-name> --ignore-daemonsets
```"""),

    ("pid-pressure", "PIDPressure",
     "Fix Kubernetes PIDPressure node condition. Resolve nodes under PID usage pressure affecting pod scheduling.",
     """## PIDPressure

A node enters PIDPressure when the number of processes (PIDs) on the node exceeds the configured threshold (default 90% of kernel.pid_max, typically 32768).

### Common Causes

- Fork bomb or runaway process creation
- Pods running many parallel processes
- System processes consuming PIDs
- pid_max kernel parameter set too low

### How to Fix

SSH to the node and check PID usage:
```bash
cat /proc/sys/kernel/pid_max
ps aux | wc -l
```

Increase pid_max:
```bash
sudo sysctl -w kernel.pid_max=65536
```

### Examples

```bash
# Increase max PIDs
ssh <node> sudo sysctl -w kernel.pid_max=65536
# Make permanent:
echo 'kernel.pid_max=65536' | sudo tee -a /etc/sysctl.d/99-pid.conf
```"""),

    ("network-unavailable", "NetworkUnavailable",
     "Fix Kubernetes NetworkUnavailable node condition. Resolve nodes where the network is not ready for pod communication.",
     """## NetworkUnavailable

This node condition indicates that the network on the node is not properly configured for pod networking. Usually caused by CNI plugin issues.

### Common Causes

- CNI plugin (Calico, Flannel, Weave, Cilium) is not installed
- CNI pod is not running on the node
- CNI configuration is invalid
- Firewall rules blocking pod-to-pod communication

### How to Fix

Check CNI pods:
```bash
kubectl get pods -n kube-system | grep -E "calico|flannel|weave|cilium"
```

Check CNI logs:
```bash
kubectl logs -n kube-system <cni-pod> --tail=50
```

On the node, check CNI config:
```bash
ls /etc/cni/net.d/
cat /etc/cni/net.d/*.conf
```

### Examples

```bash
# Check CNI status
kubectl get pods -n kube-system | grep -i "calico\\|flannel\\|weave\\|cilium"
# calico-node-xxxxx   1/1   Running

# Check node network condition
kubectl describe node <node> | grep NetworkUnavailable
```"""),

    # ===== KUBECTL CLIENT ERRORS =====

    ("unable-to-connect-server", "Unable to connect to the server",
     "Fix kubectl 'Unable to connect to the server' error. Resolve connection failures between kubectl and the Kubernetes API server.",
     """## Unable to Connect to the Server

`Unable to connect to the server: dial tcp <ip>:<port>: connect: connection refused`

This error occurs when kubectl cannot connect to the Kubernetes API server. The connection may be blocked, the server may be down, or the kubeconfig may be misconfigured.

### Common Causes

- API server is not running or has crashed
- kubectl is pointing to the wrong cluster or port
- Network connectivity issues (firewall, VPN)
- TLS certificate errors
- Cluster endpoint changed

### How to Fix

Check your current context:
```bash
kubectl config current-context
kubectl config view
```

Ping the API server:
```bash
curl -k https://<server>:<port>/healthz
```

### Examples

```bash
# Check connectivity
curl -k https://your-cluster:6443/healthz
# {"ok"}

# View current kubeconfig
kubectl config view --minify
```"""),

    ("x509-certificate-error", "x509 certificate error",
     "Fix kubectl x509 certificate error. Resolve TLS certificate verification failures when connecting to the API server.",
     """## x509 Certificate Error

`Unable to connect to the server: x509: certificate is valid for <names>, not <current-name>`

This error occurs when the API server's TLS certificate does not match the hostname or IP address used to connect.

### Common Causes

- Connecting via IP address but certificate only has DNS names
- Connecting via wrong DNS name
- Certificate has expired
- Using a self-signed certificate without the correct CA

### How to Fix

Use the correct server URL from the certificate:
```bash
openssl s_client -connect <server>:6443 -showcerts </dev/null 2>/dev/null | openssl x509 -text | grep DNS
```

Update kubeconfig with the correct server address:
```bash
kubectl config set-cluster <cluster> --server=https://<correct-dns>:6443
```

### Examples

```bash
# Check certificate DNS names
openssl s_client -connect api.example.com:6443 -showcerts </dev/null 2>/dev/null | openssl x509 -text | grep "DNS:"
```"""),

    ("connection-refused-kubectl", "kubectl connection refused",
     "Fix kubectl 'connection refused' error. Resolve API server port connectivity issues when the server is not listening.",
     """## Connection Refused

`Unable to connect to the server: dial tcp <ip>:6443: connect: connection refused`

This error occurs when the TCP connection to the API server port is actively refused. The server may not be listening on that port.

### Common Causes

- API server is not running
- API server is listening on a different port
- Firewall is blocking the port
- API server pod crashed or is restarting

### How to Fix

Check if the API server process is running (SSH to control plane):
```bash
ps aux | grep kube-apiserver
ss -tlnp | grep 6443
```

### Examples

```bash
# Check API server on control plane
ssh control-plane ss -tlnp | grep 6443
```"""),

    ("server-asked-for-credentials", "Server has asked for the credentials",
     "Fix kubectl 'server has asked for the credentials' error. Resolve authentication failures when the API server requires valid credentials.",
     """## Server Asked for Credentials

`error: You must be logged in to the server (the server has asked for the credentials)`

This error occurs when kubectl cannot authenticate with the Kubernetes API server. The server is reachable but no valid credentials are provided.

### Common Causes

- Kubeconfig is missing or incomplete
- Token has expired
- Client certificate has expired
- Wrong user context selected

### How to Fix

Check current user context:
```bash
kubectl config view --minify -o jsonpath='{.users[0].name}'
```

Re-authenticate with your cloud provider:
```bash
gcloud container clusters get-credentials <cluster> --region <region>
aws eks update-kubeconfig --name <cluster>
az aks get-credentials --name <cluster> --resource-group <rg>
```

### Examples

```bash
# EKS cluster
aws eks update-kubeconfig --region us-east-1 --name my-cluster

# GKE cluster
gcloud container clusters get-credentials my-cluster --zone us-central1-a
```"""),

    ("forbidden-kubectl", "kubectl Forbidden error",
     "Fix kubectl 'Forbidden' error. Resolve RBAC permission issues when kubectl commands are denied by the API server.",
     """## kubectl Forbidden

`Error from server (Forbidden): <resource> is forbidden: User "<user>" cannot list resource "<resource>"`

This error occurs when the authenticated user or service account does not have RBAC permissions to perform the requested operation.

### Common Causes

- User lacks necessary RBAC role bindings
- Wrong namespace context
- Service account has limited permissions
- Cluster-admin role not granted

### How to Fix

Check your current permissions:
```bash
kubectl auth can-i create deployments
kubectl auth can-i list pods --all-namespaces
```

Create a role binding:
```bash
kubectl create clusterrolebinding <name> --clusterrole=cluster-admin --user=<user>
```

### Examples

```bash
# Check permissions
kubectl auth can-i get pods
# yes

# Grant admin access
kubectl create clusterrolebinding my-admin-binding --clusterrole=admin --user=user@example.com
```"""),

    ("no-resources-found", "No resources found",
     "Fix kubectl 'No resources found' message. Resolve cases where kubectl commands return empty results in a namespace.",
     """## No Resources Found

`No resources found in <namespace> namespace.`

This message means kubectl successfully connected to the API server but found no matching resources. This may be expected or indicate a misconfiguration.

### Common Causes

- Empty namespace (no resources deployed yet)
- Wrong namespace specified
- Wrong resource name or label selector
- Resources were deleted

### How to Fix

List all resources in the namespace:
```bash
kubectl get all
```

List resources in all namespaces:
```bash
kubectl get pods --all-namespaces
```

### Examples

```bash
# List all namespaces
kubectl get ns

# List pods in all namespaces
kubectl get pods -A
```"""),

    ("unknown-command-kubectl", "kubectl unknown command",
     "Fix 'kubectl unknown command' error. Resolve kubectl command syntax and spelling errors.",
     """## Unknown Command

`Error: unknown command "<command>" for "kubectl"`

This error occurs when kubectl does not recognize the command you typed. The command may be misspelled or does not exist.

### Common Causes

- Typo in the command name
- Wrong command syntax (e.g., `kubectl pod` instead of `kubectl get pod`)
- Using a kubectl version that does not support the command

### How to Fix

Check available commands:
```bash
kubectl --help
kubectl <verb> --help
```

Use the correct syntax:
```bash
kubectl get pods         # correct
kubectl describe pod     # correct
kubectl pod get          # wrong
```

### Examples

```bash
# Common mistake: wrong order
kubectl pod get my-pod     # error: unknown command
kubectl get pod my-pod     # correct
```"""),

    ("port-forward-failed", "kubectl port-forward failed",
     "Fix 'kubectl port-forward' errors. Resolve port forwarding failures between local machine and Kubernetes pods.",
     """## Port Forward Failed

`error: unable to listen on port <port>: Listen failed: listen tcp <addr>: bind: address already in use`

This error occurs when kubectl port-forward cannot bind to the local port or connect to the remote pod.

### Common Causes

- Local port is already in use by another process
- Pod is not running or in CrashLoopBackOff
- Pod is not ready (not passing readiness probes)
- Wrong pod name or namespace

### How to Fix

Check if the local port is in use:
```bash
lsof -i :<port>
```

Use a different local port:
```bash
kubectl port-forward pod/<pod-name> <local-port>:<remote-port>
```

### Examples

```bash
# Use different local port
kubectl port-forward pod/my-app 8081:80

# Port forward with timeout
kubectl port-forward --pod-running-timeout=1m pod/my-app 8080:80
```"""),

    ("exec-failed", "kubectl exec failed",
     "Fix 'kubectl exec' errors. Resolve command execution failures inside running containers.",
     """## kubectl Exec Failed

`error: unable to upgrade connection: pod not found`

This error occurs when kubectl exec cannot connect to the container to execute a command.

### Common Causes

- Pod is not running (Pending, CrashLoopBackOff, Evicted)
- Container name is incorrect (for multi-container pods)
- exec command or binary does not exist in the container

### How to Fix

Check pod status:
```bash
kubectl get pod <pod-name>
```

For multi-container pods, specify the container:
```bash
kubectl exec -it <pod-name> -c <container-name> -- /bin/sh
```

### Examples

```bash
# List containers in pod
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}'

# Exec into specific container
kubectl exec -it my-app -c sidecar -- sh
```"""),

    ("kubeconfig-context-error", "kubeconfig context error",
     "Fix 'kubeconfig context' errors. Resolve issues when kubectl cannot find or parse the kubeconfig context.",
     """## Kubeconfig Context Error

`error: context "<context>" does not exist`

This error occurs when the specified Kubernetes context in your kubeconfig does not exist.

### Common Causes

- Typo in context name
- Context was removed or renamed
- Kubeconfig file is missing or corrupted
- KUBECONFIG environment variable points to wrong file

### How to Fix

List available contexts:
```bash
kubectl config get-contexts
```

Switch to a valid context:
```bash
kubectl config use-context <valid-context>
```

### Examples

```bash
# List all contexts
kubectl config get-contexts

# Switch context
kubectl config use-context my-cluster

# Merge multiple kubeconfigs
export KUBECONFIG=~/.kube/config:~/.kube/eks-config
kubectl config view --merge --flatten > ~/.kube/merged-config
```"""),

    # ===== VOLUME / STORAGE ERRORS =====

    ("failed-mount", "FailedMount",
     "Fix Kubernetes FailedMount volume error. Resolve pod failures when volumes cannot be mounted to the container.",
     """## FailedMount

This error occurs when the kubelet cannot mount a volume to the container. The pod may stay in ContainerCreating or crash.

### Common Causes

- PVC is not bound to a PV
- StorageClass does not exist or is not configured
- Volume driver (CSI) not installed
- NFS or network storage unreachable
- Volume already attached to another pod with ReadWriteOnce

### How to Fix

Check PVC status:
```bash
kubectl get pvc
kubectl describe pvc <name>
```

Check PV status:
```bash
kubectl get pv
kubectl describe pv <name>
```

Check StorageClass:
```bash
kubectl get storageclass
```

### Examples

```bash
# Check PVC binding
kubectl describe pvc my-claim
# Status:  Pending
# Events:  waiting for a volume to be created

# Check StorageClass provisioner
kubectl get storageclass
# gp2 (default)   kubernetes.io/aws-ebs
```"""),

    ("failed-attach-volume", "FailedAttachVolume",
     "Fix Kubernetes FailedAttachVolume error. Resolve pod failures when a persistent volume cannot be attached to the node.",
     """## FailedAttachVolume

This error occurs when the volume attachment controller cannot attach a persistent volume to the node where the pod is scheduled.

### Common Causes

- Volume already attached to another node (RWO volume)
- Cloud provider API rate limiting
- Volume does not exist in the cloud provider
- Incorrect availability zone or region
- IAM permissions insufficient for volume attachment

### How to Fix

Check the attach error:
```bash
kubectl describe pod <pod-name> | grep -A5 "FailedAttachVolume"
```

Check volume status in cloud provider:
```bash
# AWS
aws ec2 describe-volumes --volume-ids <vol-id>
# GCP
gcloud compute disks describe <disk-name>
```

### Examples

```bash
# Check for volume multi-attach
kubectl describe pod my-app | grep -i "FailedAttachVolume"
#  Volume is already exclusively attached to another node

# Force detach in AWS
aws ec2 detach-volume --volume-id vol-12345678 --force
```"""),

    ("pvc-not-found", "PersistentVolumeClaim not found",
     "Fix Kubernetes PVC not found error. Resolve pod failures when a referenced PersistentVolumeClaim does not exist.",
     """## PersistentVolumeClaim Not Found

`persistentvolumeclaim "<name>" not found`

This error occurs when a pod references a PersistentVolumeClaim that does not exist in the same namespace.

### Common Causes

- PVC name is misspelled in the pod spec
- PVC was deleted but pod still references it
- PVC is in a different namespace
- PVC hasn't been created yet

### How to Fix

List PVCs in the namespace:
```bash
kubectl get pvc
```

Create the PVC:
```bash
kubectl create -f pvc.yaml
```

### Examples

```bash
# List PVCs
kubectl get pvc --all-namespaces

# Create PVC from inline YAML
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
EOF
```"""),

    ("storageclass-not-found", "StorageClass not found",
     "Fix Kubernetes StorageClass not found error. Resolve PVC creation failures when the referenced StorageClass does not exist.",
     """## StorageClass Not Found

`storageclass.storage.k8s.io "<name>" not found`

This error occurs when a PersistentVolumeClaim references a StorageClass that does not exist in the cluster.

### Common Causes

- StorageClass name is misspelled
- StorageClass has not been created
- StorageClass was deleted
- Cluster does not have a default StorageClass

### How to Fix

List available StorageClasses:
```bash
kubectl get storageclass
```

Check the default StorageClass:
```bash
kubectl get storageclass -o jsonpath='{.items[?(@.metadata.annotations.storageclass\.kubernetes\.io/is-default-class=="true")].metadata.name}'
```

### Examples

```bash
# List StorageClasses
kubectl get storageclass
# gp2 (default)   kubernetes.io/aws-ebs
# standard        kubernetes.io/gce-pd
```"""),

    ("multi-attach-error", "Multi-Attach volume error",
     "Fix Kubernetes Multi-Attach volume error. Resolve volume attachment failures when a ReadWriteOnce volume is attached to multiple nodes.",
     """## Multi-Attach Volume Error

`Multi-Attach error for volume "<volume>"`
`Volume is already exclusively attached to one node and can't be attached to another`

This error occurs when two pods using the same ReadWriteOnce (RWO) persistent volume are scheduled on different nodes. RWO volumes can only be mounted on one node at a time.

### Common Causes

- Deployment with multiple replicas using an RWO volume
- Rolling update creates new pod on different node before old pod terminates
- StatefulSet with multiple replicas sharing the same volume

### How to Fix

Use ReadWriteMany (RWX) if the storage class supports it:
```yaml
accessModes:
  - ReadWriteMany
```

Use a StatefulSet with individual volumes per replica.

### Examples

```bash
# Check volume access mode
kubectl get pv <name> -o jsonpath='{.spec.accessModes}'

# Fix: schedule all replicas to same node
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"nodeSelector":{"kubernetes.io/hostname":"node-1"}}}}}'
```"""),

    # ===== CNI / NETWORK ERRORS =====

    ("failed-create-pod-sandbox", "Failed to create pod sandbox",
     "Fix Kubernetes 'Failed to create pod sandbox' error. Resolve pod creation failures in the container runtime during sandbox setup.",
     """## Failed to Create Pod Sandbox

`Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create containerd task`

This error occurs when the container runtime cannot create the pod sandbox (the isolation environment for the pod's containers).

### Common Causes

- CNI plugin failed to set up networking
- Container runtime (containerd/CRI-O) not responding
- Network interface already exists
- IP address allocation failure
- Kernel module missing (overlay, br_netfilter)

### How to Fix

Check the full error:
```bash
kubectl describe pod <pod-name> | grep -A10 "Failed to create pod sandbox"
```

Check containerd/CRI-O status on the node:
```bash
sudo systemctl status containerd
sudo journalctl -u containerd --tail=50
```

### Examples

```bash
# Check containerd for sandbox errors
journalctl -u containerd --no-pager --tail=100 | grep -i "sandbox\\|cni\\|network"

# Restart containerd and kubelet
sudo systemctl restart containerd && sudo systemctl restart kubelet
```"""),

    ("cni-plugin-failed", "CNI plugin failed",
     "Fix Kubernetes CNI plugin failure. Resolve network setup errors when the CNI plugin cannot configure pod networking.",
     """## CNI Plugin Failed

`NetworkPlugin cni failed: cni plugin not initialized`

This error occurs when the CNI (Container Network Interface) plugin fails to set up network connectivity for a pod.

### Common Causes

- CNI plugin binary is missing or not installed
- CNI configuration file is invalid
- CNI plugin container (Calico, Flannel) is not running
- Kernel modules not loaded (bridge, iptables)

### How to Fix

Check CNI pods:
```bash
kubectl get pods -n kube-system | grep -E "calico|flannel|weave|cilium|canal"
```

On the node, check CNI config:
```bash
ls -la /etc/cni/net.d/
cat /etc/cni/net.d/*.conf*
```

### Examples

```bash
# Check CNI config on node
ssh <node> ls /etc/cni/net.d/
# 10-flannel.conflist
ssh <node> cat /etc/cni/net.d/10-flannel.conflist
```"""),

    ("coredns-pending", "CoreDNS pending or crash looping",
     "Fix Kubernetes CoreDNS Pending or CrashLoopBackOff errors. Resolve DNS service failures in the cluster.",
     """## CoreDNS Pending / CrashLoopBackOff

CoreDNS provides DNS resolution for the cluster. If CoreDNS pods are not running, service discovery breaks and pods cannot resolve service names.

### Common Causes

- CoreDNS pods cannot be scheduled (insufficient resources)
- CoreDNS ConfigMap is misconfigured
- Network policy blocking DNS traffic
- CoreDNS image not available (rate limited)

### How to Fix

Check CoreDNS status:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

Check CoreDNS logs:
```bash
kubectl logs -n kube-system -l k8s-app=kube-dns
```

Restart CoreDNS:
```bash
kubectl rollout restart -n kube-system deployment/coredns
```

### Examples

```bash
# Check CoreDNS pods
kubectl get pods -n kube-system | grep dns
# coredns-xxxxx   0/1   CrashLoopBackOff

# View CoreDNS logs
kubectl logs -n kube-system deployment/coredns
```"""),

    ("service-endpoints-not-found", "No endpoints for service",
     "Fix Kubernetes 'no endpoints for service' error. Resolve service connectivity failures when no pods match the service selector.",
     """## No Endpoints for Service

`Warning: No endpoints for service <service>`

This warning occurs when a Kubernetes Service has no endpoints because no pods match its label selector.

### Common Causes

- Pod labels do not match the service selector
- Pods are not running (Pending, CrashLoopBackOff)
- Pods are in a different namespace
- Service selector is incorrect or has typos

### How to Fix

Check the service selector:
```bash
kubectl get service <name> -o yaml | grep selector
```

Check pod labels:
```bash
kubectl get pods --show-labels
```

Check endpoints:
```bash
kubectl get endpoints <name>
```

### Examples

```bash
# Check service selector
kubectl get service my-service -o yaml | grep -A5 selector
#   selector:
#     app: my-app

# Check pod labels
kubectl get pods -l app=my-app
# No resources found
# Fix: correct the service selector or add the correct label to pods
```"""),

    ("ingress-error", "Ingress error",
     "Fix Kubernetes Ingress errors. Resolve Ingress resource configuration and routing issues.",
     """## Ingress Error

`error: Ingress <name> does not specify any backend`

This error occurs when the Ingress resource has no rules or a default backend configured. Traffic has nowhere to go.

### Common Causes

- Ingress rules are empty or invalid
- No matching Ingress controller running in the cluster
- Ingress class name does not match the controller
- Backend service does not exist or has no endpoints

### How to Fix

Check Ingress controller is running:
```bash
kubectl get pods -n ingress-nginx
```

Check Ingress configuration:
```bash
kubectl describe ingress <name>
```

Verify the backend service exists:
```bash
kubectl get service <name>
kubectl get endpoints <name>
```

### Examples

```bash
# Check Ingress controller
kubectl get pods -A | grep -i ingress
# ingress-nginx controller

# View Ingress details
kubectl describe ingress my-ingress
# Rules:
# Host          Path    Backends
# example.com   /api    my-service:80 (0/0 endpoints)
```"""),

    # ===== API SERVER ERRORS =====

    ("api-401-unauthorized", "API 401 Unauthorized",
     "Fix Kubernetes API 401 Unauthorized error. Resolve authentication failures when accessing the Kubernetes API.",
     """## API 401 Unauthorized

This HTTP status code occurs when the API server receives a request without valid authentication credentials.

### Common Causes

- Missing or expired bearer token
- Invalid or expired client certificate
- Service account token has expired or been deleted
- Token review API failure

### How to Fix

Check the current authentication method:
```bash
kubectl config view --minify
```

Generate a new service account token:
```bash
kubectl create token <service-account>
```

Update kubeconfig:
```bash
kubectl config set-credentials <user> --token=<new-token>
```

### Examples

```bash
# Create new service account token
kubectl create token my-sa --duration=24h

# Update kubeconfig with new token
kubectl config set-credentials cluster-admin --token=$(kubectl create token admin --duration=24h)
```"""),

    ("api-403-forbidden", "API 403 Forbidden",
     "Fix Kubernetes API 403 Forbidden error. Resolve authorization failures when the user lacks permissions for a resource.",
     """## API 403 Forbidden

This HTTP status code occurs when the user is authenticated but does not have authorization to perform the requested operation.

### Common Causes

- Missing RBAC role or cluster role
- Role binding does not include the user or service account
- Operation is restricted by an admission webhook
- Namespace does not exist or user cannot access it

### How to Fix

Check RBAC permissions:
```bash
kubectl auth can-i create deployments --namespace=default
```

Check available roles and bindings:
```bash
kubectl get clusterroles
kubectl get clusterrolebindings
```

### Examples

```bash
# Check what the user can do
kubectl auth can-i --list

# Grant cluster-admin
kubectl create clusterrolebinding my-admin --clusterrole=cluster-admin --user=user@example.com
```"""),

    ("api-409-conflict", "API 409 Conflict",
     "Fix Kubernetes API 409 Conflict error. Resolve resource update conflicts when the object has been modified by another process.",
     """## API 409 Conflict

`Conflict (409): Operation cannot be fulfilled on <resource> "<name>": the object has been modified`

This error occurs when you try to update a Kubernetes resource that has been modified since you last read it. Kubernetes uses optimistic concurrency to prevent conflicting writes.

### Common Causes

- Multiple controllers or users updating the same resource
- Automation tools (CI/CD) making concurrent updates
- Using kubectl edit or kubectl patch on a stale version

### How to Fix

Re-read the resource and re-apply the change:
```bash
kubectl get <resource> <name> -o yaml | kubectl replace -f -
```

Use server-side apply:
```bash
kubectl apply --server-side --force-conflicts -f resource.yaml
```

### Examples

```bash
# Re-read and re-apply
kubectl get deployment my-app -o yaml | kubectl replace -f -
```"""),

    ("api-422-unprocessable", "API 422 Unprocessable Entity",
     "Fix Kubernetes API 422 Unprocessable Entity error. Resolve resource creation failures due to validation errors.",
     """## API 422 Unprocessable Entity

This HTTP status code occurs when the API server cannot process the request due to semantic validation errors in the resource definition.

### Common Causes

- Required fields are missing
- Invalid field values or types
- Schema validation failure
- Invalid YAML/JSON syntax
- Immutable field modification

### How to Fix

Check the exact validation error in the response:
```bash
kubectl apply -f resource.yaml --validate=true
```

Run dry-run validation:
```bash
kubectl apply -f resource.yaml --dry-run=server
```

### Examples

```bash
# Dry run validation
kubectl apply -f deployment.yaml --dry-run=server
# error: Deployment.apps "my-app" is invalid: spec.selector: Invalid value

# Fix: use matching selector and labels
```"""),

    ("api-429-too-many", "API 429 Too Many Requests",
     "Fix Kubernetes API 429 Too Many Requests error. Resolve API rate limiting issues when making too many requests.",
     """## API 429 Too Many Requests

This HTTP status code occurs when the client exceeds the API server's rate limit. Kubernetes imposes rate limits to protect the control plane.

### Common Causes

- Automated scripts making rapid API requests
- Monitoring or CI/CD tools polling too frequently
- Watch requests creating excessive load
- Controller or operator in a tight reconciliation loop

### How to Fix

Implement exponential backoff in your application:
```python
import time
time.sleep(1)  # rate limit: 1 QPS
```

Use caching to reduce redundant requests.

Bulk operations instead of individual requests:
```bash
kubectl get pods --all-namespaces  # instead of per-namespace calls
```

### Examples

```bash
# Use list instead of individual get operations
kubectl get deployments --all-namespaces
```"""),

    ("api-500-internal", "API 500 Internal Server Error",
     "Fix Kubernetes API 500 Internal Server Error. Resolve server-side failures in the Kubernetes API server.",
     """## API 500 Internal Server Error

This HTTP status code occurs when the Kubernetes API server encounters an unexpected internal error.

### Common Causes

- etcd cluster is unhealthy or unreachable
- API server ran out of memory
- API server panic or crash
- Corrupted data in etcd
- Exceeded maximum request size

### How to Fix

Check API server health:
```bash
kubectl get --raw /healthz
kubectl get --raw /livez
kubectl get --raw /readyz
```

Check etcd health:
```bash
# SSH to control plane
ETCDCTL_ENDPOINTS=https://127.0.0.1:2379 etcdctl endpoint health
```

Check API server logs:
```bash
kubectl logs -n kube-system kube-apiserver-<node>
```

### Examples

```bash
# Check all API server health endpoints
kubectl get --raw /healthz && echo "OK" || echo "FAIL"
kubectl get --raw /livez && echo "OK" || echo "FAIL"
```"""),

    ("api-503-unavailable", "API 503 Service Unavailable",
     "Fix Kubernetes API 503 Service Unavailable error. Resolve temporary API server unavailability during upgrades or overload.",
     """## API 503 Service Unavailable

This HTTP status code occurs when the Kubernetes API server is temporarily unable to handle the request, typically during upgrades or overload.

### Common Causes

- API server is restarting (upgrade or crash)
- etcd leader election in progress
- etcd is overloaded or out of disk space
- API server is under heavy load
- Webhook endpoint is down causing timeouts

### How to Fix

Wait and retry with backoff:
```bash
while ! kubectl get nodes; do sleep 5; done
```

Check API server pods:
```bash
kubectl get pods -n kube-system -l component=kube-apiserver
```

### Examples

```bash
# Retry command with backoff
for i in 1 2 3 4 5; do kubectl get nodes && break; sleep $((i*2)); done
```"""),

    # ===== RBAC / AUTH ERRORS =====

    ("rbac-forbidden", "RBAC Forbidden (user cannot access resource)",
     "Fix Kubernetes RBAC Forbidden error. Resolve permission denied errors when a user or service account lacks necessary roles.",
     """## RBAC Forbidden

`<user> is forbidden: User "<user>" cannot <verb> resource "<resource>" in API group "<group>"`

This error occurs when the authenticated user or service account does not have RBAC permissions for the requested operation.

### Common Causes

- Insufficient RBAC role bindings
- Service account has limited scope
- Wrong namespace for the role binding
- Role binding references a role that doesn't exist

### How to Fix

Check the exact error to see what permission is missing:
```bash
kubectl auth can-i <verb> <resource> --as=<user>
```

Create a role binding:
```bash
kubectl create rolebinding <name> --role=<role> --user=<user> --namespace=<ns>
```

Create a cluster role binding:
```bash
kubectl create clusterrolebinding <name> --clusterrole=<role> --user=<user>
```

### Examples

```bash
# Check permissions for specific user
kubectl auth can-i list pods --as=deploy-bot --all-namespaces
# no

# Grant permission
kubectl create clusterrolebinding deploy-bot-view --clusterrole=view --user=deploy-bot
```"""),

    ("service-account-not-found", "Service account not found",
     "Fix Kubernetes service account not found error. Resolve pod creation failures when a referenced service account does not exist.",
     """## Service Account Not Found

`serviceaccounts "<name>" not found`

This error occurs when a pod spec references a service account that does not exist in the namespace.

### Common Causes

- Service account name is misspelled
- Service account has not been created
- Service account was deleted
- Pod is in a different namespace than the service account

### How to Fix

List service accounts:
```bash
kubectl get serviceaccounts
```

Create a service account:
```bash
kubectl create serviceaccount <name>
```

### Examples

```bash
# List all service accounts
kubectl get sa --all-namespaces

# Create service account
kubectl create sa my-app-sa
```"""),

    # ===== ADMISSION WEBHOOK ERRORS =====

    ("admission-webhook-denied", "Admission webhook denied the request",
     "Fix Kubernetes admission webhook denial errors. Resolve resource creation failures rejected by admission webhooks.",
     """## Admission Webhook Denied

`admission webhook "<webhook>" denied the request: <reason>`

This error occurs when an admission webhook (ValidatingWebhookConfiguration or MutatingWebhookConfiguration) rejects a resource creation or update.

### Common Causes

- Webhook validation rules are not satisfied
- Mutating webhook modifies the resource in an invalid way
- Webhook endpoint is unreachable causing timeouts
- Multiple webhooks conflict with each other

### How to Fix

Check the webhook error message for details about what was rejected.

List webhooks:
```bash
kubectl get validatingwebhookconfigurations
kubectl get mutatingwebhookconfigurations
```

Check webhook service status:
```bash
kubectl get pods -n <webhook-namespace>
kubectl get service -n <webhook-namespace>
```

### Examples

```bash
# List admission webhooks
kubectl get validatingwebhookconfigurations
# my-webhook   ValidatingWebhookConfiguration

# Check webhook logs
kubectl logs -n webhook-ns deployment/webhook
```"""),

    # ===== POD SECURITY ADMISSION =====

    ("psa-violation", "Pod Security Admission violation",
     "Fix Kubernetes Pod Security Admission (PSA) violations. Resolve pod creation failures due to pod security standards.",
     """## Pod Security Admission Violation

`Error: pod <name> violates PodSecurity "<profile>:<version>" - <violation>`

This error occurs when a pod does not meet the Pod Security Standards enforced by Pod Security Admission in the namespace.

### Common Causes

- Container runs as root (requires `restricted` profile)
- Privileged containers not allowed
- Host network or host PID access not allowed
- HostPath volumes not allowed
- Capabilities not allowed (NET_ADMIN, SYS_ADMIN)

### How to Fix

Check the namespace's PSA labels:
```bash
kubectl get ns <namespace> -o yaml | grep pod-security
```

Apply the correct security context to the pod:
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  runAsGroup: 3000
  seccompProfile:
    type: RuntimeDefault
  capabilities:
    drop: ["ALL"]
```

Relax the namespace policy:
```bash
kubectl label ns <namespace> pod-security.kubernetes.io/enforce=baseline
```

### Examples

```bash
# Check namespace PSA level
kubectl get ns my-ns -o yaml | grep -i "pod-security"
# pod-security.kubernetes.io/enforce: restricted

# Fix: add security context to pod
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"securityContext":{"runAsNonRoot":true,"seccompProfile":{"type":"RuntimeDefault"}}}}}}'
```"""),

    # ===== CONFIG ERRORS =====

    ("invalid-yaml", "Invalid YAML or JSON in Kubernetes manifest",
     "Fix Kubernetes invalid YAML or JSON errors. Resolve resource creation failures caused by malformed manifest files.",
     """## Invalid YAML / JSON

`error: error parsing <file>: error converting YAML to JSON: yaml: line <n>: did not find expected key`

This error occurs when kubectl cannot parse a Kubernetes manifest file due to YAML or JSON syntax errors.

### Common Causes

- Incorrect indentation (YAML is space-sensitive)
- Tab characters used instead of spaces
- Missing colons or commas
- Mismatched quotes or brackets

### How to Fix

Validate the YAML file:
```bash
kubectl apply -f manifest.yaml --dry-run=server
python3 -c "import yaml; yaml.safe_load(open('manifest.yaml'))"
```

Use a YAML linter:
```bash
yamllint manifest.yaml
```

### Examples

```yaml
# Correct YAML
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.25
```"""),

    ("resource-already-exists", "Resource already exists",
     "Fix Kubernetes 'already exists' error. Resolve resource creation failures when a resource with the same name already exists.",
     """## Resource Already Exists

`Error from server (AlreadyExists): <resource> "<name>" already exists`

This error occurs when you try to create a Kubernetes resource with a name that already exists. Resource names must be unique within a namespace.

### Common Causes

- Running `kubectl create` instead of `kubectl apply` on an existing resource
- CI/CD pipeline creating resources without checking for existing ones
- Manual creation followed by automated creation

### How to Fix

Use `kubectl apply` which creates or updates:
```bash
kubectl apply -f resource.yaml
```

Delete and recreate:
```bash
kubectl delete <resource> <name>
kubectl create -f resource.yaml
```

### Examples

```bash
# Use apply instead of create
kubectl apply -f deployment.yaml
```"""),

    ("missing-required-field", "Missing required field",
     "Fix Kubernetes 'missing required field' error. Resolve resource creation failures when required fields are not specified.",
     """## Missing Required Field

`error: validation failure: missing required field "<field>" in <resource>`

This error occurs when a Kubernetes resource manifest is missing a required field. The API server validates the schema and rejects incomplete resources.

### Common Causes

- Missing `apiVersion` or `kind` fields
- Missing `name` in metadata
- Missing `containers` in pod spec
- Missing `selector` in deployment or service

### How to Fix

Add the missing field to the manifest.

Use the explain command to see required fields:
```bash
kubectl explain deployment.spec
kubectl explain pod.spec.containers
```

### Examples

```bash
# Check required fields for a deployment
kubectl explain deployment
# metadata.name, spec.selector.matchLabels, spec.template.metadata.labels, spec.template.spec.containers
```"""),

    ("namespace-terminating", "Namespace Terminating",
     "Fix Kubernetes 'namespace is terminating' error. Resolve resource creation failures in a namespace that is being deleted.",
     """## Namespace Terminating

`Error: namespace "<namespace>" is terminating`

This error occurs when you try to create resources in a namespace that is in the process of being deleted.

### Common Causes

- Running a kubectl delete namespace that hasn't completed
- Trying to recreate a namespace before it's fully removed
- Namespace stuck in Terminating state due to finalizers

### How to Fix

Wait for the namespace to finish deleting:
```bash
kubectl get ns <namespace>
```

If stuck, remove finalizers:
```bash
kubectl get namespace <name> -o json | jq '.spec.finalizers=[]' | kubectl replace --raw /api/v1/namespaces/<name>/finalize -f -
```

### Examples

```bash
# Check namespace status
kubectl get ns my-ns
# my-ns   Terminating

# Remove finalizers to force delete
kubectl get namespace my-ns -o json | jq '.spec.finalizers=[]' | kubectl replace --raw /api/v1/namespaces/my-ns/finalize -f -
```"""),

    # ===== HPA / AUTOSCALING ERRORS =====

    ("hpa-failed-get-metrics", "HPA failed to get metrics",
     "Fix Kubernetes HPA 'failed to get metrics' error. Resolve HorizontalPodAutoscaler failures when metrics are unavailable.",
     """## HPA Failed to Get Metrics

`Failed to get metrics: failed to get <metric> metric`

This error occurs when the HorizontalPodAutoscaler cannot retrieve the metrics needed for scaling decisions.

### Common Causes

- Metrics Server not installed or not running
- Resource metrics not available for the target pods
- Custom metrics API endpoint not available
- Metrics Server has insufficient permissions

### How to Fix

Check Metrics Server:
```bash
kubectl get pods -n kube-system -l k8s-app=metrics-server
```

Get resource metrics:
```bash
kubectl top pods
kubectl top nodes
```

Check HPA status:
```bash
kubectl describe hpa <name>
```

Install Metrics Server:
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Examples

```bash
# Check metrics availability
kubectl top nodes
# error: Metrics API not available

# Install Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Check HPA details
kubectl describe hpa my-hpa
```"""),

    ("hpa-target-not-found", "HPA target not found",
     "Fix Kubernetes HPA target not found error. Resolve HorizontalPodAutoscaler failures when the target resource does not exist.",
     """## HPA Target Not Found

`error: target <resource>/<name> not found`

This error occurs when the HorizontalPodAutoscaler references a deployment, statefulset, or custom resource that does not exist.

### Common Causes

- HPA target name is misspelled
- Target deployment has not been created
- Target deployment was deleted
- HPA is looking in the wrong namespace

### How to Fix

Check the HPA target:
```bash
kubectl describe hpa <name>
```

List available deployments:
```bash
kubectl get deployments
```

### Examples

```bash
# Check HPA target
kubectl get hpa my-hpa -o jsonpath='{.spec.scaleTargetRef}'
# {"apiVersion":"apps/v1","kind":"Deployment","name":"my-app"}

# Verify target exists
kubectl get deployment my-app
```"""),

    ("hpa-unable-calculate-pods", "HPA unable to calculate pod count",
     "Fix Kubernetes HPA 'unable to calculate' pod count error. Resolve HPA failures when pods lack resource requests.",
     """## HPA Unable to Calculate Pod Count

`unable to calculate pod count: missing request for <resource>`

This error occurs when the HPA cannot calculate the desired number of pods because the target pods do not have resource requests defined.

### Common Causes

- Pods in the target do not have CPU or memory requests set
- HPA is using a custom metrics query that returns no data
- Some pods in the replica set have different resource configurations

### How to Fix

Add resource requests to pods:
```yaml
resources:
  requests:
    cpu: 200m
    memory: 256Mi
```

### Examples

```bash
# Check if pods have resource requests
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[0].resources.requests}'
# {cpu: 200m memory: 256Mi}

# Add requests to deployment
kubectl set resources deployment/my-app --requests=cpu=200m,memory=256Mi
```"""),

    # ===== MISC ERRORS =====

    ("unknown-field", "Unknown field in Kubernetes manifest",
     "Fix Kubernetes 'unknown field' error. Resolve resource creation failures when the manifest contains unrecognized fields.",
     """## Unknown Field

`error: validation failure: unknown field "<field>" in <resource>`

This error occurs when a Kubernetes manifest contains a field that does not exist in the API schema.

### Common Causes

- Typo in a field name
- Field exists in a different API version
- Using a deprecated field that was removed
- API version mismatch between cluster and manifest

### How to Fix

Check the correct API version:
```bash
kubectl explain pod
```

Use the correct API version:
```yaml
apiVersion: apps/v1  # instead of extensions/v1beta1
```

### Examples

```bash
# Check supported fields
kubectl explain deployment.spec
# Find the correct field name

# Common fix: update API version
# Old: apiVersion: extensions/v1beta1
# New: apiVersion: networking.k8s.io/v1
```"""),

    ("object-has-been-modified", "The object has been modified",
     "Fix Kubernetes 'the object has been modified' error. Resolve resource update failures due to concurrent modifications.",
     """## Object Has Been Modified

`Operation cannot be fulfilled on <resource> "<name>": the object has been modified`

This error occurs when you attempt to update a resource that has been modified since you last read it. Kubernetes uses resourceVersion for optimistic concurrency control.

### Common Causes

- Multiple users or controllers updating the same resource
- CI/CD pipeline retrying updates without re-reading
- Using kubectl edit while another process updates the resource

### How to Fix

Re-read the resource and re-apply:
```bash
kubectl get <resource> <name> -o yaml | kubectl replace -f -
```

Use strategic merge patch:
```bash
kubectl patch <resource> <name> --type=merge -p '{"spec":{"replicas":5}}'
```

### Examples

```bash
# Re-read and re-apply safely
RESOURCE=$(kubectl get deployment my-app -o yaml)
echo "$RESOURCE" | sed 's/replicas: [0-9]*/replicas: 5/' | kubectl replace -f -
```"""),

    # ===== LOAD BALANCER / SERVICE =====

    ("loadbalancer-pending", "LoadBalancer Pending",
     "Fix Kubernetes LoadBalancer service stuck in Pending state. Resolve issues when a Service of type LoadBalancer does not get an external IP.",
     """## LoadBalancer Pending

`<service>   LoadBalancer   <cluster-ip>   <pending>     80:30080/TCP`

This issue occurs when a LoadBalancer service cannot get an external IP address from the cloud provider.

### Common Causes

- Running on-premises or bare-metal without a load balancer controller
- Cloud provider load balancer quota exceeded
- MetalLB or other LB controller not installed
- Service annotation misconfiguration

### How to Fix

Check the service events:
```bash
kubectl describe service <name>
```

Install a load balancer controller (for on-premises):
```bash
# MetalLB
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14/config/manifests/metallb-native.yaml
```

### Examples

```bash
# Check service events
kubectl describe service my-service | grep -A10 Events
#  Error: error creating load balancer: Quota exceeded

# Install MetalLB
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14/config/manifests/metallb-native.yaml
```"""),

    # ===== JOBS / CRONJOBS =====

    ("job-failed", "Job failed",
     "Fix Kubernetes Job failures. Resolve Job pods that terminate with non-zero exit codes or exceed the backoff limit.",
     """## Job Failed

`Job <name> has reached the specified backoff limit`

This occurs when a Kubernetes Job's pods keep failing and the backoff limit has been reached.

### Common Causes

- Application in the container crashes or exits with non-zero
- Missing environment variables or configuration
- Resource limits too low
- Service dependency unavailable

### How to Fix

Check job status:
```bash
kubectl describe job <name>
```

View logs of the failed pod:
```bash
kubectl logs job/<name>
```

Increase backoffLimit:
```yaml
spec:
  backoffLimit: 6
```

### Examples

```bash
# Check job pod logs
kubectl logs job/my-job

# View job events
kubectl describe job my-job
# BackoffLimit reached
```"""),

    # ===== CONFIGMAP / SECRET =====

    ("secret-not-found-k8s", "Secret not found in Kubernetes",
     "Fix Kubernetes 'secret not found' error. Resolve pod failures when a referenced Secret does not exist.",
     """## Secret Not Found

`secret "<name>" not found`

This error occurs when a pod references a Secret (via env, volume, or imagePullSecrets) that does not exist in the namespace.

### Common Causes

- Secret name is misspelled
- Secret has not been created yet
- Secret was deleted
- Secret is in a different namespace

### How to Fix

List secrets:
```bash
kubectl get secrets
```

Create the secret:
```bash
kubectl create secret generic <name> --from-literal=key=value
```

### Examples

```bash
# Create secret from literal
kubectl create secret generic app-secret --from-literal=api-key=abc123

# Create secret from file
kubectl create secret generic app-secret --from-file=./config.json
```"""),

    ("configmap-not-found", "ConfigMap not found",
     "Fix Kubernetes 'configmap not found' error. Resolve pod failures when a referenced ConfigMap does not exist.",
     """## ConfigMap Not Found

`configmap "<name>" not found`

This error occurs when a pod references a ConfigMap that does not exist in the namespace.

### Common Causes

- ConfigMap name is misspelled
- ConfigMap has not been created
- ConfigMap was deleted
- ConfigMap is in a different namespace

### How to Fix

List ConfigMaps:
```bash
kubectl get configmaps
```

Create the ConfigMap:
```bash
kubectl create configmap <name> --from-file=config.yaml
```

### Examples

```bash
# Create ConfigMap from file
kubectl create configmap app-config --from-file=./app.properties

# Create ConfigMap from literal
kubectl create configmap app-config --from-literal=LOG_LEVEL=debug
```"""),

    # ===== CONTAINER RUNTIME =====

    ("containerd-not-running", "containerd not running",
     "Fix Kubernetes containerd service failures. Resolve container runtime issues on worker nodes.",
     """## Containerd Not Running

`failed to connect to containerd: connection refused`

This error occurs when the kubelet cannot connect to the containerd (or CRI-O) socket.

### Common Causes

- containerd service stopped or crashed
- containerd socket (/var/run/containerd/containerd.sock) is missing
- containerd configuration is invalid
- Disk space exhausted

### How to Fix

SSH to the node and check containerd:
```bash
sudo systemctl status containerd
sudo journalctl -u containerd --no-pager --tail=100
```

Start containerd:
```bash
sudo systemctl start containerd
sudo systemctl enable containerd
```

### Examples

```bash
# Check containerd status
ssh <node> sudo systemctl status containerd
# containerd.service - Container Runtime
#    Active: failed (Result: exit-code)

# Start containerd
ssh <node> sudo systemctl start containerd
```"""),

    # ===== NODE MAINTENANCE =====

    ("drain-failed", "kubectl drain failed",
     "Fix 'kubectl drain' errors. Resolve node drain failures when evicting pods for maintenance.",
     """## Drain Failed

`error: unable to drain node "<node>" due to <reason>`

This error occurs when `kubectl drain` cannot evict pods from a node. Draining is required before node maintenance or removal.

### Common Causes

- PodDisruptionBudget (PDB) prevents eviction
- DaemonSet pods cannot be evicted (need --ignore-daemonsets)
- Pods with emptyDir volumes (need --delete-emptydir-data)
- Unmanaged pods not part of a controller

### How to Fix

Use drain with appropriate flags:
```bash
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data --force
```

Check PDBs:
```bash
kubectl get pdb --all-namespaces
```

### Examples

```bash
# Drain node with all options
kubectl drain node-3 --ignore-daemonsets --delete-emptydir-data --grace-period=120

# Check PDB blocking drain
kubectl get pdb --all-namespaces | grep -v "Allowed disruption.*>="
```"""),

    # ===== POD TERMINATION =====

    ("pod-stuck-terminating", "Pod stuck in Terminating",
     "Fix Kubernetes pod stuck in Terminating state. Resolve pods that cannot be deleted.",
     """## Pod Stuck in Terminating

A pod stuck in Terminating means the kubelet has received the deletion request but cannot stop the container(s).

### Common Causes

- Container has a process that ignores SIGTERM and SIGKILL
- PreStop hook is hanging or running indefinitely
- terminationGracePeriodSeconds is very high
- Node is unreachable (NotReady)
- Volume mount issues preventing umount

### How to Fix

Force delete a pod:
```bash
kubectl delete pod <name> --grace-period=0 --force
```

Remove finalizers:
```bash
kubectl patch pod <name> -p '{"metadata":{"finalizers":[]}}' --type=merge
```

### Examples

```bash
# Force delete terminating pod
kubectl delete pod my-app-xxx --grace-period=0 --force

# Remove finalizers from stuck pod
kubectl patch pod my-app-xxx -p '{"metadata":{"finalizers":[]}}' --type=merge
```"""),

    # ===== NETWORK POLICY =====

    ("network-policy-blocking", "Network policy blocking pod communication",
     "Fix Kubernetes network policy blocking inter-pod communication. Resolve connectivity failures caused by restrictive NetworkPolicies.",
     """## Network Policy Blocking Communication

This error occurs when a NetworkPolicy is blocking traffic between pods that need to communicate.

### Common Causes

- Default deny-all network policy is too restrictive
- Missing ingress rules for required traffic
- Missing egress rules for required outbound traffic
- Policy selector does not match source or target pods

### How to Fix

List network policies:
```bash
kubectl get networkpolicy --all-namespaces
```

Check pod labels vs policy selectors:
```bash
kubectl describe networkpolicy <name>
```

Test connectivity:
```bash
kubectl run test-$RANDOM --image=busybox -it --rm -- wget -O- http://<service>:<port>
```

### Examples

```bash
# Test connectivity between pods
kubectl run tester --image=busybox -it --rm -- wget -O- --timeout=3 http://my-service:8080
# wget: download timed out

# List all network policies
kubectl get networkpolicy --all-namespaces
```"""),

    # ===== RESOURCE QUOTA =====

    ("exceeded-quota", "Resource quota exceeded",
     "Fix Kubernetes 'exceeded quota' error. Resolve resource creation failures when namespace quotas are reached.",
     """## Resource Quota Exceeded

`exceeded quota: <quota-name>, requested: <resource>, used: <resource>, limited: <resource>`

This error occurs when a namespace has a ResourceQuota and the new resource would exceed the quota limits.

### Common Causes

- Namespace CPU or memory quota exhausted
- Pod count quota exceeded
- PVC count or storage quota exceeded
- Quotas set too restrictive

### How to Fix

Check quota usage:
```bash
kubectl get quota -n <namespace>
kubectl describe quota <name> -n <namespace>
```

Increase quota:
```bash
kubectl edit quota <name> -n <namespace>
```

Delete unnecessary resources to free up quota.

### Examples

```bash
# Check quota status
kubectl describe quota my-quota -n my-ns
# Resource     Used  Hard
# --------     ---   ---
# pods         45    50
# requests.cpu  8     10

# Free up resources
kubectl delete pod -n my-ns --field-selector=status.phase=Succeeded
```"""),

    ("limitrange-violation", "LimitRange violation",
     "Fix Kubernetes LimitRange violations. Resolve pod creation failures when resource limits do not comply with namespace LimitRange.",
     """## LimitRange Violation

This error occurs when a pod's resource requests or limits do not comply with the LimitRange constraints in the namespace.

### Common Causes

- Pod has no resource requests set but LimitRange requires them
- Pod requests are below the minimum LimitRange
- Pod limits exceed the maximum LimitRange

### How to Fix

Check LimitRange:
```bash
kubectl describe limitrange <name> -n <namespace>
```

Set resource requests on the pod:
```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
```

### Examples

```bash
# Check LimitRange constraints
kubectl describe limitrange my-limits -n my-ns
# Type      Resource  Min    Max     Default Request  Default Limit
# Container cpu       100m   1       200m             500m

# Fix pod with no requests
kubectl set resources deployment/my-app --requests=cpu=100m,memory=128Mi
```"""),

    # ===== CERT-MANAGER =====

    ("cert-manager-certificate-failed", "cert-manager certificate issuance failed",
     "Fix cert-manager certificate issuance failures in Kubernetes. Resolve TLS certificate provisioning errors.",
     """## cert-manager Certificate Failed

`Certificate <name> failed: <error>`

This error occurs when cert-manager cannot issue a TLS certificate from the configured issuer.

### Common Causes

- ACME issuer cannot validate the domain (HTTP-01 or DNS-01)
- Ingress not configured for HTTP-01 challenge
- DNS provider credentials incorrect for DNS-01
- Certificate request exceeds rate limits (Let's Encrypt)

### How to Fix

Check certificate status:
```bash
kubectl describe certificate <name>
kubectl describe certificaterequest <name>
```

Check issuer:
```bash
kubectl describe issuer <name>
kubectl describe clusterissuer <name>
```

### Examples

```bash
# Check certificate
kubectl describe certificate my-cert
#  Reason: Failed
#  Message: Failed to complete ACME challenge

# Check challenges
kubectl get challenges
kubectl describe challenge my-cert-xxx
#  Type: dns-01
#  Status: pending
```"""),

    # ===== POD PRIORITY =====

    ("pod-preempted", "Pod was preempted by higher priority pod",
     "Fix Kubernetes pod preemption. Resolve issues when a lower-priority pod is evicted for a higher-priority pod.",
     """## Pod Preempted

This occurs when a higher-priority pod cannot be scheduled and the scheduler preempts (evicts) a lower-priority pod to free resources.

### Common Causes

- Higher priority pod needs resources on a full node
- PriorityClass values not balanced properly
- Critical pods preempting non-critical ones

### How to Fix

Check priority classes:
```bash
kubectl get priorityclass
```

Adjust pod priority:
```yaml
priorityClassName: low-priority
```

### Examples

```bash
# Check PriorityClasses
kubectl get priorityclass
# system-cluster-critical   2000000000   true
# system-node-critical      2000001000   true

# Create a low priority class
kubectl create priorityclass low-priority --value=100 --global-default=false
```"""),

    # ===== DOCKER HUB RATE LIMIT =====

    ("rate-limit-docker-hub", "Docker Hub rate limited in Kubernetes",
     "Fix Kubernetes Docker Hub rate limiting errors. Resolve image pull failures when Docker Hub rate limits are exceeded.",
     """## Docker Hub Rate Limited

`toomanyrequests: You have reached your pull rate limit`

This error occurs when you exceed Docker Hub's anonymous (100 pulls/6h) or authenticated (200 pulls/6h) rate limits.

### Common Causes

- Cluster nodes pulling images without authentication
- High number of pod replicas restarting or rolling out
- Many nodes pulling the same image simultaneously

### How to Fix

Add Docker Hub credentials:
```bash
kubectl create secret docker-registry dockerhub \\
  --docker-username=<user> \\
  --docker-password=<token>
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"dockerhub"}]}'
```

Use imagePullPolicy: IfNotPresent to cache images:
```yaml
imagePullPolicy: IfNotPresent
```

### Examples

```bash
# Create image pull secret
kubectl create secret docker-registry regcred \\
  --docker-server=https://index.docker.io/v1/ \\
  --docker-username=myuser \\
  --docker-password=$(cat ~/dockerhub-token)

# Add to default service account
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"regcred"}]}'
```"""),

    # ===== VELERO BACKUP =====

    ("velero-backup-failed", "Velero backup failed",
     "Fix Velero backup failures in Kubernetes. Resolve issues with cluster backup and restore operations.",
     """## Velero Backup Failed

`Backup <name> failed: <error>`

This error occurs when Velero cannot complete a backup operation for a Kubernetes cluster.

### Common Causes

- Volume snapshot failed (CSI driver not installed)
- Cloud provider API permissions insufficient
- Backup location (S3, GCS, Azure Blob) is unreachable
- Backup storage bucket does not exist

### How to Fix

Check backup status:
```bash
velero backup describe <name> --details
kubectl logs -n velero deployment/velero
```

### Examples

```bash
# Check Velero backup
velero backup get
velero backup describe my-backup --details

# View failed backup details
velero backup logs my-backup | tail -50
```"""),

    # ===== CLUSTER AUTOSCALER =====

    ("cluster-autoscaler-failed", "Cluster autoscaler failed to scale",
     "Fix Kubernetes cluster autoscaler errors. Resolve issues when the cluster autoscaler cannot add or remove nodes.",
     """## Cluster Autoscaler Failed

`failed to scale up: AccessDenied`

This error occurs when the cluster autoscaler cannot add nodes due to cloud provider issues.

### Common Causes

- Cloud provider API permissions insufficient
- Instance quota exceeded in the cloud region
- Instance type unavailable in the availability zone
- Autoscaling group configuration issues

### How to Fix

Check cluster autoscaler logs:
```bash
kubectl logs -n kube-system deployment/cluster-autoscaler
```

### Examples

```bash
# Check cluster autoscaler status
kubectl get pods -n kube-system | grep autoscaler
# cluster-autoscaler-xxx   1/1   Running

# View autoscaler logs
kubectl logs -n kube-system deployment/cluster-autoscaler --tail=100
```"""),

    # ===== KUBERNETES VERSION =====

    ("kubelet-version-mismatch", "Kubelet version mismatch",
     "Fix Kubernetes kubelet version mismatch errors. Resolve issues when kubelet version differs from the API server version.",
     """## Kubelet Version Mismatch

This error occurs when the kubelet version on a node is too far behind or ahead of the API server version.

### Common Causes

- Node not upgraded after control plane upgrade
- New node added with outdated kubelet version
- Mixing very different Kubernetes versions

### How to Fix

Check versions:
```bash
kubectl version
kubectl get nodes -o wide
```

Upgrade kubelet on the node:
```bash
sudo apt-get update && sudo apt-get install -y kubelet=<version>
sudo systemctl restart kubelet
```

### Examples

```bash
# Check node kubelet versions
kubectl get nodes -o wide | awk '{print $1, $7}'
# node-1   v1.28.3
# node-2   v1.27.1  (outdated)

# Upgrade kubelet on node-2
ssh node-2 "sudo apt-get install -y kubelet=1.28.3-00 && sudo systemctl restart kubelet"
```"""),

    # ===== NODE DISK FULL =====

    ("node-disk-full", "Node disk full",
     "Fix Kubernetes node disk full errors. Resolve pod failures and node issues caused by exhausted disk space.",
     """## Node Disk Full

`No space left on device`

This error occurs when the node's disk is completely full. Pods may fail to start, crash, or be evicted.

### Common Causes

- Container logs filling up disk space
- Docker/containerd image cache consuming space
- Application logs not rotated
- Node has small root partition

### How to Fix

SSH to the node and check disk usage:
```bash
df -h
du -sh /var/log/
du -sh /var/lib/docker/
```

Clean up disk space:
```bash
docker system prune -a -f
sudo journalctl --vacuum-size=500M
sudo find /var/log -name "*.log" -mtime +7 -delete
```

### Examples

```bash
# Check disk space on node
ssh <node> df -h
# /dev/sda1   50G   48G   2G   96% /

# Prune Docker system
ssh <node> "docker system prune -a -f"
```"""),

    # ===== POD SECURITY POLICY (deprecated) =====

    ("psp-denied", "PodSecurityPolicy denied (deprecated in 1.25)",
     "Fix Kubernetes PodSecurityPolicy denied error (deprecated). Resolve pod creation failures blocked by PSP rules (replaced by Pod Security Admission).",
     """## PodSecurityPolicy Denied (Deprecated)

`pod "<name>" is forbidden: unable to validate against any pod security policy: <reason>`

This error occurs when no PodSecurityPolicy (PSP, deprecated in 1.25) allows the pod's security context. PSP has been replaced by Pod Security Admission.

### Common Causes

- No PSP is defined in the cluster
- Pod requires privileged access but no PSP allows it
- Pod uses host network, hostPID, or hostIPC
- Pod runs as root without allowPrivilegeEscalation: false

### How to Fix

Create a permissive PSP (if still using PSP):
```yaml
apiVersion: policy/v1beta1
kind: PodSecurityPolicy
metadata:
  name: permissive
spec:
  privileged: true
  seLinux:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  fsGroup:
    rule: RunAsAny
  volumes:
  - '*'
```

### Examples

```bash
# List existing PSPs
kubectl get psp
# No resources found

# Create permissive PSP
kubectl apply -f permissive-psp.yaml
```"""),

    # ===== PROMETHEUS =====

    ("prometheus-k8s-target-down", "Prometheus target down in Kubernetes",
     "Fix Kubernetes Prometheus target down errors. Resolve Prometheus monitoring failures in the cluster.",
     """## Prometheus Target Down

`Get "<url>": dial tcp <ip>:<port>: connect: connection refused`

This error occurs when Prometheus cannot scrape metrics from a target that has been discovered via service or pod annotations.

### Common Causes

- Target pod or service is not running
- Network policy blocking Prometheus traffic
- Target is listening on localhost instead of 0.0.0.0
- ServiceMonitor / PodMonitor misconfiguration

### How to Fix

Check the target endpoint:
```bash
kubectl get pod -l <selector> -o wide
```

Test connectivity from Prometheus pod:
```bash
kubectl exec -n monitoring prometheus-0 -- wget -O- http://<target-ip>:<port>/metrics
```

### Examples

```bash
# Test metric endpoint manually
kubectl port-forward service/my-app 8080:8080
curl http://localhost:8080/metrics

# Check Prometheus target status
kubectl port-forward service/prometheus 9090:9090
# Open http://localhost:9090/targets
```"""),

    # ===== GATEWAY API =====

    ("gateway-api-error", "Gateway API error",
     "Fix Kubernetes Gateway API errors. Resolve issues with Gateway, GatewayClass, and HTTPRoute resources.",
     """## Gateway API Error

`The Gateway "<name>" is not ready`

This error occurs when a Gateway API resource is not in a ready state, preventing HTTPRoute traffic routing.

### Common Causes

- GatewayClass does not exist or is not supported
- Gateway controller is not installed
- Gateway configuration is invalid
- Listener hostname conflict

### How to Fix

Check GatewayClass:
```bash
kubectl get gatewayclass
kubectl describe gatewayclass <name>
```

Check Gateway:
```bash
kubectl describe gateway <name>
```

### Examples

```bash
# Check Gateway API resources
kubectl get gatewayclass,gw,httproute

# Describe Gateway
kubectl describe gateway my-gateway
```"""),

    # ===== CRI RUNTIME ERROR =====

    ("cri-runtime-error", "CRI runtime error",
     "Fix Kubernetes CRI runtime errors. Resolve Container Runtime Interface failures between kubelet and containerd/CRI-O.",
     """## CRI Runtime Error

`failed to "CreateContainer" for "<container>" with CreateContainerError`

This error occurs when the CRI runtime (containerd/CRI-O) cannot create a container as requested by the kubelet.

### Common Causes

- Container runtime daemon is not responding
- OCI runtime (runc) errors during container creation
- Cgroup configuration issues
- Kernel security module (AppArmor, SELinux) blocking

### How to Fix

Check container runtime logs:
```bash
sudo journalctl -u containerd --no-pager --tail=100
sudo journalctl -u crio --no-pager --tail=100
```

### Examples

```bash
# Check containerd CRI errors
journalctl -u containerd --no-pager --tail=50 | grep -i "createcontainer\\|CreateContainerError"
```"""),

    # ===== EXPAND VOLUME =====

    ("expand-in-use-volume", "ExpandInUseVolume",
     "Fix Kubernetes ExpandInUseVolume error. Resolve issues when expanding a persistent volume that is in use by a pod.",
     """## ExpandInUseVolume

This error occurs when attempting to expand a PersistentVolumeClaim that is in use by a running pod. Kubernetes supports online volume expansion but may encounter issues.

### Common Causes

- StorageClass does not support allowVolumeExpansion
- Filesystem resizing fails on the node
- Volume driver does not support online expansion

### How to Fix

Check if the StorageClass supports expansion:
```bash
kubectl get storageclass <name> -o yaml | grep allowVolumeExpansion
```

Edit PVC to request more storage:
```bash
kubectl edit pvc <name>
# Change spec.resources.requests.storage
```

### Examples

```bash
# Enable volume expansion on StorageClass
kubectl patch storageclass gp2 -p '{"allowVolumeExpansion":true}'

# Resize PVC
kubectl patch pvc my-claim -p '{"spec":{"resources":{"requests":{"storage":"20Gi"}}}}'
```"""),

    # ===== VOLUME EXPANSION FAILED =====

    ("volume-expansion-failed", "Persistent volume expansion failed",
     "Fix Kubernetes persistent volume expansion failures. Resolve issues when filesystem resizing fails after storage backend expansion.",
     """## Volume Expansion Failed

`FileSystemResizeFailed`

This error occurs when the filesystem resize fails after the volume has been expanded in the storage backend.

### Common Causes

- Filesystem type not supported for online resize
- Volume is not in use (filesystem resize requires a running pod)
- Node kernel missing filesystem resize support

### How to Fix

Check PVC status:
```bash
kubectl describe pvc <name> | grep -i "resize\\|expansion"
```

Manually resize the filesystem:
```bash
# For ext4: resize2fs <device>
# For xfs: xfs_growfs <mount-point>
```

### Examples

```bash
# Check PVC events for resize failure
kubectl describe pvc my-claim | grep -A5 Events
#  FileSystemResizeFailed

# Check StorageClass
kubectl get sc gp2 -o yaml | grep allowVolumeExpansion
# false

# Enable expansion
kubectl patch sc gp2 -p '{"allowVolumeExpansion":true}'
```"""),

    # ===== VOLUME NODE AFFINITY =====

    ("volume-node-affinity-conflict", "VolumeNodeAffinityConflict",
     "Fix Kubernetes VolumeNodeAffinityConflict error. Resolve pod scheduling failures when volumes have node affinity constraints.",
     """## VolumeNodeAffinityConflict

This error occurs when a pod requests a volume that has node affinity constraints and no available node matches both the pod's scheduling constraints and the volume's node affinity.

### Common Causes

- PV has node affinity for a specific zone or node
- The node with the PV data is unavailable or cordoned
- Volume is in a different availability zone

### How to Fix

Check PV node affinity:
```bash
kubectl get pv <name> -o yaml | grep -A10 nodeAffinity
```

List nodes in the required topology zone:
```bash
kubectl get nodes -l topology.kubernetes.io/zone=<zone>
```

### Examples

```bash
# View PV topology constraints
kubectl get pv pvc-xxxx -o yaml | grep -A5 "nodeAffinity"

# Schedule pod to correct zone
kubectl run my-app --image=nginx --overrides='{"spec":{"nodeSelector":{"topology.kubernetes.io/zone":"us-east-1a"}}}'
```"""),

    # ===== SYSTEM OOM =====

    ("pod-oom-killed-system", "System OOM killed (node-level)",
     "Fix Kubernetes node-level OOM kills. Resolve issues where the Linux OOM killer terminates processes when the node runs out of memory.",
     """## System OOM Killed (Node-Level)

`oom_kill_process: Kill process <pid> (<name>) score <n> or a child of cgroup`

This is a node-level event where the Linux OOM killer terminates processes because the entire node is out of memory.

### Common Causes

- Node memory is overcommitted by pods
- No resource limits set on memory-hungry pods
- BestEffort pods consuming all available memory

### How to Fix

Check node memory:
```bash
kubectl top node <node-name>
```

Check pod memory usage:
```bash
kubectl top pods --all-namespaces --sort-by=memory | head -10
```

### Examples

```bash
# Find top memory consumers
kubectl top pods --all-namespaces --sort-by=memory | head -10

# Check for OOM kills in kernel logs
ssh <node> sudo dmesg | grep -i "oom_kill"
```"""),

    # ===== KURED / NODE REBOOT =====

    ("kured-node-reboot-failed", "Kured node reboot failed",
     "Fix Kured (Kubernetes Reboot Daemon) node reboot failures. Resolve issues when automatic node reboot fails.",
     """## Kured Node Reboot Failed

This error occurs when Kured (Kubernetes Reboot Daemon) cannot reboot a node that requires a reboot (e.g., pending kernel update).

### Common Causes

- Cordon succeeded but drain failed (PDB blocking)
- Reboot command not found (reboot binary missing)
- Kured not configured for the cloud provider

### How to Fix

Check Kured logs:
```bash
kubectl logs -n kube-system -l app.kubernetes.io/name=kured
```

### Examples

```bash
# Check Kured logs
kubectl logs -n kube-system -l app.kubernetes.io/name=kured --tail=50
```"""),

    # ===== CRD NOT FOUND =====

    ("crd-not-found", "CustomResourceDefinition not found",
     "Fix Kubernetes CRD not found error. Resolve issues when custom resources cannot be created because the CRD is missing.",
     """## CRD Not Found

`the server could not find the requested resource (post <resource>.example.com)`

This error occurs when you try to create a custom resource but the CustomResourceDefinition (CRD) has not been installed.

### Common Causes

- CRD manifest has not been applied
- CRD was deleted
- CRD name or API group does not match the custom resource

### How to Fix

List installed CRDs:
```bash
kubectl get crd
```

Install the CRD:
```bash
kubectl apply -f crd.yaml
```

### Examples

```bash
# List custom resources
kubectl get crd | grep -i "example.com"

# Install CRD
kubectl apply -f https://example.com/crd.yaml
```"""),

    # ===== ETCD =====

    ("etcd-leader-election", "etcd leader election failed",
     "Fix Kubernetes etcd leader election failures. Resolve etcd cluster health issues affecting the control plane.",
     """## etcd Leader Election Failed

`etcdserver: no leader`

This error occurs when the etcd cluster cannot elect a leader. Without a leader, etcd cannot process writes.

### Common Causes

- etcd member(s) are down or unreachable
- Network partition between etcd members
- Disk I/O latency too high (slow disks)
- etcd cluster has lost quorum

### How to Fix

Check etcd member health:
```bash
kubectl get pods -n kube-system -l component=etcd
```

Check etcd logs:
```bash
kubectl logs -n kube-system etcd-<node>
```

### Examples

```bash
# Check etcd cluster status
kubectl exec -n kube-system etcd-control-plane -- etcdctl endpoint status --cluster
# https://node1:2379 is unhealthy

# Check disk latency
ssh control-plane dd if=/dev/zero of=/tmp/test bs=8k count=15000 oflag=direct
# Should be under 10ms for healthy etcd
```"""),

    # ===== CRONJOB =====

    ("cronjob-missed-schedule", "CronJob missed its schedule",
     "Fix Kubernetes CronJob 'missed schedule' errors. Resolve CronJobs that fail to create Jobs on time.",
     """## CronJob Missed Schedule

This error occurs when the CronJob controller misses a scheduled run.

### Common Causes

- CronJob controller pod is not running or restarting
- Cluster was down during the scheduled time
- Controller is overloaded with too many CronJobs
- ConcurrencyPolicy is set to Forbid and previous job is still running

### How to Fix

Increase startingDeadlineSeconds:
```yaml
spec:
  startingDeadlineSeconds: 300
```

### Examples

```bash
# Check CronJob status
kubectl describe cronjob my-cronjob | grep -i "missed\\|last schedule"

# Increase deadline
kubectl patch cronjob my-cronjob -p '{"spec":{"startingDeadlineSeconds":300}}'
```"""),

    # ===== NODE CORDONED =====

    ("node-cordoned", "Node is cordoned",
     "Fix Kubernetes 'node is cordoned' scheduling errors. Resolve pod scheduling failures when nodes are cordoned for maintenance.",
     """## Node Is Cordoned

This warning or scheduling failure occurs when a node has been cordoned (marked as unschedulable). No new pods can be scheduled on it.

### Common Causes

- Node was cordoned for maintenance or upgrades
- `kubectl cordon` was run on the node
- Node was drained and not uncordoned

### How to Fix

List cordoned nodes:
```bash
kubectl get nodes | grep SchedulingDisabled
```

Uncordon the node:
```bash
kubectl uncordon <node-name>
```

### Examples

```bash
# Find all cordoned nodes
kubectl get nodes | grep SchedulingDisabled
# node-3   NotReady   SchedulingDisabled

# Uncordon node
kubectl uncordon node-3
```"""),
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
