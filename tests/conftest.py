import os
import sys
from pathlib import Path

# Add project root to PYTHONPATH
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root) 