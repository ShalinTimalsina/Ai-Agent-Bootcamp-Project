from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / 'data'
DATABASE_PATH = DATA_DIR / 'devops_academy.db'
DEFAULT_USER_ID = 1
CORS_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]
