"""Generate AWS cloud error pages - Part 2: RDS, DynamoDB, IAM"""
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
            f"The `{title.replace('AWS ', '')}` error occurs when an AWS AWS service cannot complete the requested operation.",
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
            lines.append(f"- Example scenario: {c. lower()}")
        lines.extend(["", "## Related Errors", ""])
        lines.append(f"- [AWS EC2 Error]({{{{< relref \"/cloud/aws/aws-ec2-error\" >}[}}}}) -- General EC2 errors")
        lines.append(f"- [AWS CloudWatch Error]({{{{< relref \"/cloud/aws/aws-cloudwatch-error\" >}}}}) -- CloudWatch errors")
        with open(fpath, "w") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  CREATED: {filename}")

# ===================== RDS (19 pages) =====================
add("rds", "RDS DB Instance Limit Exceeded",
    "InstanceLimitExceeded when the DB instance quota has been exceeded.",
    ["Per-region DB instance quota reached",
     "RDS engines each have separate instance limits",
     "On-Demand DB instance allocation is full",
     "Reserved instance commitment count",
     "Multi-AZ instances count toward instance quota"],
    [("Check count", "aws rds describe-db-instances --query DBInstances[*].[DBInstanceIdentifier]"),
     ("Request quota increase", "aws service-quotas request-service-quota-increase --service-code rds --quota-code L-7B9D5F6A --desired-value 50")])

add("rds", "RDS Instrument Storage Full",
    "StorageFull when the RDS instance storage is exhausted.",
    ["Allocated storage consumed by data growth",
     "Binlogs or transaction logs not purged",
     "Sort/result files use disk space temporarily",
     "Slow Query or General log fills up space"],
    [("Check size", "aws rds describe-db-instances --db-instance-identifier mydb --query DBInstances[*].AllocatedStorage"),
     ("Modify allocated storage", "aws rds modify-db-instance --db-instance-identifier mydb --allocated-storage 200 --apply-immediately")])

add("rds", "RDS Instrument Storage Scaling",
    "InvalidParameterCombination when storage scaling fails.",
    ["Modify not supported for gp2-to-gp2 storage type",
     "Current storage exceeds max for this instance class",
     "IOPS request incompatible with new storage size",
     "Storage autoscaling conflicts with manual change"],
    [("Describe instance", "aws rds describe-db-instances --db-instance-identifier mydb"),
     ("Modify storage", "aws rds modify-db-instance --db-instance-identifier mydb --allocated-storage 300 --apply-immediately")])

add("rds", "RDS Backup Retention",
    "InvalidParameterValue for backup retention period.",
    ["Backup retention period must be between 0 and 35 days",
     "Value 0 disables automated backups",
     "Read replica source requires backup retention > 0",
     "Magnetic storage cannot have retention > 1"],
    [("Check backup retention", "aws rds describe-db-instances --db-instance-identifier mydb --query DBInstances[*].BackupRetentionPeriod"),
     ("Modify backup retention", "aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7")])

add("rds", "RDS Snapshot Restore",
    "SnapshotRestoreError when restoring a DB from a snapshot fails.",
    ["Source snapshot is not in an available state",
     "Cross-region copy is incomplete",
     "Different KMS key in use between source and target",
     "Instance class incompatible with the snapshot engine"],
    [("List snapshots", "aws rds describe-db-snapshots --snapshot-type manual"),
     ("Restore from snapshot", "aws rds restore-db-instance-from-db-snapshot --db-instance-identifier my-restored-db --db-snapshot-identifier my-snapshot")])

add("rds", "RDS Read Replica Lag",
    "ReplicationReplicaLagInMilliSeconds too high causing issues.",
    ["Replica is slower than the source instance",
     "Large write transactions on source",
     "Replica has smaller hardware than the source",
     "Network latency between regions"],
    [("Check lag", "aws rds describe-db-instances --db-instance-identifier mydb-replica --query DBInstances[*].ReadReplicaSourceDBInstanceIdentifier"),
     ("Promote replica", "aws rds promote-read-replica --db-instance­identifier mydb-replica")])

add("rds", "RDS Multi-AZ Failover",
    "FailoverError when Multi-AZ failover does not succeed.",
    ["Failover triggered but standby is unsynchronized",
     "Replication stall between AZs",
     "Network partition between AZs",
     "Standby instance crash during failover"],
    [("Reboot with failover", "aws rds reboot-db-instance --db-instance-identifier mydb --force-failover")])

add("rds", "RDS Parameter Group",
    "InvalidParameterValue for RDS parameter group assignment.",
    ["Parameter group incompatible with DB engine version",
     "Parameter value out of range for the engine",
     "Custom parameter group is missing",
     "Pending reboot for static parameters"],
    [("List groups", "aws rds describe-db-parame ter-groups"),
     ("Associate with instance", "aws rds modify-db-instance --db-instance-identifier mydb --db-parameter-group-name custom-params")])

