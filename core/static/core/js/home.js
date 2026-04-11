/* ── AUTO-SLIDING EVENT STRIP ── */
/* Now uses CSS animation instead of JS */


document.addEventListener('DOMContentLoaded', function() {
    const track = document.getElementById('track');
    const prevBtn = document.getElementById('prev');
    const nextBtn = document.getElementById('next');
    const trackWrap = document.getElementById('trackWrap');

    if (!track || !prevBtn || !nextBtn || !trackWrap) {
        console.log('Slider elements not found');
        return;
    }

    const cardWidth = 254; // card width (240px) + gap (14px)
    let currentPosition = 0;
    let isDragging = false;
    let startX = 0;
    let startPosition = 0;

    function updateButtons() {
        const maxPosition = Math.max(0, track.scrollWidth - trackWrap.clientWidth);
        prevBtn.disabled = currentPosition <= 0;
        nextBtn.disabled = currentPosition >= maxPosition - 10;
    }

    function moveToPosition(position) {
        const maxPosition = Math.max(0, track.scrollWidth - trackWrap.clientWidth);
        currentPosition = Math.max(0, Math.min(position, maxPosition));
        track.style.transform = `translateX(-${currentPosition}px)`;
        updateButtons();
    }

    function slideNext() {
        moveToPosition(currentPosition + cardWidth);
    }

    function slidePrev() {
        moveToPosition(currentPosition - cardWidth);
    }

    let autoSlideInterval;

    function startAutoSlide() {
        autoSlideInterval = setInterval(() => {
            const maxPosition = Math.max(0, track.scrollWidth - trackWrap.clientWidth);
            if (currentPosition >= maxPosition - 10) {
                // Reset to beginning when reaching the end
                moveToPosition(0);
            } else {
                slideNext();
            }
        }, 3000); // Auto slide every 3 seconds
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    // Button event listeners
    prevBtn.addEventListener('click', () => {
        stopAutoSlide();
        slidePrev();
        startAutoSlide(); // Restart auto-slide after manual interaction
    });

    nextBtn.addEventListener('click', () => {
        stopAutoSlide();
        slideNext();
        startAutoSlide(); // Restart auto-slide after manual interaction
    });

    // Drag functionality
    function startDrag(e) {
        isDragging = true;
        stopAutoSlide();
        startX = e.pageX || e.touches[0].pageX;
        startPosition = currentPosition;
        trackWrap.style.cursor = 'grabbing';
        trackWrap.style.userSelect = 'none';
    }

    function drag(e) {
        if (!isDragging) return;
        e.preventDefault();
        const currentX = e.pageX || e.touches[0].pageX;
        const diff = startX - currentX;
        moveToPosition(startPosition + diff);
    }

    function endDrag() {
        isDragging = false;
        trackWrap.style.cursor = 'grab';
        trackWrap.style.userSelect = '';
        startAutoSlide();
    }

    // Mouse events
    trackWrap.addEventListener('mousedown', startDrag);
    window.addEventListener('mousemove', drag);
    window.addEventListener('mouseup', endDrag);

    // Touch events
    trackWrap.addEventListener('touchstart', startDrag, { passive: false });
    window.addEventListener('touchmove', drag, { passive: false });
    window.addEventListener('touchend', endDrag);

    // Pause auto-slide on hover
    trackWrap.addEventListener('mouseenter', stopAutoSlide);
    trackWrap.addEventListener('mouseleave', startAutoSlide);

    // Initialize
    updateButtons();
    startAutoSlide();

    // Handle window resize
    window.addEventListener('resize', function() {
        const maxPosition = Math.max(0, track.scrollWidth - trackWrap.clientWidth);
        if (currentPosition > maxPosition) {
            moveToPosition(maxPosition);
        }
        updateButtons();
    });

    console.log('Featured Events auto-sliding carousel initialized successfully');
});