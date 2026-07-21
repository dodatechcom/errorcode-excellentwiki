import os, json

OUT = "/home/admin1/projects/ErrorCode.excellentwiki.com/content/cloud/aws"
E = {f.rsplit(".", 1)[0] for f in os.listdir(OUT) if f.endswith(".md")}

def slug(title):
    return title.lower().replace(" ", "-").replace("/", "-").replace("--", "-")

def gen(prefix, title, desc, causes, cmds):
    s = slug(f"{prefix} {title}")
    if s in E:
        i = 2
        while f"{s}-v{i}" in E:
            i += 1
        s = f"{s}-v{i}"
    name = f"aws-{s}.md"
    path = os.path.join(OUT, name)
    if os.path.exists(path):
        print(f"  skip: {name}")
        return
    short = title.replace("AWS ", "")
    L = [
        "---",
        "title: \"[Solution] AWS " + title + "\"",
        "description: \"" + desc + "\"",
        "cloud: [\"aws\"]",
        "error-types: [\"cloud-error\"]",
        "severities: [\"error\"]",
        "weight: 5",
        "---",
        "",
        "The `" + short + "` error occurs when an AWS service cannot complete the requested operation.",
        "",
        "## Common Causes",
        "",
    ]
    for c in causes:
        L.append(f"- {c}")
    L += ["", "## How to Fix", ""]
    for lbl, cmd in cmds:
        L.append(f"### {lbl}")
        L.append("")
        L.append("```bash")
        L.append(cmd)
        L.append("```")
        L.append("")
    L += ["## Examples", ""]
    for c in causes[:4]:
        L.append(f"- Example: {c.lower()}")
    L += ["", "## Related Errors", ""]
    L.append("- [AWS EC2 Error]({{< relref \"/cloud/aws/aws-ec2-error\" >}}) -- EC2 errors")
    L.append("- [AWS CloudWatch Error]({{< relref \"/cloud/aws/aws-cloudwatch-error\" >}}) -- CW errors")
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"  CREATED: {name}")

