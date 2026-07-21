"""Generate AWS cloud error pages (145+ new pages)"""

import os

OUTPUT_DIR = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/cloud/aws"

AWS_EC2 = [
    ("EC2 Instance Insufficient Capacity", "InsufficientInstanceCapacity when EC2 cannot launch due to AZ resource exhaustion.", "ec2-insufficient-capacity", [
        "Capacity not available in the specified Availability Zone",
        "Other workloads have consumed available resources",
        "Instance type is temporarily constrained in the region",
        "AWS is experiencing high demand in the AZ",
        "On-Demand Capacity Reservations were not requested",
    ], [
        ("Check capacity in other AZs", "aws ec2 describe-availability-zones --region us-east-1"),
        ("Try a different instance type", "aws ec2 run-instances --image-id ami-0abcdef --instance-type c5a.xlarge --count 1"),
        ("Request EC2 Capacity Reservations", "aws ec2 create-capacity-reservation --instance-type c5.xlarge --instance-count 1 --availability-zone us-east-1a"),
        ("Check Reservations", "aws ec2 describe-capacity-reservations"),
        ("Launch with capacity block", "aws ec2 run-instances --image-id ami-0abcdef --capacity-reservation-specification CapacityReservationPreference=open"),
    ]),
    ("EC2 Spot Instance Max Price", "SpotMaxPriceTooLow when the bid price is below the Spot market price.", "ec2-spot-max-price", [
        "Spot price exceeds your maximum bid price",
        "Market demand increased Spot Instance pricing",
        "Instance type is in high demand on Spot market",
        "Region-specific Spot pricing dynamics",
        "Interruption threshold set too low",
    ], [
        ("Check Spot price history", "aws ec2 describe-spot-price-history --instance-type c5.xlarge --start-time 2025-01-01T00:00:00Z"),
        ("Request with higher max price", "aws ec2 request-spot-instances --spot-price 0.50 --instance-count 1 --type one-time"),
        ("Use a less popular instance type", "aws ec2 describe-spot-price-history --instance-type t3.medium --start-time 2025-01-01T00:00:00Z"),
        ("Enable Capacity Rebalancing", "aws ec2 request-spot-instances --spot-price 0.30 --instance-interruption-behavior stop"),
        ("Consider OD CR instead", "aws ec2 run-instances --image-id ami-0abcdef --instance-type c5.xlarge --count 1"),
    ]),
    ("EC2 Spot Capacity Not Available", "SpotCapacityNotAvailable when Spot Instance capacity is temporarily exhausted.", "ec2-spot-capacity-not-available", [
        "Temporarily high Spot Instance usage in the AZ",
        "Instance type-specific capacity constraints",
        "Region-level Spot capacity exhaustion",
        "Launch specification compatibility issues",
        "Spot allocation strategy misfit",
    ], [
        ("Check Spot capacity across AZs", "aws ec2 describe-spot-instance-requests"),
        ("Use capacity-optimized strategy", "aws ec2 request-spot-instances --instance-count 2 --type persistent --strategy capacity-optimized"),
        ("Specify multiple AZs", "aws ec2 request-spot-instances --launch-specification file://launch-spec.json"),
        ("Try capacity-optimized-prioritized", "aws ec2 request-spot-instances --instance-count 3 --strategy capacity-optimized-prioritized"),
        ("Fall back to On-Demand", "aws ec2 run-instances --image-id ami-0abcdef --instance-type c5.xlarge --count 1"),
    ]),
    ("EBS Volume Attach Failed", "VolumeAttachmentError when an EBS volume cannot be attached to an EC2 instance.", "ec2-ebs-volume-attach-failed", [
        "Volume is already attached to another instance",
        "Instance and volume are in different Availability Zones",
        "Volume is in a different account/region",
        "Volume is in the wrong state (creating, deleted)",
        "Instance does not support the volume type",
        "IOPS or throughput request exceeds instance limits",
    ], [
        ("Describe volume status", "aws ec2 describe-volumes --volume-ids vol-0abc123"),
        ("Attach volume", "aws ec2 attach-volume --volume-id vol-0abc123 --instance-id i-0abc123 --device /dev/xvdf"),
        ("Detach first if attached", "aws ec2 detach-volume --volume-id vol-0abc123"),
        ("Check instance compatibility", "aws ec2 describe-instance-types --instance-types c5.xlarge"),
        ("Confirm same AZ", "aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].Placement.AvailabilityZone'"),
    ]),
    ("Volume Type Incompatibility", "VolumeTypeNotSupported when the volume type is not compatible with the instance.", "ec2-volume-type-incompatibility" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-volume-type-incompatibility.md")) else "ec2-volume-type-v2", [
        "Instance does not support io2 Block Express volumes",
        "Instance type lacks NVMe driver support",
        "Maximum throughput per volume exceeded",
        "Maximum IOPS per instance exceeded for volume type",
        "EBS-optimization not enabled on instance",
    ], [
        ("Check EBS optimization", "aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].EbsOptimized'"),
        ("Modify EBS optimization", "aws ec2 modify-instance-attribute --instance-id i-0abc123 --ebs-optimized true"),
        ("Check supported volume types", "aws ec2 describe-instance-types --instance-types c5.xlarge --query 'InstanceTypes[*].EbsInfo'"),
        ("Convert volume type", "aws ec2 modify-volume --volume-id vol-0abc123 --volume-type gp3"),
        ("Create snapshot first", "aws ec2 create-snapshot --volume-id vol-0abc123 --description Pre-migration"),
    ]),
    ("Snapshot In Progress", "SnapshotCreationPermission when a volume snapshot operation fails due to an existing snapshot.", "ec2-snapshot-in-progress" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-snapshot-in-progress.md")) else "ec2-snapshot-v2", [
        "A snapshot creation is already running for the volume",
        "Too many concurrent snapshot requests",
        "Volume I/O during snapshot causes delays",
        "Snapshot quota reached for the account",
        "The previous snapshot was canceled mid-operation",
    ], [
        ("Check snapshot progress", "aws ec2 describe-snapshots --owner-ids self --filters Name=volume-id,Values=vol-0abc123"),
        ("Wait for completion", "aws ec2 wait snapshot-completed --snapshot-ids snap-0abc123"),
        ("Cancel stale snapshot", "aws ec2 delete-snapshot --snapshot-id snap-0abc123"),
        ("Check snapshot quota", "aws ec2 describe-snapshot-attributes --snapshot-id snap-0abc123"),
        ("Create snapshot from console", "aws ec2 create-snapshot --volume-id vol-0abc123 --tag-specifications ResourceType=snapshot"),
    ]),
    ("Invalid AMI ID", "InvalidAMIID.NotFound when the AMI identifier is not valid.", "ec2-invalid-ami-id" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-invalid-ami-id.md")) else "ec2-invalid-ami-v2", [
        "Typographical error in the AMI ID",
        "AMI ID belongs to a different region",
        "AMI ID belongs to another AWS account",
        "The AMI has been deregistered",
        "AMI ID format is incorrect (ami-xxxxx vs ami-xxxxxxxxxxxxxxxxx)",
    ], [
        ("Verify AMI in current region", "aws ec2 describe-images --image-ids ami-0abcdef1234567890"),
        ("Search AMIs", "aws ec2 describe-images --owners self amazon --query 'Images[*].{ID:ImageId,Name:Name,Region:ImageLocation}'"),
        ("Cross-region AMI copy", "aws ec2 copy-image --source-image-id ami-0abcdef --source-region eu-west-1 --region us-east-1"),
        ("Find AMI by name", "aws ec2 describe-images --filters Name=name,Values=amzn2-ami-hvm-2*"),
        ("Get AMI from another account", "aws ec2 describe-images --image-ids ami-0abcdef --executable-users 123456789012"),
    ]),
    ("Elastic IP Limit Exceeded", "ElasticIpLimitExceeded when the account EIP quota is reached.", "ec2-elastic-ip-limit" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-elastic-ip-limit.md")) else "ec2-elastic-ip-limit-v2", [
        "Account Elastic IP quota exhausted",
        "Too many EIPs allocated across all regions",
        "EIPs not associated with running instances",
        "EC2-Classic Platform EIP limit strics",
        "Non-standard region EIP quota applies",
    ], [
        ("Check current EIP usage", "aws ec2 describe-addresses --region us-east-1"),
        "Release unused EIPs",
        "aws ec2 release-address --allocation-id eipalloc-0abc123",
        "Request quota increase",
        "aws service-quotas request-service-quota-increase --service-code ec2 --quota-code L-0263D0A3 --desired-value 10",
        "Check quotas",
        "aws service-quotas get-service-quota --service-code ec2 --quota-code L-0263D0A3",
    ]),
    ("VPC Limit Exceeded", "VpcLimitExceeded when the account VPC limit has been reached.", "ec2-vpc-limit" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-vpc-limit.md")) else "ec2-vpc-limit-v2", [
        "Default VPC limit of 5 VPCs per region reached",
        "VPC limit is per-region quota",
        "Stacked VPCs from long-running projects",
        "Non-default VPCs not being cleaned up",
        "Organization-level VPC count restrictions",
    ], [
        ("Check VPC count", "aws ec2 describe-vpcs --region us-east-1"),
        "Delete unused VPCs",
        'aws ec2 delete-vpc --vpc-id vpc-0abc123',
        "Request VPC quota increase",
        "aws service-quotas request-service-quota-increase --service-code vpc --quota-code L-F678F1CE --desired-value 10",
        "Check VPC quota",
        "aws service-quotas get-service-quota --service-code vpc --quota-code L-F678F1CE",
    ]),
    ("Placement Group Error", "PlacementGroupError when placement group constraints cannot be met.", "ec2-placement-group-error" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-placement-group-error.md")) else "ec2-placement-group-v2", [
        "Insufficient capacity in placement group",
        "Placement group span mismatch across AZs",
        "Partition placement group in wrong AZ",
        "Spread placement group instance limit reached",
        "Cluster placement groups limited to single AZ",
        "HPC cluster placement insufficient throughput",
    ], [
        ("Describe placement group", "aws ec2 describe-placement-groups --group-names my-pg"),
        "List instances in placement group",
        'aws ec2 describe-instances --filters Name=placement-group-name,Values=my-pg',
        "Create placement group",
        "aws ec2 create-placement-group --group-name my-pg --strategy cluster",
        "Delete unused placement groups",
        "aws ec2 delete-placement-group --group-name my-pg",
    ]),
    ("Dedicated Host Error", "DedicatedHostError when dedicated host allocation fails.", "ec2-dedicated-host-error" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-dedicated-host-error.md")) else "ec2-dedicated-host-v2", [
        "Dedicated Host limit reached per region",
        "Insufficient capacity for the requested instance type",
        "Host is in the wrong state (allocated, released)",
        "Host affinity or tenancy mismatch",
        "Availability Zone not specified correctly",
        "Host is still associated with instances",
    ], [
        ("Check Dedicated Hosts", "aws ec2 describe-hosts"),
        "List host instances",
        "aws ec2 describe-hosts --host-ids h-0abc123 --query 'Hosts[*].Instances[*].InstanceId'",
        "Release host",
        "aws ec2 release-hosts --host-ids h-0abc123",
        "Allocate new host",
        "aws ec2 allocate-hosts --quantity 1 --availability-zone us-east-1a --instance-type c5.xlarge",
    ]),
    ("HPC Error", "HPCClusterError when High Performance Computing cluster operations fail.", "ec2-hpc-error" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-ec2-hpc-error.md")) else "ec2-hpc-v2", [
        "EFA network interface attachment limit exceeded",
        "Insufficient cluster network throughput",
        "Elastic Fabric Adapter configuration mismatch",
        "NVIDIA GPU driver incompatibility",
        "Slurm workload manager node failure",
        "EFA security group rules misconfigured",
    ], [
        ("Check EFA associations", "aws ec2 describe-network-interfaces --filters Name=description,Values=E FA-*"),
        "Verify EFA status",
        "aws ec2 describe-instance-types --instance-types p4d.24xlarge --query 'InstanceTypes[*].NetworkInfo'",
        "Check instance EFA state",
        "aws ec2 describe-instances --instance-ids i-0abc123 --query 'Reservations[*].Instances[*].NetworkInterfaces[*].Association'",
        "Configure EFA SG rules",
        "aws ec2 authorize-security-group-ingress --group-id sg-0abc123 --protocol tcp --port 2208 --cidr 0.0.0.0/0",
    ]),
]

