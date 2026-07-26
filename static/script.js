// 1. Image Slider
let currentSlide = 0;
const slides = document.querySelectorAll(".slide");

function showNextSlide() {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
}

if (slides.length > 0) {
    setInterval(showNextSlide, 3000);
}

// 2. Number Counter Animation
function animateCounter(counter) {
    const target = +counter.getAttribute("data-target");
    let current = 0;
    const increment = target / 60;

    function updateCounter() {
        current += increment;
        if (current < target) {
            counter.innerText = Math.ceil(current);
            requestAnimationFrame(updateCounter);
        } else {
            counter.innerText = target;
        }
    }
    updateCounter();
}

// 3. Fade-in on Scroll + trigger counters when visible
const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("visible");

            // If this fade-in box has counters inside, animate them
            const counters = entry.target.querySelectorAll(".counter");
            counters.forEach((counter) => {
                if (!counter.classList.contains("counted")) {
                    counter.classList.add("counted");
                    animateCounter(counter);
                }
            });

            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.3 });

document.querySelectorAll(".fade-in").forEach((el) => observer.observe(el));