import os
import json

# 프로젝트 루트 및 데이터 디렉토리 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 로컬 스토리지 Pandas 연동 파일 경로
USER_DB_PATH = os.path.join(DATA_DIR, "users.csv")
PORTFOLIO_DB_PATH = os.path.join(DATA_DIR, "portfolios.csv")
APP_SETTINGS_PATH = os.path.join(DATA_DIR, "app_settings.json")

# 모던 UI 테마 정의
APPEARANCE_MODE = "light" # 밝은 토스 스타일 라이트 모드
THEME_COLOR = "blue"     # 포인트 블루 컬러

# 폰트 통합 설정
FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUBTITLE = ("Segoe UI", 16, "bold")
FONT_BODY = ("Segoe UI", 12)

def load_app_settings():
    if not os.path.exists(APP_SETTINGS_PATH):
        return {}
    try:
        with open(APP_SETTINGS_PATH, "r", encoding="utf-8") as settings_file:
            data = json.load(settings_file)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError, TypeError):
        return {}


def save_app_settings(settings):
    os.makedirs(DATA_DIR, exist_ok=True)
    temp_path = APP_SETTINGS_PATH + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as settings_file:
        json.dump(settings, settings_file, ensure_ascii=False, indent=2)
    os.replace(temp_path, APP_SETTINGS_PATH)


def get_gemini_api_key():
    return str(load_app_settings().get("gemini_api_key", "")).strip()


def save_gemini_api_key(api_key):
    settings = load_app_settings()
    cleaned_key = str(api_key or "").strip()
    if cleaned_key:
        settings["gemini_api_key"] = cleaned_key
    else:
        settings.pop("gemini_api_key", None)
    save_app_settings(settings)
