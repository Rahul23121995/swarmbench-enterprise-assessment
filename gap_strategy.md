# Gap Strategy

## Why Single-Agent Should Struggle
- Number of artifacts: 10 target files spread across 7 directories
- Estimated input size: ~15,000 tokens of file contents and instruction context
- Coverage pressure: High. The agent must successfully locate, modify, and test 10 completely independent modules (e.g. Python, Groovy, CSV formats) without missing secondary requirements.
- Reconciliation pressure: High. The agent must apply non-adjacent changes across multiple files, maintain synchronization, and verify execution without letting changes in one module (like parallel log concurrency or browser teardown) interfere with others.
- Expected failure mode: Incomplete coverage (forgetting or skipping smaller files like the Jenkinsfile or CSV mapper), attention degradation (making copy-paste errors or syntax mistakes in later edits due to long context length), and running out of time/tokens under timeout limits.

## Why Multi-Agent Should Succeed
- Natural subproblems: 10 highly decoupled, independent defects, each isolated to a single file/responsibility.
- Sub-agent ownership plan: 10 parallel sub-agents are spawned, each dedicated to solving a single, well-defined defect in their own clean, isolated context.
- Reducer strategy: A final synthesis/reducer agent reconciles all the independent patches, resolves any merging or file collisions, runs the validation tests, and outputs a completely recovered QA framework.
- Why final synthesis is verifiable: The verifier provides deterministic, independent scoring checks (0.1 points per bug) with immediate diagnostic feedback, allowing the synthesizer to easily verify complete recovery.

## Expected Score Pattern
- Oracle expected score: 1.0
- Single-agent expected score: 0.50
- Multi-agent expected score: 0.90
- Target gap: 40.0%

## Oracle Validation
- Oracle run completed: yes
- Oracle reward: 1.0
- Notes: Fully verified utilizing the executable test harness, scoring exactly 1.0.
