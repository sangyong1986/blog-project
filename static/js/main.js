// ===========================
// 패피슈슈 블로그 - main.js
// ===========================

// 사이드바 섹션 토글
function toggleSection(btn) {
    const card = btn.closest('.sidebar-card');
    const list = card.querySelector('.category-list, .activity-info');
    if (!list) return;

    const isHidden = list.style.display === 'none';
    list.style.display = isHidden ? '' : 'none';
    btn.textContent = isHidden ? '▲' : '▼';
}

// 목록 보기 토글 (컴팩트 ↔ 기본)
let isCompact = false;
function toggleListView() {
    isCompact = !isCompact;
    const container = document.getElementById('postsContainer');
    const btn = document.querySelector('.list-toggle-btn');
    if (!container) return;

    if (isCompact) {
        container.classList.add('compact-view');
        btn.textContent = '목록닫기';
    } else {
        container.classList.remove('compact-view');
        btn.textContent = '목록열기';
    }
}

// URL 복사
document.addEventListener('click', function(e) {
    if (e.target.classList.contains('action-btn') &&
        e.target.textContent.trim() === 'URL 복사') {
        navigator.clipboard.writeText(window.location.href)
            .then(() => showToast('URL이 복사되었습니다 🔗'))
            .catch(() => showToast('복사에 실패했습니다'));
    }
});

// 토스트 메시지
function showToast(message) {
    const existing = document.querySelector('.toast-msg');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = 'toast-msg';
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed;
        bottom: 32px;
        left: 50%;
        transform: translateX(-50%);
        background: #3A3040;
        color: white;
        padding: 10px 22px;
        border-radius: 24px;
        font-size: 13px;
        z-index: 9999;
        animation: fadeInUp 0.25s ease;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    `;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2500);
}

// 컴팩트 뷰 CSS 동적 주입
const compactStyle = document.createElement('style');
compactStyle.textContent = `
    .compact-view .post-card {
        display: grid;
        grid-template-columns: 200px 1fr;
    }
    .compact-view .post-screenshot {
        min-height: unset;
    }
    .compact-view .ss-title {
        font-size: 14px;
        -webkit-line-clamp: 2;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .compact-view .screenshot-emoji {
        display: none;
    }
    @media (max-width: 600px) {
        .compact-view .post-card {
            grid-template-columns: 1fr;
        }
    }
`;
document.head.appendChild(compactStyle);

// 페이지 로드 완료
document.addEventListener('DOMContentLoaded', () => {
    console.log('🎀 패피슈슈 블로그 로드 완료!');
});
