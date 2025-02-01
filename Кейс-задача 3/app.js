let slideIndex = 0;

function showSlides() {
    const slides = document.querySelectorAll('.slide');
    slides.forEach((slide, index) => {
        slide.style.display = index === slideIndex ? 'block' : 'none';
    });

    const slideNumberDisplay = document.getElementById('slide-number');
    slideNumberDisplay.textContent = `${slideIndex + 1} / ${slides.length}`;
}

function changeSlide(n) {
    const slides = document.querySelectorAll('.slide');
    slideIndex += n;

    if (slideIndex >= slides.length) {
        slideIndex = 0;
    } 
    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }
    showSlides();
}

showSlides();