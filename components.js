// components.js - Shared HTML components

// Site configuration - Edit this to update across all pages
const siteConfig = {
    siteName: "Giorgia - photography blog",
    author: {
        name: "Giorgia",
        bio: "I’m Giorgia, a creator at heart with a love for exploring different forms of expression. From photography to knitting, painting, and ceramics.",
        social: {
            instagram: "#",
            facebook: "#", 
            twitter: "#",
            youtube: "#"
        }
    },
    navigation: [
        { name: "Home", href: "index.html" },
        { name: "Photo", href: "#" },
        { name: "Travel", href: "#" },
        { name: "Creations", href: "#" },
        { name: "About", href: "#" }
    ],
    relatedPosts: [
        {
            title: "Chasing Light in Patagonia",
            date: "Nov 28, 2024",
            image: "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=60&h=60&fit=crop&auto=format",
            href: "#"
        },
        {
            title: "Urban Nights in Seoul", 
            date: "Nov 25, 2024",
            image: "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=60&h=60&fit=crop&auto=format",
            href: "#"
        },
        {
            title: "Ocean Moods in Iceland",
            date: "Nov 22, 2024", 
            image: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=60&h=60&fit=crop&auto=format",
            href: "#"
        }
    ]
};

// Generate Header HTML
function generateHeader() {
    const navItems = siteConfig.navigation.map(item => 
        `<li><a href="${item.href}">${item.name}</a></li>`
    ).join('');

    return `
        <div class="container">
            <div class="header-content">
                <a href="index.html" class="logo">${siteConfig.siteName}</a>
                <nav>
                    <ul>
                        ${navItems}
                    </ul>
                </nav>
            </div>
        </div>
    `;
}

// Generate Sidebar HTML
function generateSidebar() {
    const relatedPostsHtml = siteConfig.relatedPosts.map(post => `
        <a href="${post.href}" class="related-post">
            <img src="${post.image}" alt="${post.title}">
            <div class="related-post-content">
                <div class="related-post-title">${post.title}</div>
                <div class="related-post-date">${post.date}</div>
            </div>
        </a>
    `).join('');

    return `
        <!-- Search -->
        <div class="sidebar-section">
            <h3 class="sidebar-title">Search</h3>
            <input type="text" placeholder="Search photos..." class="search-box">
        </div>

        <!-- About -->
        <div class="sidebar-section">
            <h3 class="sidebar-title">About</h3>
            <p class="about-text">
                ${siteConfig.author.bio}
            </p>
            <div class="social-links">
                <a href="${siteConfig.author.social.instagram}" class="social-link">IG</a>
                <a href="${siteConfig.author.social.facebook}" class="social-link">FB</a>
                <a href="${siteConfig.author.social.twitter}" class="social-link">TW</a>
                <a href="${siteConfig.author.social.youtube}" class="social-link">YT</a>
            </div>
        </div>

        <!-- Newsletter -->
        <div class="sidebar-section">
            <h3 class="sidebar-title">Newsletter</h3>
            <p class="about-text" style="font-size: 0.9rem; margin-bottom: 20px;">
                Get weekly photo stories and tips delivered to your inbox.
            </p>
            <input type="email" placeholder="Your email..." class="newsletter-input">
            <button class="newsletter-btn">Subscribe</button>
        </div>

        <!-- Related Posts -->
        <div class="sidebar-section">
            <h3 class="sidebar-title">You Might Also Like</h3>
            <div class="related-posts">
                ${relatedPostsHtml}
            </div>
        </div>
    `;
}

// Initialize shared components when page loads
function initializeSharedComponents() {
    // Insert header
    const headerElement = document.querySelector('header');
    if (headerElement) {
        headerElement.innerHTML = generateHeader();
    }

    // Insert sidebar
    const sidebarElement = document.querySelector('.sidebar');
    if (sidebarElement) {
        sidebarElement.innerHTML = generateSidebar();
    }

    // Initialize shared functionality
    initializeSearch();
    initializeNewsletter();
    initializeLightbox();
}

// Search functionality
function initializeSearch() {
    const searchBox = document.querySelector('.search-box');
    const posts = document.querySelectorAll('.post');

    if (searchBox && posts.length > 0) {
        searchBox.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            
            posts.forEach(post => {
                const title = post.querySelector('.post-title')?.textContent.toLowerCase() || '';
                const excerpt = post.querySelector('.post-excerpt')?.textContent.toLowerCase() || '';
                const category = post.querySelector('.post-category')?.textContent.toLowerCase() || '';
                
                if (title.includes(searchTerm) || excerpt.includes(searchTerm) || category.includes(searchTerm)) {
                    post.style.display = 'block';
                    post.style.animation = 'fadeInUp 0.5s ease-out';
                } else {
                    post.style.display = searchTerm ? 'none' : 'block';
                }
            });
        });
    }
}

// Newsletter functionality
function initializeNewsletter() {
    const newsletterBtn = document.querySelector('.newsletter-btn');
    const newsletterInput = document.querySelector('.newsletter-input');

    if (newsletterBtn && newsletterInput) {
        newsletterBtn.addEventListener('click', function() {
            const email = newsletterInput.value.trim();
            if (email && email.includes('@')) {
                newsletterBtn.textContent = 'Subscribed!';
                newsletterBtn.style.background = '#4CAF50';
                newsletterInput.value = '';
                
                setTimeout(() => {
                    newsletterBtn.textContent = 'Subscribe';
                    newsletterBtn.style.background = '#2c2c2c';
                }, 2000);
            } else {
                newsletterInput.style.borderColor = '#e74c3c';
                setTimeout(() => {
                    newsletterInput.style.borderColor = '#f0f0f0';
                }, 1000);
            }
        });
    }
}

// Lightbox functionality
function initializeLightbox() {
    document.querySelectorAll('.post-image, .featured-image, .gallery-image').forEach(img => {
        img.addEventListener('click', function() {
            const lightbox = document.createElement('div');
            lightbox.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.9);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 1000;
                cursor: pointer;
            `;
            
            const lightboxImg = document.createElement('img');
            lightboxImg.src = this.src;
            lightboxImg.style.cssText = `
                max-width: 90%;
                max-height: 90%;
                object-fit: contain;
                border-radius: 8px;
            `;
            
            lightbox.appendChild(lightboxImg);
            document.body.appendChild(lightbox);
            
            lightbox.addEventListener('click', () => {
                document.body.removeChild(lightbox);
            });
        });
    });
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeSharedComponents);