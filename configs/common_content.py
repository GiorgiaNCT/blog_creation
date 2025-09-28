from configs.blog_details import blog_post

HEADER_HTML = """
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <a href="../index.html" class="logo">Giorgia - photography blog</a>
                <nav>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../index.html#Photos">Photography</a></li>
                        <li><a href="../index.html#Creations">Creations</a></li>
                    </ul>
                </nav>
                <button class="sidebar-toggle" aria-label="Toggle sidebar">☰</button>
            </div>
        </div>
    </header>
"""

def get_script(additional_script: str): 

    SCRIPT_HTML = """
    <script>

        // Sidebar toggle for small screens
        const sidebarToggle = document.querySelector('.sidebar-toggle');
        const sidebar = document.querySelector('.sidebar');
        const sidebarClose = document.querySelector('.sidebar-close');
        if (sidebarToggle) {
            sidebarToggle.addEventListener('click', () => {
                sidebar.classList.toggle('open');
            });
        }
        if (sidebarClose) {
            sidebarClose.addEventListener('click', () => {
                sidebar.classList.remove('open');
            });
        }

        // Smooth scrolling for navigation links
        document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
        
        // Smooth scrolling for navigation links
        document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Search functionality
        const searchBox = document.querySelector('.search-box');
        const posts = document.querySelectorAll('.post');

        searchBox.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase();
            
            posts.forEach(post => {
                const title = post.querySelector('.post-title').textContent.toLowerCase();
                const excerpt = post.querySelector('.post-excerpt').textContent.toLowerCase();
                const category = post.querySelector('.post-category').textContent.toLowerCase();
                
                if (title.includes(searchTerm) || excerpt.includes(searchTerm) || category.includes(searchTerm)) {
                    post.style.display = 'block';
                    post.style.animation = 'fadeInUp 0.5s ease-out';
                } else {
                    post.style.display = searchTerm ? 'none' : 'block';
                }
            });
        });

        // Newsletter subscription
        const newsletterBtn = document.querySelector('.newsletter-btn');
        const newsletterInput = document.querySelector('.newsletter-input');

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

        // Image hover effects
        document.querySelectorAll('.post-image').forEach(img => {
            img.addEventListener('click', function() {
                // Simple lightbox effect
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

        // Scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe all posts
        posts.forEach(post => {
            post.style.opacity = '0';
            post.style.transform = 'translateY(30px)';
            post.style.transition = 'all 0.8s ease-out';
            observer.observe(post);
        });

        // Filter functionality for both header and sidebar navigation
        function setupFilterLinks(selector) {
            const filterLinks = document.querySelectorAll(selector);

            filterLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    const filter = link.getAttribute('data-filter');
        
                    posts.forEach(post => {
                        const category = post.getAttribute('data-category');

                        if (filter === "all" || category === filter) {
                            post.style.display = 'block';
                            post.style.animation = 'fadeInUp 0.5s ease-out';
                        } else {
                            post.style.display = 'none';
                        }
                    });

                    // Close sidebar after selection on mobile
                    if (window.innerWidth <= 768) {
                        sidebar.classList.remove('open');
                    }

                    // Update active states for both header and sidebar
                    document.querySelectorAll('.filter-link, .sidebar-filter-link').forEach(l => {
                        l.classList.remove('active');
                    });
                    
                    // Find corresponding links in both menus and mark as active
                    document.querySelectorAll(`[data-filter="${filter}"]`).forEach(correspondingLink => {
                        correspondingLink.classList.add('active');
                    });
                });
            });
        }

        // Setup filter links for both header and sidebar
        setupFilterLinks('.filter-link');
        setupFilterLinks('.sidebar-filter-link');
    """

    SCRIPT_HTML = SCRIPT_HTML + additional_script +  """  
    </script>
</body>
</html>
    """
    return SCRIPT_HTML



def get_related_post():

    SIDEBAR_HTML_COMMON = """

            <aside class="sidebar">
                <button class="sidebar-close" aria-label="Close sidebar">&times;</button>

                <!-- Navigation Menu (Mobile Only) -->
                <div class="sidebar-section mobile-nav-section">
                    <h3 class="sidebar-title">Menu</h3>
                    <nav class="sidebar-nav">
                        <a href="../index.html" class="sidebar-filter-link" >Home</a>
                        <a href="../index.html#Photos" class="sidebar-filter-link" >Photography</a>
                        <a href="../index.html#Creations" class="sidebar-filter-link" >Creations</a>
                    </nav>
                </div>
                
                <!-- Search -->
                <div class="sidebar-section">
                    <h3 class="sidebar-title">Search</h3>
                    <input type="text" placeholder="Search photos..." class="search-box">
                </div>

                <!-- About -->
                <div class="sidebar-section">
                    <h3 class="sidebar-title">About</h3>
                    <p class="about-text">
                        I’m Giorgia, a creator at heart with a love for exploring different forms of expression. From photography to knitting, painting, and ceramics.
                    </p>
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
    """

    for i in range(3):

        post = blog_post[i]
        related_post_template = f"""
            <a href="posts/{post.filename}" class="related-post">
                <img src="{post.main_photo}" alt="Mountain sunset">
                <div class="related-post-content">
                    <div class="related-post-title">{post.title}</div>
                    <div class="related-post-date">{post.date.strftime("%B %d, %Y")}</div>
                </div>
            </a>
        """

        SIDEBAR_HTML_COMMON = SIDEBAR_HTML_COMMON + related_post_template

    return SIDEBAR_HTML_COMMON