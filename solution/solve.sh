#!/usr/bin/env bash
set -e

# Copy the oracle (perfect) implementation into the workspace for verification
cp -r /solution/oracle/* /workspace/

# Optionally, run the verifier to ensure reward 1.0 (not required here)
# python3 /tests/verify.py