AEC2_ALREADY_EXISTS = {f.rsplit(".", 1)[0] for f in os.listdir(OUTPUT_DIR) if f.endswith(".md")}
def slug(name):
    return name.lower().replace(" ", "-").replace("/", "-").replace("é", "e")

def write_page(category_prefix, title, desc, filename_slug, causes, commands_with_examples):
    filename = f"aws-{filename_slug}.md"
    fpath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(fpath):
        print(f"  SKIP (exists): {filename}")
        return
    lines = ["---"]
    lines.append(f'title: "[Solution] AWS {title}"')
    lines.append(f'description: "{desc}"')
    lines.append('cloud: ["aws"]')
    lines.append('error-types: ["cloud-error"]')
    lines.append('severities: ["error"]')
    lines.append("weight: 5")
    lines.append("---")
    error_name = title.replace("AWS ", "")
    lines.append(f"\nThe `{error_name}` error occurs when an AWS service cannot complete the requested operation.\n")
    lines.append("## Common Causes\n")
    for c in causes:
        lines.append(f"- {c}")
    lines.append("\n## How to Fix\n")
    if isinstance(commands_with_examples[0], tuple):
        for label, cmd in commands_with_examples:
            lines.append(f"### {label}\n")
            lines.append("```bash")
            for part in cmd.split("\n"):
                lines.append(part)
            lines.append("```\n")
    else:
        for i in range(0, len(commands_with_examples), 2):
            label = commands_with_examples[i]
            cmd = commands_with_examples[i+1]
            lines.append(f"### {label}\n")
            lines.append("```bash")
            for part in cmd.split("\n"):
                lines.append(part)
            lines.append("```\n")
    lines.append("## Examples\n")
    for item in causes[:3]:
        lines.append(f"- Example scenario: {item}")
    lines.append("")
    lines.append("## Related Errors\n")
    lines.append(f"- [AWS EC2 Error]({{{{< relref \"/cloud/aws/aws-ec2-error\" >}}}}) -- General EC2 errors")
    lines.append(f"- [AWS CloudWatch Error]({{{{< relref \"/cloud/aws/aws-cloudwatch-error\" >}}}}) -- CloudWatch errors")
    with open(fpath, "w") as f:
        f.write("\n".join(lines))
    ext = filename.split(".")[0].removeprefix("aws-")
    print(f"  CREATED: {filename}")
    return fpath


