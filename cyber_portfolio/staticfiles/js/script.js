document.addEventListener("DOMContentLoaded", function() {
    
    // --- 1. Dark Mode Logic ---
    const toggleSwitch = document.querySelector('.theme-toggle');
    const currentTheme = localStorage.getItem('theme');

    // Check for saved user preference
    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
        if(currentTheme === 'dark'){
            toggleSwitch.classList.remove('bi-sun-fill');
            toggleSwitch.classList.add('bi-moon-fill');
        }
    }

    function switchTheme(e) {
        if (e.target.classList.contains('bi-sun-fill')) {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            e.target.classList.replace('bi-sun-fill', 'bi-moon-fill');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
            e.target.classList.replace('bi-moon-fill', 'bi-sun-fill');
        }
    }

    toggleSwitch.addEventListener('click', switchTheme);


    // --- 2. Scroll Animations (Intersection Observer) ---
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    });

    const hiddenElements = document.querySelectorAll('.fade-in-up');
    hiddenElements.forEach((el) => observer.observe(el));


    // --- 3. Navbar Scroll Effect ---
    window.addEventListener('scroll', () => {
        const nav = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            nav.classList.add('shadow-sm');
        } else {
            nav.classList.remove('shadow-sm');
        }
    });
});