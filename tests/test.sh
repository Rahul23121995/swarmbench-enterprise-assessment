#!/usr/bin/env bash
set -e
# Run the verifier script
python3 /tests/verify.py 2>&1 | tee /logs/verifier/test-output.log || true
# Ensure reward file exists (fallback if verifier didn't write it)
if [ ! -f /logs/verifier/reward.txt ]; then
  echo 0 > /logs/verifier/reward.txt
fi
exit 0