add("rds", "Option Group Error",
    "InvalidOptionGroupState/InvalidParameterValue for option groups.",
    ["Option group not compatible with the engine",
     "Cannot remove a permanent option",
     "Option already associated with the instance",
     "Option group deleted while in use"],
    [("List groups", "aws rds describe-option-groups")])

add("rds", "RDS Subnet Group",
    "InvalidVPCNetworkStateFault/DBSubnetGroupNotFound for subnet groups.",
    ["Subnet group references deleted subnets",
     "Subnets in different Availability Zones",
     "Subnet count insufficient for Multi-AZ",
     "Subnet CIDR conflicts with VPC peer"],
    [("List groups", "aws rds describe-db-subnet-groups")])

add("rds", "RDS VPC Security Group",
    "AuthorizationNotFound/InvalidParameter for RDS VPC SGs.",
    ["Security group in the wrong VPC",
     "Security group ID belongs to a different region",
     "Inbound rule missing for RDS port (3306/5432)",
     "Cross-account SG reference not authorized"],
    [("Check inbound rules", "aws ec2 describe-security-groups --group-ids sg-abc --query SGs")])

add("rds", "RDS KMS Encryption",
    "KMS.KeyUnavailableException/KMS.AccessDenied for RDS.",
    ["KMS key disabled or pending deletion",
     "KMS key policy does not allow RDS",
     "RDS service principal denied by key policy",
     "KMS key belongs to a different region"],
    [("Describe key", "aws kms describe-key --key-alias rds-key")])

add("rds", "IAM DB Authentication",
    "AccessDeniedException when using IAM DB Auth.",
    ["IAM DB Auth not enabled on the RDS instance",
     "RDS resource ID missing in the IAM policy",
     "Wrong action rds-db:connect resource"],
    [("Check IAM Auth", "aws rds describe-db-instances --db-instance-identifier mydb --query DBInstances[*].IAMDatabaseAuthenticationEnabled")])

add("rds", "RDS Engine Version",
    "DBInstanceNotFound/IncompatibleRestore for engine upgrades.",
    ["Major version upgrade unsupported for this instance class",
     "Engine version unavailable in this region",
     "Incompatible parameter group for the target version"],
    [("Check versions", "aws rds describe-db-engine-versions --engine mysql")])

add("rds", "RDS Upgrade",
    "UpgradeFailed when the engine upgrade does not complete.",
    ["Major version upgrade requires modify + reboot",
     "PostgreSQL upgrade heuristic failure",
     "Incompatible parameters blocking the upgrade"],
    [("Describe instance", "aws rds describe-db-instances --db-instance-identifier mydb")])

add("rds", "Maintenance Window",
    "InvalidMaintenanceWindow for scheduling.",
    ["Window duration < 30 minutes",
     "Window not in UTC time zone",
     "Window conflicts with auto minor upgrade window"],
    [("Change window", "aws rds modify-db-instance --db-instance-identifier mydb --preferred-maintenance-window mon:03:00-mon:04:30")])

add("rds", "Automated Backup",
    "AutomatedBackupDisabled/ValidationError for backups.",
    ["Backup retention set to 0",
     "Automated backups not enabled",
     "Cross-Region copy not configured"],
    [("Change retention", "aws rds modify-db-instance --db-instance-identifier mydb --backup-retention-period 7")])

add("rds", "RDS Final Snapshot",
    "FinalDBSnapshotRequired when deleting an RDS instance.",
    ["SkipFinalSnapshot not set",
     "FinalDBSnapshotIdentifier not provided"],
    [("Delete without snapshot", "aws rds delete-db-instance --db-instance-identifier mydb --skip-final-snapshot")])

# ===================== DynamoDB (19 pages) =====================
add("dynamodb", "DynamoDB Table Not Active",
    "ResourceInUseException when the table is not yet ACTIVE.",
    ["Table in CREATING or UPDATING status",
     "Deleting state table cannot be used",
     "CloudFormation rollback causing inconsistency",
     "Backup/restore in progress"],
    [("Wait for Active", "aws dynamodb wait table-exists --table-name my-table")])

add("dynamodb", "Provisioned Throughput Exceeded",
    "ProvisionedThroughputExceededException when capacity exhausts.",
    ["RCU/WCU consumed too quickly, burst depleted",
     "Hot partition receives excessive requests",
     "Auto Scaling cannot keep up"],
    [("Describe table", "aws dynamodb describe-table --table-name my-table")])

