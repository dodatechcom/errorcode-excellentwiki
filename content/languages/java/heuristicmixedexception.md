---
title: "[Solution] Java HeuristicMixedException — XA Transaction Fix"
description: "Fix javax.transaction.HeuristicMixedException by implementing proper XA transaction handling, checking 2PC protocol, and investigating resource managers."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# HeuristicMixedException — XA Transaction Fix

A `HeuristicMixedException` is thrown when a heuristic decision was made across multiple resources during a two-phase commit (2PC) — some resources committed while others rolled back. This results in an inconsistent state that requires manual intervention.

## Description

HeuristicMixedException is a checked exception from the `javax.transaction` package. It indicates that the transaction manager could not achieve a uniform outcome across all participating resources. In a distributed transaction, one resource manager may have committed while another rolled back, leaving the system in an inconsistent state.

Common message variants include:

- `HeuristicMixedException: heuristic decision: some resources committed, some rolled back`
- `HeuristicMixedException: Partial commit detected in XA transaction`
- `HeuristicMixedException: Mixed outcome in two-phase commit`

## Common Causes

```java
// Cause 1: Network partition during 2PC
// TM sends prepare to Resource1 (success) and Resource2 (success)
// TM sends commit to Resource1 (success) but Resource2 unreachable
// Resource2 eventually decides to roll back — mixed heuristic

// Cause 2: Resource manager crash during commit phase
// Resource1 commits, Resource2 crashes — TM marks heuristic mixed

// Cause 3: Timeout during distributed transaction
// Different resource managers have different timeout settings
// One commits, other times out and rolls back
```

## Solutions

### Fix 1: Implement proper XA resource management

```java
import javax.transaction.xa.XAResource;
import javax.transaction.xa.Xid;
import javax.transaction.xa.XAException;

public class ReliableXAResource implements XAResource {
    private Connection connection;

    @Override
    public int prepare(Xid xid) throws XAException {
        try {
            // Prepare local resource
            connection.prepareStatement("PREPARE TRANSACTION " + xid.toString())
                .execute();
            return XA_OK; // Vote yes
        } catch (SQLException e) {
            // Unable to prepare — vote no
            throw new XAException(XAException.XAER_RMFAIL);
        }
    }

    @Override
    public void commit(Xid xid, boolean onePhase) throws XAException {
        try {
            if (onePhase) {
                connection.commit();
            } else {
                connection.prepareStatement("COMMIT PREPARED '" + xid.toString() + "'")
                    .execute();
            }
        } catch (SQLException e) {
            throw new XAException(XAException.XA_HEURMIX);
        }
    }

    @Override
    public void rollback(Xid xid) throws XAException {
        try {
            connection.prepareStatement("ROLLBACK PREPARED '" + xid.toString() + "'")
                .execute();
        } catch (SQLException e) {
            throw new XAException(XAException.XA_HEURMIX);
        }
    }
}
```

### Fix 2: Add XA recovery logging

```java
import javax.transaction.TransactionManager;

public class XARecoveryLogger {
    private final TransactionManager tm;

    public void logTransactionOutcome(Xid xid, boolean committed) {
        // Log the heuristic outcome for later investigation
        String outcome = committed ? "COMMITTED" : "ROLLED_BACK";
        System.err.println("HEURISTIC: Transaction " + xid + " " + outcome);

        // Persist for manual reconciliation
        saveRecoveryRecord(xid, outcome);
    }

    private void saveRecoveryRecord(Xid xid, String outcome) {
        // Write to recovery log
        // This record helps identify and fix inconsistent state
    }
}
```

### Fix 3: Implement resource manager timeout alignment

```java
// Ensure all resource managers use the same timeout
Properties props = new Properties();

// Database resource manager
props.put("hibernate.connection.timeout", "30");
props.put("hibernate.connection.socketTimeout", "30");

// JMS resource manager
props.put("jakarta.jms.client.receiveTimeout", "30000");

// Set global transaction timeout
UserTransaction utx = // lookup from JNDI
utx.setTransactionTimeout(30); // All resources must complete within 30s
```

### Fix 4: Add heuristic recovery procedure

```java
public class HeuristicRecoveryProcedure {
    public void recover() {
        // 1. Identify in-doubt transactions from TM recovery log
        Xid[] inDoubt = transactionManager.getResourceManager()
            .getInDoubtTransactions();

        for (Xid xid : inDoubt) {
            // 2. Query each resource manager for transaction outcome
            boolean resource1Committed = checkResource1Outcome(xid);
            boolean resource2Committed = checkResource2Outcome(xid);

            if (resource1Committed && !resource2Committed) {
                // 3. Force rollback on resource1 to match resource2
                forceRollbackResource1(xid);
            } else if (!resource1Committed && resource2Committed) {
                // 3. Force rollback on resource2 to match resource1
                forceRollbackResource2(xid);
            }
            // If both committed or both rolled back — consistent state
        }
    }
}
```

## Prevention Checklist

- Ensure all XA resources have compatible timeout settings.
- Implement XA recovery logging for all distributed transactions.
- Test network resilience during 2PC protocol operations.
- Monitor resource manager health during transaction processing.
- Set up automated heuristic recovery procedures.

## Related Errors

- [HeuristicCompletionException](../heuristiccompletionexception) — Heuristic decision completed.
- [RollbackException](../rollbackexception) — Transaction rolled back.
- [SystemException](../systemexception) — Transaction manager system error.
