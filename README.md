# GTD-Stockhelper

GTD는 초보 투자자가 투자 근거를 기록하고, 보유 종목과 관심 종목의 시세·뉴스·재무 정보를 한 화면에서 확인하도록 돕는 Python 데스크톱 앱입니다.
현재 프로젝트는 개인용 프로토타입입니다. 표시되는 분석과 점수는 참고 자료이며 투자 권유나 수익 보장을 의미하지 않습니다.

## 주요 기능

- 로컬 회원가입 및 로그인
- 사용자별 투자 종목·관심 종목 관리
- 국내 및 미국 종목 검색과 자동완성
- 현재가, 전일 대비 등락률, 투자 수익률 표시
- 종목별·섹터별·국내외 투자 비중 차트
- PC의 로컬 시각 기준 최근 24시간 거시경제 뉴스
- 뉴스 원문 링크와 호재·악재·복합 분류 근거
- Gemini 3.1 Flash-Lite 기반 뉴스 설명과 투자 근거 점검
- 이번 주 주목 섹터와 국내 2개·미국 2개 대표 종목
- 종목 상세 차트, 재무 지표, 업종 평균 비교, 레이더 차트
- 회사 로고 자동 조회와 대체 로고
- 데스크톱·좁은 창에 대응하는 반응형 레이아웃과 양방향 스크롤

## 화면 구성

### 대시보드

투자 상태, 시장 요약, 투자 비중, 투자 종목, 관심 종목, 최근 24시간 경제 뉴스, 주간 섹터를 보여줍니다.

### 나의 종목

종목을 검색해 투자 또는 관심 종목으로 추가합니다. 투자 종목은 매수가와 수량을 입력하며, 상세 화면에서 차트·재무 지표·뉴스·메모를 확인할 수 있습니다.

### 설정

Gemini API 키를 입력하고 저장·표시·연결 테스트·삭제할 수 있습니다. 현재 사용하는 모델은 `gemini-3.1-flash-lite`입니다.

## 실행 환경

- Python 3.10 이상
- Windows 권장
- 인터넷 연결
- Gemini 기능 사용 시 Google AI Studio API 키

## 설치

저장소 루트에서 가상 환경을 만들고 필요한 패키지를 설치합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install customtkinter pandas requests pillow beautifulsoup4 matplotlib numpy yfinance google-genai
```

Windows용 Python을 python.org에서 설치했다면 `tkinter`는 일반적으로 함께 제공됩니다.

## 실행

```powershell
python main.py
```

처음 실행하면 `data` 폴더와 로컬 CSV 파일이 자동 생성됩니다. 회원가입 후 로그인하면 메인 화면이 열립니다.

## Gemini 설정

1. 앱의 왼쪽 사이드바에서 `설정`을 엽니다.
2. API 키를 입력하고 `저장`을 누릅니다.
3. `연결 테스트`로 키와 모델 접근 권한을 확인합니다.

모델 ID는 [config.py](config.py)의 `GEMINI_MODEL`에서 관리합니다. 현재 모델 정보는 [Google 공식 문서](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ko)에서 확인할 수 있습니다.

## 데이터 저장

앱 데이터는 저장소의 `data` 폴더에 로컬로 저장되며 `.gitignore`에 의해 Git에서 제외됩니다.

| 파일 | 내용 |
| --- | --- |
| `data/users.csv` | 로컬 사용자 계정 |
| `data/portfolios.csv` | 투자·관심 종목, 매수가, 수량, 메모 |
| `data/app_settings.json` | Gemini API 키 등 앱 설정 |

주의: 현재 사용자 비밀번호와 Gemini API 키는 로컬 파일에 암호화되지 않은 상태로 저장됩니다. 공용 PC에서는 사용하지 말고, 파일을 외부에 공유하거나 커밋하지 마세요.

## 외부 데이터 소스

| 용도 | 소스 |
| --- | --- |
| 국내 현재가·재무 정보 | 네이버 금융 웹 API |
| 미국 현재가·차트·재무 정보 | Yahoo Finance, `yfinance` |
| 종목 자동완성 | 네이버 주식 자동완성, Yahoo Finance 검색 제안 |
| 주요 뉴스 | 네이버 뉴스 검색 |
| 국내 종목 로고 | Toss Securities 이미지 CDN |
| 해외 종목 로고 | Google·DuckDuckGo favicon |
| AI 분석 | Google Gemini API |

일부 데이터 소스는 공개적으로 안정성이 보장된 공식 SDK가 아닌 웹 엔드포인트를 사용합니다. 제공처의 응답 형식이나 접근 정책이 바뀌면 일부 기능이 동작하지 않을 수 있습니다.

## 뉴스 처리 방식

1. 네이버 뉴스 검색을 최신순·최근 1일 조건으로 요청합니다.
2. 검색 결과에서 기사 제목, 원문 링크, 표시 시간을 추출합니다.
3. PC의 로컬 시각을 기준으로 24시간을 넘긴 결과를 제외합니다.
4. 대시보드에서는 금리·물가·환율·고용·GDP 등 거시경제 제목만 표시합니다.
5. 종목 상세 화면에서는 선택한 종목명·티커·대표 별칭이 제목에 포함된 기사만 표시합니다.
6. 제목의 긍정·부정 키워드로 호재·악재·복합을 1차 분류합니다.
7. 사용자가 분석 버튼을 누르면 Gemini가 초보자용 설명을 생성합니다.

뉴스 분류는 제목 중심의 보조 판단입니다. 기사 본문, 공시, 실적 수치를 함께 확인해야 합니다.

## AI 프롬프트

개발 기준과 런타임 프롬프트의 입력·출력 형식은 [prompts.txt](prompts.txt)에 정리되어 있습니다.

현재 프롬프트는 다음 작업을 담당합니다.

- 뉴스 호재·악재·복합 이유 설명
- 주간 주목 섹터와 대표 종목 JSON 생성
- 보유 종목 투자 근거 점검 및 점수화
- 관심 종목 분석 점검
- API 연결 테스트

## 프로젝트 구조

```text
GTD-Stockhelper/
├─ main.py              # UI, 데이터 조회, 차트, 뉴스, AI 흐름
├─ config.py            # 경로, 테마, Gemini 모델과 로컬 설정 저장
├─ prompts.txt          # 개발 기준과 Gemini 프롬프트 명세
├─ assets/
│  └─ gtd_logo.png      # 앱 로고
├─ data/                # 실행 시 생성되는 로컬 데이터, Git 제외
└─ README.md
```