add("dynamodb", "On-Demand Capacity Issue",
    "RequestLimitExceeded for an on-demand table.",
    ["Per-table max throughput reached for on-demand",
     "On-demand is not suitable for steady high traffic"],
    [("Switch billing mode", "aws dynamodb update-table --table-name my-table --billing-mode PAY_PER_REQUEST")])

add("dynamodb", "Write Capacity Exceeded",
    "WriteCapacityExceededException for write capacity.",
    ["WCU limit reached on this table",
     "Burst capacity fully consumed",
     "GSI write capacity too low"],
    [("Increase WCU", "aws dynamodb update-table --table-name my-table --provisioned-throughput WriteCapacityUnits=20")])

add("dynamodb", "Read Capacity Exceeded",
    "ReadCapacityExceededException for read capacity.",
    ["RCU limit reached on this table",
     "Expensive Scan/Query operations",
     "Consistent reads cost double"],
    [("Increase RCU", "aws dynamodb update-table --table-name my-table --provisioned-throughput ReadCapacityUnits=20"),
     ("Optimize queries", "aws dynamodb query --table-name my-table --key-condition UserId=:uid")])

add("dynamodb", "Auto Scaling err",
    "ValidationException/ResourceInUse for scaling.",
    ["Target tracking metric invalid",
     "Min and max set to equal values",
     "Role permissions insufficient"],
    [("Check scalable targets", "aws app-autoscaling describe-scalable-targets --service dynamodb")])

add("dynamodb", "Global Table Error",
    "GlobalTableNotFoundException/ReplicaNotFound.",
    ["Table not global",
     "Region not in replication",
     "Version mismatch (2017 vs 2019)"],
    [("Describe global table", "aws dynamodb describe-global-table --global-table-name my-table")])

add("dynamodb", "Replica Not Found",
    "ReplicaNotFoundException for global table replicas.",
    ["Replica name does not exist",
     "Replica deleted from the global table",
     "Replica creation still in progress"],
    [("Check replicas", "aws dynamodb describe-global-table --global-table-name my-table")])

add("dynamodb", "Stream Not Enabled",
    "ValidationException when streams are off.",
    ["Stream spec not set on the table",
     "Stream activated after trigger creation"],
    [("Check stream", "aws dynamodb describe-table --table-name my-table --query StreamSpec")])

add("dynamodb", "TTL Error",
    "ValidationException when configuring TTL.",
    ["TTL attribute missing from the schema",
     "Wrong data type (needs number)",

     "TTL value in the past causes instant deletion"],
    [("Check TTL", "aws dynamodb describe-time-to-live --table my-table")])

add("dynamodb", "Item Too Large",
    "ValidationException when the item is above 400KB.",
    ["size > 400KB DynamoDB limit",
     "Nested json/document exceeding size",
     "Binary data not compressed"],
    [("Check size", "aws dynamodb get-item --table-name my-table")])

add("dynamodb", "Batch Get Error",
    "ValidationException/PTExceeded for BatchGetItem.",
    ["Too many items in batch (max 100)",
     "Total request > 16MB",

     "Capacity throttle unprocessed keys"],
    [("Retry unprocessed", "aws dynamodb batch-get-item --request-items file://batch.json")])

add("dynamodb", "Batch Write Error",
    "ValidationException/PTExceeded for BatchWriteItem.",
    ["Too many items in batch (max 25)",
     "Duplicate items in same batch",
     "Capacity throttling"],
    [("Write one by one", "aws dynamodb put-item --table-name my-table --item file://item.json")])

add("dynamodb", "Transaction Error",
    "TransactionCanceledException/TransactionConflict.",
    ["Concurrent modification causing conflict",
     "Conditional check failed",
     "Transaction > 4MB limit"],
    [("TransactWrite", "aws dynamodb transact-write-items --transact file://transact.json")])

add("dynamodb", "Condition Expression",
    "ConditionalCheckFailedException for condition failure.",
    ["Expression evaluated to false",
     "Attribute nonexistent",
     "Data type mismatch in comparison"],
    [("Put with condition", "aws dynamodb put-item --table my-table --item file://item.json --condition attribute_not_exists(PK)")])

add("dynamodb", "Filter Expression",
    "ValidationException for invalid filter expression.",
    ["Syntax error in the condition",
     "Invalid function name",
     "Data type mismatch"],
    [("Query with filter", "aws dynamodb query --table my-table --filter file://filter.json")])

add("dynamodb", "Key Schema",
    "ValidationException for invalid key schema.",
    ["Missing partition or sort key",
     "GSI key existing attribute mismatch"],
    [("Describe schema", "aws dynamodb describe-table --table my-table --query KeySchema")])

