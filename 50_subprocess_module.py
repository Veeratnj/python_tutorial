"""
Subprocess Module

Example and comments for Subprocess Module.
"""

# Subprocess Module
import subprocess
print(subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True).stdout)
