import os

# 프로젝트 루트 및 데이터 디렉토리 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 로컬 스토리지 Pandas 연동 파일 경로
USER_DB_PATH = os.path.join(DATA_DIR, "users.csv")
PORTFOLIO_DB_PATH = os.path.join(DATA_DIR, "portfolios.csv")

# 모던 UI 테마 정의
APPEARANCE_MODE = "dark" # 어두운 다크 모드 스타일
THEME_COLOR = "blue"     # 버튼 등 포인트 컬러

# 폰트 통합 설정
FONT_TITLE = ("Pretendard", 24, "bold")
FONT_SUBTITLE = ("Pretendard", 16, "bold")
FONT_BODY = ("Pretendard", 12)