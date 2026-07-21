import os, json

def get_cat(title):
    t = title.lower()
    if t.startswith("ec2") or t.startswith("ebs") or t.startswith("snapshot") or t.startswith("placement") or t.startswith("dedicated") or t.startswith("hpc") or t.startswith("vpc") or t.startswith("elastic ip"):
        return "ec2", "aws-ec2-error"
    if t.startswith("s3") or t.startswith("glacier"):
        return "s3", "aws-s3-error"
    if t.startswith("lambda") or t.startswith("runtime") or t.startswith("concurrency") or t.startswith("vpc config") or t.startswith("eni") or t.startswith("layer") or t.startswith("code storage") or t.startswith("zip") or t.startswith("iam role") or t.startswith("dlq") or t.startswith("async") or t.startswith("event source") or t.startswith("reserved") or t.startswith("provisioned") or t.startswith("snapstart"):
        return "lambda", "aws-lambda-error"
    if t.startswith("rds") or t.startswith("db instance"):
        return "rds", "aws-rds-error"
    if t.startswith("dynamodb") or t.startswith("provisioned") or t.startswith("on-demand") or t.startswith("write capacity") or t.startswith("read capacity") or t.startswith("auto scaling") or t.startswith("global table") or t.startswith("replica") or t.startswith("stream") or t.startswith("ttl") or t.startswith("item") or t.startswith("batch") or t.startswith("transaction") or t.startswith("condition") or t.startswith("filter") or t.startswith("key schema") or t.startswith("index"):
        return "dynamodb", "aws-dynamodb-error"
    if t.startswith("iam") or t.startswith("policy") or t.startswith("role") or t.startswith("user") or t.startswith("access key") or t.startswith("secret") or t.startswith("service role") or t.startswith("trust") or t.startswith("permissions") or t.startswith("passrole") or t.startswith("assumerole") or t.startswith("saml") or t.startswith("oidc") or t.startswith("mfa") or t.startswith("scp") or t.startswith("organization"):
        return "iam", "aws-iam-error"
    if t.startswith("ecs") or t.startswith("fargate") or t.startswith("elb") or t.startswith("service auto") or t.startswith("service discovery") or t.startswith("eks") or t.startswith("kubeconfig") or t.startswith("irsa") or t.startswith("ecr") or t.startswith("docker") or t.startswith("container") or t.startswith("repo"):
        return "ecs", "aws-ecs-error"
    if t.startswith("rest") or t.startswith("deployment") or t.startswith("stage") or t.startswith("resource") or t.startswith("method") or t.startswith("integration") or t.startswith("model") or t.startswith("api key") or t.startswith("usage") or t.startswith("waf") or t.startswith("domain") or t.startswith("base path") or t.startswith("canary") or t.startswith("throttling"):
        return "apigw", "aws-api-gateway-error"
    if t.startswith("distribution") or t.startswith("origin") or t.startswith("cname") or t.startswith("ssl") or t.startswith("viewer") or t.startswith("cache") or t.startswith("ttl") or t.startswith("invalidation") or t.startswith("field") or t.startswith("geo") or t.startswith("signed url") or t.startswith("signed cookie") or t.startswith("oai") or t.startswith("origin access"):
        return "cloudfront", "aws-cloudfront-error"
    if t.startswith("hosted") or t.startswith("record") or t.startswith("alias") or t.startswith("health") or t.startswith("failover") or t.startswith("latency") or t.startswith("geolocation") or t.startswith("geoproximity") or t.startswith("weighted") or t.startswith("multivalue") or t.startswith("dnssec") or t.startswith("domain reg") or t.startswith("ns") or t.startswith("soa") or t.startswith("private") or t.startswith("resolver"):
        return "route53", "aws-route53-error"
    if t.startswith("log") or t.startswith("metric") or t.startswith("alarm") or t.startswith("insufficient") or t.startswith("sns") or t.startswith("dashboard") or t.startswith("metric math") or t.startswith("logs") or t.startswith("contributor") or t.startswith("anomaly") or t.startswith("composite") or t.startswith("service quota") or t.startswith("cloudwatch") or t.startswith("unified"):
        return "cloudwatch", "aws-cloudwatch-error"
    if t.startswith("kms") or t.startswith("custom key") or t.startswith("cloudhsm") or t.startswith("secret") or t.startswith("certificate") or t.startswith("private ca") or t.startswith("guardduty") or t.startswith("security") or t.startswith("config") or t.startswith("waf rule") or t.startswith("shield"):
        return "kms", "aws-kms-error"
    return "ec2", "aws-ec2-error"