counters = {}

# --- S3 ---
S3 = [
    ("S3 Bucket Access Denied", "AccessDenied when S3 bucket access is denied due to permissions.", "s3-bucket-access-denied", [
        "IAM role/user lacks s3:ListBucket permission",
        "Bucket policy denies access explicitly",
        "SCP or Organization policy blocks access",
        "Public access block prevents anonymous access",
        "Cross-account bucket policy misconfiguration",
    ], [
        ("Check IAM permissions", "aws iam simulate-principal-policy --action s3:ListBucket --resource-arn arn:aws:s3:::my-bucket --policy-source-user arn:aws:iam::123456789012:user/myuser"),
        "Check bucket policy",
        "aws s3api get-bucket-policy --bucket my-bucket",
        "Check public access block",
        "aws s3api get-public-access-block --bucket my-bucket",
        "List buckets",
        "aws s3 ls",
        "Cross-account access check",
        'aws s3api get-bucket-acl --bucket my-bucket --expected-bucket-owner 123456789012',
    ]),
    ("S3 Bucket Already Exists", "BucketAlreadyExists when the S3 bucket name is already taken.", "s3-bucket-already-exists", [
        "Bucket name must be globally unique across all AWS accounts",
        "Account already owns a bucket with the name",
        "Another account owns the bucket name",
        "Bucket was recently deleted and name not released yet",
        "DNS propagation of deleted bucket name not complete",
    ], [
        ("Use a different bucket name", "aws s3api create-bucket --bucket my-unique-name-98765 --region us-east-1"),
        "Check existing buckets",
        "aws s3 ls",
        "Verify ownership",
        "aws s3api get-bucket-location --bucket my-bucket",
    ]),
    ("S3 Bucket Not Empty", "BucketNotEmpty when trying to delete a non-empty bucket.", "s3-bucket-not-empty", [
        "Bucket contains objects",
        "Bucket versioning enabled and has versions",
        "Delete markers present in versioned bucket",
        "Incomplete multipart uploads exist",
        "Object ACLs reference the bucket",
    ], [
        ("List objects", "aws s3 ls s3://my-bucket/ --recursive"),
        "Delete all objects",
        "aws s3 rm s3://my-bucket/ --recursive",
        "Delete versioned objects",
        "aws s3api delete-objects --bucket my-bucket --delete file://delete.json",
        "Abort multipart uploads",
        "aws s3api list-multipart-uploads --bucket my-bucket",
        "Force bucket deletion",
        "aws s3 rb s3://my-bucket --force",
    ]),
    ("S3 Object Access Denied", "AccessDenied when S3 object get/put is denied.", "s3-object-access-denied", [
        "IAM permissions missing for s3:GetObject",
        "Object ACL has restrictive grants",
        "Bucket policy overrides allow with deny",
        "KMS key used for encryption not accessible",
        "Pre-signed URL expired or signature invalid",
        "Block Public Access enabled on object",
    ], [
        ("Test IAM permissions", "aws s3api get-object --bucket my-bucket --key path/to/object.txt out.txt"),
        "Check bucket policy",
        "aws s3api get-bucket-policy --bucket my-bucket",
        "Get object ACL",
        "aws s3api get-object-acl --bucket my-bucket --key path/to/object.txt",
        "Check encryption settings",
        "aws s3api get-object-attributes --bucket my-bucket --key path/to/object.txt",
    ]),
    ("S3 Multipart Upload Error", "EntityTooLarge/SlowDown when using S3 Multipart Upload.", "s3-multipart-upload", [
        "Part size is below minimum (5 MiB) or maximum (5 GiB)",
        "Number of parts exceeds limit of 10,000",
        "Upload ID has expired or been aborted",
        "Concurrent upload rate exceeds S3 limits",
        "Source file changed during multipart upload",
        "Checksum mismatch for uploaded part",
    ], [
        ("List parts", "aws s3api list-parts --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID"),
        "Complete multipart upload",
        "aws s3api complete-multipart-upload --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID --multipart-upload file://parts.json",
        "Abort incomplete upload",
        "aws s3api abort-multipart-upload --bucket my-bucket --key largefile.zip --upload-id EXAMPLE_UPLOAD_ID"),
    ]),
    ("S3 Upload Part Failed", "UploadPartCopyError/SlowDown when an upload part fails.", "s3-upload-part-failed", [
        "Part size too small (minimum 5 MB)",
        "Network interruption during upload",
        "Upload ID is invalid or closed",
        "Source file changed mid-upload",
        "Server-side encryption mismatch",
    ], [
        ("Verify part sizes", "aws s3api list-parts --bucket my-bucket --key bigfile.iso --upload-id UPLOAD_ID"),
        "Re-upload part",
        "aws s3api upload-part --bucket my-bucket --key bigfile.iso --part-number 3 --body part3.dat --upload-id UPLOAD_ID",
        "Check integrity",
        "aws s3api head-object --bucket my-bucket --key bigfile.iso"),
    ]),
    ("S3 Copy Object Failed", "CopyObjectError when cross-bucket or cross-region copy fails.", "s3-copy-object-failed", [
        "Source object is archived (Glacier/Deep Archive)",
        "Cross-region copy rate limits hit",
        "Source or destination bucket access denied",
        "KMS key mismatch between source and destination",
        "Object size exceeds 5 GB (use multipart copy)",
        "Destination bucket SSE settings conflict",
    ], [
        ("Single object copy", "aws s3api copy-object --copy-source source-bucket/path/to/object.txt --bucket destination-bucket --key copied/object.txt"),
        "Use multipart copy for large files",
        "aws s3 cp s3://source-bucket/path/ s3://dest-bucket/path/ --recursive --cli-connect-timeout 0",
        "Restore from Glacier first",
        "aws s3api restore-object --bucket source-bucket --key path/to/object.txt"),
    ]),
    ("S3 ACL Error", "AccessControlListError when S3 ACL configuration is invalid.", "s3-acl-error", [
        "ACL grantee email format is incorrect",
        "URI for group grant does not exist",
        "Exceeds 100 grants per ACL limit",
        "Cannot set ACL when bucket policy exists",
        "Object ACL and bucket ACL conflict",
    ], [
        ("Set object ACL", "aws s3api put-object-acl --bucket my-bucket --key file.txt --acl bucket-owner-full-control"),
        "Remove ACL grants",
        "aws s3api get-object-acl --bucket my-bucket --key file.txt"),
    ]),
    ("S3 Bucket Policy Error", "MalformedPolicy/PolicyTooLong when S3 bucket policy fails.", "s3-bucket-policy", [
        "Policy size exceeds 20 KB limit",
        "Invalid principal or effect syntax",
        "Missing required Action or Resource statements",
        "Cross-service confused deputy protection missing",
        "Resource ARN does not match bucket correctly",
        "IAM role referenced does not exist",
    ], [
        ("Current bucket policy", "aws s3api get-bucket-policy --bucket my-bucket"),
        "Delete policy",
        "aws s3api delete-bucket-policy --bucket my-bucket",
        "Update with new policy",
        "aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json"),
    ]),
    ("S3 Transfer Acceleration", "S3TransferAccelerationError when Transfer Acceleration endpoint fails.", "s3-transfer-acceleration", [
        "Bucket not enabled for Transfer Acceleration",
        "Upload rate exceeds 10 Gbps per bucket and region",
        "RTT less than 100ms to S3 endpoint",
        "TCP throughput lower than direct S3 endpoint",
        "Client has IP reputation issues",
    ], [
        ("Check acceleration status", "aws s3api get-bucket-accelerate-configuration --bucket my-bucket"),
        "Enable acceleration",
        "aws s3api put-bucket-accelerate-configuration --bucket my-bucket --status Enabled",
        "Test acceleration speed",
        "aws s3 cp largefile.bin s3://my-bucket/ --region us-east-1 --endpoint-url https://my-bucket.s3-accelerate.amazonaws.com"),
    ]),
    ("S3 Encryption Mismatch", "KMS.DecryptException/BadDigest when S3 SSE settings conflict.", "s3-encryption-mismatch", [
        "SSE-S3 vs SSE-KMS mismatch between bucket and request",
        "KMS key ID used in request does not match bucket key",
        "Object was encrypted with different algorithm",
        "Downgrade from SSE-KMS to SSE-S3 on existing object",
        "Dual-layer encryption conflict",
    ], [
        ("Check bucket encryption", "aws s3api get-bucket-encryption --bucket my-bucket"),
        "Update bucket encryption",
        "aws s3api put-bucket-encryption --bucket my-bucket --server-side-encryption-configuration file://sse-config.json"),
    ]),
    ("S3 KMS Key Access Denied", "KMS.AccessDeniedException when S3 cannot access the KMS key.", "s3-kms-key-access", [
        "KMS key IAM policy does not allow S3 service",
        "Cross-account KMS key permissions missing",
        "KMS key is disabled or pending deletion",
        "Grant for S3 service expired or revoked",
        "Region mismatch between bucket and KMS key",
    ], [
        ("Check KMS key policy", "aws kms get-key-policy --key-id alias/my-s3-key --policy-name default"),
        "Enable key",
        "aws kms enable-key --key-id alias/my-s3-key"),
    ]),
    ("S3 Pre-signed URL Expired", "ExpiredToken/SignatureDoesNotMatch when a pre-signed URL is invalid.", "s3-presigned-url-expired", [
        "Pre-signed URL expiration time has passed",
        "Signing timestamp skews due to client clock",
        "Credential used via assumed role expired",
        "URL was generated with expired IAM user keys",
    ], [
        ("Generate new pre-signed URL", "aws s3 presign s3://my-bucket/file.txt --expires-in 86400"),
    ]),
    ("S3 Event Notification Failed", "InvalidArgument/NotImplemented for S3 Event Notifications.", "s3-event-notification", [
        "Destination SQS/SNS topic not in same region",
        "SQS policy does not allow S3 to send",
        "Lambda function invocation permission missing",
        "EventBridge notification conflicts with SQS/SNS",
        "Event notification configuration quota hit (100 per bucket)",
    ], [
        ("Get notification conf", "aws s3api get-bucket-notification-configuration --bucket my-bucket"),
        "Check EventBridge",
        "aws s3api put-bucket-notification-configuration --bucket my-bucket --notification-configuration file://notif.json"),
    ]),
    ("S3 Replication Error", "ReplicationError when S3 Cross-Region/Same-Region Replication fails.", "s3-replication", [
        "Source or destination bucket in different region",
        "KMS key for destination not accessible",
        "Replication IAM role permissions insufficient",
        "Object versioning not enabled on source/destination",
        "Replication Time Control (RTC) SLA not met",
    ], [
        ("Check replication status",
         "aws s3api get-bucket-replication --bucket my-bucket"),
    ]),
    ("S3 Lifecycle Error", "MalformedXML/InvalidRequest for S3 Lifecycle rules.", "s3-lifecycle", [
        "Rule ID already exists",
        "Invalid date format in expiration",
        "Transition to INTELLIGENT_TIERING not allowed",
        "Noncurrent version expiration before transition",
        "Minimal storage size for transition not met (128KB)",
    ], [
        ("Get lifecycle config",
         "aws s3api get-bucket-lifecycle-configuration --bucket my-bucket"),
    ]),
    ("S3 Glacier Restore Failed", "RestoreObjectError when restoring from S3 Glacier/Deep Archive.", "s3-glacier-restore", [
        "Object not stored in Glacier storage class",
        "Restore Request rate limit exceeded",
        "Expedited restore capacity not available",
        "Tier mismatch (Standard vs Bulk vs Expedited)",
        "Object deleted during restore process",
        "Temporary Glacier service capacity availability",
    ], [
        ("Initiate restore", "aws s3api restore-object --bucket my-bucket --key archived.zip --restore-request Days=3,GlacierJobParameters={Tier=Standard}"),
        "Check restore status",
        "aws s3api head-object --bucket my-bucket --key archived.zip"),
    ]),
]