# ===================== IAM (19 pages) =====================
add("iam", "IAM Policy Not Found",
    "ResourceNotFoundException/NoSuchEntity for policies.",
    ["Policy with given ARN not found",
     "Policy was recently deleted",
     "Custom vs managed policy confusion"],
    [("List policies", "aws iam list-policies --scope AWS")])

add("iam", "Policy Size Too Large",
    "LimitExceeded when the policy exceeds max allowed size.",
    ["IAM policy > 6,144 bytes",
     "Trust policy > 6,144 bytes",

     "SCP > 5,120 bytes"],
    [("Create new policy", "aws iam create-policy --policy my-policy --file policy.json")])

add("iam", "Role Limit",
    "LimitExceeded when the role count limit is reached.",
    ["Default 1000 roles per account",
     "Service-linked roles count toward limit"],
    [("Count roles", "aws iam list-roles --query length(Roles)")])

add("iam", "User Limit",
    "LimitExceeded when user count limit is reached.",
    ["Default 5000 users per account",
     "Federated accounts toward limit"],
    [("List users", "aws iam list-users")])

add("iam", "Access Key Expired",
    "ExpiredToken/InvalidClientTokenId for expired keys.",
    ["Key not rotated beyond aging policy",
     "Administrator deactivated the key"],
    [("Create new key", "aws iam create-access-key")])

add("iam", "Secret Key mismatch",
    "SignatureDoesNotMatch for wrong secret key.",
    ["secret key and access key mismatch",
     "Old secret cached after rotation"],
    [("Create new pair", "aws iam create-access-key")])

add("iam", "Service Role",
    "InvalidServiceRole/ServiceFailure for service-linked roles.",
    ["Trust policy does not include the AWS service"],
    [("Check role", "aws iam get-role --role-name the-role")])

add("iam", "Trust Policy",
    "MalformedPolicyDocument for trust policy issues.",
    ["Principal entry invalid",
     "Missing Action "sts:AssumeRole""],
    [("Get trust policy", "aws iam get-role --role-name my-role --query Role.AssumeRolePolicy")])

add("iam", "Permissions Boundary",
    "PermissionsBoundaryNotSupported/AccessDenied.",
    ["Action disallowed by the boundary",

     "Resource outside the boundary scope"],
    [("Check boundary", "aws iam get-role --role my-role --query boundary")])

add("iam", "PassRole Error",
    "AccessDenied when PassRole is not permitted.",
    ["Role is missing PassRole permission",
     "Permissions boundary blocking the pass"],
    [("Simulate PassRole", "aws iam simulate-custom-policy --action PassRole")])

add("iam", "AssumeRole Error",
    "AccessDenied/Validation for AssumeRole.",
    ["Trust policy excludes the principal",

     "MFA missing when required",

     "Session duration too long"],
    [("Check trust", "aws iam get-role --role my-role --query AssumeRolePolicy")])

add("iam", "SAML Provider",
    "InvalidInput/EntityAlreadyExists for SAML.",
    ["SAML metadata document invalid",

     "SAM provider name duplicate"],
    [("Create provider", "aws iam create-saml-provider --saml name.xml --name MySAML")])

add("iam", "OIDC Provider",
    "InvalidInput/EntityAlreadyExists for OIDC.",
    ["OIDC provider URL unreachable",
     "Thumbprint list incorrect"],
    [("List OIDC", "aws iam list-open-id-connect-providers")])

add("iam", "MFA Required",
    "AccessDenied when MFA is enforced.",
    ["MFA not configured on the user",
     "Session without MFA token"],
    [("List MFA", "aws iam list-virtual-mfa-devices")])

add("iam", "SCP Error",
    "AccessDenied due to SCP.",
    ["SCP explicitly denies the action",
     "Multiple overlapping SCPs conflict"],
    [("List SCPs", "aws organizations list-policies --filter SERVICE_CONTROL")])

add("iam", "Organization SCP",
    "AccessDenied due to Organizations policy.",
    ["SCP at the account or OU level blocks"],
    [("Describe effective policy", "aws organizations effective-policy --type SCP")])

# Fix duplicate entries and missing items
# Also add missing entries
add("iam", "PassRole Denied",
    "AccessDenied when PassRole is not allowed.",
    ["IAM role without PassRole permission",
     "Permissions boundary prevents PassRole",
     "Resource in different account"],
    [("Simulate Permissions", "aws iam simulate-custom-policy --action PassRole")])

add("iam", "Role Limit Hit",
    "LimitExceeded when the role limit is reached.",
    ["1000 roles per account (default) is reached",
     "Service-linked and custom roles cumulated"],
    [("Count current roles", "aws iam list-roles --output text | wc -l")])

if __name__ == "__main__":
    write_pages()
    print(f"Total new RDS/Dynamo/IAM pages: {len(PAGES)}")