def generate_pages(provider, output_dir, pages, prefix_for_filename):
    existing = {f.rsplit(".", 1)[0] for f in os.listdir(output_dir) if f.endswith(".md")}
    count = 0
    for title, desc, causes, cmds in pages:
        base = title.lower().replace(" ", "-").replace("/", "-")
        prefixed = f"{prefix_for_filename}-{base}"
        if prefixed in existing:
            idx = 2
            while f"{prefixed}-v{idx}" in existing:
                idx += 1
            prefixed = f"{prefixed}-v{idx}"
        filename = f"{prefixed}.md"
        filepath = os.path.join(output_dir, filename)
        if os.path.exists(filepath):
            print(f"  skip: {filename}")
            continue
        short = title.replace(f"{provider.upper()} ", "")
        cat, ref = get_cat(title)
        lines = []
        lines.append("---")
        lines.append(f"title: \"[Solution] {provider.upper()} {title}\"")
        lines.append(f"description: \"{desc}\"")
        lines.append(f"cloud: [\"{provider.lower()}\"]")
        lines.append("error-types: [\"cloud-error\"]")
        lines.append("severities: [\"error\"]")
        lines.append("weight: 5")
        lines.append("---")
        lines.append("")
        lines.append(f"The `{short}` error occurs when a {provider.upper()} service cannot complete the requested operation.")
        lines.append("")
        lines.append("## Common Causes")
        lines.append("")
        for c in causes:
            lines.append("- " + c)
        lines.append("")
        lines.append("## How to Fix")
        lines.append("")
        for lbl, cmd in cmds:
            lines.append(f"### {lbl}")
            lines.append("")
            lines.append("```bash")
            lines.append(cmd)
            lines.append("```")
            lines.append("")
        lines.append("## Examples")
        lines.append("")
        for c in causes[:4]:
            lines.append("- Example scenario: " + c.lower().rstrip("."))
        lines.append("")
        lines.append("## Related Errors")
        lines.append("")
        lines.append(f"- [{provider.upper()} {cat.upper()} Error]({{{{< relref \"/cloud/{provider.lower()}/{ref}\" >}}}}) -- General {cat} errors")
        lines.append(f"- [{provider.upper()} CloudWatch Error]({{{{< relref \"/cloud/{provider.lower()}/aws-cloudwatch-error\" >}}}}) -- CloudWatch errors")
        with open(filepath, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  CREATED: {filename}")
        count += 1
    return count

# ---- AWS pages ----
# Wrap causes and commands in dedicated helper arrays to avoid bracket issues
def aws_causes(*args): return list(args)
def aws_cmds(*args): return list(args)

AWS_PAGES = []

# EC2
AWS_PAGES.append(("EC2 Insufficient Capacity",
"InsufficientInstanceCapacity when EC2 cannot launch due to AZ resource exhaustion.",
["Capacity not available in the specified AZ","AZ resource exhaustion due to other workloads","Instance type temporarily constrained","AWS high demand in the AZ"],
[("Check capacity in other AZs","aws ec2 describe-availability-zones --region us-east-1"),("Try different instance type","aws ec2 run-instances --image-id ami-0abcdef --instance-type c5a.xlarge --count 1")]))

AWS_PAGES.append(("EC2 Spot Max Price",
"SpotMaxPriceTooLow when the bid is below the Spot market price.",
["Spot price exceeds the max bid","Market demand increased pricing","Instance type high demand on Spot"],
[("Check Spot price history","aws ec2 describe-spot-price-history --instance-type c5.xlarge -s 2025-01-01T00:00:00Z"),("Higher max price","aws ec2 request-spot-instances --spot-price 0.50 --count 1"),("Fall back to On-Demand","aws ec2 run-instances --image-id ami-0abcdef --count 1")]))

AWS_PAGES.append(("EC2 Spot Capacity Not Available",
"SpotCapacityNotAvailable Spot request capacity exhausted.",
["Temporarily high Spot usage in AZ","Instance constraints","Spot allocation strategy"],
[("Check Spot requests","aws ec2 describe-spot-instance-requests"),("Use capacity-optimized","aws ec2 request-spot-instances --type persistent --strategy capacity-optimized")]))

AWS_PAGES.append(("EBS attach failed",
"VolumeAttachmentError when an EBS volume cannot attach.",
["Volume already attached elsewhere","Volume and instance in different AZ","Volume in the wrong state"],
[("Describe volume","aws ec2 describe-volumes --volume-ids vol-0abc"),("Attach","aws ec2 attach-volume --vol vol-0abc --ins i-0abc --dev /dev/xvdf"),("Detach first","aws ec2 detach-volume --vol vol-0abc")]))

AWS_PAGES.append(("Volume type incompatible",
"VolumeTypeNotSupported for the EBS volume type.",
["Instance lacks NVMe driver","io2 Block Express unsupported","EBS optimization off"],
[("Check EBS optimization","aws ec2 describe-instances --instance i-0abc --query EbsOptimized"),("Modify EBS optimization","aws ec2 modify-instance-attribute --instance i-0abc --ebs-optimized true")]))

AWS_PAGES.append(("Snapshot in progress",
"SnapshotCreationPermission when another snapshot is active.",
["Another snapshot running for the volume","Too many concurrent snapshots","Snap quota reached"],
[("Check progress","aws ec2 describe-snapshots --owner self --filters Name=volume,Values=vol-0abc"),("Wait for completion","aws ec2 wait snapshot-completed --snap snap-0abc")]))

AWS_PAGES.append(("Invalid AMI ID",
"InvalidAMIID.NotFound for the AMI identifier.",
["Typo in the AMI ID","AMI belongs to other region","AMI deregistered by owner","Wrong AMI format"],
[("Verify AMI","aws ec2 describe-images --image-ids ami-0abc"),("Search AMIs","aws ec2 describe-images --owners self amazon --query Images[*].ImageId")]))

AWS_PAGES.append(("Elastic IP Limit",
"ElasticIpLimitExceeded when EIP quota reached.",
["Account EIP quota exhausted","Unassociated EIPs wasting limit"],
[("Check usage","aws ec2 describe-addresses"),("Release unused","aws ec2 release-address --allocation-id eipalloc-0abc")]))

AWS_PAGES.append(("VPC Limit Exceeded",
"VpcLimitExceeded when the account VPC limit reached.",
["Default 5 VPCs per region exhausted","Stacked from many projects"],
[("Count VPCs","aws ec2 describe-vpcs --query length(Vpcs)"),("Delete unused","aws ec2 delete-vpc --vpc vpc-0abc")]))

AWS_PAGES.append(("Placement Group",
"PlacementGroupError constraints cannot be met.",
["Capacity insufficient in the group","Spread limit reached","Single AZ groups only"],
[("Describe group","aws ec2 describe-placement-groups --names my-pg")]))

AWS_PAGES.append(("Dedicated Host",
"DedicatedHostError when allocation fails.",
["Host limit per region reached","Insufficient capacity for instance","Host in wrong state"],
[("Check hosts","aws ec2 describe-hosts"),("Allocate host","aws ec2 allocate-hosts --quantity 1 --az us-east-1a --instance c5.xlarge")]))

AWS_PAGES.append(("HPC Cluster Error",
"HPCClusterError for High Performance Computing.",
["EFA attachment limit exceeded","Slurm node failure","EFA security rules misconfigured"],
[("Check EFA","aws ec2 describe-network-interfaces --filter description,EFA-*"),("Verify EFA status","aws ec2 describe-instance-types --p4d.24xlarge --query NetworkInfo")]))

# S3
AWS_PAGES.append(("S3 Bucket Access Denied",
"AccessDenied for S3 bucket due to permissions.",
["Missing s3:ListBucket IAM permission","Bucket policy denies explicitly","SCP blocks this action","Public access block active"],
[("Simulate IAM","aws iam simulate-principal-policy --action s3:ListBucket --policy-user arn:aws:iam::123:user/myuser"),("Check bucket policy","aws s3api get-bucket-policy --bucket my-bucket"),("Check public block","aws s3api get-public-access-block --bucket my-bucket")]))

AWS_PAGES.append(("S3 Bucket Already Exists",
"BucketAlreadyExists globally taken name.",
["Bucket name globally unique","Another account owns the name"],
[("Use different name","aws s3api create-bucket --bucket my-unique-98765 --region us-east-1")]))

AWS_PAGES.append(("Delete non-empty bucket",
"BucketNotEmpty for deleting a non-empty bucket.",
["Bucket contains objects","Versioning enabled with delete markers","Multipart uploads in progress"],
[("Delete all objects","aws s3 rm s3://my-bucket/ --recursive"),("Force bucket deletion","aws s3 rb s3://my-bucket --force")]))

AWS_PAGES.append(("Object Access Denied",
"AccessDenied for object operations.",
["s3:GetObject IAM missing","Object ACL restrictive","KMS key not accessible"],
[("Test permissions","aws s3api get-object --bucket my-bucket --key path/to/object.txt out.txt")]))

AWS_PAGES.append(("Multipart upload",
"EntityTooLarge/SlowDown for S3 multipart upload.",
["Part less than 5 MiB or more than 5 GiB","Upload ID expired or aborted","Number of parts more than 10000"],
[("List parts","aws s3api list-parts --bucket my-bucket --key largefile.zip --upload-id ID"),("Complete multipart","aws s3api complete-multipart-upload --bucket my-bucket --key largefile.zip")]))

AWS_PAGES.append(("Upload part failed",
"UploadPartCopyError for upload part.",
["Part too small","Network interruption","Upload ID invalid"],
[("Check part sizes","aws s3api list-parts --bucket my-bucket --key bigfile.iso")]))

AWS_PAGES.append(("S3 copy object",
"CopyObjectError for cross-bucket copy.",
["Source archived in Glacier","Cross-region rate limits","KMS key mismatch"],
[("Copy single","aws s3api copy-object --copy-source src/object.txt --bucket dest --key object.txt"),("use multicommand","aws s3 cp s3://src/ s3://dest/ --recursive")]))

AWS_PAGES.append(("S3 ACL error",
"AccessControlListError for ACL configuration.",
["Invalid grantee email or URI","Exceeds 100 ACL grants","Bucket policy conflicts"],
[("Set ACL","aws s3api put-object-acl --bucket my-bucket --key file.txt --acl bucket-owner-full-control")]))

AWS_PAGES.append(("S3 bucket policy",
"Malformed/PolicyTooLong for bucket policy.",
["Size more than 20 KB","Syntax error in principal","Missing Action in statement"],
[("Get policy","aws s3api get-bucket-policy --bucket my-bucket"),("Put new policy","aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json")]))

AWS_PAGES.append(("S3 Transfer Acceleration",
"S3TransferAccelerationError acceleration endpoint fails.",
["Bucket not enabled","Upload more than 10 Gbps in region"],
[("Check status","aws s3api get-bucket-accelerate-config --bucket my-bucket"),("Enable","aws s3api put-bucket-accelerate-config --bucket my-bucket --state Enabled")]))

AWS_PAGES.append(("Encryption mismatch",
"KMS.DecryptException/BadDigest SSE settings conflict.",
["Bucket SSE and request SSE mismatch","Algorithm differs between source and dest"],
[("Check encryption","aws s3api get-bucket-encryption --bucket my-bucket")]))

AWS_PAGES.append(("KMS key access",
"KMS.AccessDenied for S3 accessing the key.",
["KMS key policy doesn't allow S3","Cross-account permissions missing"],
[("Get key policy","aws kms get-key-policy --key alias/s3-key --name default")]))

AWS_PAGES.append(("Pre-signed expired",
"ExpiredToken/SignatureDoesNotMatch for pre-signed URL.",
["URL expiration passed","Assumed role expired"],
[("Generate new URL","aws s3 presign s3://my-bucket/file.txt --expires 86400")]))

AWS_PAGES.append(("Event notification",
"InvalidArgument for S3 event notifications.",
["Dest SQS/SNS in different region","SQS policy missing","100 per bucket quota hit"],
[("Get notification config","aws s3api get-bucket-notification-config --bucket my-bucket")]))

AWS_PAGES.append(("S3 replication",
"ReplicationError for S3 replication.",
["Source or dest in different regions","KMS dest inaccessible","Versioning not enabled"],
[("Check replication","aws s3api get-bucket-replication --bucket my-bucket")]))

AWS_PAGES.append(("S3 Lifecycle",
"MalformedXML/InvalidRequest for lifecycle rules.",
["Rule ID duplicate","Date format invalid","128KB min for transitions"],
[("Get lifecycle","aws s3api get-bucket-lifecycle-config --bucket my-bucket")]))

AWS_PAGES.append(("Glacier Restore",
"RestoreObjectError Glacier restore fails.",
["Object not in Glacier class","Expedited capacity not available","Tier mismatch"],
[("Initiate restore","aws s3api restore-object --bucket my-bucket --key archived.zip --restore Days=3")]))

# Lambda
AWS_PAGES.append(("Lambda handler not found",
"HandlerNotFound for Lambda function.",
["Handler export name does not match","File extension missing (.py/.js)","Handler in subdirectory"],
[("Check config","aws lambda get-function-config --function my-function"),("Set handler","aws lambda update-function-config --function my-function --handler index.handler")]))

AWS_PAGES.append(("Runtime Not Supported",
"RuntimeNotSupportedException deprecated runtime.",
["Runtime reached end of support","Security patches no longer applied","Node/Python/Java version is deprecated"],
[("Check runtime","aws lambda get-function-config --function my-function --query Runtime"),("Change runtime","aws lambda update-function-config --function my-function --runtime nodejs20.x")]))

AWS_PAGES.append(("Concurrency Limit",
"ReservedFunctionConcurrencyInvocationLimit exceeded.",
["Account-level reached (1000 default)","Burst region reached"],
[("Check concurrency","aws lambda get-function-concurrency --function my-function")]))

AWS_PAGES.append(("Unreserved pool",
"UnreservedConcurrentExecutions limit hit.",
["Reserved concurrency uses all capacity","No unreserved slot available"],
[("Check account settings","aws lambda get-account-settings")]))

AWS_PAGES.append(("VPC Config",
"InvalidParameterValue for VPC config.",
["VPC deleted or non-existent","Subnet belongs to wrong AZ","SG in the wrong VPC"],
[("Check VPC config","aws lambda get-function-config --function my-function"),("Update VPC","aws lambda update-function-config --function my-function --vpc SubnetIds=s1,s2,SecurityIds=sg-1")]))

AWS_PAGES.append(("ENI creation",
"ENILimit/InsufficientIP for ENI creation.",
["ENI region limit reached","VPC exhausted IPs","Rate limiting on EC2 API"],
[("Check ENI count","aws ec2 describe-network-interfaces --f vpc,vpc-abc")]))

AWS_PAGES.append(("Lambda@Edge",
"LambdaAtEdgeError CloudFront triggers.",
["Viewer events limited to 128MB","Function not in us-east-1","Timeout more than 5s for viewer"],
[("Check size","aws lambda get-function --function my-function --query CodeSize")]))

AWS_PAGES.append(("Layer Not Found",
"ResourceNotFoundException for Lambda Layer.",
["Layer ARN incorrect","Layer was deleted","Layer in wrong region","Permissions not granted"],
[("List layers","aws lambda list-layers")]))

AWS_PAGES.append(("Code Storage",
"CodeStorageExceeded storage limit.",
["Total code more than 75GB across functions","Function code more than 250MB unzipped"],
[("Check usage","aws lambda get-account-settings --query AccountUsage")]))

AWS_PAGES.append(("ZIP size",
"InvalidParameterException zip more than 50MB.",
["Direct zip limited to 50MB","Can use S3 for larger"],
[("Check size","ls -lh my-function.zip")]))

AWS_PAGES.append(("IAM role",
"InvalidParameterException for IAM role.",
["Role ARN invalid or deleted","Trust policy missing Lambda service"],
[("Check role","aws iam get-role --role my-lambda-role")]))

AWS_PAGES.append(("DLQ not active",
"Custom resources lost DLQ missing.",
["SQS/SNS target invalid","No DLQ provided"],
[("Set DLQ","aws lambda update-function-config --function my-function --dead-letter TargetArn=arn:aws:sqs::123:mydlq")]))

AWS_PAGES.append(("Async invocation",
"AsyncInvocationError events dropped.",
["Queue full or throttled","Payload more than 256KB"],
[("Check invoke config","aws lambda get-function-event-invoke-config --function my-function")]))

AWS_PAGES.append(("Event Source Mapping",
"InvalidParameter/ResourceConflict for mappings.",
["Dynamo/Kinesis access denied","Mapping limit per function reached","SQS does not exist"],
[("List mappings","aws lambda list-event-source-mappings --function my-function")]))

AWS_PAGES.append(("Reserved Concurrency",
"ReservedConcurrentExecutionsLimit.",
["Cannot be 0","Exceeds total account limit"],
[("Set reserved concurrency","aws lambda put-function-concurrency --function my-function --reserved 10")]))

AWS_PAGES.append(("Provisioned Concurrency",
"ProvisionedConcurrencyConfigNotFoundException.",
["Alias/version missing","Account limit reached"],
[("Put PC","aws lambda put-provisioned-concurrency-config --function m-f --qual prod --count 100")]))

AWS_PAGES.append(("SnapStart error",
"SnapStartNotSupported for Lambda SnapStart.",
["Network connections during init","UUID seeded during init","Temp credentials fetched during init"],
[("Set SnapStart","aws lambda update-function-config --function my-function --snap ApplyOn=Published")]))

# RDS
AWS_PAGES.append(("RDS Instance Limit",
"InstanceLimitExceeded when the DB instance quota has been exceeded.",
["Per-region DB instance quota reached","RDS engines have separate limits"],
[("Check count","aws rds describe-db-instances --query DBInstances[*].[DBInstanceIdentifier]"),("Request increase","aws service-quotas request-service-quota-increase --service-code rds --quota-code L-7B9D5F6A --desired-value 50")]))

AWS_PAGES.append(("RDS Storage Full",
"StorageFull when the RDS instance storage is exhausted.",
["Allocated storage consumed by data growth","Binlogs not purged"],
[("Check size","aws rds describe-db-instances --db-instance-identifier mydb --query DBInstances[*].AllocatedStorage"),("Modify","aws rds modify-db-instance --db-instance-identifier mydb --allocated-storage 200 --apply-immediately")]))

AWS_PAGES.append(("RDS Storage Scaling",
"InvalidParameterCombination when storage scaling fails.",
["Modify not supported","Storage exceeds max for instance class"],
[("Describe instance","aws rds describe-db-instances --db-instance-identifier mydb")]))

AWS_PAGES.append(("RDS Backup Retention",
"InvalidParameterValue for backup retention.",
["Must be between 0 and 35 days","Value 0 disables backups"],
[("Check retention","aws rds describe-db-instances --db-instance-identifier mydb --query DBInstances[*].BackupRetentionPeriod"),("Modify","aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7")]))

AWS_PAGES.append(("RDS Snapshot Restore",
"SnapshotRestoreError when restoring from snapshot fails.",
["Source snapshot not available","Cross-region copy incomplete","KMS key mismatch"],
[("List snapshots","aws rds describe-db-snapshots --snapshot-type manual"),("Restore","aws rds restore-db-instance-from-db-snapshot --db-instance-identifier my-restored-db --db-snapshot-identifier my-snapshot")]))

AWS_PAGES.append(("RDS Read Replica Lag",
"ReplicaLag too high causing issues.",
["Replica slower than source","Large write transactions","Network latency"],
[("Check lag","aws rds describe-db-instances --db-instance-identifier mydb-replica --query ReadReplicaSourceDBInstanceIdentifier")]))

AWS_PAGES.append(("RDS Multi-AZ Failover",
"FailoverError when Multi-AZ failover fails.",
["Standby unsynchronized","Replication stall","Network partition"],
[("Reboot with failover","aws rds reboot-db-instance --db-instance-identifier mydb --force-failover")]))

AWS_PAGES.append(("RDS Parameter Group",
"InvalidParameterValue for parameter group.",
["Group incompatible with engine version","Value out of range"],
[("List groups","aws rds describe-db-parameter-groups")]))

AWS_PAGES.append(("RDS Option Group",
"InvalidOptionGroupState for option groups.",
["Group not compatible with engine","Cannot remove permanent option"],
[("List groups","aws rds describe-option-groups")]))

AWS_PAGES.append(("RDS Subnet Group",
"InvalidVPCNetworkStateFault for subnet groups.",
["References deleted subnets","Subnets in different AZs"],
[("List groups","aws rds describe-db-subnet-groups")]))

AWS_PAGES.append(("RDS VPC Security Group",
"AuthorizationNotFound for VPC SGs.",
["Wrong VPC","Region mismatch","Inbound rule missing"],
[("Check rules","aws ec2 describe-security-groups --group-ids sg-abc --query IpPermissions")]))

AWS_PAGES.append(("RDS KMS Encryption",
"KMS.KeyUnavailableException for RDS.",
["Key disabled","Key policy denies RDS","Region mismatch"],
[("Describe key","aws kms describe-key --key-id alias/rds-key")]))

AWS_PAGES.append(("RDS IAM DB Auth",
"AccessDeniedException for IAM DB Auth.",
["IAM DB Auth not enabled","Resource ID mismatch"],
[("Check Auth","aws rds describe-db-instances --db-instance-identifier mydb --query IAMDatabaseAuthenticationEnabled")]))

AWS_PAGES.append(("RDS Engine Version",
"IncompatibleRestore for engine upgrades.",
["Major version unsupported","Version unavailable in region"],
[("Check versions","aws rds describe-db-engine-versions --engine mysql")]))

AWS_PAGES.append(("RDS Upgrade",
"UpgradeFailed when engine upgrade fails.",
["Major requires reboot","PostgreSQL heuristic failure"],
[("Describe instance","aws rds describe-db-instances --db-instance-identifier mydb")]))

AWS_PAGES.append(("RDS Maintenance Window",
"InvalidMaintenanceWindow for scheduling.",
["Window less than 30 min","Not in UTC"],
[("Change window","aws rds modify-db-instance --db-instance-identifier mydb --preferred-maintenance-window mon:03:00-mon:04:30")]))

AWS_PAGES.append(("RDS Automated Backup",
"AutomatedBackupDisabled error.",
["Retention set to 0","Not enabled on instance"],
[("Change retention","aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7")]))

AWS_PAGES.append(("RDS Final Snapshot",
"FinalDBSnapshotRequired when deleting instance.",
["SkipFinalSnapshot not set"],
[("Delete without snapshot","aws rds delete-db-instance --db-instance-identifier mydb --skip-final-snapshot")]))

# DynamoDB
AWS_PAGES.append(("DynamoDB Table Not Active",
"ResourceInUseException when table not ACTIVE.",
["Table in CREATING or UPDATING","CloudFormation rollback"],
[("Wait for Active","aws dynamodb wait table-exists --table my-table")]))

AWS_PAGES.append(("Provisioned Throughput Exceeded",
"ProvisionedThroughputExceededException.",
["Capacity consumed too quickly","Hot partition"],
[("Describe table","aws dynamodb describe-table --table my-table")]))

AWS_PAGES.append(("On-Demand Capacity",
"RequestLimitExceeded for on-demand table.",
["Per-table max reached","Not suitable for steady traffic"],
[("Switch billing","aws dynamodb update-table --table my-table --billing PAY_PER_REQUEST")]))

AWS_PAGES.append(("Write Capacity Exceeded",
"WriteCapacityExceededException.",
["WCU limit reached","Burst consumed"],
[("Increase WCU","aws dynamodb update-table --table my-table --provisioned-throughput WriteCapacityUnits=20")]))

AWS_PAGES.append(("Read Capacity Exceeded",
"ReadCapacityExceededException.",
["RCU limit reached","Expensive Scan operation","Consistent reads cost double"],
[("Increase RCU","aws dynamodb update-table --table my-table --provisioned-throughput ReadCapacityUnits=20")]))

AWS_PAGES.append(("Auto Scaling",
"ValidationException for scaling.",
["Target tracking invalid","Min and max equal"],
[("Check targets","aws app-autoscaling describe-scalable-targets --service dynamodb")]))

AWS_PAGES.append(("Global Table",
"GlobalTableNotFoundException.",
["Table not global","Region not in replication"],
[("Describe global table","aws dynamodb describe-global-table --global-table-name my-table")]))

AWS_PAGES.append(("Replica Not Found",
"ReplicaNotFoundException.",
["Replica name does not exist","Deleted from global table"],
[("Check replicas","aws dynamodb describe-global-table --global-table-name my-table")]))

AWS_PAGES.append(("Stream Not Enabled",
"ValidationException when streams off.",
["Stream spec not set","Trigger without stream"],
[("Check stream","aws dynamodb describe-table --table my-table --query StreamSpec")]))

AWS_PAGES.append(("TTL Error",
"ValidationException for TTL config.",
["TTL attribute missing from schema","Wrong data type"],
[("Check TTL","aws dynamodb describe-time-to-live --table my-table")]))

AWS_PAGES.append(("Item Too Large",
"ValidationException size exceeds 400KB.",
["Size over 400 KB","Binary data not compressed"],
[("Check item","aws dynamodb get-item --table my-table")]))

AWS_PAGES.append(("Batch Get Error",
"ValidationException for BatchGetItem.",
["Too many items (max 100)","Total request more than 16MB"],
[("Retry unprocessed","aws dynamodb batch-get-item --request file://batch.json")]))

AWS_PAGES.append(("Batch Write Error",
"ValidationException for BatchWriteItem.",
["Too many items (max 25)","Duplicate items"],
[("Write one by one","aws dynamodb put-item --table my-table --item file://item.json")]))

AWS_PAGES.append(("Transaction Error",
"TransactionCanceledException.",
["Concurrent modification","Conditional check failed","Transaction more than 4MB"],
[("TransactWrite","aws dynamodb transact-write-items --transact file://transact.json")]))

AWS_PAGES.append(("Condition Expression",
"ConditionalCheckFailedException.",
["Expression false","Attribute nonexistent"],
[("Put with condition","aws dynamodb put-item --table my-table --item file://item.json --condition attribute_not_exists(PK)")]))

AWS_PAGES.append(("Filter Expression",
"ValidationException for filter.",
["Syntax error","Invalid function name","Type mismatch"],
[("Query with filter","aws dynamodb query --table my-table --filter file://filter.json")]))

AWS_PAGES.append(("Key Schema",
"ValidationException for key schema.",
["Missing partition key","GSI key mismatch"],
[("Describe schema","aws dynamodb describe-table --table my-table --query KeySchema")]))

# IAM
AWS_PAGES.append(("IAM Policy Not Found",
"ResourceNotFoundException for policies.",
["Policy not found","Recently deleted"],
[("List policies","aws iam list-policies --scope AWS")]))

AWS_PAGES.append(("Policy Size Too Large",
"LimitExceeded for policy size.",
["Policy more than 6144 bytes","SCP more than 5120 bytes"],
[("Create new","aws iam create-policy --policy my-policy --file policy.json")]))

AWS_PAGES.append(("Role Limit",
"LimitExceeded for role count.",
["1000 roles per account default","Service-linked roles"],
[("Count roles","aws iam list-roles --query length(Roles)")]))

AWS_PAGES.append(("User Limit",
"LimitExceeded for user count.",
["5000 users per account default"],
[("List users","aws iam list-users")]))

AWS_PAGES.append(("Access Key Expired",
"ExpiredToken for expired keys.",
["Key not rotated","Deactivated by admin"],
[("Create new key","aws iam create-access-key")]))

AWS_PAGES.append(("Secret Key Mismatch",
"SignatureDoesNotMatch for wrong secret key.",
["Access key and secret mismatch","Old secret cached"],
[("Create new pair","aws iam create-access-key")]))

AWS_PAGES.append(("Service Role",
"InvalidServiceRole for service-linked roles.",
["Trust policy missing service principal"],
[("Check role","aws iam get-role --role AWSServiceRoleForAmazonElasticsearchService")]))

AWS_PAGES.append(("Trust Policy",
"MalformedPolicyDocument.",
["Principal invalid","Missing sts:AssumeRole"],
[("Get trust policy","aws iam get-role --role my-role --query AssumeRolePolicy")]))

AWS_PAGES.append(("Permissions Boundary",
"PermissionsBoundaryNotSupported.",
["Action disallowed by boundary"],
[("Check boundary","aws iam get-role --role my-role --query PermissionsBoundary")]))

AWS_PAGES.append(("PassRole Error",
"AccessDenied for PassRole.",
["Missing PassRole permission","Boundary blocking"],
[("Simulate passrole","aws iam simulate-custom-policy --action PassRole")]))

AWS_PAGES.append(("AssumeRole Error",
"AccessDenied for AssumeRole.",
["Trust policy excludes principal","MFA missing","Session too long"],
[("Check trust","aws iam get-role --role my-role --query AssumeRolePolicy")]))

AWS_PAGES.append(("SAML Provider",
"InvalidInput for SAML providers.",
["Metadata invalid","Name duplicate"],
[("Create SAML","aws iam create-saml-provider --saml metadata.xml --name MySAML")]))

AWS_PAGES.append(("OIDC Provider",
"InvalidInput for OIDC providers.",
["URL unreachable","Thumbprint incorrect"],
[("List OIDC","aws iam list-open-id-connect-providers")]))

AWS_PAGES.append(("MFA Required",
"AccessDenied when MFA enforced.",
["MFA not configured","Session without token"],
[("List MFA","aws iam list-virtual-mfa-devices")]))

AWS_PAGES.append(("SCP Error",
"AccessDenied due to SCP.",
["SCP denies the action","Overlapping SCPs"],
[("List SCPs","aws organizations list-policies --filter SERVICE_CONTROL_POLICY")]))

AWS_PAGES.append(("Organization SCP",
"AccessDenied due to Org policy.",
["SCP at account or OU blocks"],
[("Describe effective","aws organizations describe-effective-policy --type SERVICE_CONTROL")]))

# ECS/EKS
AWS_PAGES.append(("ECS Cluster Not Found",
"ClusterNotFoundException for ECS.",
["Cluster name incorrect","Cluster deleted","Region mismatch"],
[("List clusters","aws ecs list-clusters")]))

AWS_PAGES.append(("ECS Service Not Stable",
"ServiceNotActiveException.",
["Minimum healthy percent not met","Task exec changes break tasks"],
[("Describe service","aws ecs describe-services --services my-service --cluster my-cluster")]))

AWS_PAGES.append(("ECS Task Def",
"InvalidParameterException for task def.",
["Container image not exist","Env vars > 4KB"],
[("List task defs","aws ecs list-task-definitions")]))

AWS_PAGES.append(("Container Image Pull",
"CannotPullContainerError.",
["Image not in registry","Registry URL wrong","Credentials expired"],
[("Check image","aws ecr describe-images --repo my-repo")]))

AWS_PAGES.append(("Fargate Capacity",
"FargateCapacityExhaustion.",
["Regional capacity limit hit","Spot exhausted"],
[("Check Fargate usage","aws service-quotas get-service-quota --service-code fargate --quota-code L-2FA1B95F")]))

AWS_PAGES.append(("Fargate Spot",
"FargateSpotCapacityUnavailable.",
["Spot exhausted in region","Platform version not supported"],
[("Use On-Demand","aws ecs run-task --launch FARGATE --cluster my-cluster")]))

AWS_PAGES.append(("ELB Target Group",
"InvalidTargetException for ELB.",
["Target group not exist","Health check fails"],
[("List target groups","aws elbv2 describe-target-groups")]))

AWS_PAGES.append(("Service Auto Scaling",
"ServiceAutoScalingError.",
["IAM role misconfigured","Min > max tasks"],
[("Describe targets","aws app-autoscaling describe-scalable-targets --service ecs")]))

AWS_PAGES.append(("Service Discovery",
"ServiceDiscoveryDisabled.",
["Private zone not created","Namespace not exist"],
[("List services","aws servicediscovery list-services")]))

AWS_PAGES.append(("EKS Not Found",
"ResourceNotFoundException for EKS.",
["Cluster name incorrect","Cluster deleted","IAM missing"],
[("List clusters","aws eks list-clusters")]))

AWS_PAGES.append(("EKS Node Group",
"ResourceNotFoundException for node groups.",
["Node group not in cluster","Node group in DELETE state"],
[("List node groups","aws eks list-nodegroups --cluster my-cluster")]))

AWS_PAGES.append(("Fargate Profile (EKS)",
"InvalidParameterException for fargate profile.",
["Selector doesn't match pods","IAM role missing"],
[("List profiles","aws eks list-fargate-profiles --cluster my-cluster")]))

AWS_PAGES.append(("kubeconfig Error",
"AccessDenied for kubeconfig.",
["Not configured for this cluster","Role not authorized"],
[("Update kubeconfig","aws eks update-kubeconfig --region us-east-1 --name my-cluster")]))

AWS_PAGES.append(("IRSA Error",
"AccessDenied for IAM roles for SA.",
["SA annotation missing","Trust policy misconfigured"],
[("Check SA","kubectl describe serviceaccount my-sa -n default")]))

AWS_PAGES.append(("ECR Auth",
"AccessDenied for ECR.",
["Login expired","IAM user no permissions"],
[("Get login","aws ecr get-login-password --region us-east-1")]))

AWS_PAGES.append(("Docker push",
"Denied/DiskFull for Docker push.",
["Repo not exist","Image size > 40GB","Auth expired"],
[("Create repo","aws ecr create-repository --repo my-repo")]))

AWS_PAGES.append(("Repo Policy",
"InvalidParameterException for ECR policy.",
["Policy > 20 KB","Syntax invalid"],
[("Get repo policy","aws ecr get-repository-policy --repo my-repo")]))

# API Gateway
AWS_PAGES.append(("REST API Not Found",
"NotFoundException for REST API.",
["API ID incorrect","API deleted","Region missmatch"],
[("List APIs","aws apigateway get-rest-apis")]))

AWS_PAGES.append(("Deployment Error",
"BadRequestException for deployment.",
["ID already exists","Stage not supported"],
[("Create deployment","aws apigateway create-deployment --rest-api abc123 --stage prod")]))

AWS_PAGES.append(("Stage Not Found",
"NotFoundException for stage.",
["Stage name incorrect","Deleted"],
[("List stages","aws apigateway get-stages --rest-api abc123")]))

AWS_PAGES.append(("Resource Path",
"BadRequestException for path.",
["Path not matched","Param not defined"],
[("List resources","aws apigateway get-resources --rest-api abc123")]))

AWS_PAGES.append(("Method Not Defined",
"NotFoundException for method.",
["Method not enabled","Not in API def"],
[("Get method","aws apigateway get-method --rest-api abc123 --resource def456 --http POST")]))

AWS_PAGES.append(("Integration Failed",
"BadRequestException for integration.",
["Type not set","Endpoint unreachable","Timeout 29s"],
[("Get integration","aws apigateway get-integration --rest-api abc123 --resource def456 --http GET")]))

AWS_PAGES.append(("Lambda Proxy Integration",
"InternalServerError for Lambda proxy.",
["Lambda not exist","Invalid response format","Role insufficient"],
[("Check Lambda response","aws lambda invoke --function my-function response.json")]))

AWS_PAGES.append(("Model/Schema",
"BadRequestException for schema.",
["Body doesn't match schema","Required fields missing"],
[("Get model","aws apigateway get-model --rest-api abc123 --model MyModel")]))

AWS_PAGES.append(("API Key Error",
"Forbidden for API key issues.",
["Key missing","Key deactivated","Plan mismatch"],
[("List API keys","aws apigateway get-api-keys")]))

AWS_PAGES.append(("Usage Plan",
"BadRequestException for usage plan.",
["API not in plan","Throttle/Quota exceeded"],
[("List plans","aws apigateway get-usage-plans")]))

AWS_PAGES.append(("WAF Association",
"BadRequestException for WAF.",
["Regional web ACL not exist","ACL version mismatch"],
[("List for resource","aws wafv2 list-resources-for-web-acl --web-acl-arn arn:aws:waf...")]))

AWS_PAGES.append(("Domain Name",
"NotFoundException for custom domain.",
["Domain not set up","ACM cert mismatch"],
[("List domains","aws apigateway get-domain-names")]))

AWS_PAGES.append(("Base Path Mapping",
"NotFoundException for base path.",
["Path doesn't match mapping","Domain not found"],
[("Get mappings","aws apigateway get-base-path-mappings --domain my-api.com")]))

AWS_PAGES.append(("Canary Deployment",
"BadRequestException for canary.",
["Canary not enabled","Invalid traffic percentage"],
[("Get stage","aws apigateway get-stage --rest-api abc123 --stage prod")]))

AWS_PAGES.append(("Throttling Quota",
"LimitExceededException for throttling.",
["Account limit 10000 RPS","Usage plan exceeded"],
[("Check plan","aws apigateway get-usage-plan --plan-id plan123")]))

# CloudFront
AWS_PAGES.append(("Distribution Not Found",
"NoSuchDistribution for CloudFront.",
["ID incorrect","Deleted","Other account"],
[("List distributions","aws cloudfront list-distributions")]))

AWS_PAGES.append(("Origin Not Accessible",
"OriginAccessDenied for origin.",
["Bucket policy missing CloudFront","Different account","OAI/OAC incorrect"],
[("Check origin","aws cloudfront get-distribution --id E123EXAMPLE")]))

AWS_PAGES.append(("CNAME Already Exists",
"CNAMEAlreadyExists.",
["Already associated with another dist","Other account"],
[("List aliases","aws cloudfront get-distribution --id E123EXAMPLE --query Aliases")]))

AWS_PAGES.append(("SSL Cert Not Found",
"InvalidViewerCertificate.",
["ACM cert not in us-east-1","Doesn't match CNAME","Expired"],
[("List certs","aws acm list-certificates --region us-east-1")]))

AWS_PAGES.append(("Viewer Protocol",
"InvalidProtocolException.",
["HTTPS only without SSL cert","Policy mismatch"],
[("Update behavior","aws cloudfront update-distribution --id E123EXAMPLE --behavior file://behavior.json")]))

AWS_PAGES.append(("Cache Behavior",
"InvalidArgumentException for behavior.",
["Path pattern conflicts","Priority ambiguous"],
[("Get config","aws cloudfront get-distribution-config --id E123EXAMPLE")]))

AWS_PAGES.append(("TTL Config",
"InvalidArgumentException for TTL.",
["Min > max TTL","Default > max TTL"],
[("Update distribution","aws cloudfront update-distribution --id E123EXAMPLE --config file://config.json")]))

AWS_PAGES.append(("Invalidation",
"InvalidArgumentException for invalidations.",
["Path format wrong","Too many items"],
[("Create invalidation","aws cloudfront create-invalidation --id E123EXAMPLE --paths /images/*")]))

AWS_PAGES.append(("Field Level Encryption",
"NotFound for field-level encryption.",
["Config not found","Profile not exist","Key not configured"],
[("List field-level enc","aws cloudfront list-field-level-encryption-configs")]))

AWS_PAGES.append(("WAF Web ACL",
"InvalidWebACLId for CloudFront WAF.",
["ACL not for CloudFront","Must be us-east-1"],
[("List web ACLs","aws wafv2 list-web-acls --scope CLOUDFRONT")]))

AWS_PAGES.append(("Geo Restriction",
"IllegalUpdate for geo restriction.",
["Invalid location code","Both whitelist and blocklist"],
[("Update geo","aws cloudfront update-distribution --id E123EXAMPLE --config file://config.json")]))

AWS_PAGES.append(("Signed URL",
"AccessDenied for signed URLs.",
["Policy invalid","Expired signature","Resource mismatch"],
[("Generate signed URL","aws cloudfront sign --url https://xxx.cloudfront.net/file.txt --key-pair-id K12XYZ")]))

AWS_PAGES.append(("OAI/OAC",
"OriginAccessControlNotFound.",
["OAC not enabled","OAI ID not exist"],
[("Create OAC","aws cloudfront create-origin-access-control --config file://oac.json")]))

AWS_PAGES.append(("Origin Access Denied",
"OriginAccessIdentityAccessDenied.",
["Bucket ACL missing perms","Protocol mismatch"],
[("Check bucket policy","aws s3api get-bucket-policy --bucket my-bucket")]))

# Route53
AWS_PAGES.append(("Hosted Zone Not Found",
"NoSuchHostedZone.",
["Zone ID incorrect","Deleted","Different account"],
[("List zones","aws route53 list-hosted-zones")]))

AWS_PAGES.append(("Record Set Conflict",
"InvalidChangeBatch.",
["Record exists with same name/type","CNAME at apex"],
[("List records","aws route53 list-resource-record-sets --hosted-zone ZONE123")]))

AWS_PAGES.append(("Alias Target",
"InvalidChangeBatch for alias.",
["Target not exist","ELB/CF DNS mismatch"],
[("Get alias","aws route53 list-resource-record-sets --hosted-zone ZONE123")]))

AWS_PAGES.append(("Health Check",
"NoSuchHealthCheck.",
["ID not exist","Config invalid"],
[("List health checks","aws route53 list-health-checks")]))

AWS_PAGES.append(("Failover Routing",
"InvalidChangeBatch for failover.",
["Must have PRIMARY and SECONDARY","Duplicate entries"],
[("Get failover records","aws route53 list-resource-record-sets --hosted-zone ZONE123")]))

AWS_PAGES.append(("Latency Routing",
"InvalidChangeBatch for latency.",
["Alias must include region","Invalid region ID"],
[("List records","aws route53 list-resource-record-sets --hosted-zone ZONE123")]))

AWS_PAGES.append(("Geolocation Routing",
"InvalidChangeBatch for geolocation.",
["Code invalid","Overlapping scopes","Default missing"],
[("List records","aws route53 list-resource-record-sets --hosted-zone ZONE123")]))

AWS_PAGES.append(("Weighted Routing",
"InvalidChangeBatch for weighted.",
["Sum of weights zero","Identifier missing"],
[("List records","aws route53 list-resource-record-sets --hosted-zone ZONE123")]))

AWS_PAGES.append(("Multivalue Answer",
"InvalidChangeBatch for multivalue.",
["Multiple records with same name required"],
[("Check multivalue","aws route53 list-resource-record-sets --hosted-zone ZONE123")]))

AWS_PAGES.append(("DNSSEC",
"InvalidSigningStatus.",
["KSK not created","DNSSEC not enabled","Key not ACTIVE"],
[("Check DNSSEC","aws route53 get-dnssec --hosted-zone ZONE123")]))

AWS_PAGES.append(("Domain Registration",
"InvalidDomainSummary.",
["Domain exists for other account","Not available"],
[("List domains","aws route53domains list-domains")]))

AWS_PAGES.append(("NS Delegation",
"InvalidChangeBatch for NS.",
["Less than 2 NS records","TTL mismatch"],
[("Get NS records","aws route53 list-resource-record-sets --hosted-zone ZONE123 --filter Type=NS")]))

AWS_PAGES.append(("SOA Record",
"InvalidChangeBatch for SOA.",
["TTL cannot be changed directly"],
[("Get SOA","aws route53 list-resource-record-sets --hosted-zone ZONE123 --filter Type=SOA")]))

AWS_PAGES.append(("Private Hosted Zone",
"InvalidVPCId for private zones.",
["No VPC associated","Private zone not for this VPC"],
[("List by VPC","aws route53 list-hosted-zones-by-vpc --vpc vpc-abc")]))

AWS_PAGES.append(("Resolver Rule",
"ResourceNotFoundException for resolver.",
["Rule ID not exist","Type mismatch"],
[("List rules","route53resolver list-resolver-rules")]))

# CloudWatch
AWS_PAGES.append(("Log Group",
"ResourceNotFoundException for log groups.",
["Name incorrect","Not exist","Wrong region"],
[("Describe log groups","aws logs describe-log-groups")]))

AWS_PAGES.append(("Log Stream",
"ResourceNotFoundException for log streams.",
["Name not exist","Deleted","Wrong log group"],
[("Describe log streams","aws logs describe-log-streams --log-group /aws/lambda/myFunc")]))

AWS_PAGES.append(("Metric Filter",
"InvalidParameterException for filters.",
["Filter pattern syntax wrong","Metric name invalid"],
[("List filters","aws logs describe-metric-filters --log-group /aws/lambda/myFunc")]))

AWS_PAGES.append(("Alarm Evaluation",
"BadRequest for alarm evaluation.",
["Period not divisor of 60","Evaluation periods exhausted","Insufficient data"],
[("Describe alarm","aws cloudwatch describe-alarms --alarm-names my-alarm")]))

AWS_PAGES.append(("Insufficient Data",
"InsufficientData for CloudWatch alarm.",
["No datapoints in period","Metric generation stopped","Recently created"],
[("Get metric data","aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric CPUUtilization")]))

AWS_PAGES.append(("SNS Action",
"InvalidParameter for SNS actions.",
["SNS topic not exist","Permissions missing","Cross-region not supported"],
[("Check alarm actions","aws cloudwatch describe-alarms --alarm-name my-alarm")]))

AWS_PAGES.append(("Dashboard",
"InvalidParameter for dashboards.",
["JSON invalid","Name > 255 chars","Widget unsupported"],
[("List dashboards","aws cloudwatch list-dashboards")]))

AWS_PAGES.append(("Metric Math",
"InvalidExpression for metric math.",
["Syntax error in expression","Period mismatch","Statistic invalid"],
[("Get metric math","aws cloudwatch get-metric-data --queries file://queries.json")]))

AWS_PAGES.append(("Logs Insights",
"InvalidQueryException for Logs Insights.",
["Syntax error","Log group not found","Query timeout"],
[("Query logs","aws logs start-query --log-group-names /aws/lambda/myFunc --query file://query.json")]))

AWS_PAGES.append(("Contributor Insights",
"AccessDenied for Contributor Insights.",
["Rule not found","S3 bucket not configured"],
[("List rules","aws logs describe-resource-policies")]))

AWS_PAGES.append(("Anomaly Detection",
"InvalidParameter for anomaly detection.",
["Band not exist","Time series too short","Too many zeros"],
[("Describe anomaly detectors","aws cloudwatch describe-anomaly-detectors")]))

AWS_PAGES.append(("Composite Alarm",
"BadRequest for composite alarms.",
["Rule expression empty","References non-existent alarm","Circular dependency"],
[("List composite alarms","aws cloudwatch describe-alarms --alarm-type CompositeAlarm")]))

AWS_PAGES.append(("Service Quota",
"LimitExceeded for CloudWatch.",
["5000 alarms per region","500 dashboards","1000 metric filters"],
[("Check quotas","aws service-quotas get-service-quota --service-code cloudwatch --quota-code L-00CMI9Q0")]))

AWS_PAGES.append(("CloudWatch Agent",
"CloudWatchAgentConfigurationError.",
["Config file invalid","Agent not running","Firewall blocking"],
[("Check agent","sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status")]))

AWS_PAGES.append(("Unified Agent",
"CWAgentConfigurationError.",
["Agent version mismatch","Plugins invalid"],
[("Restart agent","sudo systemctl restart amazon-cloudwatch-agent")]))

AWS_PAGES.append(("Logs Subscription",
"BadRequest for subscription.",
["Destination not in same account","Access policy missing"],
[("Describe subscriptions","aws logs describe-subscription-filters --log-group my-group")]))

# KMS / Security
AWS_PAGES.append(("KMS Key Not Found",
"NotFoundException for KMS key.",
["Key ID not exist","Deleted or pending deletion","Wrong account/region"],
[("List keys","aws kms list-keys")]))

AWS_PAGES.append(("KMS Key Disabled",
"DisabledException for disabled key.",
["Admin disabled the key","Scheduled for deletion"],
[("Enable key","aws kms enable-key --key-id alias/MyKey")]))

AWS_PAGES.append(("KMS Key Pending Deletion",
"KMSInvalidStateException for pending key.",
["Key is pending deletion"],
[("Cancel deletion","aws kms cancel-key-deletion --key-id 1234abcd-12ab-34cd-56ef-1234567890ab")]))

AWS_PAGES.append(("KMS Key Usage",
"ValidationException for key usage.",
["Usage mismatch (ENCRYPT vs SIGN)","Forbidden operation"],
[("Describe key","aws kms describe-key --key-id alias/my-key")]))

AWS_PAGES.append(("Custom Key Store",
"CustomKeyStoreNotFoundException for CloudHSM.",
["HSM cluster not active","Store ID invalid","Proxy auth failed"],
[("List custom stores","aws kms list-custom-key-stores")]))

AWS_PAGES.append(("CloudHSM",
"CloudHsmAccessDenied.",
["HSM not provisioned","Client IP not authorized"],
[("List clusters","cloudhsm list-clusters")]))

AWS_PAGES.append(("Secret Not Found",
"ResourceNotFoundException for Secrets Manager.",
["Name/ARN incorrect","Deleted or scheduled for deletion"],
[("List secrets","aws secretsmanager list-secrets")]))

AWS_PAGES.append(("Secret Rotation",
"InvalidRequestException for rotation.",
["Lambda for rotation not exist","Period invalid"],
[("Describe secret","aws secretsmanager describe-secret --secret-id my-secret")]))

AWS_PAGES.append(("Certificate Not Found",
"ResourceNotFoundException for ACM.",
["Certificate not exist","Deleted","Domain mismatch"],
[("List certificates","aws acm list-certificates")]))

AWS_PAGES.append(("Certificate Renewal",
"ValidationException for renewal.",
["Email validation pending","DNS records missing","CAA records blocking"],
[("Describe cert","aws acm describe-certificate --certificate-arn arn:aws:acm::123:certificate/xxx")]))

AWS_PAGES.append(("Private CA Renewal",
"ResourceNotFound for private CA cert.",
["CA not exist","CA suspended"],
[("List CAs","aws acm-pca list-certificate-authorities")]))

AWS_PAGES.append(("GuardDuty",
"ResourceNotFoundException for GuardDuty.",
["Not enabled","Detector ID not exist"],
[("List detectors","guardduty list-detectors")]))

AWS_PAGES.append(("Security Hub",
"AccessDeniedException for Security Hub.",
["Not enabled","Member not invited"],
[("Enable Security Hub","aws securityhub enable-security-hub")]))

AWS_PAGES.append(("Config Rule",
"ResourceNotFoundException for Config.",
["Rule not exist","Recording not enabled"],
[("Describe config rules","aws configservice describe-config-rules")]))

AWS_PAGES.append(("WAF Rule",
"WAFNonexistentRuleException.",
["Rule name incorrect","Deleted but still used"],
[("List WAF rules","aws wafv2 list-rules --scope REGIONAL")]))

AWS_PAGES.append(("Shield Advanced",
"AccessDenied for Shield.",
["Subscription not active","Resource ID invalid","Protection not exist"],
[("List protections","shield list-protections")]))

print("=== AWS ===")
count = generate_pages("aws", "/home/admin1/projects/ErrorCode.excellentwiki.com/content/cloud/aws", AWS_PAGES, "aws")
print(f"AWS total: {count}")
