#!/usr/bin/env python3
"""Generate final Kubernetes error pages (batch 3)"""
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
    # More Istio/service mesh
    ("istio-sidecar-injection-failed", "Istio sidecar injection failed",
     "Fix Istio sidecar injection failures in Kubernetes. Resolve issues when the Istio sidecar proxy is not injected into pods.",
     """## Istio Sidecar Injection Failed

`istio-sidecar-injector: Sidecar injection failed: failed to inject sidecar`

This error occurs when Istio cannot inject the Envoy sidecar proxy into a pod.

### Common Causes

- Namespace does not have the `istio-injection: enabled` label
- Istio sidecar injector is not installed or not running
- Pod annotations disable injection (`sidecar.istio.io/inject: "false"`)
- Resource limits too low for sidecar
- Istio version incompatibility
- Webhook timeout during injection

### How to Fix

Check namespace label:
```bash
kubectl get ns <namespace> --show-labels | grep istio
```

Enable injection on the namespace:
```bash
kubectl label ns <namespace> istio-injection=enabled --overwrite
```

Check the sidecar injector status:
```bash
kubectl get pods -n istio-system | grep sidecar-injector
```

Restart the pod after enabling injection:
```bash
kubectl rollout restart deployment/<name>
```

### Examples

```bash
# Enable Istio injection
kubectl label ns default istio-injection=enabled

# Verify injection
kubectl describe pod <name> | grep -i istio
# Should show istio-proxy container
```"""),

    ("helm-install-failed-k8s", "Helm install failed in Kubernetes",
     "Fix Helm install failures in Kubernetes. Resolve errors when deploying Helm charts.",
     """## Helm Install Failed

`Error: failed post-install: timed out waiting for the condition`

This error occurs when a Helm chart installation times out or fails.

### Common Causes

- Resource creation timeout (pods not becoming Ready)
- Missing required values
- CRDs not installed
- Resource already exists
- Insufficient cluster resources
- Helm chart has invalid templates

### How to Fix

Check the Helm release status:
```bash
helm status <release>
```

View detailed error:
```bash
helm get manifest <release> | kubectl apply --dry-run=server -f -
```

Rollback failed release:
```bash
helm rollback <release> <revision>
```

Install with increased timeout:
```bash
helm install <release> <chart> --timeout 10m
```

### Examples

```bash
# Install with debug output
helm install my-app ./chart --debug --timeout 10m

# Check release status
helm list -a
helm status my-app
```"""),

    ("kustomize-build-error", "Kustomize build error",
     "Fix Kustomize build errors in Kubernetes. Resolve issues when building Kubernetes manifests with Kustomize.",
     """## Kustomize Build Error

`Error: accumulating resources: accumulation err: ...`

This error occurs when `kubectl kustomize` or `kustomize build` fails to generate Kubernetes manifests.

### Common Causes

- Resource file not found in the specified path
- Invalid YAML in base or overlay files
- Patch does not match the target resource
- Name prefix/suffix conflicts
- Duplicate resource names after transformation
- CRD not found when using vars or replacements

### How to Fix

Check the kustomization.yaml syntax:
```bash
kustomize build <dir> 2>&1
```

Validate individual resource files:
```bash
kubectl apply -f <file> --dry-run=server
```

Use `--load-restrictor` for loading resources from outside the root:
```bash
kustomize build --load-restrictor LoadRestrictionsNone <dir>
```

### Examples

```bash
# Build and check for errors
kustomize build overlays/production/ 2>&1

# Validate output
kustomize build overlays/production/ | kubectl apply --dry-run=server -f -
```"""),

    ("container-restart-policy", "Container restart policy error",
     "Fix Kubernetes container restart policy issues. Resolve pods that restart unexpectedly or not at all.",
     """## Container Restart Policy

Kubernetes uses the pod's `restartPolicy` to determine when to restart containers. Misconfiguration can cause unexpected behavior.

### Restart Policies

- `Always` (default for Deployments): always restart
- `OnFailure`: restart only on non-zero exit codes
- `Never`: never restart (used for Jobs)

### Common Causes

- restartPolicy set to Never for a deployment (stuck in Terminating)
- restartPolicy set to Always for a Job (never completes)
- Exit code 0 with Always policy causes unnecessary restart
- Sidecar containers with Always policy restarting the pod
- Pod marked as Failed even though container completed

### How to Fix

Check restart policy:
```bash
kubectl get pod <name> -o jsonpath='{.spec.restartPolicy}'
```

Update the restart policy:
```bash
kubectl patch deployment <name> -p '{"spec":{"template":{"spec":{"restartPolicy":"Always"}}}}'
```

### Examples

```bash
# Check pod restart policy
kubectl get pod my-job-xxx -o jsonpath='{.spec.restartPolicy}'

# For Jobs, use OnFailure or Never
# For Deployments, Always must be used
```"""),

    # More containerd errors
    ("sandbox-image-pull-failed", "Sandbox image pull failed",
     "Fix Kubernetes sandbox image pull failures. Resolve errors when the container runtime cannot pull the pause (sandbox) image.",
     """## Sandbox Image Pull Failed

`Failed to create pod sandbox: failed to get sandbox image "registry.k8s.io/pause:3.9": failed to pull image`

This error occurs when the container runtime cannot pull the pause/sandbox image required for pod isolation.

### Common Causes

- pause image is not available in the configured registry
- Network connectivity issues to registry.k8s.io
- registry.k8s.io is not accessible from the node
- containerd sandbox_image configuration is incorrect
- Image pull rate limiting for pause image
- containerd cannot reach the configured sandbox registry

### How to Fix

Check the sandbox image configuration:
```bash
sudo cat /etc/containerd/config.toml | grep sandbox_image
```

Pull the sandbox image manually:
```bash
sudo crictl pull registry.k8s.io/pause:3.9
```

Configure a mirror registry for containerd:
```toml
[plugins."io.containerd.grpc.v1.cri".registry.mirrors."registry.k8s.io"]
  endpoint = ["https://mirror.gcr.io"]
```

### Examples

```bash
# Check sandbox image
sudo crictl images | grep pause
# registry.k8s.io/pause:3.9

# Pull sandbox image if missing
sudo crictl pull registry.k8s.io/pause:3.9
```"""),

    # More kube-proxy
    ("kube-proxy-not-running", "kube-proxy not running",
     "Fix Kubernetes kube-proxy not running errors. Resolve service connectivity issues when kube-proxy is down on a node.",
     """## kube-proxy Not Running

`kube-proxy: error running: error: could not start daemon`

This error occurs when kube-proxy is not running on a node, causing service traffic to fail.

### Common Causes

- kube-proxy DaemonSet pod is not running on the node
- kube-proxy configuration is invalid
- iptables/nftables kernel modules not loaded
- kube-proxy image not available
- kube-proxy cannot connect to the API server
- IPVS mode requires kernel modules

### How to Fix

Check kube-proxy pods:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-proxy
```

Check kube-proxy logs:
```bash
kubectl logs -n kube-system -l k8s-app=kube-proxy
```

Restart kube-proxy:
```bash
kubectl delete pod -n kube-system -l k8s-app=kube-proxy
```

### Examples

```bash
# Check kube-proxy status
kubectl get pods -n kube-system | grep kube-proxy
# kube-proxy-xxxxx   0/1   CrashLoopBackOff

# View kube-proxy logs
kubectl logs -n kube-system kube-proxy-xxxxx
```"""),

    # More cluster operations
    ("token-expired-bootstrap", "Bootstrap token expired",
     "Fix Kubernetes bootstrap token expiration errors. Resolve node join failures when the cluster bootstrap token has expired.",
     """## Bootstrap Token Expired

`[discovery] Failed to request cluster-info, will try again: Get "https://<ip>:6443/api/v1/namespaces/kube-public/configmaps/cluster-info": x509: certificate has expired or is not yet valid`

This error occurs when the bootstrap token used to join a node to the cluster has expired.

### Common Causes

- Default token expiration (24 hours) has passed
- Token was deleted after use
- Cluster was created and node joined too late
- Token creation date is not tracked properly
- Manual token deletion

### How to Fix

Create a new bootstrap token on the control plane:
```bash
kubeadm token create
```

List existing tokens:
```bash
kubeadm token list
```

Create a token with longer expiration:
```bash
kubeadm token create --ttl 48h0m0s
```

### Examples

```bash
# Create new token
TOKEN=$(kubeadm token create)
echo $TOKEN

# Get the full join command
kubeadm token create --print-join-command
```"""),

    ("kubelet-config-invalid", "Kubelet configuration invalid",
     "Fix Kubernetes kubelet configuration validation errors. Resolve kubelet startup failures due to invalid configuration.",
     """## Kubelet Configuration Invalid

`failed to run kubelet: the component is using a deprecated or unknown configuration`

This error occurs when the kubelet configuration file has validation errors.

### Common Causes

- Kubelet config has invalid or unsupported fields
- Configuration version mismatch
- Feature gate names are misspelled
- Resource limits are negative or zero
- Duplicate configuration keys
- Configuration file has YAML syntax errors

### How to Fix

Validate the kubelet config:
```bash
sudo kubelet --validate-config --config /var/lib/kubelet/config.yaml
```

Check for deprecation warnings:
```bash
sudo journalctl -u kubelet --no-pager | grep -i "deprecated\\|unknown"
```

Regenerate the default configuration:
```bash
sudo kubelet --generate-config > /tmp/kubelet-config.yaml
# Compare with current config
```

### Examples

```bash
# Validate kubelet config
sudo kubelet --validate-config --config /var/lib/kubelet/config.yaml 2>&1

# Check for errors
sudo journalctl -u kubelet --no-pager --tail=50 | grep -i "error"
```"""),

    ("kubectl-proxy-error", "kubectl proxy error",
     "Fix kubectl proxy errors. Resolve issues when running kubectl proxy to access the Kubernetes API locally.",
     """## kubectl Proxy Error

`error: unable to listen on port 8001: Listen failed: listen tcp 127.0.0.1:8001: bind: address already in use`

This error occurs when kubectl proxy cannot start because the port is already in use.

### Common Causes

- Another kubectl proxy process is already running
- Another application is using port 8001
- Incorrect API server URL or unreachable
- TLS certificate issue with the proxy
- Permission denied to listen on the port

### How to Fix

Find and kill existing proxy:
```bash
pkill -f "kubectl proxy"
```

Use a different port:
```bash
kubectl proxy --port=8080
```

Check what is using the port:
```bash
lsof -i :8001
```

### Examples

```bash
# Kill existing proxy and restart on a different port
pkill -f "kubectl proxy" || true
kubectl proxy --port=8080 --accept-hosts='.*'

# Access API through proxy
curl http://localhost:8080/api/v1/namespaces
```"""),

    # More storage
    ("ceph-rbd-mount-failed", "Ceph RBD volume mount failed",
     "Fix Kubernetes Ceph RBD volume mount failures. Resolve persistent volume mount errors with Ceph RBD storage.",
     """## Ceph RBD Mount Failed

`MountVolume.SetUp failed for volume "<name>" : rbd: map failed: exit status 1`

This error occurs when Kubernetes cannot mount a Ceph RBD (RADOS Block Device) volume.

### Common Causes

- Ceph cluster is unreachable
- Ceph secret key incorrect or missing
- RBD image does not exist
- Kernel RBD module not loaded
- Ceph monitor addresses incorrect
- Cephx authentication failure
- Pool or image name incorrect

### How to Fix

Check Ceph cluster connectivity:
```bash
ceph -s
```

Verify the Ceph secret in Kubernetes:
```bash
kubectl get secret <ceph-secret> -o yaml
```

Install ceph-common on all nodes:
```bash
sudo apt-get install -y ceph-common
```

### Examples

```bash
# Check Ceph status
ceph -s
# cluster: id: xxxx, health: HEALTH_OK

# Verify the RBD image exists
rbd info <pool>/<image>
```"""),

    ("nfs-permission-denied", "NFS volume permission denied in Kubernetes",
     "Fix Kubernetes NFS volume permission denied errors. Resolve access issues when pods cannot read or write to NFS mounts.",
     """## NFS Permission Denied

`Permission denied` when accessing files on a mounted NFS volume

This error occurs when the container user does not have the correct permissions on the NFS exported directory.

### Common Causes

- Container runs as a non-root user but NFS files are owned by root
- NFS export has root_squash enabled (maps root to nobody)
- NFS directory permissions do not allow the container UID
- Pod securityContext runAsUser does not match NFS file ownership
- NFS export options restrict access
- SELinux blocking NFS access

### How to Fix

Set the pod's securityContext to match the NFS file ownership:
```yaml
securityContext:
  runAsUser: 1000
  runAsGroup: 1000
  fsGroup: 1000
```

Configure NFS export with no_root_squash (if using root):
```bash
# /etc/exports
/path/to/export *(rw,no_root_squash,no_subtree_check)
```

Check NFS mount permissions:
```bash
kubectl exec <pod> -- ls -la /mount/path
kubectl exec <pod> -- id
```

### Examples

```bash
# Check current user in container
kubectl exec my-pod -- id
# uid=1000(appuser) gid=1000(appuser)

# Fix file ownership on NFS server
sudo chown -R 1000:1000 /path/to/export
```"""),

    # More resource management
    ("cpu-manager-policy-error", "CPU Manager policy error",
     "Fix Kubernetes CPU Manager policy errors. Resolve issues when the CPU Manager configuration causes pod scheduling failures.",
     """## CPU Manager Policy Error

`Failed to start container: failed to set cpu_manager policy: error updating CPU manager`

This error occurs when the kubelet's CPU Manager policy configuration causes errors during pod startup.

### Common Causes

- CPU Manager policy set to `static` but node does not have exclusive CPUs
- CPU Manager state file is corrupted
- CPU Manager cannot allocate the requested CPUs
- kubelet restart with stale CPU manager state
- Insufficient CPU capacity for static policy
- SMT (Hyper-Threading) alignment issues

### How to Fix

Reset the CPU Manager state:
```bash
sudo systemctl stop kubelet
sudo rm -f /var/lib/kubelet/cpu_manager_state
sudo systemctl start kubelet
```

Change CPU Manager policy:
```bash
# In kubelet config
cpuManagerPolicy: none
```

### Examples

```bash
# Reset CPU manager state
sudo systemctl stop kubelet
sudo rm -f /var/lib/kubelet/cpu_manager_state
sudo systemctl start kubelet

# Check current policy
sudo cat /var/lib/kubelet/cpu_manager_state | jq .
```"""),

    # Final misc errors
    ("pod-anti-affinity-exceeded", "Pod anti-affinity rules preventing scheduling",
     "Fix Kubernetes pod anti-affinity rules that prevent all pods from being scheduled. Resolve when anti-affinity is too strict.",
     """## Pod Anti-Affinity Preventing Scheduling

This error occurs when pod anti-affinity rules are too strict and prevent any new pods from being scheduled.

### Common Causes

- requiredDuringScheduling anti-affinity with no overlap allowed
- Too many pods already running that match the anti-affinity
- Insufficient nodes to spread pods according to anti-affinity
- Same topology key on too few nodes
- Rolling update creates new pods before old ones are removed

### How to Fix

Change required to preferred:
```yaml
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
    ...
```

Increase the topology key scope:
```yaml
topologyKey: "topology.kubernetes.io/zone"  # instead of kubernetes.io/hostname
```

### Examples

```bash
# Change anti-affinity from required to preferred
kubectl patch deployment my-app --type=json -p='[{"op": "replace", "path": "/spec/template/spec/affinity/podAntiAffinity/requiredDuringSchedulingIgnoredDuringExecution", "value": null}]'
```"""),

    # Helm specific
    ("helm-upgrade-failed", "Helm upgrade failed",
     "Fix Helm upgrade failures in Kubernetes. Resolve errors when upgrading Helm releases.",
     """## Helm Upgrade Failed

`Error: UPGRADE FAILED: <release> has no deployed releases`

This error occurs when a Helm upgrade cannot find a deployed release to upgrade.

### Common Causes

- Release was deleted with `helm delete` but not `helm uninstall`
- Release history was purged
- Release name is misspelled
- Release is in a failed state
- Wrong Helm version compatibility

### How to Fix

Check release history:
```bash
helm history <release>
```

List all releases:
```bash
helm list -a
```

Reinstall instead of upgrade:
```bash
helm upgrade --install <release> <chart>
```

Force rollback to a working revision:
```bash
helm rollback <release> <revision>
```

### Examples

```bash
# Install or upgrade
helm upgrade --install my-app ./chart --namespace default --create-namespace

# Check release history
helm history my-app
# REVISION  STATUS     CHART
# 1         failed     my-app-1.0.0
# 2         deployed   my-app-1.0.1
```"""),

    # More config
    ("configmap-missing-key", "ConfigMap key not found",
     "Fix Kubernetes ConfigMap key not found errors. Resolve pod failures when a referenced ConfigMap key does not exist.",
     """## ConfigMap Key Not Found

This error occurs when a pod references a specific key from a ConfigMap that does not exist.

### Common Causes

- ConfigMap key name is misspelled
- ConfigMap key was renamed or removed
- Key name is case-sensitive
- Wrong ConfigMap referenced
- Key has special characters that need escaping

### How to Fix

Check the ConfigMap contents:
```bash
kubectl get configmap <name> -o yaml
# Check the data section for available keys
```

List keys in a ConfigMap:
```bash
kubectl get configmap <name> -o jsonpath='{.data}'
```

Update the deployment to use the correct key name.

### Examples

```bash
# View ConfigMap keys
kubectl get configmap app-config -o yaml
# data:
#   DATABASE_URL: "postgres://..."
#   LOG_LEVEL: "debug"

# Correct the env var reference in deployment
kubectl set env deployment/my-app --from=configmap/app-config
```"""),

    # More API server
    ("watch-connection-closed", "Watch connection closed unexpectedly",
     "Fix Kubernetes watch connection closed errors. Resolve issues when watch requests are terminated unexpectedly.",
     """## Watch Connection Closed

`watch close: etcdserver: request timed out`

This error occurs when a watch request to the API server is terminated prematurely. Watches are used by controllers and kubectl get --watch to monitor resource changes.

### Common Causes

- etcd is slow or unhealthy
- Watch cache is too large
- Network connectivity issues
- Client has not processed events fast enough
- Watch timed out (default 5-10 minutes for idle connections)
- API server restart during upgrade

### How to Fix

This is often temporary. Retry the watch operation:
```bash
kubectl get pods --watch
```

If persistent, check etcd health:
```bash
kubectl get --raw /healthz/etcd
```

### Examples

```bash
# Reconnect watch
kubectl get pods --watch 2>&1 | head

# Keep watch alive with periodic requests
while true; do kubectl get pods --watch --request-timeout=300s; sleep 1; done
```"""),

    # Static pod
    ("static-pod-error", "Static pod error in Kubernetes",
     "Fix Kubernetes static pod errors. Resolve issues with static pods managed directly by the kubelet on a node.",
     """## Static Pod Error

Static pods are pods managed directly by the kubelet on a specific node. They are defined in the kubelet's manifest directory.

### Common Causes

- Manifest file has YAML syntax errors
- Static pod conflict with API server-created pod
- Kubelet cannot read the manifest directory
- Invalid pod specification
- Duplicate pod names across nodes
- Mirror pod not created on the API server

### How to Fix

Check the static pod manifest directory:
```bash
sudo ls /etc/kubernetes/manifests/
```

Validate the manifest:
```bash
sudo kubelet --validate-config --config /var/lib/kubelet/config.yaml
```

Check kubelet logs for static pod errors:
```bash
sudo journalctl -u kubelet | grep -i "static\\|mirror"
```

### Examples

```bash
# List static pods
sudo ls /etc/kubernetes/manifests/
# kube-apiserver.yaml
# kube-controller-manager.yaml
# kube-scheduler.yaml

# Validate a static pod manifest
kubectl apply -f /etc/kubernetes/manifests/kube-apiserver.yaml --dry-run=server
```"""),

    # Resource cleanup
    ("orphaned-resources", "Orphaned Kubernetes resources",
     "Fix orphaned Kubernetes resources. Resolve issues when resources remain after their parent controller is deleted.",
     """## Orphaned Resources

Orphaned resources occur when Kubernetes resources remain after the controller that created them is deleted or when ownerReferences point to non-existent resources.

### Common Causes

- Deployment deleted but ReplicaSets remain (without cascade deletion)
- Namespace deleted but resources remain due to finalizer
- CRD deleted but custom resources remain
- Owner reference to a resource that no longer exists
- Foreground deletion fails (child resources block deletion)
- Background deletion leaves some resources

### How to Fix

Find orphaned resources:
```bash
kubectl get all --all-namespaces | grep -v "Running\\|ready"
```

Clean up manually:
```bash
kubectl delete replicaset <name> --cascade=orphan
```

Delete with cascade:
```bash
kubectl delete deployment <name> --cascade=foreground
```

### Examples

```bash
# Find ReplicaSets not owned by any Deployment
kubectl get replicaset --all-namespaces -o json | jq '.items[] | select(.metadata.ownerReferences == null) | .metadata.name'

# Delete orphaned resources
kubectl delete rs <orphaned-rs>
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
