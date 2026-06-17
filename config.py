import os

# 프로젝트 루트 및 데이터 디렉토리 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 로컬 스토리지 Pandas 연동 파일 경로
USER_DB_PATH = os.path.join(DATA_DIR, "users.csv")
PORTFOLIO_DB_PATH = os.path.join(DATA_DIR, "portfolios.csv")

# 모던 UI 테마 정의
APPEARANCE_MODE = "light" # 밝은 토스 스타일 라이트 모드
THEME_COLOR = "blue"     # 포인트 블루 컬러

# 폰트 통합 설정
FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUBTITLE = ("Segoe UI", 16, "bold")
FONT_BODY = ("Segoe UI", 12)

# ── Gemini AI API 키 ──────────────────────────────────────────────────
# 환경 변수 GEMINI_API_KEY 또는 아래에 직접 입력하세요
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AQ.Ab8RN6LAek_3LWTnfJ1Ik7PzwiNMwa5OuKk1oO6LG3E5I4HDJg")