# EC2 = 19 topics
pages = [
("ec2", "EC2 Insufficient Capacity",
 "InsufficientInstanceCapacity when EC2 cannot launch due to AZ resource exhaustion.",
 ["Capacity not available in the specified AZ",
  "AZ resource exhaustion due to other workloads",
  "Instance type temporarily constrained",
  "AWS high demand in the AZ"], [
 ("Check capacity in other AZs", "aws ec2 describe-availability-zones --region us-east-1"),
 ("Try different instance type", "aws ec2 run-instances --image-id ami-0abcdef --instance-type c5a.xlarge --count 1"),
 ("Reserve capacity", "aws ec2 create-capacity-reservation --instance-type c5.xlarge --instance-count 1 --availability-zone us-east-1a"),
 ("Launch with block", "aws ec2 run-instances --image-id ami-0abcdef --capacity-reservation-spec CapacityReservationPreference=open")
]),

("ec2", "EC2 Spot Max Price",
 "SpotMaxPriceTooLow when the bid is below the Spot market price.",
 ["Spot price exceeds the max bid",
  "Market demand increased pricing",
  "Instance type high demand on Spot"], [
 ("Check Spot price history", "aws ec2 describe-spot-price-history --instance-type c5.xlarge -s 2025-01-01T00:00:00Z"),
 ("Higher max price", "aws ec2 request-spot-instances --spot-price 0.50 --count 1"),
 ("Less popular instance", "aws ec2 describe-spot-price-history --instance t3.medium"),
 ("Fall back to On-Demand", "aws ec2 run-instances --image-id ami-0abcdef --count 1")
]),

("ec2", "EC2 Spot Capacity Not Available",
 "SpotCapacityNotAvailable Spot request capacity exhausted.",
 ["Temporarily high Spot usage in AZ",
  "Instance constraints",
  "Spot allocation strategy"}, [
 ("Check Spot requests", "aws ec2 describe-spot-instance-requests"),
 ("Use capacity-optimized", "aws ec2 request-spot-instances --type persistent --strategy capacity-optimized")
]),

("ec2", "EBS attach failed",
 "VolumeAttachmentError when an EBS volume cannot attach.",
 ["Volume already attached elsewhere",
  "Volume and instance in different AZ",
  "Volume in the wrong state"], [
 ("Describe volume", "aws ec2 describe-volumes --volume-ids vol-0abc"),
 ("Attach", "aws ec2 attach-volume --vol vol-0abc --ins i-0abc --dev /dev/xvdf"),
 ("Detach first", "aws ec2 detach-volume --vol vol-0abc")
]),

("ec2", "Volume type incompatible",
 "VolumeTypeNotSupported for the EBS volume type.",
 ["Instance lacks NVMe driver",
  "io2 Block Express unsupported",
  "EBS optimization off"], [
 ("Check EBS optimization", "aws ec2 describe-instances --instance i-0abc --query EbsOptimized"),
 ("Modify EBS optimization", "aws ec2 modify-instance-attribute --instance i-0abc --ebs-optimized true")
]),

("ec2", "Snapshot in progress",
 "SnapshotCreationPermission when another snapshot is active.",

 ["Another snapshot running for the volume",
  "Too many concurrent snapshots",
  "Snap quota reached"], [
 ("Check progress", "aws ec2 describe-snapshots --owner self --filters Name=volume,Values=vol-0abc"),
 ("Wait for completion", "aws ec2 wait snapshot-completed --snap snap-0abc")
]),

("ec2", "Invalid AMI ID",
 "InvalidAMIID.NotFound for the AMI identifier.",

 ["Typo in the AMI ID",
  "AMI belongs to other region",
  "AMI deregistered by owner",
  "Wrong AMI format"], [
 ("Verify AMI", "aws ec2 describe-images --image-ids ami-0abc"),
 ("Search AMIs", "aws ec2 describe-images --owners self amazon --query Images[*].ImageId")
]),

("ec2", "Elastic IP Limit",
 "ElasticIpLimitExceeded when EIP quota reached.",

 ["Account EIP quota exhausted",
  "Unassociated EIPs wasting limit"], [
 ("Check usage", "aws ec2 describe-addresses"),
 ("Release unused", "aws ec2 release-address --allocation-id eipalloc-0abc"),
 ("Request increase", "aws service-quotas request-service-quota-increase --service-code ec2 --quota L-0263D0A3")
]),

("ec2", "VPC Limit Exceeded",
 "VpcLimitExceeded when the account VPC limit reached.",

 ["Default 5 VPCs per region exhausted",
  "Stacked from many projects"], [
 ("Count VPCs", "aws ec2 describe-vpcs --query length(Vpcs)"),
 ("Delete unused", "aws ec2 delete-vpc --vpc vpc-0abc")
]),

("ec2", "Placement Group",
 "PlacementGroupError constraints cannot be met.",
 ["Capacity insufficient in the group",
  "Spread limit reached",
  "Single AZ groups only"], [
 ("Describe group", "aws ec2 describe-placement-groups --names my-pg")
]),

("ec2", "Dedicated Host",
 "DedicatedHostError when allocation fails.",
 ["Host limit per region reached",
  "Insufficient capacity for instance",
  "Host in wrong state"], [
 ("Check hosts", "aws ec2 describe-hosts"),
 ("Allocate host", "aws ec2 allocate-hosts --quantity 1 --az us-east-1a --instance c5.xlarge")
]),

("ec2", "HPC Cluster Error",
 "HPCClusterError for High Performance Computing.",

 ["EFA attachment limit exceeded",
  "Slurm node failure",
  "EFA security rules misconfigured"], [
 ("Check EFA", "aws ec2 describe-network-interfaces --filter description,EFA-*"),
 ("Verify EFA status", "aws ec2 describe-instance-types --p4d.24xlarge --query NetworkInfo")
]),

# S3 = 19 topics
("s3", "S3 Bucket Access Denied",
 "AccessDenied for S3 bucket due to permissions.",
 ["Missing s3:ListBucket IAM permission",
  "Bucket policy denies explicitly",
  "SCP blocks this action",
  "Public access block active"], [
 ("Simulate IAM", "aws iam simulate-principal-policy --action s3:ListBucket --policy-user arn:aws:iam::123:user/myuser"),
 ("Check bucket policy", "aws s3api get-bucket-policy --bucket my-bucket"),
 ("Check public block", "aws s3api get-public-access-block --bucket my-bucket")
]),

("s3", "S3 Bucket Already Exists",
 "BucketAlreadyExists globally taken name.",
 ["Bucket name globally unique",
  "Another account owns the name"], [
 ("Use different name", "aws s3api create-bucket --bucket my-unique-98765 --region us-east-1")
]),

("s3", "Delete non-empty bucket",
 "BucketNotEmpty for deleting a non-empty bucket.",

 ["Bucket contains objects",
  "Versioning enabled with delete markers",
  "Multipart uploads in progress"], [
 ("List objects", "aws s3 ls s3://my-bucket/ --recursive"),
 ("Delete all", "aws s3 rm s3://my-bucket/ --recursive"),
 ("Force bucket deletion", "aws s3 rb s3://my-bucket --force")
]),

("s3", "Object Access Denied",
 "AccessDenied for object operations.",

 ["s3:GetObject IAM missing",
  "Object ACL restrictive",
  "KMS key not accessible"], [
 ("Test permissions", "aws s3api get-object --bucket my-bucket --key path/to/object.txt out.txt")
]),

("s3", "Multipart upload",
 "EntityTooLarge/SlowDown for S3 multipart upload.",

 ["Part < 5 MiB or > 5 GiB",
  "Upload ID expired or aborted",
  "Number of parts > 10000"], [
 ("List parts", "aws s3api list-parts --bucket my-bucket --key largefile.zip --upload-id ID"),
 ("Complete multipart", "aws s3api complete-multipart-upload --bucket my-bucket --key largefile.zip")
]),

("s3", "Upload part failed",
 "UploadPartCopyError for upload part.",
 ["Part too small",
  "Network interruption",
  "Upload ID invalid"], [
 ("Check part sizes", "aws s3api list-parts --bucket my-bucket --key bigfile.iso"),
 ("re-upload", "aws s3api upload-part --bucket my-bucket --part 3 --body p3.dat --upload ID")
]),

("s3", "S3 copy object",
 "CopyObjectError for cross-bucket copy.",

 ["Source archived in Glacier",
  "Cross-region rate limits",
  "KMS key mismatch"], [
 ("Copy single", "aws s3api copy-object --copy-source src/object.txt --bucket dest --key object.txt"),
 ("use multicommand", "aws s3 cp s3://src/ s3://dest/ --recursive")
]),

("s3", "S3 ACL error",
 "AccessControlListError for ACL configuration.",
 ["Invalid grantee email/URI",
  "Exceeds 100 ACL grants",
  "Bucket policy conflicts"], [
 ("Set ACL", "aws s3api put-object-acl --bucket my-bucket --key file.txt --acl bucket-owner-full-control")
]),

("s3", "S3 bucket policy",
 "Malformed/PolicyTooLong for bucket policy.",

 ["Size > 20 KB",
  "Syntax error in principal",


  "Missing Action in statement"], [
 ("Get policy", "aws s3api get-bucket-policy --bucket my-bucket"),
 ("Put new policy", "aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json")
]),

("s3", "S3 Transfer Acceleration",
 "S3TransferAccelerationError acceleration endpoint fails.",

 ["Bucket not enabled",
  "Upload > 10 Gbps in region"], [
 ("Check status", "aws s3api get-bucket-accelerate-config --bucket my-bucket"),
 ("Enable", "aws s3api put-bucket-accelerate-config --bucket my-bucket --state Enabled")
]),

("s3", "Encryption mismatch",
 "KMS.DecryptException/BadDigest SSE settings conflict.",
 ["Bucket SSE and request SSE mismatch",
  "Algorithm differs between source and dest"], [
 ("Check encryption", "aws s3api get-bucket-encryption --bucket my-bucket")
]),

("s3", "KMS key access",
 "KMS.AccessDenied for S3 accessing the key.",

 ["KMS key policy doesn't allow S3",
  "Cross-account permissions missing"], [
 ("Get key policy", "aws kms get-key-policy --key alias/s3-key --name default")
]),

("s3", "Pre-signed expired",
 "ExpiredToken/SignatureDoesNotMatch for pre-signed URL.",
 ["URL expiratoin passed",
  "Assumed role expired"], [
 ("Generate new URL", "aws s3 presign s3://my-bucket/file.txt --expires 86400")
]),

("s3", "Event notification",
 "InvalidArgument for S3 event notifications.",

 ["Dest SQS/SNS in different region",
  "SQS policy missing",


  "100 per bucket quota hit"], [
 ("Get notification conf", "aws s3api get-bucket-notification-conf --bucket my-bucket")
]),

("s3", "S3 replication",
 "ReplicationError for S3 replication.",

 ["Source or dest in different regions",
  "KMS dest inaccessible",
  "Versioning not enabled"], [
 ("Check replication", "aws s3api get-bucket-replication --bucket my-bucket")
]),

("s3", "S3 Lifecycle",
 "MalformedXML/InvalidRequest for lifecycle rules.",
 ["Rule ID duplicate",
  "Date format invalid",
  "128KB min for transitions"], [
 ("Get lifecycle", "aws s3api get-bucket-lifecycle-config --bucket my-bucket")
]),

("s3", "Glacier Restore",
 "RestoreObjectError Glacier restore fails.",

 ["Object not in Glacier class",
  "Expedited capacity not available",
  "Tier mismatch"], [
 ("Initiate restore", "aws s3api restore-object --bucket my-bucket --key archived.zip --restore Days=3")
]),

# Lambda = 19 topics
("lambda", "Lambda handler not found",
 "HandlerNotFound for Lambda function.",
 ["Handler export name does not match",
  "File extension missing (.py/.js)",
  "Handler in subdirectory"], [
 ("Check config", "aws lambda get-function-config --function my-function"),
 ("Set handler", "aws lambda update-function-config --function my-function --handler index.handler")
]),

("lambda", "Runtime Not Supported",
 "RuntimeNotSupportedException deprecated runtime.",

 ["Runtime reached end of support",
  "Security patches no longer applied",
  "Node/Python/Java version is deprecated"], [
 ("Check runtime", "aws lambda get-function-config --function my-function --query Runtime"),
 ("Change runtime", "aws lambda update-function-config --function my-function --runtime nodejs20.x")
]),

("lambda", "Concurrency Limit",
 "ReservedFunctionConcurrencyInvocationLimit exceeded.",

 ["Account-level reached (1000 default)",
  "Burst region reached"], [
 ("Check concurrency", "aws lambda get-function-concurrency --function my-function")
]),

("lambda", "Unreserved pool",
 "UnreservedConcurrentExecutions limit hit.",

 ["Reserved concurrency uses all capacity",
  "No unreserved slot available"], [
 ("Check account settings", "aws lambda get-account-settings")
]),

("lambda", "VPC Config",
 "InvalidParameterValue for VPC config.",

 ["VPC deleted or non-existent",
  "Subnet belongs to wrong AZ",
  "SG in the wrong VPC"], [
 ("Check VPC config", "aws lambda get-function-config --function my-function"),
 ("Update VPC", "aws lambda update-function-config --function my-function --vpc SubnetIds=s1,s2,SecurityIds=sg-1")
]),

("lambda", "ENI creation",
 "ENILimit/InsufficientIP for ENI creation.",
 ["ENI region limit reached",
  "VPC exhausted IPs",
  "Rate limiting on EC2 API"], [
 ("Check ENI count", "aws ec2 describe-network-interfaces --f vpc,vpc-abc")
]),

("lambda", "Lambda@Edge",
 "LambdaAtEdgeError CloudFront triggers.",

 ["Viewer events limited to 128MB",
  "Function not in us-east-1",
  "Timeout >5s for viewer"], [
 ("Check size", "aws lambda get-function --function my-function --query CodeSize")
]),

("runtime", "Runtime Not Found",
 "ResourceNotFoundException for Lambda layer reference.",

 ["Layer ARN incorrect",
  "Layer was deleted",
  "Layer in wrong region"], [
 ("List layers", "aws lambda list-layers")
]),

("lambda", "Layer Broken",
 "ResourceNotFoundException for Lambda layer.",

 ["Layer does not exist",
  "Layer permissions not granted"], [
 ("List layer versions", "aws lambda list-layer-versions --layer my-layer")
]),

("lambda", "Code Storage",
 "CodeStorageExceeded storage limit.",

 ["Total code > 75GB across functions",
  "Function code > 250MB unzipped"], [
 ("Check usage", "aws lambda get-account-settings --query AccountUsage")
]),

("lambda", "ZIP size",
 "InvalidParameterException zip > 50MB.",

 ["Direct zip limited to 50MB",
  "Can use S3 for larger"],
 [("Check size", "ls -lh my-function.zip")]),


("lambda", "IEM role",
 "InvalidParameterException for IEM role.",

 ["Role ARN invalid or deleted",
  "Trust policy missing Lambda service"], [
 ("Check role", "aws iam get-role --role my-lambda-role")
]),

("lambda", "DLQ not active",
 "Custom resources lost DLQ missing.",

 ["SQS/SNS target invalid",
  "No DLQ provided"],
 [("Set DLQ", "aws lambda update-function-config --function my-function --dead-letter TargetArn=arn:aws:sqs::123:mydlq")
]),

("lambda", "Async invocation",
 "AsyncInvocationError events dropped.",

 ["Queue full or throttled",
  "Payload > 256KB"], [
 ("Check invoke config", "aws lambda get-function-event-invoke-config --function my-function")
]),

("lambda", "Event Source Mapping",
 "InvalidParameter/ResourceConflict for mappings.",
 ["Dynamo/Kinesis access denied",
  "Mapping limit per function reached",
  "SQS does not exist"], [
 ("List mappings", "aws lambda list-event-source-mappings --function my-function")
]),

("reserved", "Concurrency Reserver",
 "ReservedConcurrentExecutionsLimit.",

 ["Cannot be 0",
  "exceeds total account limit"], [
 ("Set reserved concurrency", "aws lambda put-function-concurrency --function my-function --reserved 10")
]),

("provd concu", "Provisioned Concurrency",
 "ProvisionedConcurrencyConfigNotFoundException.",

 ["Alias/version missing",
  "Account limit reached"], [
 ("Put PC", "aws lambda put-provisioned-concurrency-config --function m-f --qual prod --count 100")
]),

("snapstart", "SnapStart error",
 "SnapStartNotSupported for Lambda SnapStart.",

 ["Network connections during init",
  "UUID seeded during init",
  "Temp credentials fetched during init"], [
 ("Set SnapStart", "aws lambda update-function-config --function my-function --snap ApplyOn=Published")
]),
]

for p in pages:
    gen(*p)

print(f"\nTotal AWS created: {len(pages)}")
