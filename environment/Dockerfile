FROM python:3.11-slim

# Set a non-root user for safety (optional)
RUN useradd -m appuser
USER appuser

WORKDIR /workspace

# Copy the workspace code and requirements
COPY workspace/ /workspace/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the /logs/ directory exists for verifier output
RUN mkdir -p /logs/verifier

# Default command (will be overridden by Harbor)
CMD ["bash"]
