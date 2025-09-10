// Custom cursor
const cursor = document.querySelector('.cursor');
const hoverElements = document.querySelectorAll('a, img, .entry-image');

document.addEventListener('mousemove', (e) => {
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
});

hoverElements.forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
});

// Navigation scroll effect
const nav = document.querySelector('.nav');
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Scroll animations for entries
const entries = document.querySelectorAll('.entry');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, { threshold: 0.1 });

entries.forEach(entry => {
    observer.observe(entry);
});

// Parallax gallery mouse effect
const parallaxGallery = document.querySelector('.parallax-gallery');
const parallaxImages = document.querySelector('.parallax-images');

parallaxGallery.addEventListener('mousemove', (e) => {
    const rect = parallaxGallery.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const centerX = rect.width / 2;
    const moveX = (x - centerX) * 0.02;

    parallaxImages.style.transform = `translateX(${moveX}px)`;
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Image lazy loading effect
const images = document.querySelectorAll('img');
const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.style.transform = 'scale(0.9)';
            setTimeout(() => {
                img.style.transition = 'all 0.8s ease';
                img.style.transform = 'scale(1)';
            }, 100);
            imageObserver.unobserve(img);
        }
    });
});

images.forEach(img => {
    imageObserver.observe(img);
});

// Parallax scrolling effect for hero image
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const heroImage = document.querySelector('.hero-image');
    const parallaxSpeed = scrolled * 0.5;
    heroImage.style.transform = `translateY(${parallaxSpeed}px) scale(1.1)`;
});