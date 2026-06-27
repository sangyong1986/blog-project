# 🎀 패피슈슈 블로그

파스텔톤 디자인 + 캡쳐 이미지 느낌의 네이버 블로그 스타일 웹사이트

## 📁 프로젝트 구조

```
blog-project/
├── app.py                  # Flask 메인 앱
├── requirements.txt        # 파이썬 패키지
├── vercel.json             # Vercel 배포 설정
├── .gitignore
├── templates/
│   ├── base.html           # 공통 레이아웃 (헤더 + 사이드바 + 푸터)
│   ├── index.html          # 포스트 목록 페이지
│   └── post.html           # 포스트 상세 페이지
└── static/
    ├── css/
    │   └── style.css       # 전체 스타일 (파스텔톤)
    └── js/
        └── main.js         # 인터랙션 스크립트
```

## 🚀 로컬 실행

```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. 실행
python app.py

# 3. 브라우저에서 열기
# http://localhost:5000
```

## ☁️ GitHub + Vercel 배포

### 1. GitHub 업로드
```bash
git init
git add .
git commit -m "첫 커밋: 패피슈슈 블로그"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### 2. Vercel 배포
1. [vercel.com](https://vercel.com) 접속 → GitHub 로그인
2. **New Project** → GitHub 저장소 선택
3. Framework Preset: **Other**
4. **Deploy** 클릭
5. 자동으로 URL 생성됨 ✅

## 🎨 디자인 특징

- **파스텔 핑크/라벤더/민트** 컬러 팔레트
- **캡쳐 이미지 느낌** - 브라우저 프레임(빨/노/초 닷)
- Gowun Dodum + Noto Sans KR 폰트 조합
- 사이드바: 카테고리, 프로필, 활동정보
- 반응형 (모바일 대응)
- 목록/컴팩트 뷰 토글

## 📝 포스트 추가 방법

`app.py`의 `POSTS` 리스트에 추가:
```python
{
    "id": 6,
    "category": "방송v패션v맛집v제품",
    "title": "새 포스트 제목",
    "author": "패피슈슈",
    "time": "방금 전",
    "tags": ["#태그1", "#태그2"],
    "description": "포스트 설명",
    "image": "sunglasses",  # sunglasses / cafe / beauty / fashion / padding
    "views": 0,
    "scraps": 0
}
```