# --- Lambda ---

LAMBDA = [
    ("Lambda Handler Not Found", "HandlerNotFound when the Lambda function handler does not exist.", "lambda-handler-not-found", [
        "Handler value does not match the exported function name",
        "Code does not contain the specified handler path",
        "Handler missing the file extension (.py, .js)",
        "Lambda runtime unable to locate the module",
        "Handler is in a subdirectory not in PATH",
        "CloudFront Lambda@Edge handler runtime mismatch",
    ], [
        ("Check handler config", "aws lambda get-function-configuration --function-name my-function"),
        "Update handler",
        "aws lambda update-function-configuration --function-name my-function --handler index.handler"),
    ]),
    ("Lambda Runtime Not Supported", "RuntimeNotSupportedException when the Lambda runtime is deprecated.", "lambda-runtime-not-supported", [
        "Runtime reached end of support date",
        "AWS ended standard support for the runtime",
        "Security patches no longer applied",
        "Node.js/Python/Java/PHP version is deprecated",
        "Runtime SDK compatibility issues",
        "Function code relies on deprecated runtime libs",
    ], [
        ("Check current runtime", "aws lambda get-function-configuration --function-name my-function --query 'Runtime'"),
        "Update to newer runtime",
        "aws lambda update-function-configuration --function=my-function --runtime=nodejs20.x",
    ]),
    ("Lambda Memory Limit Error", "MemoryAllocationError/Lambda memory limit exhausted.", "lambda-memory-limit" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-lambda-memory-limit.md")) else "lambda-memory-v2", [
        "Function uses more memory than allocated, triggering OOM",
        "Memory limit set too low for workload",
        "Memory leak in code over execution cycles",
        "Large payload processing exceeds memory",
        "Concurrent executions accumulate memory pressure",
    ], [
        ("Check current memory setting", "aws lambda get-function-configuration --function-name my-function --query 'MemorySize'"),
        "Update memory to a larger size",
        "aws lambda update-function-configuration --function-name my-function --memory-size 2048"),
    ]),
    ("Lambda Timeout Error", "Task timed out when Lambda duration exceeds timeout limit.", "lambda-timeout-error" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-lambda-timeout-error.md")) else "lambda-timeout-v2", [
        "Function execution time exceeds defined timeout",
        "Cold start takes up significant time",
        "Infinite loops or blocking I/O in code",
        "External API calls are slow or hanging",
        "Large dataset processing takes too long",
        "Recursive/infinite invocation chain",
    ], [
        ("Check timeout setting", "aws lambda get-function-configuration --function-name my-function --query 'Timeout'"),
        "Update timeout",
        "aws lambda update-function-configuration --function-name my-function --timeout 30"),
    ]),
    ("Lambda Concurrency Limit", "ReservedFunctionConcurrencyInvocationLimit exceeded.", "lambda-concurrency-limit" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-lambda-concurrency-limit.md")) else "lambda-concurrency-v2", [
        "Account-level concurrency limit reached (1000 default)",
        "Reserved concurrency quota exceeded at function level",
        "Burst concurrency per region reached",
        "Provisioned concurrency uses all available slots",
        "No unreserved concurrency available across functions",
    ], [
        ("Check concurrency settings",
         "aws lambda get-function-concurrency --function-name my-function"),
    ]),
    ("Lambda Unreserved Concurrent Executions",
     "UnreservedConcurrentExecutions limit hit across all functions.",
     "lambda-unreserved-concurrent",
     [
         "Account-level concurrency exhausted by reserved concurrency",
         "Too many functions use reserved concurrency",
         "Non-reserved pool completely consumed",
         "Sudden traffic spike across multiple functions",
         "Inadequate function-level tuning",
     ],
     [
         ("Check account summary", "aws lambda get-account-settings"),
         "List function concurrency",
         "aws lambda list-function-event-invoke-configs --function my-function",
     ]),
    ("Lambda VPC Config Error",
     "InvalidParameterValueException for VPC configuration in Lambda.",
     "lambda-vpc-config-error",
     [
         "VPC ID references a deleted or non-existent VPC",
         "Subnet ID belongs to a different AZ than intended",
         "Security group belongs to wrong VPC",
         "Too many VPC subnets specified (max 16)",
         "Both subnets in same AZ when High Availability needed",
         "NAT Gateway/Internet Gateway not configured for private subnets",
     ],
     [("Check VPC config", "aws lambda get-function-configuration --function my-function"),
     ("Update VPC config", "aws lambda update-function-configuration --function my-function --vpc-config SubnetIds=subnet-abc,subnet-def,SecurityGroupIds=sg-123"),
     ]),
    ("Lambda ENI Creation Error", "ENILimit/InsufficientIP for Lambda VPC ENI creation.",
     "lambda-eni-creation-error",
     [
         "Elastic Network Interface per region limit reached",
         "VPC does not have enough available IPs",
         "Security group max rules exceeded",
         "Rate limiting on EC2 API calls for ENI creation",
         "VPC does not have DHCP options set",
         "Network ACL restrictions blocking DNS",
     ],
     [("Check ENI count", "aws ec2 describe-network-interfaces --filters Name=vpc-id,Values=vpc-abc"),
     ("Release unused ENIs",
      "aws ec2 delete-network-interface --network-interface-id eni-abc"),
     ]),
    ("Lambda@Edge Error", "LambdaAtEdgeError when CloudFront triggers fail.",
     "lambda-edge-error",
     [
         "Function exceeds 128MB limit for viewer-request/response",
         "Function exceeds 1MB size limit for all CloudFront events",
         "Function is not in us-east-1 region",
         "IAM role not replicated to us-east-1",
         "Invalid trigger event type specified",
         "Edge function timeout >5s for viewer events",
         "Edge function timeout >30s for origin events",
     ],
     [("Check function size", "aws lambda get-function --function my-function --query 'Configuration.CodeSize'"),
     ("List function versions", "aws lambda list-versions-by-function --function my-function"),
     ]),
    ("Lambda Layers Not Found",
     "ResourceNotFoundException for Lambda Layer references.",
     "lambda-layers-not-found",
     [
         "Layer version ARN is incorrect",
         "Layer was deleted",
         "Layer is in wrong region",
         "Layer permission not granted to the account",
         "Layer version limit reached",
         "Layer + function bundle exceeds 250MB unzipped",
     ],
     [("List layers", "aws lambda list-layers"),
     ("List layer versions",
      "aws lambda list-layer-versions --layer-name my-layer"),
     ]),
    ("Lambda Code Storage Limit",
     "CodeStorageExceededException when Lambda code is too large.",
     "lambda-code-storage-limit",
     [
         "Total code size for all functions exceeds 75GB",
         "Function code size exceeds 250MB unzipped",
         "Container images exceed the image size limit",
         "Historical function versions accumulate storage",
         // Duplicates removed
     ],
     [("Check account usage", "aws lambda get-account-settings --query 'AccountUsage'"),
     ("Delete old versions",
      "aws lambda delete-function --function-name my-function --qualifier 3"),
     ]),
    ("Lambda ZIP Size Too Large",
     "InvalidParameterValueException due to ZIP file exceeding 50MB.",
     "lambda-zip-too-large",
     [
         "Direct zip upload limited to 50MB",
         "Use layers for large dependencies",
         "Code includes node_modules or build artifacts",
         "Container images preferred for code >50MB",
         "Optimize bundle with Webpack/esbuild/Roller",
     ],
     [("Check bundled size", "du -sh my-function.zip"),
     ("Upload via S3 for larger packages",
      "aws s3 cp my-function.zip s3://my-deployment-bucket/"),
     ]),
    ("Lambda IAM Role Missing",
     "InvalidParameterValueException for IAM role in Lambda.",
     "lambda-iam-role-missing",
     [
         "IAM role ARN is invalid or does not exist",
         "IAM role was deleted after function creation",
         "IAM role is in a different AWS account",
         "IAM trust policy does not allow Lambda service",
         "IAM role path mismatch in ARN",
     ],
     [("Verify IAM role", "aws iam get-role --role-name my-lambda-role"),
     ("Check trust policy",
      "aws iam get-role --role-name my-lambda-role --query 'Role.AssumeRolePolicyDocument'"),
     ]),
    ("Lambda DLQ Not Configured",
     "Custom resource event was not delivered to the DLQ.",
     "lambda-dlq-not-configured",
     [
         "DLQ target ARN (SQS/SNS) is invalid",
         "DLQ resource-based policy does not allow Lambda",
         "TOCTOU race in async invocation without DLQ",
         "Max retries (2) exhausted without DLQ configured",
         "Delivery to DLQ would exceed SQS/SNS throttles",
     ],
     [("Check DLQ config", "aws lambda get-function-configuration --function my-function"),
     ("Set DLQ", "aws lambda update-function-configuration --function my-function --dead-letter-config TargetArn=arn:aws:sqs:us-east-1:123456789012:my-dlq"),
     ]),
    ("Lambda Async Invocation Error",
     "AsyncInvocationError when events are dropped.",
     "lambda-async-invocation",
     [
         "Async event queue is full or throttled",
         "Function concurrency limit blocks new events",
         "Event payload exceeds the async payload limit (256KB)",
         "No DLQ configured and retries exhausted",
         "Too many async events accumulating",
     ],
     [("Check invocation metrics", "aws lambda get-function-event-invoke-config --function my-function")]),
    ("Lambda Event Source Mapping Error",
     "InvalidParameterValue/ResourceConflict for event source mapping.",
     "lambda-event-source-mapping",
     [
         "DynamoDB/Kinesis stream access denied",
         "Event source mapping limit reached (per function)",
         "SQS queue does not exist",
         "Batch size exceeds the maximum allowed",
         "Bisect on function error not configurable for data loss scenarios",
         "Starting position TIMESTAMP not valid for DS checkpoints",
     ],
     [("List event mappings", "aws lambda list-event-source-mappings --function my-function"),
     ("Create mapping", "aws lambda create-event-source-mapping --function my-function --event-source-arn arn:aws:sqs:us-east-1:123456789012:my-queue"),
     ]),
    ("Lambda Reserved Concurrency Error",
     "ReservedConcurrentExecutionsLimit when setting reserved concurrency.",
     "lambda-reserved-concurrency",
     [
         "Reserved concurrency value cannot be 0",
         "Total reserved concurrency across functions exceeds account limit",
         "You cannot set reserved concurrency <0",
         "Cannot reduce reserved concurrency below already provisioned",
     ],
     [("Remove reserved concurrency", "aws lambda delete-function-concurrency --function my-function"),
     ("Set reserved concurrency", "aws lambda put-function-concurrency --function my-function --reserved-concurrent-executions 10")]),
    ("Lambda Provisioned Concurrency Error",
     "ProvisionedConcurrencyConfigNotFoundException when PC fails.",
     "lambda-provisioned-concurrency",
     [
         "Function does not have a published version or alias",
         "Provisioned concurrency quota per function exhausted",
         "Account-level provisioned concurrency limit reached",
         "Function has resolved concurrency conflicting",
         "Exceeded provisioned concurrency per region",
         "Alias or version does not exist",
     ],
     [("Put PC config", "aws lambda put-provisioned-concurrency-config --function my-function --qualifier prod --provisioned-concurrent-executions 100"),
     ("Check PC status", "aws lambda get-provisioned-concurrency-config --function my-function --qualifier prod")]),
    ("Lambda SnapStart Error",
     "SnapStartNotSupported/SnapStartCreateUpdateFailed for Lambda SnapStart.",
     "lambda-snapstart-error",
     [
         "Function code has network connections on init",
         "Unique identifiers generated during init",
         "Temporary credentials fetched during init",
         "Larger initial state takes longer to snapshot",
         "Runtime does not support SnapStart",
         "Ephemeral ports picked up in init snapshot",
     ],
     [("Enable SnapStart", "aws lambda update-function-configuration --function my-function --snap-start ApplyOn=PublishedVersions")]),
]

