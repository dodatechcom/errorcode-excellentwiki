#!/usr/bin/env python3
"""Generate additional Kubernetes error pages (batch 2)"""
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
    # More scheduling errors
    ("node-resources-exceeded", "Node resources exceeded",
     "Fix Kubernetes node resource exceeded errors. Resolve pod scheduling failures when a single node does not have enough remaining resources.",
     """## Node Resources Exceeded

`0/4 nodes are available: 1 Insufficient cpu, 1 Insufficient memory, 2 node(s) didn't match pod anti-affinity rules`

This error occurs when individual nodes have different resource constraints. The scheduler evaluates each node against the pod's requirements.

### Common Causes

- Multiple resource constraints on different nodes
- CPU requested but only available on nodes without enough memory
- Memory available but only on nodes without enough CPU
- Nodes have different hardware configurations

### How to Fix

Check each node's available resources:
```bash
kubectl describe nodes | grep -A10 "Allocated resources"
```

Consider using multiple node pools with different resource profiles.

Reduce resource requests or increase node capacity.

### Examples

```bash
# Check node resource allocation
kubectl describe nodes | grep -A5 "Allocated resources"
#  Resource           Requests     Limits
#  cpu                3500m/4000m  4500m/4000m
#  memory             6Gi/8Gi      7Gi/8Gi
```"""),

    ("match-node-selector", "MatchNodeSelector",
     "Fix Kubernetes MatchNodeSelector scheduling error. Resolve pods stuck in Pending when nodeSelector cannot be satisfied.",
     """## MatchNodeSelector

`0/4 nodes are available: 4 node(s) didn't match node selector`

This scheduling error means no nodes have labels matching the pod's nodeSelector requirements.

### Common Causes

- Node labels were removed or never set
- pod has a restrictive nodeSelector
- Pod was moved to a cluster without the required labels
- Node pool label differs from what the pod expects

### How to Fix

Check the pod's nodeSelector:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.nodeSelector}'
```

List node labels:
```bash
kubectl get nodes --show-labels
```

Remove or relax the nodeSelector:
```bash
kubectl patch deployment <name> -p '{"spec":{"template":{"spec":{"nodeSelector":null}}}}'
```

### Examples

```bash
# Find nodes with specific label
kubectl get nodes -l kubernetes.io/os=linux
```"""),

    ("failed-to-provision-volume", "Failed to provision volume",
     "Fix Kubernetes volume provisioning failures. Resolve PVC pending when the StorageClass provisioner cannot create the volume.",
     """## Failed to Provision Volume

`Failed to provision volume with StorageClass "<name>"`

This error occurs when the storage provisioner (EBS, GCE PD, Azure Disk) cannot create a persistent volume for a PVC.

### Common Causes

- Cloud provider API rate limiting
- Insufficient permissions to create volumes
- Volume type is not available in the region
- StorageClass parameters are invalid
- Cloud provider quota exceeded

### How to Fix

Check PVC events:
```bash
kubectl describe pvc <name>
```

Check StorageClass configuration:
```bash
kubectl describe storageclass <name>
```

Check cloud provider limits:
```bash
# AWS
aws ec2 describe-account-attributes
# GCP
gcloud compute regions describe <region>
# Azure
az vm list-usage --location <region>
```

### Examples

```bash
# Check PVC events for provisioning error
kubectl describe pvc my-claim | grep -A5 Events
#  Failed to provision volume: AccessDenied
```"""),

    ("volume-limit-exceeded", "Volume limit exceeded",
     "Fix Kubernetes volume limit exceeded errors. Resolve pod scheduling failures when a node has reached its maximum volume attachment limit.",
     """## Volume Limit Exceeded

`0/4 nodes are available: 4 node(s) exceed max volume count`

This error occurs when the node has reached its maximum number of attached volumes. Each EC2 instance type, for example, has a limit on how many EBS volumes can be attached.

### Common Causes

- Node has reached the maximum attachable volumes
- Too many PVCs scheduled on a single node
- Some volumes remain attached but are not in use
- Instance type limits (e.g., t3.medium supports 3 EBS volumes)

### How to Fix

Check volume attachment limits for your instance type.

Use larger instance types that support more volumes.

Check which volumes are attached to the node:
```bash
kubectl get pods -o wide | grep <node> | wc -l
```

### Examples

```bash
# Check PVCs per node
kubectl get pods --all-namespaces -o wide | awk '{print $8}' | sort | uniq -c | sort -rn
```"""),

    # More networking
    ("dns-resolution-failure", "DNS resolution failure in pod",
     "Fix Kubernetes DNS resolution failures inside pods. Resolve service discovery and name resolution issues.",
     """## DNS Resolution Failure

`wget: bad address 'my-service'`

This error occurs when pods cannot resolve DNS names (service names, external hostnames).

### Common Causes

- CoreDNS pods are not running or in CrashLoopBackOff
- CoreDNS ConfigMap is misconfigured
- Network policy blocking DNS traffic (port 53)
- Pod's dnsPolicy is set to None without explicit nameservers
- ndots setting causes excessive DNS queries
- Cluster DNS IP is incorrect

### How to Fix

Check CoreDNS pods:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```

Test DNS from a pod:
```bash
kubectl run test-$RANDOM --image=busybox -it --rm -- nslookup kubernetes.default
```

Check pod DNS configuration:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.dnsPolicy}'
```

### Examples

```bash
# Test DNS
kubectl run dns-test --image=busybox -it --rm -- nslookup kubernetes.default.svc.cluster.local
# Server:    10.96.0.10
# Address:   10.96.0.10:53
# Name:      kubernetes.default.svc.cluster.local
# Address:   10.96.0.1
```"""),

    ("service-port-conflict", "Service port conflict",
     "Fix Kubernetes service port conflicts. Resolve issues when multiple services try to use the same NodePort.",
     """## Service Port Conflict

`Error: Service "<name>" is invalid: spec.ports[0].nodePort: Invalid value: 30080: provided port is already allocated`

This error occurs when a NodePort or LoadBalancer service requests a port that is already in use by another service.

### Common Causes

- Manually specified NodePort is already allocated
- Multiple services with the same static NodePort
- Pod hostPort conflicts with the service NodePort
- Port range (30000-32767) exhausted

### How to Fix

List services and their NodePorts:
```bash
kubectl get svc --all-namespaces -o wide
```

Use a different NodePort or omit it to let Kubernetes assign one automatically:
```yaml
spec:
  ports:
  - port: 80
    nodePort: 0  # auto-assign
```

### Examples

```bash
# Find conflicting NodePort
kubectl get svc --all-namespaces -o yaml | grep nodePort

# Let Kubernetes assign the port
kubectl patch service my-service -p '{"spec":{"ports":[{"port":80,"nodePort":0}]}}'
```"""),

    ("service-external-ip-pending", "Service ExternalIP pending",
     "Fix Kubernetes service ExternalIP stuck pending. Resolve external IP assignment delays for services.",
     """## Service ExternalIP Pending

`<service>   LoadBalancer   <cluster-ip>   <pending>     80:30080/TCP`

This occurs when a LoadBalancer service's external IP is pending assignment. The cloud load balancer may not have finished provisioning.

### Common Causes

- Cloud load balancer provisioning is slow (can take 1-5 minutes)
- Cloud provider account has resource limits
- Incorrect service annotations for the cloud provider
- Network or subnet configuration issues
- No external load balancer controller (on-premises)

### How to Fix

Wait and retry:
```bash
kubectl get svc --watch
```

Check service events:
```bash
kubectl describe service <name>
```

For AWS, check the ELB/NLB:
```bash
aws elb describe-load-balancers
aws elbv2 describe-load-balancers
```

### Examples

```bash
# Watch service until IP is assigned
kubectl get svc my-service -w

# Check for errors
kubectl describe service my-service | grep -A10 Events
```"""),

    # More volume errors
    ("csi-driver-not-installed", "CSI driver not installed",
     "Fix Kubernetes CSI driver not installed errors. Resolve volume provisioning failures when the Container Storage Interface driver is missing.",
     """## CSI Driver Not Installed

`failed to get CSI driver: rpc error: code = Unimplemented`

This error occurs when a CSI driver is not installed or not registered on the node where the volume needs to be mounted.

### Common Causes

- CSI driver (EBS CSI, GCE PD CSI, etc.) not installed
- CSI driver pods are not running
- CSI node driver is not registered on the specific node
- Old Kubernetes version without CSI support
- Invalid CSIDriver object

### How to Fix

List installed CSI drivers:
```bash
kubectl get csidrivers
```

Check CSI driver pods:
```bash
kubectl get pods -n kube-system | grep csi
```

Install the CSI driver:
```bash
# EBS CSI driver
kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/"

# GCE PD CSI driver
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gcp-compute-persistent-disk-csi-driver/master/deploy/kubernetes/overlays/stable/gcp-pd-csi-driver.yaml
```

### Examples

```bash
# Check CSI drivers
kubectl get csidrivers
# ebs.csi.aws.com

# Check CSI node status
kubectl get csinodes
```"""),

    ("failed-to-delete-pvc", "Failed to delete PVC",
     "Fix Kubernetes failed PVC deletion errors. Resolve persistent volume claim stuck in Terminating state.",
     """## Failed to Delete PVC

This error occurs when a PersistentVolumeClaim cannot be deleted because it is still in use or has protection finalizers.

### Common Causes

- PVC protection finalizer not removed
- Pod still referencing the PVC
- Volume snapshot exists for the PVC
- Storage system is unreachable
- PV retention policy preventing deletion

### How to Fix

Find pods using the PVC:
```bash
kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.volumes[]?.persistentVolumeClaim.claimName=="<pvc-name>") | .metadata.namespace + "/" + .metadata.name'
```

Remove finalizers:
```bash
kubectl patch pvc <name> -p '{"metadata":{"finalizers":[]}}' --type=merge
```

Delete the protecting pods first.

### Examples

```bash
# Force remove a stuck PVC
kubectl patch pvc my-claim -p '{"metadata":{"finalizers":[]}}' --type=merge
kubectl delete pvc my-claim --grace-period=0 --force
```"""),

    # More pod lifecycle
    ("unexpected-admission-error", "UnexpectedAdmissionError",
     "Fix Kubernetes UnexpectedAdmissionError. Resolve pod failures when the container runtime encounters unexpected errors during pod creation.",
     """## UnexpectedAdmissionError

This error occurs when the kubelet encounters an unexpected error during pod admission. The container runtime may not be functioning correctly.

### Common Causes

- Container runtime (containerd/CRI-O) is unhealthy or crashed
- Disk I/O errors on the node
- Node is low on memory or other resources
- Kernel module issues (overlay, devicemapper)
- Inode exhaustion on the filesystem

### How to Fix

Check node conditions:
```bash
kubectl describe node <node-name>
```

Check kubelet logs:
```bash
sudo journalctl -u kubelet --no-pager --tail=100
```

Restart containerd and kubelet:
```bash
sudo systemctl restart containerd
sudo systemctl restart kubelet
```

### Examples

```bash
# Check node for pressure conditions
kubectl describe node <node> | grep -A10 Conditions
# MemoryPressure  True

# Restart container runtime
ssh <node> sudo systemctl restart containerd && sudo systemctl restart kubelet
```"""),

    ("preempting", "Preempting (pod being preempted by scheduler)",
     "Fix Kubernetes pod preemption warnings. Resolve pods that are being preempted (evicted) by the scheduler to make room for higher-priority pods.",
     """## Preempting

`Preempting: preempting <pod> to schedule <higher-priority-pod>`

This is a scheduler action where a lower-priority pod is being preempted (evicted) to free resources for a higher-priority pod.

### Common Causes

- Higher priority pod needs resources on the node
- Low-priority pods are scheduled on a node needed for critical workloads
- Scheduler is doing normal priority-based preemption
- No other nodes available for the high-priority pod

### How to Fix

This is expected behavior when using priority classes. To reduce preemption:

- Set appropriate PriorityClass values for your workloads
- Add more nodes to reduce resource contention
- Use podDisruptionBudget on the low-priority pods to limit disruption
- Set preemptionPolicy: Never on the high-priority pod if preemption is not desired

### Examples

```bash
# Check PriorityClasses
kubectl get priorityclass

# Create a balanced priority scheme
kubectl create priorityclass high --value=1000
kubectl create priorityclass medium --value=500
kubectl create priorityclass low --value=100
```"""),

    # More kubectl
    ("config-merge-error", "kubectl config merge error",
     "Fix kubectl config merge errors. Resolve issues when merging multiple kubeconfig files.",
     """## Config Merge Error

`error: unable to merge multiple kubeconfig files`

This error occurs when kubectl cannot merge configuration from multiple kubeconfig files specified in KUBECONFIG.

### Common Causes

- Conflicting cluster, user, or context names
- Corrupted kubeconfig files
- Duplicate entries with different configurations
- Invalid YAML formatting in one of the files
- Incompatible kubeconfig versions

### How to Fix

Merge configs manually:
```bash
export KUBECONFIG=~/.kube/config:~/.kube/other-config
kubectl config view --merge --flatten > ~/.kube/merged
mv ~/.kube/merged ~/.kube/config
```

Validate the kubeconfig:
```bash
kubectl config view
```

### Examples

```bash
# Merge two configs
export KUBECONFIG=~/.kube/config:~/.kube/eks-config
kubectl config view --merge --flatten > ~/.kube/all-config
cp ~/.kube/all-config ~/.kube/config
```"""),

    # More API server
    ("api-400-bad-request", "API 400 Bad Request",
     "Fix Kubernetes API 400 Bad Request errors. Resolve malformed request failures when interacting with the API server.",
     """## API 400 Bad Request

This HTTP status code occurs when the API server receives a malformed or invalid request.

### Common Causes

- Invalid JSON or YAML body
- Request body too large
- Missing required headers
- Invalid query parameters
- Malformed URL path
- Request timeout

### How to Fix

Check the request body format. Use `--dry-run=server` for validation:
```bash
kubectl apply -f manifest.yaml --dry-run=server
```

Check for special characters or encoding issues in the request.

For curl requests, ensure proper Content-Type header:
```bash
curl -X POST -H "Content-Type: application/json" -d @body.json https://api-server:6443/api/v1/namespaces
```

### Examples

```bash
# Validate manifest
kubectl apply -f deployment.yaml --dry-run=server --validate=true

# Check for encoding issues
file deployment.yaml
# Ensure it's UTF-8 encoded
```"""),

    # More node
    ("node-lost", "NodeLost (node unreachable)",
     "Fix Kubernetes NodeLost error. Resolve nodes that have become unreachable from the control plane.",
     """## NodeLost

`status.conditions: [{type: "NodeLost", status: "True"}]`

The NodeLost condition indicates the control plane has lost communication with the node. Kubernetes waits for `pod-eviction-timeout` (default 5 minutes) before evicting pods.

### Common Causes

- Node is powered off or crashed
- Network connectivity lost between node and API server
- Kubelet process crashed or is hung
- Firewall or security group blocking traffic
- Node was terminated by the cloud provider

### How to Fix

Check node status:
```bash
kubectl get node <node-name> -o wide
```

SSH to the node (if possible):
```bash
ssh <node-ip> systemctl status kubelet
ssh <node-ip> systemctl restart kubelet
```

If the node is permanently lost, remove it:
```bash
kubectl delete node <node-name>
```

### Examples

```bash
# Check node conditions
kubectl describe node <node> | grep NodeLost

# Force delete node
kubectl delete node failed-node

# Check pod eviction
kubectl get pods -o wide | grep failed-node
```"""),

    # More admission
    ("validating-webhook-failed", "ValidatingWebhookConfiguration failed",
     "Fix Kubernetes ValidatingWebhookConfiguration failures. Resolve errors when a validating admission webhook cannot process requests.",
     """## ValidatingWebhookConfiguration Failed

`Internal error occurred: failed calling webhook "<webhook>": Post "<url>": dial tcp: lookup <service>: i/o timeout`

This error occurs when the API server cannot reach the validating webhook service.

### Common Causes

- Webhook service is not running
- Webhook service endpoint is misconfigured
- Network policy blocking traffic
- TLS certificate error
- Webhook service is in a different namespace
- Webhook timeout (default 10s) too short

### How to Fix

Check webhook configuration:
```bash
kubectl get validatingwebhookconfiguration <name> -o yaml
```

Verify the webhook service exists:
```bash
kubectl get service -n <namespace>
kubectl get endpoints -n <namespace>
```

Check the webhook pod logs:
```bash
kubectl logs -n <namespace> deployment/<webhook-name>
```

### Examples

```bash
# Check webhook service endpoints
kubectl get endpoints -n webhook-ns webhook-service
# No endpoints

# Restart webhook deployment
kubectl rollout restart -n webhook-ns deployment/webhook
```"""),

    ("mutating-webhook-failed", "MutatingWebhookConfiguration failed",
     "Fix Kubernetes MutatingWebhookConfiguration failures. Resolve errors when a mutating admission webhook cannot process requests.",
     """## MutatingWebhookConfiguration Failed

`Internal error occurred: failed calling webhook "<webhook>": Post "<url>": context deadline exceeded`

This error occurs when the API server cannot reach the mutating webhook service or the webhook takes too long to respond.

### Common Causes

- Webhook service is down or slow
- Webhook timeout too short (default 10s)
- Webhook is modifying resources in a way that triggers an infinite loop
- TLS certificate validation failure
- Webhook returns unexpected content type

### How to Fix

Check webhook configuration:
```bash
kubectl get mutatingwebhookconfiguration <name> -o yaml
```

Check the webhook service connectivity:
```bash
kubectl run test-$RANDOM --image=busybox -it --rm -- wget -O- https://webhook-service:443
```

Temporarily disable the webhook for debugging:
```bash
kubectl patch mutatingwebhookconfiguration <name> --type=json -p='[{"op": "replace", "path": "/webhooks/0/failurePolicy", "value": "Ignore"}]'
```

### Examples

```bash
# Check webhook failure policy
kubectl get mutatingwebhookconfiguration <name> -o yaml | grep failurePolicy
# FailurePolicy: Fail

# Change to Ignore for debugging
kubectl patch mutatingwebhookconfiguration <name> --type=json -p='[{"op": "replace", "path": "/webhooks/0/failurePolicy", "value": "Ignore"}]'
```"""),

    # More storage
    ("pvc-wait-for-first-consumer", "PVC WaitForFirstConsumer",
     "Fix Kubernetes PVC WaitForFirstConsumer mode. Resolve volume provisioning delays when using delayed volume binding.",
     """## PVC WaitForFirstConsumer

`Status: Pending (WaitForFirstConsumer)`

This is not an error but a volume binding mode where the PVC stays Pending until a pod using it is created. The volume is provisioned in the same zone as the pod.

### Common Causes

- StorageClass uses volumeBindingMode: WaitForFirstConsumer
- No pod has been created to consume the PVC yet
- Normal behavior for topology-aware provisioning
- Pod scheduling constraints may cause provisioning delays

### How to Fix

This is expected behavior. Create a pod that uses the PVC:
```bash
kubectl create -f pod-with-pvc.yaml
```

If the PVC stays pending, check pod scheduling events:
```bash
kubectl describe pod <pod-name>
```

### Examples

```bash
# Check StorageClass binding mode
kubectl get sc <name> -o yaml | grep volumeBindingMode
# volumeBindingMode: WaitForFirstConsumer

# Create a pod to trigger volume provisioning
kubectl run test-pod --image=nginx --overrides='{"spec":{"volumes":[{"name":"data","persistentVolumeClaim":{"claimName":"my-pvc"}}],"containers":[{"name":"nginx","image":"nginx","volumeMounts":[{"name":"data","mountPath":"/data"}]}]}}'
```"""),

    # More HPA
    ("hpa-missing-metrics-server", "HPA missing Metrics Server",
     "Fix Kubernetes HPA 'Metrics Server not available' error. Resolve HPA failures when resource metrics API is not installed.",
     """## HPA Missing Metrics Server

`the metrics server is not configured to handle the request`

This error occurs when the HorizontalPodAutoscaler cannot query resource metrics because the Metrics Server is not installed.

### Common Causes

- Metrics Server is not deployed in the cluster
- Metrics Server is not reachable via the API
- Metrics API endpoint is disabled
- Metrics Server is in CrashLoopBackOff
- Aggregation layer is not configured

### How to Fix

Install Metrics Server:
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Check Metrics Server availability:
```bash
kubectl get apiservice v1beta1.metrics.k8s.io
kubectl get --raw /apis/metrics.k8s.io/v1beta1
```

### Examples

```bash
# Check if Metrics API is available
kubectl get --raw /apis/metrics.k8s.io/v1beta1 | jq .
# Error: the server could not handle the request

# Install Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```"""),

    # More RBAC
    ("rbac-role-binding-missing", "RBAC RoleBinding missing",
     "Fix Kubernetes RBAC RoleBinding missing errors. Resolve when a role binding does not exist for the required role and user.",
     """## RBAC RoleBinding Missing

`(user "user@example.com" cannot list resource "pods" in API group "" in the namespace "default")`

This error occurs when a user or service account has a role assigned but no RoleBinding links it to the namespace.

### Common Causes

- RoleBinding has not been created in the namespace
- RoleBinding references a role that does not exist
- RoleBinding is in the wrong namespace
- ClusterRoleBinding was created but not ClusterRole

### How to Fix

List RoleBindings in the namespace:
```bash
kubectl get rolebindings -n <namespace>
```

Create a RoleBinding:
```bash
kubectl create rolebinding <name> --role=<role> --user=<user> --namespace=<ns>
```

### Examples

```bash
# Check existing bindings
kubectl get rolebindings --all-namespaces | grep <user>

# Create binding
kubectl create rolebinding pod-reader --role=pod-reader --user=user@example.com --namespace=default
```"""),

    # More pod conditions
    ("pod-failed-admission", "Pod failed admission",
     "Fix Kubernetes pod failed admission errors. Resolve pods that are rejected during admission control before scheduling.",
     """## Pod Failed Admission

`pod "<name>" is forbidden: <reason>`

This error occurs when a pod is rejected by Kubernetes admission controllers before it reaches the scheduler.

### Common Causes

- PodSecurityPolicy or Pod Security Admission rejection
- ResourceQuota exceeded in the namespace
- LimitRange validation failure
- Admission webhook rejection
- ServiceAccount does not exist
- ImagePullSecret missing

### How to Fix

Check the full error message for the specific reason:
```bash
kubectl apply -f pod.yaml 2>&1
```

Fix the specific issue mentioned in the error (resource limits, missing SA, security context, etc).

### Examples

```bash
# Apply with verbose output
kubectl apply -f pod.yaml 2>&1
# Error: pods "my-pod" is forbidden: exceeded quota: compute-quota
# Fix: reduce resource requests or increase quota
```"""),

    # More container runtime
    ("image-gc-failed", "Image garbage collection failed",
     "Fix Kubernetes image garbage collection failures. Resolve issues when the kubelet cannot clean up unused images.",
     """## Image GC Failed

`Failed to garbage collect images: failed to remove image "<image>": rpc error: code = Unknown desc = ...`

This error occurs when the kubelet's image garbage collector cannot remove unused container images to free disk space.

### Common Causes

- Image is in use by a running container
- Disk I/O errors preventing image removal
- containerd/CRI-O not responding
- Filesystem corruption on the image storage
- Permission issues on image storage directory

### How to Fix

Manually prune images:
```bash
sudo crictl rmi --prune
sudo docker image prune -a -f
```

Check image storage disk usage:
```bash
sudo du -sh /var/lib/containerd/
sudo du -sh /var/lib/docker/
```

### Examples

```bash
# Manual image cleanup
ssh <node> sudo crictl rmi --prune
ssh <node> sudo docker image prune -a -f
```"""),

    ("container-runtime-not-ready", "Container runtime not ready",
     "Fix Kubernetes container runtime not ready errors. Resolve kubelet startup failures when the container runtime is not available.",
     """## Container Runtime Not Ready

`Container runtime not ready: runtime "containerd" is not ready: connection refused`

This error occurs when the kubelet starts but cannot connect to the container runtime (containerd or CRI-O).

### Common Causes

- containerd/CRI-O service is not started
- containerd/CRI-O crashed during startup
- containerd socket path is incorrect in kubelet config
- containerd configuration is invalid
- containerd is enabled but failed to start due to cgroup issues

### How to Fix

Check the runtime status:
```bash
sudo systemctl status containerd
sudo journalctl -u containerd --no-pager --tail=100
```

Start the runtime:
```bash
sudo systemctl start containerd
```

Check the kubelet config for the correct runtime endpoint:
```bash
sudo cat /var/lib/kubelet/kubeadm-flags.env
```

### Examples

```bash
# Check containerd status
ssh <node> sudo systemctl status containerd
# Active: failed (Result: exit-code)

# Restart containerd
ssh <node> sudo systemctl restart containerd
```"""),

    # More scheduling
    ("pod-fits-resources", "PodFitsResources predicate failed",
     "Fix Kubernetes PodFitsResources scheduling failures. Resolve pods that cannot be scheduled due to cumulative resource constraints.",
     """## PodFitsResources Failed

`0/4 nodes are available: 4 Insufficient cpu, 3 Insufficient memory`

This error occurs when the scheduler evaluates nodes and finds that no node has enough remaining resources for the pod.

### Common Causes

- Pod's resource requests exceed available resources on all nodes
- Cluster has been scaled down and cannot accommodate new pods
- Many pods with small requests but cumulative total is high
- Node allocatable resources are less than capacity due to reserved resources

### How to Fix

Check aggregate cluster resource usage:
```bash
kubectl top nodes
kubectl describe nodes | grep -A5 "Allocated resources"
```

Reduce resource requests or add nodes.

Check for reserved resources on nodes:
```bash
kubectl describe node <name> | grep -i "Allocatable"
```

### Examples

```bash
# Check allocatable vs capacity
kubectl describe node <name> | grep -E "Capacity|Allocatable"
# cpu:                4
# cpu:                3920m
# memory:             8192088Ki
# memory:             7986008Ki
```"""),

    # More taints
    ("node-taint-dedicated", "Node taint: dedicated for specific workloads",
     "Fix Kubernetes dedicated node taint errors. Resolve pod scheduling failures on nodes tainted for specific workloads.",
     """## Dedicated Node Taint

`0/4 nodes are available: 2 node(s) had taint {node-role.kubernetes.io/master: }, 2 node(s) had taint {dedicated: gpu}`

This occurs when nodes have dedicated taints to reserve them for specific workloads and the pod does not have matching tolerations.

### Common Causes

- Nodes are tainted for dedicated workloads (GPU, storage, etc.)
- Master/control-plane nodes have NoSchedule taint
- Infrastructure nodes tainted for system components
- Pods need proper tolerations to use dedicated nodes

### How to Fix

List node taints:
```bash
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.taints[*].key}{":"}{.spec.taints[*].value}{":"}{.spec.taints[*].effect}{"\n"}{end}'
```

Add tolerations to the pod:
```yaml
tolerations:
- key: "dedicated"
  operator: "Equal"
  value: "gpu"
  effect: "NoSchedule"
```

### Examples

```bash
# Add toleration to deployment for GPU nodes
kubectl patch deployment my-app -p '{"spec":{"template":{"spec":{"tolerations":[{"key":"nvidia.com/gpu","operator":"Exists","effect":"NoSchedule"}]}}}}'
```"""),

    # More admission
    ("image-pull-secret-missing-k8s", "ImagePullSecret missing",
     "Fix Kubernetes ImagePullSecret missing errors. Resolve pod creation failures when private registry credentials are required but not provided.",
     """## ImagePullSecret Missing

`Failed to pull image "<image>": rpc error: code = Unknown desc = Error response from daemon: pull access denied for <repository>`

This error occurs when a pod references an image from a private registry but does not provide authentication credentials via an imagePullSecret.

### Common Causes

- Image is in a private registry (ECR, GCR, private Docker Hub, etc.)
- No imagePullSecret is configured in the pod spec or service account
- The imagePullSecret exists but has incorrect credentials
- The service account does not have the imagePullSecret attached

### How to Fix

Create an imagePullSecret:
```bash
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<token>
```

Add to pod spec:
```yaml
spec:
  imagePullSecrets:
  - name: regcred
```

Or add to the default service account:
```bash
kubectl patch serviceaccount default -p '{"imagePullSecrets":[{"name":"regcred"}]}'
```

### Examples

```bash
# Create ECR pull secret
kubectl create secret docker-registry ecr-cred \
  --docker-server=<account>.dkr.ecr.us-east-1.amazonaws.com \
  --docker-username=AWS \
  --docker-password=$(aws ecr get-login-password)
```"""),

    # More config
    ("annotation-invalid", "Invalid annotation in Kubernetes manifest",
     "Fix Kubernetes invalid annotation errors. Resolve resource creation failures when annotations have invalid format.",
     """## Invalid Annotation

`Invalid annotation: <key>: <value>`

This error occurs when a Kubernetes resource has annotations with invalid keys or values.

### Common Causes

- Annotation key does not follow the prefix/name format
- Annotation value is too long (>256KB)
- Annotation key has invalid characters
- Reserved annotation prefix used without permission
- Annotation key is empty or missing

### How to Fix

Check annotation format:
```yaml
metadata:
  annotations:
    # Valid format: <prefix>/<name>
    nginx.ingress.kubernetes.io/rewrite-target: /
    # Built-in annotations don't need prefix
    kubectl.kubernetes.io/last-applied-configuration: "..."
```

Remove or correct the annotation:
```bash
kubectl annotate <resource> <name> <key>-  # remove annotation
kubectl annotate <resource> <name> <key>=<value> --overwrite
```

### Examples

```bash
# Remove an invalid annotation
kubectl annotate deployment my-app my-invalid-annotation-

# Add corrected annotation
kubectl annotate deployment my-app nginx.ingress.kubernetes.io/rewrite-target=/
```"""),

    # More logging
    ("kubectl-logs-failed", "kubectl logs failed",
     "Fix 'kubectl logs' failures. Resolve errors when trying to view container logs.",
     """## kubectl Logs Failed

`error: previous terminated container "<name>" in pod "<name>" not found`

This error occurs when kubectl cannot retrieve logs from a container.

### Common Causes

- Pod has not started yet or is in Pending state
- Container has never run (no logs available)
- Container name is incorrect (multi-container pods)
- Pod has been deleted and logs are no longer available
- Container crashed before producing any output

### How to Fix

Check pod status:
```bash
kubectl get pod <pod-name>
```

List containers in the pod:
```bash
kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].name}'
```

For multi-container pods, specify the container:
```bash
kubectl logs <pod-name> -c <container-name>
```

Use `--tail` and `--since` to limit output:
```bash
kubectl logs <pod-name> --tail=50 --since=5m
```

### Examples

```bash
# View logs for specific container
kubectl logs my-app -c sidecar

# Stream logs
kubectl logs -f my-app

# Check previous instance logs
kubectl logs my-app --previous
```"""),

    # More autoscaling
    ("vpa-recommendation-failed", "VPA recommendation failed",
     "Fix Kubernetes Vertical Pod Autoscaler (VPA) recommendation failures. Resolve VPA issues when resource recommendations cannot be calculated.",
     """## VPA Recommendation Failed

This error occurs when the Vertical Pod Autoscaler cannot generate resource recommendations for a pod.

### Common Causes

- Metrics Server is not installed
- Pod has not been running long enough for metrics collection (minimum 8 hours for default mode)
- VPA recommender pod is not running
- VPA admission controller is not installed
- Pod resource requests are not set

### How to Fix

Check VPA components:
```bash
kubectl get pods -n kube-system | grep vpa
```

Check VPA status:
```bash
kubectl describe vpa <name>
```

Update mode to auto or recreate:
```yaml
spec:
  updateMode: Auto
```

### Examples

```bash
# Check VPA status
kubectl describe vpa my-app-vpa
#  Conditions:
#    Type    Status  Reason
#    Update  False   NoPodHistory

# Install VPA
git clone https://github.com/kubernetes/autoscaler.git
kubectl apply -k autoscaler/vertical-pod-autoscaler/deploy/
```"""),

    # More cluster
    ("cluster-ip-range-exhausted", "Cluster IP range exhausted",
     "Fix Kubernetes cluster IP range exhausted errors. Resolve service creation failures when the ClusterIP range is full.",
     """## Cluster IP Range Exhausted

`Failed to assign IP address to service: IP range exhausted`

This error occurs when the cluster's Service IP range is fully allocated and no more ClusterIPs can be assigned.

### Common Causes

- Too many services created in the cluster
- Cluster CIDR is too small for the number of services
- Services are not cleaned up after use
- Non-RFC1918 address range used
- Default /24 CIDR space exhausted (256 IPs)

### How to Fix

List services:
```bash
kubectl get svc --all-namespaces | wc -l
```

Delete unused services:
```bash
kubectl delete svc <unused-service>
```

Check Service CIDR:
```bash
kubectl cluster-info dump | grep -i "service-cluster-ip-range"
```

### Examples

```bash
# Count services
kubectl get svc -A | wc -l

# List services sorted by creation timestamp
kubectl get svc --all-namespaces --sort-by=.metadata.creationTimestamp
```"""),

    # More webhook
    ("webhook-missing-service", "Webhook service not found",
     "Fix Kubernetes webhook service not found errors. Resolve admission webhook failures when the backing service is missing.",
     """## Webhook Service Not Found

`failed calling webhook "<webhook>": Post "https://<service>.<namespace>.svc:443/<path>": dial tcp: lookup <service> on <dns>: no such host`

This error occurs when a ValidatingWebhookConfiguration or MutatingWebhookConfiguration references a service that does not exist.

### Common Causes

- Webhook service has not been deployed yet
- Service name in the webhook config is misspelled
- Webhook service is in a different namespace
- Webhook service was deleted but config remains
- Service port mismatch

### How to Fix

Check the webhook configuration for the service reference:
```bash
kubectl get validatingwebhookconfiguration <name> -o yaml
kubectl get mutatingwebhookconfiguration <name> -o yaml
```

Verify the service exists:
```bash
kubectl get svc -n <namespace>
kubectl describe svc <name> -n <namespace>
```

### Examples

```bash
# Find the referenced service
kubectl get validatingwebhookconfiguration <name> -o jsonpath='{.webhooks[0].clientConfig.service}'
# {"name":"webhook-service","namespace":"webhook-ns"}

# Verify service exists
kubectl get svc -n webhook-ns webhook-service
```"""),

    # More containerd
    ("containerd-config-error", "containerd configuration error",
     "Fix containerd configuration errors in Kubernetes. Resolve container runtime startup failures due to invalid config.",
     """## Containerd Configuration Error

`failed to load plugin "io.containerd.grpc.v1.cri": no such binary`

This error occurs when containerd cannot start because its configuration file has invalid entries.

### Common Causes

- containerd config.toml has syntax errors
- Missing or invalid plugin configuration
- Incompatible containerd version with config
- Missing required binaries (runc, cni plugins)
- Invalid sandbox image configuration

### How to Fix

Check containerd config:
```bash
sudo containerd config dump 2>&1 | head -50
```

Check the config file:
```bash
sudo cat /etc/containerd/config.toml
```

Validate and regenerate config:
```bash
sudo containerd config default > /etc/containerd/config.toml
sudo systemctl restart containerd
```

### Examples

```bash
# Backup and regenerate config
sudo cp /etc/containerd/config.toml /etc/containerd/config.toml.bak
sudo containerd config default | sudo tee /etc/containerd/config.toml
sudo systemctl restart containerd
```"""),

    # More node management
    ("node-pressure-eviction", "Node pressure eviction",
     "Fix Kubernetes node pressure eviction. Resolve pods evicted due to resource pressure on the node.",
     """## Node Pressure Eviction

`The node was low on resource: <resource>. Evicted pod <name>.`

This occurs when the kubelet evicts pods from a node due to resource pressure (disk, memory, PID).

### Common Causes

- DiskPressure triggered eviction (most common)
- MemoryPressure triggered eviction
- PIDPressure triggered eviction
- BestEffort QoS pods evicted first
- Burstable QoS pods evicted next
- Guaranteed QoS pods evicted last

### How to Fix

Check node conditions before eviction:
```bash
kubectl describe node <node-name>
```

Set appropriate resource limits on all pods:
```yaml
resources:
  limits:
    memory: 512Mi
  requests:
    memory: 256Mi
```

Add more nodes to the cluster.

### Examples

```bash
# Check for evicted pods
kubectl get pods --all-namespaces -o wide | grep Evicted

# Clean up evicted pods
kubectl get pods --all-namespaces | grep Evicted | awk '{print $2 " -n " $1}' | xargs kubectl delete pod
```"""),

    # More service
    ("service-type-clusterip-none", "Service ClusterIP is None (headless)",
     "Fix Kubernetes headless service issues. Resolve connectivity problems when using headless services with ClusterIP: None.",
     """## Headless Service (ClusterIP: None)

This is not an error but a configuration. Headless services (ClusterIP: None) do not load-balance traffic. DNS queries return all pod IPs instead of a single virtual IP.

### Common Causes

- StatefulSets use headless services by design
- Application not handling multiple DNS A/AAAA records
- Client expects a single IP but gets multiple
- DNS caching issues with multiple endpoints
- Pod readiness affecting DNS records

### How to Fix

Ensure your application can handle multiple IP addresses from DNS.

For StatefulSets, use the specific pod DNS name:
```
<pod-name>.<service-name>.<namespace>.svc.cluster.local
```

If you need load balancing, use a regular service instead:
```yaml
spec:
  type: ClusterIP
  clusterIP: ""  # let Kubernetes assign
```

### Examples

```bash
# Check if service is headless
kubectl get svc <name> -o jsonpath='{.spec.clusterIP}'
# None

# DNS lookup returns all pod IPs
kubectl run test --image=busybox -it --rm -- nslookup my-headless-service
# Name:   my-headless-service
# Address: 10.1.0.1
# Address: 10.1.0.2
```"""),

    # More statefulset
    ("statefulset-ordering-error", "StatefulSet pod ordering error",
     "Fix Kubernetes StatefulSet pod ordering errors. Resolve StatefulSet startup and shutdown ordering issues.",
     """## StatefulSet Pod Ordering Error

`StatefulSet <name> is waiting for pod <pod-name> to be Running and Ready`

This occurs when a StatefulSet cannot proceed with pod creation or deletion due to its ordinal ordering guarantees.

### Common Causes

- Pod with lower ordinal is not Ready
- Pod deletion is blocked by PDB
- Pod is stuck in Pending or ContainerCreating
- Volume provisioning is slow for the next pod
- Partitioned rollout with updateStrategy.rollingUpdate.partition

### How to Fix

Check pod status:
```bash
kubectl get pods -l app=<name>
```

Check the StatefulSet status:
```bash
kubectl describe statefulset <name>
```

Force delete a stuck pod:
```bash
kubectl delete pod <name> --grace-period=0 --force
```

### Examples

```bash
# Check StatefulSet status
kubectl describe statefulset my-sts
#  Waiting for pods 1 to be ready

# Check pod status
kubectl get pods -l app=my-sts
# my-sts-0   1/1   Running
# my-sts-1   0/1   Pending
```"""),

    # More kubectl
    ("kubectl-apply-merge-error", "kubectl apply merge error",
     "Fix kubectl apply merge conflicts. Resolve errors when applying Kubernetes manifests with conflicting changes.",
     """## kubectl Apply Merge Error

`error: failed to apply patch: <resource> "<name>" is invalid: <field>: Invalid value: "<value>": <conflict>`

This error occurs when kubectl apply cannot merge the changes from the manifest with the existing resource.

### Common Causes

- Conflicting field values
- Immutable field modification (selector, nodePort, etc.)
- Server-side apply conflict
- Wrong merge strategy
- Resource drift between apply calls

### How to Fix

Use server-side apply:
```bash
kubectl apply --server-side --force-conflicts -f manifest.yaml
```

Re-read and re-apply the manifest:
```bash
kubectl get <resource> <name> -o yaml > current.yaml
# Merge changes manually
kubectl apply -f current.yaml
```

### Examples

```bash
# Force server-side apply
kubectl apply --server-side --force-conflicts -f deployment.yaml

# Read current state and compare
kubectl diff -f deployment.yaml
```"""),

    # More networking
    ("pod-cidr-available", "Pod CIDR not available",
     "Fix Kubernetes pod CIDR allocation failures. Resolve pod creation failures when the pod IP range is exhausted.",
     """## Pod CIDR Not Available

`Failed to create pod: No IP addresses available in network <name>`

This error occurs when the cluster's pod network CIDR range has been fully allocated and no more IP addresses can be assigned to new pods.

### Common Causes

- Pod CIDR is too small for the number of pods
- Many terminated pods still holding IPs (IPAM cleanup delay)
- CNI plugin IPAM (host-local) IP release delay
- Node has exhausted its local pod IP range
- Cluster was created with a small pod CIDR

### How to Fix

List pods per node:
```bash
kubectl get pods -o wide | awk '{print $8}' | sort | uniq -c
```

Check CNI IPAM configuration:
```bash
kubectl get nodes -o jsonpath='{.items[0].spec.podCIDR}'
```

Delete terminated pods to release IPs:
```bash
kubectl delete pods --field-selector=status.phase=Succeeded
```

### Examples

```bash
# Check pod CIDR
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.podCIDR}{"\n"}{end}'

# Release terminated pod IPs
kubectl delete pods --all-namespaces --field-selector=status.phase=Succeeded
```"""),

    # More QoS
    ("qos-class-eviction", "QoS class eviction (BestEffort/Burstable)",
     "Fix Kubernetes QoS class eviction. Resolve pod eviction priority based on Quality of Service classes.",
     """## QoS Class Eviction

Kubernetes uses Quality of Service (QoS) classes to determine pod eviction priority under resource pressure.

### QoS Classes (lowest to highest eviction priority)

1. BestEffort (no requests or limits set)
2. Burstable (requests < limits)
3. Guaranteed (requests == limits for all resources)

### Common Causes

- BestEffort pods are evicted first under node pressure
- Burstable pods evicted next if more resources needed
- Guaranteed pods are evicted last (only if absolutely necessary)
- OOM score is higher for BestEffort pods
- No resource limits set on critical pods

### How to Fix

Set Guaranteed QoS for critical workloads:
```yaml
resources:
  requests:
    memory: 512Mi
    cpu: 500m
  limits:
    memory: 512Mi
    cpu: 500m
```

Check pod QoS class:
```bash
kubectl get pod <name> -o jsonpath='{.status.qosClass}'
```

### Examples

```bash
# Check pod QoS class
kubectl get pod my-app -o jsonpath='{.status.qosClass}'
# Burstable

# Upgrade to Guaranteed
kubectl set resources deployment/my-app --requests=cpu=500m,memory=512Mi --limits=cpu=500m,memory=512Mi

# Check QoS class again
kubectl get pod my-app-xxx -o jsonpath='{.status.qosClass}'
# Guaranteed
```"""),

    # More security
    ("pod-identity-error", "Pod identity / workload identity error",
     "Fix Kubernetes pod identity and workload identity errors. Resolve authentication failures when pods need to access cloud resources.",
     """## Pod Identity / Workload Identity Error

`Failed to get credentials: AccessDenied`

This error occurs when a pod configured with workload identity (IAM roles for service accounts, GCP workload identity, Azure AD pod identity) cannot obtain credentials for cloud resource access.

### Common Causes

- IAM role / service account annotation is missing or incorrect
- OIDC provider is not configured for the cluster
- Trust relationship between cloud IAM and K8s SA is misconfigured
- Service account exists but annotation is missing
- GKE workload identity: K8s SA to GCP SA binding missing

### How to Fix

For AWS EKS IRSA:
```bash
kubectl annotate serviceaccount <sa> eks.amazonaws.com/role-arn=arn:aws:iam::<account>:role/<role>
```

For GKE Workload Identity:
```bash
kubectl annotate serviceaccount <sa> iam.gke.io/gcp-service-account=<gcp-sa>@<project>.iam.gserviceaccount.com
```

For Azure AD Pod Identity:
```bash
kubectl label serviceaccount <sa> aadpodidbinding=<identity-name>
```

### Examples

```bash
# EKS - associate IAM role with service account
kubectl annotate serviceaccount my-sa eks.amazonaws.com/role-arn=arn:aws:iam::123456789:role/my-app-role

# Verify the trust policy
aws iam get-role --role-name my-app-role | jq '.Role.AssumeRolePolicyDocument'
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
