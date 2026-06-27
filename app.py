from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# 샘플 블로그 데이터
POSTS = [
    {
        "id": 1,
        "category": "방송v패션v맛집v제품",
        "title": "나혼산 코쿤 향수 박지현 선물 무엇 선글라스 모자 안경 시계 편집샵 옷가게 어디 맨투맨 티셔츠 니트 가디건 비니 바지 가방 백팩 발가락 양말 신발 운동화 653회 나혼자산다",
        "author": "패피슈슈",
        "time": "12시간 전",
        "tags": ["#코쿤향수", "#코쿤박지현향수", "#코쿤향수선물"],
        "description": "쿠팡파트너스활동의 일환으로 일정액의 수수료를 제공받습니다. but, 구매자에게 수수료를 부과하지 않습니다",
        "image": "sunglasses",
        "views": 1240,
        "scraps": 42
    },
    {
        "id": 2,
        "category": "맛집여행지추천",
        "title": "서울 성수동 카페 맛집 추천 숨겨진 감성 카페 TOP 10 주말 데이트 코스",
        "author": "패피슈슈",
        "time": "1일 전",
        "tags": ["#성수동카페", "#서울카페", "#주말데이트"],
        "description": "성수동의 숨겨진 감성 카페들을 직접 방문하고 정리했습니다. 주말 데이트나 친구와의 나들이에 딱 좋은 곳들이에요!",
        "image": "cafe",
        "views": 3891,
        "scraps": 128
    },
    {
        "id": 3,
        "category": "제품리뷰",
        "title": "다이슨 에어랩 vs 드라이기 차이점 솔직 후기 헤어 스타일링 꿀팁",
        "author": "패피슈슈",
        "time": "3일 전",
        "tags": ["#다이슨에어랩", "#헤어스타일링", "#뷰티꿀팁"],
        "description": "1년 넘게 사용해본 다이슨 에어랩의 솔직한 후기를 공유합니다. 장단점 모두 담았어요.",
        "image": "beauty",
        "views": 5672,
        "scraps": 211
    },
    {
        "id": 4,
        "category": "방송v패션v맛집v제품",
        "title": "환승연애3 출연자 패션 어디서 샀나 의상 정보 브랜드 총정리",
        "author": "패피슈슈",
        "time": "5일 전",
        "tags": ["#환승연애3", "#패션정보", "#의상브랜드"],
        "description": "화제의 환승연애3 출연자들의 패션 아이템을 모두 찾아봤습니다!",
        "image": "fashion",
        "views": 8904,
        "scraps": 334
    },
    {
        "id": 5,
        "category": "제품소개",
        "title": "겨울 필수템 패딩 추천 2024 노스페이스 캐나다구스 비교 어떤게 나을까",
        "author": "패피슈슈",
        "time": "1주 전",
        "tags": ["#패딩추천", "#노스페이스", "#캐나다구스"],
        "description": "이번 겨울을 따뜻하게 날 수 있는 패딩 추천 가이드입니다.",
        "image": "padding",
        "views": 12034,
        "scraps": 445
    },
]

CATEGORIES = [
    {"name": "전체보기", "count": 5286},
    {"name": "방송v패션v맛집v제품", "count": 5286},
    {"name": "맛집여행지추천", "count": 18},
    {"name": "제품리뷰", "count": 0},
    {"name": "제품소개", "count": 0},
    {"name": "일상(요리)", "count": 0},
]

@app.route('/')
def index():
    category = request.args.get('category', '전체보기')
    if category == '전체보기':
        posts = POSTS
    else:
        posts = [p for p in POSTS if p['category'] == category]
    
    return render_template('index.html',
                           posts=posts,
                           categories=CATEGORIES,
                           active_category=category,
                           total=len(POSTS))

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((p for p in POSTS if p['id'] == post_id), None)
    if not post:
        return "Post not found", 404
    return render_template('post.html', post=post, categories=CATEGORIES)

@app.route('/api/posts')
def api_posts():
    return jsonify(POSTS)

if __name__ == '__main__':
    app.run(debug=True)