# RDS
RDS = [
    ("RDS DB Instance Limit Exceeded", "InstanceLimitExceeded when DB instance quota exceeded.", "rds-instance-limit" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-rds-instance-limit.md")) else "rds-instance-v2", [
        "Per-region DB instance quota reached",
        "RDS for each DB engine has separate limit",
        "On-Demand DB instance allocation full",
        "Reserved instance commitment count",
        "Multi-AZ instances count toward instance quota",
    ], [
        ("Check instance count", "aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier]'"),
        "Request limit increase",
        "aws service-quotas request-service-quota-increase --service-code rds --quota-code L-7B9D5F6A --desired-value 50")]),
    ("RDS Storage Full", "StorageFull when RDS instance storage is exhausted.", "rds-storage-full" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-rds-storage-full.md")) else "rds-storage-v2", [
        "Allocated storage consumed by data growth",
        "Binlogs or transaction logs not purged",
        "Temporary sort/result files use disk space",
        "Slow query log / General log enabled",
        "Buffer pool overflow without SSD cache",
    ], [
        ("Check allocated size", "aws rds describe-db-instances --db-instance-identifier mydb --query 'DBInstances[*].AllocatedStorage'"),
        "Modify to add storage",
        "aws rds modify-db-instance --db-instance-identifier mydb --allocated-storage 200 --apply-immediately")]),
    ("RDS Storage Scaling Error", "InvalidParameterCombination when RDS storage scaling fails.", "rds-storage-scaling", [
        "Modify not supported for storage type gp2 to gp2",
        "Current storage exceeds max for instance class",
        "IOPS request incompatible with new storage size",
        "Storage autoscaling conflict with manual change",
        "Maximum storage limit for the instance class reached",
        "Allocated storage is less than engine minimum",
    ], [
        ("Check instance details", "aws rds describe-db-instances --db-instance-identifier mydb"),
        "Modify storage",
        "aws rds modify-db-instance --db-instance-identifier mydb --allocated-storage 300 --apply-immediately"),
        "Check max storage by instance class",
        "aws rds describe-db-instance-types --db-instance-type db.r5.large")]),
    ("RDS Backup Retention Error", "InvalidParameterValue for RDS backup retention period.", "rds-backup-retention", [
        "Backup retention period must be between 0 and 35 days",
        "Value 0 disables automated backups",
        "Read replica source must have backup retention >0",
        "Magnetic storage cannot have backup retention >1",
        "Multi-AZ cluster backup retention minimum is 1",
    ], [
        ("Check backup retention", "aws rds describe-db-instances --db-instance-identifier mydb --query 'DBInstances[*].BackupRetentionPeriod'"),
        "Modify backup retention",
        "aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7")]),
    ("RDS Snapshot Restore Failed",
     "SnapshotRestoreError when restoring a DB from snapshot fails.",
     "rds-snapshot-restore",
     [
         "Source snapshot is not in available state",
         "Insufficient storage allocated for restore",
         "Cross-region snapshot copy incomplete",
         "Snapshot uses different KMS key than target",
         "Instance class incompatible with snapshot engine",
         "Source snapshot from unsupported engine version",
     ],
     [("List snapshots", "aws rds describe-db-snapshots --snapshot-type manual"),
     ("Restore an RDS snapshot",
      "aws rds restore-db-instance-from-db-snapshot --db-instance-identifier my-restored-db --db-snapshot-identifier my-snapshot")]),
    ("RDS Read Replica Lag",
     "ReplicationReplicaLagInMilliSeconds too high causing issues.",
     "rds-read-replica-lag" if not os.path.exists(os.path.join(OUTPUT_DIR, "aws-rds-read-replica-lag.md")) else "rds-readreplica-v2",
     [
         "Replica processing slower than the source",
         "Large write transaction on source takes time to apply",
         "Replica hardware instance smaller than source",
         "Network latency between regions",
         "Long running queries on the replica blocking apply",
         "Transactional replication lag from large DDL changes",
     ],
     [("Check replicate lag", "aws rds describe-db-instances --db-instance-identifier mydb-replica --query 'DBInstances[*].ReadReplicaSourceDBInstanceIdentifier'"),
     ("Promote replica", "aws rds promote-read-replica --db-instance-identifier mydb-replica")]),
    ("RDS Multi-AZ Failover",
     "FailoverError when RDS Multi-AZ failover does not complete.",
     "rds-multi-az-failover",
     [
         "Failover triggered but standby is unsynchronized",
         "Synchronous replication stall between AZs",
         "Network partition between AZs",
         "Standby instance crashes during failover",
         "Enhanced Monitoring alarm triggered incorrectly",
     ],
     [("Reboot with failover", "aws rds reboot-db-instance --db-instance-identifier mydb --force-failover")]),
    ("RDS Parameter Group Error",
     "InvalidParameterValue for RDS parameter group assignment.",
     "rds-parameter-group",
     [
         "Parameter group incompatible with DB engine version",
         "Parameter value out of range for the DB engine",
         "Custom parameter group does not exist",
         "Parameters requiring reboot are pending",
         "Modifying static vs dynamic parameters confusion",
     ],
     [("List available parameter groups", "aws rds describe-db-parameter-groups"),
     ("Associate with instance",
      "aws rds modify-db-instance --db-instance-identifier mydb --db-parameter-group-name custom-params")]),
    ("RDS Option Group Error",
     "InvalidOptionGroupState/InvalidParameterValue for option groups.",
     "rds-option-group",
     [
         "Option group is not compatible with the engine",
         "You cannot remove an option that is permenant",
         "Option is already associated with the instance",
         "Option group is being deleted while in use",
         "Option group assignment requires a reboot",
     ],
     [("List option groups", "aws rds describe-option-groups"),
     ("Modify associated option group",
      "aws rds modify-db-instance --db-instance-identifier mydb --option-group-name custom-options")]),
    ("RDS Subnet Group Error",
     "InvalidVPCNetworkStateFault/DBSubnetGroupNotFound for subnet groups.",
     "rds-subnet-group",
     [
         "Subnet group references deleted or nonexistent subnets",
         "Subnets in different Availability Zones (non-RDS Multi-AZ)",
         "Subnet count insufficient for Multi-AZ deployment (2+)",
         "Minimum one subnet must exist in the group",
         "Subnet IP CIDR conflicts with VPC peer",
     ],
     [("List subnet groups", "aws rds describe-db-subnet-groups"),
     ("Create subnet group",
      "aws rds create-db-subnet-group --db-subnet-group-name my-sng --db-subnet-group-description MySNG --subnet-ids subnet-abc subnet-def")]),
    ("RDS VPC Security Group Error",
     "AuthorizationNotFound/InvalidParameterValue for RDS VPC SGs.",
     "rds-vpc-security-group",
     [
         "Security group belongs to a different VPC",
         "Security group ID is in a different region",
         "Inbound rule missing for RDS port (3306, 5432, etc)",
         "Security group deleted but still attached",
         "Cross-account security group reference not authorized",
     ],
     [("Check inbound rules", "aws ec2 describe-security-groups --group-ids sg-abc --query 'SecurityGroups[*].IpPermissions'"),
     ("Authorize security group ingress",
      "aws ec2 authorize-security-group-ingress --group-id sg-abc --protocol tcp --port 3306 --cidr 10.0.0.0/16")]),
    ("RDS KMS Encryption Error",
     "KMS.KeyUnavailableException/KMS.AccessDeniedException for RDS.",
     "rds-kms-encryption",
     [
         "KMS key is disabled, pending import, or deleted",
         "KMS key IAM policy does not grant kms:Encrypt",
         "RDS service principal denied on KMS key policy",
         "KMS key in different region than RDS instance",
         "Cross-account KMS key permissions missing",
     ],
     [("Check KMS key status", "aws kms describe-key --key-id alias/rds-key")]),
    ("RDS IAM DB Authentication Error",
     "AccessDeniedException when using IAM DB Auth.",
     "rds-iam-db-auth",
     [
         "IAM DB Auth not enabled on the RDS instance",
         "RDS resource ID mismatch in IAM policy",
         "Policy action set to rds-db:connect with wrong resource",
         "Aurora Serverless v1 is not supported",
         "Port not included in RDS resource ARN",
         **
     ],
     [("Check if IAM DB Auth is enabled",
      "aws rds describe-db-instances --db-instance-identifier mydb --query 'DBInstances[*].IAMDatabaseAuthenticationEnabled'"),
     ("Enable IAM DB Auth",
      "aws rds modify-db-instance --db-instance-identifier mydb --enable-iam-database-authentication")]),
    ("RDS Engine Version Error",
     "DBInstanceNotFound/IncompatibleRestore for engine upgrades.",
     "rds-engine-version",
     [
         "Major version upgrade not supported for this instance class",
         "Engine version specified is not available for this region",
         "Upgrade in progress blocks new modifications",
         "Incompatible parameter group for target version",
         "Replica attached with older engine version",
     ],
     [("Check supported versions", "aws rds describe-db-engine-versions --engine mysql"),
     ("Upgrade minor version", "aws rds modify-db-instance --db-instance-identifier mydb --engine-version 8.0.28")]),
    ("RDS Upgrade Error",
     "UpgradeFailed when an engine upgrade does not complete.",
     "rds-upgrade-error",
     [
         "Major version upgrade requires a modify & reboot",
         "Multi-AZ upgrade can cause extended downtime",
         "Blue/Green deployment conflicts",
         "PostgreSQL upgrade heuristic failure",
         "Incompatible parameters blocking upgrade",
         "KMS key version incompatibility post upgrade",
     ],
     [("Stop and start upgrade monitoring", "aws rds describe-db-instances --db-instance-identifier mydb")]),
    ("RDS Maintenance Window Error",
     "InvalidMaintenanceWindow for RDS maintenance scheduling.",
     "rds-maintenance-window",
     [
         "Window must be at least 30 minutes duration",
         "Window must be expressed in UTC time zone",
         "Maintenance window conflicts with AutoMinorVersionUpgrade window",
         "Two maintenance windows overlapping within 24h",
     ],
     [("Modify maintenance window",
      "aws rds modify-db-instance --db-instance-identifier mydb --preferred-maintenance-window mon:03:00-mon:04:30")]),
    ("RDS Automated Backup Error",
     "AutomatedBackupDisabled/ValidationError for automated backups.",
     "rds-automated-backup",
     [
         "Backup retention period is set to 0 (disabled)",
         "Automated backups are not enabled on the instance",
         "Insufficient backup storage available",
         "Cross-Region backup copy not configured",
         "Manual snapshot in progress during automated backup window",
     ],
     [("Modify backup retention",
      "aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7")]),
    ("RDS Final Snapshot Error",
     "FinalDBSnapshotRequired when deleting an RDS instance.",
     "rds-final-snapshot",
     [
         "Parameter SkipFinalSnapshot not set to true",
         "You must provide a FinalDBSnapshotIdentifier",
         "Snapshot name must follow DB identifier pattern",
         "You cannot use the same snapshot name twice",
     ],
     [("Delete without final snapshot",
      "aws rds delete-db-instance --db-instance-identifier mydb --skip-final-snapshot")]),
]

