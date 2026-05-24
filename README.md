# SwarmBench Enterprise Assessment

This repository contains a self-contained, production-grade SwarmBench benchmark task named **Enterprise QA Infrastructure Recovery** (`swarmbench-enterprise-assessment`). 

The task is designed to evaluate and demonstrate the structural performance gap between a **Single-Agent AI** and a **Multi-Agent system** utilizing advanced decomposition and parallel execution.

---

## 📋 Task Overview
An enterprise-grade Python test automation framework has been migrated to a new environment, but it currently has multiple integration and infrastructure defects. There are **10 distinct, independent bugs** spread across UI page objects, wait utilities, API validation clients, CSV mappers, E2E checkout flows, retry decorators, parallel logging thread synchronizers, conftest webdrivers, HTML reporters, and Groovy Jenkinsfiles.

A single agent is highly likely to fail this task due to context overload and attention decay, while a multi-agent system easily solves it by decomposing the work into 10 parallel subproblems, which are finally reconciled by a reducer.

---

## 🛠️ Repository Structure
This task complies fully with the official SwarmBench evaluation harness specifications:
```text
swarmbench-enterprise-assessment/
├── instruction.md          # Role-neutral task description provided to the agent
├── task.toml               # Meta-data, timeout limits, and resource configuration
├── decomposition.yaml      # fan-out-synthesize blueprint for multi-agent execution
├── gap_strategy.md         # Full gap analysis & reported Oracle validation score
├── environment/
│   ├── Dockerfile          # Task runtime environment
│   └── workspace/          # The starting codebase containing the 10 bugs
├── tests/
│   ├── test.sh             # Main verifier pipeline executor
│   └── verify.py           # Robust multi-file verifier with 0.1 partial scoring per bug
└── solution/
    ├── solve.sh            # Oracle solution execution path
    └── oracle/             # The fully repaired oracle files
```

---

## ⚡ How to Run & Verify Locally

### 1. Check Starting State (Broken - Score: 0.0)
To run the verifier against the starting codebase to confirm all 10 bugs are active:
```powershell
python tests/verify.py
```
*Expected Output:* Shows `FAIL` for all 10 checks with `TOTAL SCORE: 0.0` (exiting with code `1`).

### 2. Run the Oracle Fix (Fixed - Score: 1.0)
To simulate an agent successfully completing all 10 tasks:
```powershell
# Copy the oracle files into the workspace
Copy-Item -Path "solution\oracle\*" -Destination "environment\workspace\" -Recurse -Force

# Re-run the verifier
python tests/verify.py
```
*Expected Output:* Shows `PASS` for all 10 checks with `TOTAL SCORE: 1.0` (exiting with code `0`).

---

## 📊 Expected Performance Profile
* **Oracle Score**: `1.0`
* **Multi-Agent (Expected)**: `0.90` (Successfully decomposes and merges parallel fixes)
* **Single-Agent (Expected)**: `0.50` (Fails due to sequential context decay)
* **Target Structural Gap**: **`40.0%`**

---
*Created as part of the SwarmBench Candidate Assessment.*
