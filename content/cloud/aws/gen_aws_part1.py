"""Generate AWS cloud error pages - Part 1: EC2, S3, Lambda"""
import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/cloud/aws"
EXISTING = {f.rsplit(".", 1)[0] for f in os.listdir(OUTPUT_DIR) if f.endswith(".md")}

PAGES = []

def add(prefix, title, desc, causes, commands):
    base = title.lower().replace(" ", "-").replace("/", "-").replace("--", "-").replace("_", "-")
    candidate = f"{prefix}-{base}"
    slug = candidate
    if slug in EXISTING:
        i = 2
        while f"{slug}-v{i}" in EXISTING:
            i += 1
        slug = f"{slug}-v{i}"
    PAGES.append((title, desc, slug, causes, commands))

def write_pages():
    for title, desc, slug, causes, commands in PAGES:
        filename = f"aws-{slug}.md"
        fpath = os.path.join(OUTPUT_DIR, filename)
        if os.path.exists(fpath):
            print(f"  SKIP: {filename}")
            continue
        lines = [
            "---",
            f'title: "[Solution] AWS {title}"',
            f'description: "{desc}"',
            'cloud: ["aws"]',
            'error-types: ["cloud-error"]',
            'severities: ["error"]',
            "weight: 5",
            "---",
            "",
            f"The `{title.replace('AWS ', '')}` error occurs when an AWS service cannot complete the requested operation.",
            "",
            "## Common Causes",
            "",
        ]
        for c in causes:
            lines.append(f"- {c}")
        lines.extend(["", "## How to Fix", ""])
        for label, cmd in commands:
            lines.append(f"### {label}")
            lines.append("")
            lines.append("```bash")
            lines.append(cmd)
            lines.append("```")
            lines.append("")
        lines.extend(["## Examples", ""])
        for c in causes[:4]:
            lines.append(f"- Example scenario: {c.lower()}")
        lines.extend(["", "## Related Errors", ""])
        lines.append(f"- [AWS EC2 Error]({{{{< relref \"/cloud/aws/aws-ec2-error\" >}}}}) -- General EC2 errors")
        lines.append(f"- [AWS CloudWatch Error]({{{{< relref \"/cloud/aws/aws-cloudwatch-error\" >}}}}) -- CloudWatch errors")
        with open(fpath, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  CREATED: {filename}")

# ===================== EC2 (19 pages) =====================
add("ec2", "EC2 Instance Insufficient Capacity",
    "InsufficientInstanceCapacity when EC2 cannot launch due to AZ resource exhaustion.",
    ["Capacity not available in the specified Availability Zone",
     "Other workloads have consumed available resources in the AZ",
     "Instance type is temporarily constrained in the region",
     "AWS is experiencing high demand in the AZ",
     "On-Demand Capacity Reservations were not requested"],
    [("Check capacity in other AZs", "aws ec2 describe-availability-zones --region us-east-1"),
     ("Try different instance type", "aws ec2 run-instances --image-id ami-0abcdef --instance-type c5a.xlarge --count 1"),
     ("Request Capacity Reservations", "aws ec2 create-capacity-reservation --instance-type c5.xlarge --instance-count 1 --availability-zone us-east-1a"),
     ("Check existing reservations", "aws ec2 describe-capacity-reservations"),
     ("Launch with capacity block", "aws ec2 run-instances --image-id ami-0abcdef --capacity-reservation-specification CapacityReservationPreference=open")])

add("ec2", "EC2 Spot Instance Max Price",
    "SpotMaxPriceTooLow when the bid price is below the Spot market price.",
    ["Spot price exceeds your maximum bid price",
     "Market demand increased Spot Instance pricing",
     "Instance type is in high demand on Spot market",
     "Region-specific Spot pricing dynamics",
     "Interruption threshold set too low"],
    [("Check Spot price history", "aws ec2 describe-spot-price-history --instance-type c5.xlarge --start-time 2025-01-01T00:00:00Z"),
     ("Request with higher max price", "aws ec2 request-spot-instances --spot-price 0.50 --instance-count 1 --type one-time"),
     ("Use less popular instance type", "aws ec2 describe-spot-price-history --instance-type t3.medium --start-time 2025-01-01T00:00:00Z"),
     ("Enable Capacity Rebalancing", "aws ec2 request-spot-instances --spot-price 0.30 --instance-interruption-behavior stop"),
     ("Fall back to On-Demand", "aws ec2 run-instances --image-id ami-0abcdef --instance-type c5.xlarge --count 1")])

add("ec2", "EC2 Spot Capacity Not Available",
    "SpotCapacityNotAvailable when Spot Instance capacity is temporarily exhausted.",
    ["Temporarily high Spot Instance usage in the AZ",
     "Instance type-specific capacity constraints",
     "Region-level Spot capacity exhaustion",
     "Launch specification compatibility issues",
     "Spot allocation strategy misfit"],
    [("Check Spot requests", "aws ec2 describe-spot-instance-requests"),
     ("Use capacity-optimized strategy", "aws ec2 request-spot-instances --instance-count 2 --type persistent --strategy capacity-optimized"),
     ("Specify multiple AZs", "aws ec2 request-spot-instances --launch-specification file://launch-spec.json"),
     ("Try capacity-optimized-prioritized", "aws ec2 request-spot-instances --instance-count 3 --strategy capacity-optimized-prioritized"),
     ("Fall back to On-Demand", "aws ec2 run-instances --image-id ami-0abcdef --instance-type c5.xlarge --count 1")])

add("ec2", "EBS Volume Attach Failed",
    "VolumeAttachmentError when an EBS volume cannot be attached to an EC2 instance.",
    ["Volume is already attached to another instance",
     "Instance and volume are in different Availability Zones",
     "Volume is in a different account or region",
     "Volume is in wrong state (creating, deleted)",
     "Instance does not support the volume type"],
    [("Describe volume status", "aws ec2 describe-volumes --volume-ids vol-0abc123"),
     ("Attach volume", "aws ec2 attach-volume --volume-id vol-0abc123 --instance-id i-0abc123 --device /dev/xvdf"),
     ("Detach first if attached", "aws ec2 detach-volume --volume-id vol-0abc123"),
     ("Check instance compatibility", "aws ec2 describe-instance-types --instance-types c5.xlarge"),
     ("Confirm same AZ", "aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].Placement.AvailabilityZone'")])

add("ec2", "Volume Type Incompatibility",
    "VolumeTypeNotSupported when the volume type is not compatible with the instance.",
    ["Instance does not support io2 Block Express volumes",
     "Instance type lacks NVMe driver support",
     "Maximum throughput per volume exceeded",
     "Maximum IOPS per instance exceeded for volume type",
     "EBS-optimization not enabled on instance"],
    [("Check EBS optimization", "aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].EbsOptimized'"),
     ("Modify EBS optimization", "aws ec2 modify-instance-attribute --instance-id i-0abc123 --ebs-optimized true"),
     ("Check supported volume types", "aws ec2 describe-instance-types --instance-types c5.xlarge --query 'InstanceTypes[*].EbsInfo'"),
     ("Convert volume type", "aws ec2 modify-volume --volume-id vol-0abc123 --volume-type gp3"),
     ("Create snapshot first", "aws ec2 create-snapshot --volume-id vol-0abc123 --description Pre-migration")])

add("ec2", "Snapshot In Progress",
    "SnapshotCreationPermission when a volume snapshot operation fails due to an existing snapshot.",
    ["A snapshot creation is already running for the volume",
     "Too many concurrent snapshot requests",
     "Volume I/O during snapshot causes delays",
     "Snapshot quota reached for the account",
     "The previous snapshot was canceled mid-operation"],
    [("Check snapshot progress", "aws ec2 describe-snapshots --owner-ids self --filters Name=volume-id,Values=vol-0abc123"),
     ("Wait for completion", "aws ec2 wait snapshot-completed --snapshot-ids snap-0abc123"),
     ("Cancel stale snapshot", "aws ec2 delete-snapshot --snapshot-id snap-0abc123"),
     ("Check snapshot quota", "aws ec2 describe-snapshot-attributes --snapshot-id snap-0abc123"),
     ("Create new snapshot", "aws ec2 create-snapshot --volume-id vol-0abc123 --tag-specifications ResourceType=snapshot")])

add("ec2", "Invalid AMI ID",
    "InvalidAMIID.NotFound when the AMI identifier is not valid.",
    ["Typographical error in the AMI ID",
     "AMI ID belongs to a different region",
     "AMI ID belongs to another AWS account",
     "The AMI has been deregistered",
     "AMI ID format is incorrect (ami-xxxxx vs ami-xxxxxxxxxxxxxxxxx)"],
    [("Verify AMI in current region", "aws ec2 describe-images --image-ids ami-0abcdef1234567890"),
     ("Search AMIs", "aws ec2 describe-images --owners self amazon --query 'Images[*].{ID:ImageId,Name:Name,Region:ImageLocation}'"),
     ("Cross-region AMI copy", "aws ec2 copy-image --source-image-id ami-0abcdef --source-region eu-west-1 --region us-east-1"),
     ("Find AMI by name", "aws ec2 describe-images --filters Name=name,Values=amzn2-ami-hvm-2*"),
     ("Get AMI from another account", "aws ec2 describe-images --image-ids ami-0abcdef --executable-users 123456789012")])

add("ec2", "Elastic IP Limit Exceeded",
    "ElasticIpLimitExceeded when the account EIP quota is reached.",
    ["Account Elastic IP quota exhausted",
     "Too many EIPs allocated across all regions",
     "EIPs not associated with running instances",
     "EC2-Classic Platform EIP limit restrictions",
     "Non-standard region EIP quota applies"],
    [("Check current EIP usage", "aws ec2 describe-addresses --region us-east-1"),
     ("Release unused EIPs", "aws ec2 release-address --allocation-id eipalloc-0abc123"),
     ("Request quota increase", "aws service-quotas request-service-quota-increase --service-code ec2 --quota-code L-0263D0A3 --desired-value 10"),
     ("Check quotas", "aws service-quotas get-service-quota --service-code ec2 --quota-code L-0263D0A3")])

add("ec2", "VPC Limit Exceeded",
    "VpcLimitExceeded when the account VPC limit has been reached.",
    ["Default VPC limit of 5 VPCs per region reached",
     "VPC limit is per-region quota",
     "Stacked VPCs from long-running projects",
     "Non-default VPCs not being cleaned up",
     "Organization-level VPC count restrictions"],
    [("Check VPC count", "aws ec2 describe-vpcs --region us-east-1"),
     ("Delete unused VPCs", "aws ec2 delete-vpc --vpc-id vpc-0abc123"),
     ("Request VPC quota increase", "aws service-quotas request-service-quota-increase --service-code vpc --quota-code L-F678F1CE --desired-value 10"),
     ("Check VPC quota", "aws service-quotas get-service-quota --service-code vpc --quota-code L-F678F1CE")])

add("ec2", "Placement Group Error",
    "PlacementGroupError when placement group constraints cannot be met.",
    ["Insufficient capacity in placement group",
     "Placement group span mismatch across AZs",
     "Partition placement group in wrong AZ",
     "Spread placement group instance limit reached",
     "Cluster placement groups limited to single AZ"],
    [("Describe placement group", "aws ec2 describe-placement-groups --group-names my-pg"),
     ("List instances in group", "aws ec2 describe-instances --filters Name=placement-group-name,Values=my-pg"),
     ("Create placement group", "aws ec2 create-placement-group --group-name my-pg --strategy cluster"),
     ("Delete unused group", "aws ec2 delete-placement-group --group-name my-pg")])

add("ec2", "Dedicated Host Error",
    "DedicatedHostError when dedicated host allocation fails.",
    ["Dedicated Host limit reached per region",
     "Insufficient capacity for the requested instance type",
     "Host is in wrong state (allocated, released)",
     "Host affinity or tenancy mismatch",
     "Availability Zone not specified correctly",
     "Host is still associated with instances"],
    [("Check Dedicated Hosts", "aws ec2 describe-hosts"),
     ("List host instances", "aws ec2 describe-hosts --host-ids h-0abc123 --query 'Hosts[*].Instances[*].InstanceId'"),
     ("Release host", "aws ec2 release-hosts --host-ids h-0abc123"),
     ("Allocate new host", "aws ec2 allocate-hosts --quantity 1 --availability-zone us-east-1a --instance-type c5.xlarge")])

add("ec2", "HPC Error",
    "HPCClusterError when High Performance Computing cluster operations fail.",
    ["EFA network interface attachment limit exceeded",
     "Insufficient cluster network throughput",
     "Elastic Fabric Adapter configuration mismatch",
     "NVIDIA GPU driver incompatibility",
     "Slurm workload manager node failure",
     "EFA security group rules misconfigured"],
    [("Check EFA associations", "aws ec2 describe-network-interfaces --filters Name=description,Values=EFA-*"),
     ("Verify EFA status", "aws ec2 describe-instance-types --instance-types p4d.24xlarge --query 'InstanceTypes[*].NetworkInfo'"),
     ("Check instance EFA state", "aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].NetworkInterfaces[*].Association'"),
     ("Configure EFA SG rules", "aws ec2 authorize-security-group-ingress --group-id sg-0abc123 --protocol tcp --port 2208 --cidr 0.0.0.0/0")])

# ===================== S3 (19 pages) =====================
add("s3", "S3 Bucket Access Denied",
    "AccessDenied when S3 bucket access is denied due to permissions.",
    ["IAM role/user lacks s3:ListBucket permission",
     "Bucket policy denies access explicitly",
     "SCP or Organization policy blocks access",
     "Public access block prevents anonymous access",
     "Cross-account bucket policy misconfiguration"],
    [("Check IAM permissions", "aws iam simulate-principal-policy --action s3:ListBucket --resource-arn arn:aws:s3:::my-bucket --policy-source-user arn:aws:iam::123456789012:user/myuser"),
     ("Check bucket policy", "aws s3api get-bucket-policy --bucket my-bucket"),
     ("Check public access block", "aws s3api get-public-access-block --bucket my-bucket"),
     ("List buckets", "aws s3 ls"),
     ("Cross-account check", "aws s3api get-bucket-acl --bucket my-bucket --expected-bucket-owner 123456789012")])

add("s3", "S3 Bucket Already Exists",
    "BucketAlreadyExists when the S3 bucket name is already taken.",
    ["Bucket name must be globally unique across all AWS accounts",
     "Account already owns a bucket with the name",
     "Another account owns the bucket name",
     "Bucket was recently deleted and name not released yet",
     "DNS propagation of deleted bucket name not complete"],
    [("Use a different bucket name", "aws s3api create-bucket --bucket my-unique-name-98765 --region us-east-1"),
     ("Check existing buckets", "aws s3 ls"),
     ("Verify ownership", "aws s3api get-bucket-location --bucket my-bucket")])

add("s3", "S3 Bucket Not Empty",
    "BucketNotEmpty when trying to delete a non-empty bucket.",
    ["Bucket contains objects",
     "Bucket versioning enabled and has versions",
     "Delete markers present in versioned bucket",
     "Incomplete multipart uploads exist",
     "Object ACLs reference the bucket"],
    [("List objects", "aws s3 ls s3://my-bucket/ --recursive"),
     ("Delete all objects", "aws s3 rm s3://my-bucket/ --recursive"),
     ("Delete versioned objects", "aws s3api delete-objects --bucket my-bucket --delete file://delete.json"),
     ("Abort multipart uploads", "aws s3api list-multipart-uploads --bucket my-bucket"),
     ("Force bucket deletion", "aws s3 rb s3://my-bucket --force")])

add("s3", "S3 Object Access Denied",
    "AccessDenied when S3 object get/put is denied.",
    ["IAM permissions missing for s3:GetObject",
     "Object ACL has restrictive grants",
     "Bucket policy overrides allow with deny",
     "KMS key used for encryption not accessible",
     "Pre-signed URL expired or signature invalid"],
    [("Test IAM permissions", "aws s3api get-object --bucket my-bucket --key path/to/object.txt out.txt"),
     ("Check bucket policy", "aws s3api get-bucket-policy --bucket my-bucket"),
     ("Get object ACL", "aws s3api get-object-acl --bucket my-bucket --key path/to/object.txt"),
     ("Check encryption settings", "aws s3api get-object-attributes --bucket my-bucket --key path/to/object.txt")])

add("s3", "S3 Multipart Upload Error",
    "EntityTooLarge/SlowDown when using S3 Multipart Upload.",
    ["Part size is below minimum (5 MiB) or above maximum (5 GiB)",
     "Number of parts exceeds limit of 10,000",
     "Upload ID has expired or been aborted",
     "Concurrent upload rate exceeds S3 limits",
     "Source file changed during multipart upload"],
    [("List parts", "aws s3api list-parts --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID"),
     ("Complete multipart upload", "aws s3api complete-multipart-upload --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID --multipart-upload file://parts.json"),
     ("Abort incomplete upload", "aws s3api abort-multipart-upload --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID")])

add("s3", "S3 Upload Part Failed",
    "UploadPartCopyError/SlowDown when an upload part fails.",
    ["Part size too small (minimum 5 MB)",
     "Network interruption during upload",
     "Upload ID is invalid or closed",
     "Source file changed mid-upload",
     "Server-side encryption mismatch"],
    [("Verify part sizes", "aws s3api list-parts --bucket my-bucket --key bigfile.iso --upload-id UPLOAD_ID"),
     ("Re-upload part", "aws s3api upload-part --bucket my-bucket --key bigfile.iso --part-number 3 --body part3.dat --upload-id UPLOAD_ID"),
     ("Check integrity", "aws s3api head-object --bucket my-bucket --key bigfile.iso")])

add("s3", "S3 Copy Object Failed",
    "CopyObjectError when cross-bucket or cross-region copy fails.",
    ["Source object is archived (Glacier/Deep Archive)",
     "Cross-region copy rate limits hit",
     "Source or destination bucket access denied",
     "KMS key mismatch between source and destination",
     "Object size exceeds 5 GB (use multipart copy)"],
    [("Single object copy", "aws s3api copy-object --copy-source source-bucket/path/to/object.txt --bucket destination-bucket --key copied/object.txt"),
     ("Use multipart copy for large files", "aws s3 cp s3://source-bucket/path/ s3://dest-bucket/path/ --recursive --cli-connect-timeout 0"),
     ("Restore from Glacier first", "aws s3api restore-object --bucket source-bucket --key path/to/object.txt")])

add("s3", "S3 ACL Error",
    "AccessControlListError when S3 ACL configuration is invalid.",
    ["ACL grantee email format is incorrect",
     "URI for group grant does not exist",
     "Exceeds 100 grants per ACL limit",
     "Cannot set ACL when bucket policy exists",
     "Object ACL and bucket ACL conflict"],
    [("Set object ACL", "aws s3api put-object-acl --bucket my-bucket --key file.txt --acl bucket-owner-full-control"),
     ("Get ACL", "aws s3api get-object-acl --bucket my-bucket --key file.txt")])

add("s3", "S3 Bucket Policy Error",
    "MalformedPolicy/PolicyTooLong when S3 bucket policy fails.",
    ["Policy size exceeds 20 KB limit",
     "Invalid principal or effect syntax",
     "Missing required Action or Resource statements",
     "Cross-service confused deputy protection missing",
     "Resource ARN does not match bucket correctly"],
    [("Get current bucket policy", "aws s3api get-bucket-policy --bucket my-bucket"),
     ("Delete policy", "aws s3api delete-bucket-policy --bucket my-bucket"),
     ("Put new policy", "aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json")])

add("s3", "S3 Transfer Acceleration",
    "S3TransferAccelerationError when Transfer Acceleration endpoint fails.",
    ["Bucket not enabled for Transfer Acceleration",
     "Upload rate exceeds 10 Gbps per bucket and region",
     "RTT less than 100ms to S3 endpoint",
     "TCP throughput lower than direct S3 endpoint",
     "Client has IP reputation issues"],
    [("Check acceleration status", "aws s3api get-bucket-accelerate-configuration --bucket my-bucket"),
     ("Enable acceleration", "aws s3api put-bucket-accelerate-configuration --bucket my-bucket --status Enabled"),
     ("Test acceleration speed", "aws s3 cp largefile.bin s3://my-bucket/ --region us-east-1 --endpoint-url https://my-bucket.s3-accelerate.amazonaws.com")])

add("s3", "S3 Encryption Mismatch",
    "KMS.DecryptException/BadDigest when S3 SSE settings conflict.",
    ["SSE-S3 vs SSE-KMS mismatch between bucket and request",
     "KMS key ID used in request does not match bucket key",
     "Object was encrypted with different algorithm",
     "Downgrade from SSE-KMS to SSE-S3 on existing object",
     "Dual-layer encryption conflict"],
    [("Check bucket encryption", "aws s3api get-bucket-encryption --bucket my-bucket"),
     ("Update bucket encryption", "aws s3api put-bucket-encryption --bucket my-bucket --server-side-encryption-configuration file://sse-config.json")])

add("s3", "S3 KMS Key Access Denied",
    "KMS.AccessDeniedException when S3 cannot access the KMS key.",
    ["KMS key IAM policy does not allow S3 service",
     "Cross-account KMS key permissions missing",
     "KMS key is disabled or pending deletion",
     "Grant for S3 service expired or revoked",
     "Region mismatch between bucket and KMS key"],
    [("Check KMS key policy", "aws kms get-key-policy --key-id alias/my-s3-key --policy-name default"),
     ("Enable key", "aws kms enable-key --key-id alias/my-s3-key")])

add("s3", "S3 Pre-signed URL Expired",
    "ExpiredToken/SignatureDoesNotMatch when a pre-signed URL is invalid.",
    ["Pre-signed URL expiration time has passed",
     "Signing timestamp skews due to client clock difference",
     "Credential used via assumed role has expired",
     "URL was generated with expired IAM user keys"],
    [("Generate new pre-signed URL", "aws s3 presign s3://my-bucket/file.txt --expires-in 86400")])

add("s3", "S3 Event Notification Failed",
    "InvalidArgument/NotImplemented for S3 Event Notifications.",
    ["Destination SQS/SNS topic not in same region",
     "SQS policy does not allow S3 to send messages",
     "Lambda function invocation permission missing",
     "EventBridge notification conflicts with SQS/SNS",
     "Event notification configuration quota hit (100 per bucket)"],
    [("Get notification conf", "aws s3api get-bucket-notification-configuration --bucket my-bucket"),
     ("Check EventBridge", "aws s3api put-bucket-notification-configuration --bucket my-bucket --notification-configuration file://notif.json")])

add("s3", "S3 Replication Error",
    "ReplicationError when S3 Cross-Region/Same-Region Replication fails.",
    ["Source or destination bucket in different region",
     "KMS key for destination not accessible",
     "Replication IAM role permissions insufficient",
     "Object versioning not enabled on source or destination",
     "Replication Time Control SLA not met"],
    [("Check replication config", "aws s3api get-bucket-replication --bucket my-bucket")])

add("s3", "S3 Lifecycle Error",
    "MalformedXML/InvalidRequest for S3 Lifecycle rules.",
    ["Rule ID already exists",
     "Invalid date format in expiration",
     "Transition to INTELLIGENT_TIERING not allowed",
     "Noncurrent version expiration before transition",
     "Minimal storage size for transition not met (128KB)"],
    [("Get lifecycle config", "aws s3api get-bucket-lifecycle-configuration --bucket my-bucket")])

add("s3", "S3 Glacier Restore Failed",
    "RestoreObjectError when restoring from S3 Glacier/Deep Archive.",
    ["Object not stored in Glacier storage class",
     "Restore Request rate limit exceeded",
     "Expedited restore capacity not available",
     "Tier mismatch (Standard vs Bulk vs Expedited)",
     "Object deleted during restore process"],
    [("Initiate restore", "aws s3api restore-object --bucket my-bucket --key archived.zip --restore-request Days=3,GlacierJobParameters={Tier=Standard}"),
     ("Check restore status", "aws s3api head-object --bucket my-bucket --key archived.zip")])

# ===================== Lambda (19 pages) =====================
add("lambda", "Lambda Handler Not Found",
    "HandlerNotFound when the Lambda function handler does not exist.",
    ["Handler value does not match the exported function name",
     "Code does not contain the specified handler path",
     "Handler missing the file extension (.py, .js)",
     "Lambda runtime unable to locate the module",
     "Handler is in a subdirectory not in PATH"],
    [("Check handler config", "aws lambda get-function-configuration --function-name my-function"),
     ("Update handler", "aws lambda update-function-configuration --function-name my-function --handler index.handler")])

add("lambda", "Lambda Runtime Not Supported",
    "RuntimeNotSupportedException when the Lambda runtime is deprecated.",
    ["Runtime reached end of support date",
     "AWS ended standard support for the runtime",
     "Security patches no longer applied",
     "Node.js/Python/Java/PHP version is deprecated",
     "Runtime SDK compatibility issues"],
    [("Check current runtime", "aws lambda get-function-configuration --function-name my-function --query Runtime"),
     ("Update to newer runtime", "aws lambda update-function-configuration --function=my-function --runtime=nodejs20.x")])

add("lambda", "Lambda Memory Limit Error",
    "MemoryAllocationError/Lambda memory limit exhausted.",
    ["Function uses more memory than allocated, triggering OOM",
     "Memory limit set too low for workload",
     "Memory leak in code over execution cycles",
     "Large payload processing exceeds memory",
     "Concurrent executions accumulate memory pressure"],
    [("Check memory setting", "aws lambda get-function-configuration --function-name my-function --query MemorySize"),
     ("Update memory", "aws lambda update-function-configuration --function-name my-function --memory-size 2048")])

add("lambda", "Lambda Timeout Error",
    "Task timed out when Lambda duration exceeds timeout limit.",
    ["Function execution time exceeds defined timeout",
     "Cold start takes up significant time",
     "Infinite loops or blocking I/O in code",
     "External API calls are slow or hanging",
     "Large dataset processing takes too long"],
    [("Check timeout setting", "aws lambda get-function-configuration --function-name my-function --query Timeout"),
     ("Update timeout", "aws lambda update-function-configuration --function-name my-function --timeout 30")])

add("lambda", "Lambda Concurrency Limit",
    "ReservedFunctionConcurrencyInvocationLimit exceeded.",
    ["Account-level concurrency limit reached (1000 default)",
     "Reserved concurrency quota exceeded at function level",
     "Burst concurrency per region reached",
     "Provisioned concurrency uses all available slots",
     "No unreserved concurrency available across functions"],
    [("Get concurrency settings", "aws lambda get-function-concurrency --function-name my-function")])

add("lambda", "Lambda Unreserved Concurrent Executions",
    "UnreservedConcurrentExecutions limit hit across all functions.",
    ["Account-level concurrency exhausted by reserved concurrency",
     "Too many functions use reserved concurrency",
     "Non-reserved pool completely consumed",
     "Sudden traffic spike across multiple functions",
     "Inadequate function-level tuning"],
    [("Check account summary", "aws lambda get-account-settings")])

add("lambda", "Lambda VPC Config Error",
    "InvalidParameterValueException for VPC configuration in Lambda.",
    ["VPC ID references a deleted or non-existent VPC",
     "Subnet ID belongs to a different AZ than intended",
     "Security group belongs to wrong VPC",
     "Too many VPC subnets specified (max 16)",
     "Both subnets in same AZ when High Availability needed"],
    [("Check VPC config", "aws lambda get-function-configuration --function-name my-function"),
     ("Update VPC config", "aws lambda update-function-configuration --function-name my-function --vpc-config SubnetIds=subnet-abc,subnet-def,SecurityGroupIds=sg-123")])

add("lambda", "Lambda ENI Creation Error",
    "ENILimit/InsufficientIP for Lambda VPC ENI creation.",
    ["Elastic Network Interface per region limit reached",
     "VPC does not have enough available IPs",
     "Security group max rules exceeded",
     "Rate limiting on EC2 API calls for ENI creation",
     "VPC does not have DHCP options set"],
    [("Check ENI count", "aws ec2 describe-network-interfaces --filters Name=vpc-id,Values=vpc-abc"),
     ("Release unused ENIs", "aws ec2 delete-network-interface --network-interface-id eni-abc")])

add("lambda", "Lambda@Edge Error",
    "LambdaAtEdgeError when CloudFront triggers fail.",
    ["Function exceeds 128MB limit for viewer-request/response",
     "Function exceeds 1MB size limit for all CloudFront events",
     "Function is not in us-east-1 region",
     "IAM role not replicated to us-east-1",
     "Invalid trigger event type specified",
     "Edge function timeout exceeds 5s for viewer events"],
    [("Check function size", "aws lambda get-function --function-name my-function --query Configuration.CodeSize"),
     ("List function versions", "aws lambda list-versions-by-function --function-name my-function")])

add("lambda", "Lambda Layers Not Found",
    "ResourceNotFoundException for Lambda Layer references.",
    ["Layer version ARN is incorrect",
     "Layer was deleted",
     "Layer is in wrong region",
     "Layer permission not granted to the account",
     "Layer version limit reached"],
    [("List layers", "aws lambda list-layers"),
     ("List layer versions", "aws lambda list-layer-versions --layer-name my-layer")])

add("lambda", "Lambda Code Storage Limit",
    "CodeStorageExceededException when Lambda code is too large.",
    ["Total code size for all functions exceeds 75GB",
     "Function code size exceeds 250MB unzipped",
     "Container images exceed the image size limit",
     "Historical function versions accumulate storage",
     "Large dependencies not moved to Lambda Layers"],
    [("Check account usage", "aws lambda get-account-settings --query AccountUsage"),
     ("Delete old versions", "aws lambda delete-function --function-name my-function --qualifier 3")])

add("lambda", "Lambda ZIP Size Too Large",
    "InvalidParameterValueException due to ZIP file exceeding 50MB.",
    ["Direct zip upload limited to 50MB",
     "Code includes node_modules or build artifacts",
     "Large dependencies not using layers",
     "Container images preferred for code > 50MB",
     "Optimize bundle with Webpack/esbuild/Rollup"],
    [("Check bundled size", "ls -lh my-function.zip"),
     ("Upload via S3 for larger packages", "aws s3 cp my-function.zip s3://my-deployment-bucket/")])

add("lambda", "Lambda IAM Role Missing",
    "InvalidParameterValueException for IAM role in Lambda.",
    ["IAM role ARN is invalid or does not exist",
     "IAM role was deleted after function creation",
     "IAM role is in a different AWS account",
     "IAM trust policy does not allow Lambda service",
     "IAM role path mismatch in ARN"],
    [("Verify IAM role", "aws iam get-role --role-name my-lambda-role"),
     ("Check trust policy", "aws iam get-role --role-name my-lambda-role --query Role.AssumeRolePolicyDocument")])

add("lambda", "Lambda DLQ Not Configured",
    "Custom resource events not delivered when DLQ is missing.",
    ["DLQ target ARN (SQS/SNS) is invalid",
     "DLQ resource-based policy does not allow Lambda",
     "TOCTOU race in async invocation without DLQ",
     "Max retries (2) exhausted without DLQ configured",
     "Delivery to DLQ would exceed SQS/SNS throttles"],
    [("Check DLQ config", "aws lambda get-function-configuration --function-name my-function"),
     ("Set DLQ", "aws lambda update-function-configuration --function-name my-function --dead-letter-config TargetArn=arn:aws:sqs:us-east-1:123456789012:my-dlq")])

add("lambda", "Lambda Async Invocation Error",
    "AsyncInvocationError when events are dropped.",
    ["Async event queue is full or throttled",
     "Function concurrency limit blocks new events",
     "Event payload exceeds the async payload limit (256KB)",
     "No DLQ configured and retries exhausted",
     "Too many async events accumulating"],
    [("Check event invoke config", "aws lambda get-function-event-invoke-config --function-name my-function")])

add("lambda", "Lambda Event Source Mapping Error",
    "InvalidParameterValue/ResourceConflict for event source mapping.",
    ["DynamoDB/Kinesis stream access denied",
     "Event source mapping limit reached (per function)",
     "SQS queue does not exist",
     "Batch size exceeds the maximum allowed",
     "Starting position not valid for stream checkpoint"],
    [("List mappings", "aws lambda list-event-source-mappings --function-name my-function"),
     ("Create mapping", "aws lambda create-event-source-mapping --function-name my-function --event-source-arn arn:aws:sqs:us-east-1:123456789012:my-queue")])

add("lambda", "Lambda Reserved Concurrency Error",
    "ReservedConcurrentExecutionsLimit when setting reserved concurrency.",
    ["Reserved concurrency value cannot be zero",
     "Total reserved concurrency across functions exceeds account limit",
     "Cannot set reserved concurrency below already provisioned amount",
     "Requested value exceeds available unreserved concurrency"],
    [("Remove reserved concurrency", "aws lambda delete-function-concurrency --function-name my-function"),
     ("Set reserved concurrency", "aws lambda put-function-concurrency --function-name my-function --reserved-concurrent-executions 10")])

add("lambda", "Lambda Provisioned Concurrency Error",
    "ProvisionedConcurrencyConfigNotFoundException when PC fails.",
    ["Function does not have a published version or alias",
     "Provisioned concurrency quota per function exhausted",
     "Account-level provisioned concurrency limit reached",
     "Function has resolved concurrency conflicting",
     "Alias or version does not exist"],
    [("Put PC config", "aws lambda put-provisioned-concurrency-config --function-name my-function --qualifier prod --provisioned-concurrent-executions 100"),
     ("Check PC status", "aws lambda get-provisioned-concurrency-config --function-name my-function --qualifier prod")])

add("lambda", "Lambda SnapStart Error",
    "SnapStartNotSupported/SnapStartCreateUpdateFailed for Lambda SnapStart.",
    ["Function code has network connections on init",
     "Unique identifiers generated during initialization",
     "Temporary credentials fetched during init",
     "Larger initial state takes longer to snapshot",
     "Runtime does not support SnapStart"],
    [("Enable SnapStart", "aws lambda update-function-configuration --function-name my-function --snap-start ApplyOn=PublishedVersions")])

if __name__ == "__main__":
    write_pages()
    print(f"\nTotal new AWS pages generated: {len(PAGES)}")
