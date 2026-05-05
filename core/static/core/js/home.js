/* ── AUTO-SLIDING EVENT STRIP ── */

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
                moveToPosition(0);
            } else {
                slideNext();
            }
        }, 3000);
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    // Button event listeners
    prevBtn.addEventListener('click', () => {
        stopAutoSlide();
        slidePrev();
        startAutoSlide();
    });

    nextBtn.addEventListener('click', () => {
        stopAutoSlide();
        slideNext();
        startAutoSlide();
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

    // Handle window resize
    window.addEventListener('resize', function() {
        const maxPosition = Math.max(0, track.scrollWidth - trackWrap.clientWidth);
        if (currentPosition > maxPosition) {
            moveToPosition(maxPosition);
        }
        updateButtons();
    });

    // Initialize
    updateButtons();
    startAutoSlide();

    console.log('Featured Events auto-sliding carousel initialized successfully');
});

/* ── ENERGY RADIO PLAYER ── */
document.addEventListener('DOMContentLoaded', function() {
    const playBtn = document.getElementById('radioPlayBtn');
    const pauseBtn = document.getElementById('radioPauseBtn');
    const radioPlayer = document.getElementById('radio-audio-player');

    if (!playBtn || !pauseBtn || !radioPlayer) {
        console.log('Radio player elements not found');
        return;
    }

    // Play button functionality
    playBtn.addEventListener('click', function(e) {
        e.preventDefault();
        radioPlayer.play().catch(error => {
            console.error('Error playing radio:', error);
        });
    });

    // Pause button functionality
    pauseBtn.addEventListener('click', function(e) {
        e.preventDefault();
        radioPlayer.pause();
    });

    // Update UI when audio starts playing
    radioPlayer.addEventListener('play', function() {
        playBtn.classList.add('hidden');
        pauseBtn.classList.remove('hidden');
    });

    // Update UI when audio pauses
    radioPlayer.addEventListener('pause', function() {
        pauseBtn.classList.add('hidden');
        playBtn.classList.remove('hidden');
    });

    // Handle errors
    radioPlayer.addEventListener('error', function() {
        console.error('Stream error occurred');
        pauseBtn.classList.add('hidden');
        playBtn.classList.remove('hidden');
    });

    // Volume control functionality
    const volumeSlider = document.getElementById('radioVolume');
    const muteBtn = document.getElementById('muteBtn');
    let previousVolume = 70;

    if (volumeSlider) {
        // Set initial volume (70% = 0.7)
        radioPlayer.volume = 0.7;

        // Update volume when slider changes
        volumeSlider.addEventListener('input', function() {
            radioPlayer.volume = this.value / 100;
            previousVolume = this.value;

            // Remove muted state when volume is adjusted
            if (this.value > 0 && muteBtn.classList.contains('muted')) {
                muteBtn.classList.remove('muted');
                muteBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
            }
        });

        console.log('Radio player volume control initialized');
    }

    // Mute button functionality
    if (muteBtn && radioPlayer && volumeSlider) {
        muteBtn.addEventListener('click', function() {
            if (muteBtn.classList.contains('muted')) {
                // Unmute
                muteBtn.classList.remove('muted');
                muteBtn.innerHTML = '<i class="fas fa-volume-up"></i>';
                radioPlayer.volume = previousVolume / 100;
                volumeSlider.value = previousVolume;
            } else {
                // Mute
                muteBtn.classList.add('muted');
                muteBtn.innerHTML = '<i class="fas fa-volume-mute"></i>';
                previousVolume = volumeSlider.value;
                radioPlayer.volume = 0;
                volumeSlider.value = 0;
            }
        });

        console.log('Radio player mute button initialized');
    }
});