# DynamoDB
DYNAMODB = [
    ("DynamoDB Table Not Found",
     "ResourceNotFoundException for DynamoDB table operations.",
     "dynamodb-table-not-found",
     [
         "Table name is misspelled in the application code",
         "Table has been deleted by another process",
         "Region mismatch in table ARN or endpoint URL",
         "Table creation is still in ACTIVE state",
     ],
     [("List active tables", "aws dynamodb list-tables"),
     ("Describe table", "aws dynamodb describe-table --table-name my-table")]),
    ("DynamoDB Table Not Active",
     "ResourceInUseException when table is not yet ACTIVE.",
     "dynamodb-table-not-active",
     [
         "Table is in CREATING or UPDATING status",
         "Deleting table cannot be used in operations",
         "Inconsistent state after CloudFormation rollback",
         "Backup or restore operation in progress",
     ],
     [("Wait for table Active", "aws dynamodb wait table-exists --table-name my-table")]),
    ]

try:
    DYNAMODB = DYNAMODB
except Exception as e:
    DYNAMODB = DYNAMODB

# IAM
IAM = [
    ("IAM Policy Not Found",
     "ResourceNotFoundException/NoSuchEntity for IAM policies.",
     "iam-policy-not-found",
     [
         "Policy with ARN does not exist",
         "Policy was deleted",
         "Region mismatch in the ARN format",
         "Custom vs AWS managed policy confusion",
         "Account ID in the policy ARN is incorrect",
     ],
     [("List policies", "aws iam list-policies --scope AWS")]),
    ("IAM Role Limit Exceeded",
     "LimitExceeded when role limit is eclipsed.",
     "iam-role-limit",
     [
         "Maximum roles per account limit (1000 by default)",
         "Path segregation increases duplicates",
         "Roles with service-linked categories",
         "Organization SCP limiting role creation",
     ],
     [("Count existing roles", "aws iam list-roles --query 'length(Roles[*])'")]),
    ]

# Write all
for section_name, pages in [
    ("EC2", AEC2_ALREADY_EXISTS), ("S3", S3), ("Lambda", LAMBDA),
    ("RDS", RDS)
]:
    pass

import sys

def main():
    all_pages = [
        (AWS_EC2, "ec2", "EC2"),
        (S3, "s3", "S3"),
        (LAMBDA, "lambda", "Lambda"),
        (RDS, "rds", "RDS"),
    ]

    total = 0
    for pages, prefix, name in all_pages:
        print(f"\n=== {name} ===")
        for entry in pages:
            title = entry[0]
            desc = entry[1]
            slug_val = entry[2]
            causes = entry[3]
            cmds = entry[4]
            write_page(name, title, desc, slug_val, causes, cmds)
            total += 1
            counters[name] = counters.get(name, 0) + 1

    print(f"\n=== TOTAL NEW AWS PAGES: {total} ===")

if __name__ == "__main__":
    main()
