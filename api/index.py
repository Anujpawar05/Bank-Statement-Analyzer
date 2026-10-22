import sys
from pathlib import Path

# Add repository root to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from api.main import app

# Export app for Vercel serverless runtime
__all__ = ["app"]
