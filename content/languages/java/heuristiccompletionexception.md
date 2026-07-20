---
title: "[Solution] Java HeuristicCompletionException — Transaction Recovery Fix"
description: "Fix javax.transaction.HeuristicCompletionException by investigating resource manager state, implementing recovery logging, and checking transaction coordinator."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# HeuristicCompletionException — Transaction Recovery Fix

A `HeuristicCompletionException` is thrown when a heuristic decision has been completed — meaning the transaction manager or resource manager has made an autonomous decision about a transaction's outcome without coordination. This typically occurs during recovery or when a resource manager times out.

## Description

HeuristicCompletionException is a checked exception from the `javax.transaction` package. It is thrown when `getRollbackOnly()` or `getStatus()` is called on a transaction that has already completed via a heuristic decision. The transaction ended with a heuristic outcome rather than a coordinated commit or rollback.

Common message variants include:

- `HeuristicCompletionException: Transaction already heuristic completed`
- `HeuristicCompletionException: Status unknown after heuristic completion`
- `HeuristicCompletionException: Heuristic commit has been completed`

## Common Causes

```java
// Cause 1: Calling getRollbackOnly() after heuristic completion
UserTransaction utx = ...;
utx.begin();
// ... some operations ...
// Transaction ends with heuristic decision
utx.getRollbackOnly(); // Throws HeuristicCompletionException

// Cause 2: Resource manager timeout leads to heuristic completion
// TM waiting for resource manager response — RM times out and decides independently

// Cause 3: Recovery process encounters already-heuristic transaction
// After TM restart, recovery finds transaction with heuristic outcome
```

## Solutions

### Fix 1: Check transaction status before operations

```java
import javax.transaction.UserTransaction;
import javax.transaction.Status;

public void safeTransactionOperation(UserTransaction utx) {
    try {
        int status = utx.getStatus();

        switch (status) {
            case Status.STATUS_ACTIVE:
            case Status.STATUS_MARKED_ROLLBACK:
                // Transaction is active — safe to operate
                utx.commit();
                break;
            case Status.STATUS_COMMITTED:
            case Status.STATUS_ROLLEDBACK:
            case Status.STATUS_UNKNOWN:
                // Transaction already completed — don't attempt operations
                break;
            default:
                // Status is transitional — wait or skip
                break;
        }
    } catch (Exception e) {
        handleTransactionError(e);
    }
}
```

### Fix 2: Implement comprehensive recovery logging

```java
import javax.transaction.xa.Xid;

public class TransactionRecoveryLog {
    private final Connection logConnection;

    public void logTransactionStart(Xid xid) throws SQLException {
        PreparedStatement ps = logConnection.prepareStatement(
            "INSERT INTO tx_recovery_log (xid, status, start_time) VALUES (?, ?, ?)");
        ps.setString(1, xid.toString());
        ps.setString(2, "ACTIVE");
        ps.setTimestamp(3, Timestamp.from(Instant.now()));
        ps.executeUpdate();
    }

    public void logHeuristicCompletion(Xid xid, boolean committed) throws SQLException {
        PreparedStatement ps = logConnection.prepareStatement(
            "UPDATE tx_recovery_log SET status = ?, end_time = ? WHERE xid = ?");
        ps.setString(1, committed ? "HEUR_COMMITTED" : "HEUR_ROLLEDBACK");
        ps.setTimestamp(2, Timestamp.from(Instant.now()));
        ps.setString(3, xid.toString());
        ps.executeUpdate();
    }

    public List<Xid> getHeuristicTransactions() throws SQLException {
        List<Xid> heuristics = new ArrayList<>();
        ResultSet rs = logConnection.createStatement().executeQuery(
            "SELECT xid FROM tx_recovery_log WHERE status LIKE 'HEUR_%'");
        while (rs.next()) {
            heuristics.add(parseXid(rs.getString("xid")));
        }
        return heuristics;
    }
}
```

### Fix 3: Add transaction coordinator monitoring

```java
public class TransactionCoordinatorMonitor {
    private final TransactionManager tm;

    public void monitorTransactionHealth() {
        try {
            // Check for stuck transactions
            List<Transaction> activeTransactions = getActiveTransactions();

            for (Transaction tx : activeTransactions) {
                long age = System.currentTimeMillis() - tx.getStartTime();
                if (age > MAX_TRANSACTION_AGE_MS) {
                    log.warn("Long-running transaction detected: " + tx.getXid()
                        + " age: " + age + "ms");

                    // Force timeout to prevent heuristic completion
                    tx.setTransactionTimeout(SHORT_TIMEOUT);
                }
            }
        } catch (SystemException e) {
            log.error("Failed to monitor transactions", e);
        }
    }

    private void forceTransactionTimeout(Transaction tx) {
        try {
            // Force the transaction to complete
            tm.setTransactionTimeout(1); // 1 second timeout
            // Next operation will timeout the transaction
        } catch (SystemException e) {
            log.error("Failed to set timeout for transaction: " + tx.getXid(), e);
        }
    }
}
```

### Fix 4: Handle heuristic completion during recovery

```java
public class HeuristicRecoveryHandler {
    public void handleHeuristicCompletion(Xid xid) {
        try {
            // Query all resource managers for the transaction outcome
            boolean allCommitted = true;
            boolean allRolledBack = true;

            for (XAResource resource : getResources()) {
                int vote = resource.prepare(xid);
                if (vote == XA_RDONLY) {
                    // Resource already decided — check its state
                    boolean committed = isResourceCommitted(resource, xid);
                    if (!committed) allCommitted = false;
                    if (committed) allRolledBack = false;
                }
            }

            if (allCommitted) {
                // Force commit on remaining resources
                commitAll(xid);
            } else if (allRolledBack) {
                // Force rollback on remaining resources
                rollbackAll(xid);
            } else {
                // Mixed state — log for manual intervention
                logHeuristicMixed(xid);
            }
        } catch (XAException e) {
            log.error("Recovery failed for " + xid, e);
        }
    }
}
```

## Prevention Checklist

- Always check `getStatus()` before calling `getRollbackOnly()`.
- Implement transaction timeout monitoring to prevent stale transactions.
- Log all heuristic outcomes for post-mortem analysis.
- Set up automated recovery procedures for heuristic transactions.
- Monitor resource manager response times during 2PC.

## Related Errors

- [HeuristicMixedException](../heuristicmixedexception) — Mixed commit/rollback across resources.
- [RollbackException](../rollbackexception) — Transaction rolled back.
- [SystemException](../systemexception) — Transaction manager system error.
