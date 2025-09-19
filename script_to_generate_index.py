import os
from configs.blog_details import blog_post

start_html_index = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giorgia Photo Blog</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Dancing+Script:wght@600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            color: #2c2c2c;
            background-color: #fefefe;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Header */
        header {
            padding: 40px 0;
            border-bottom: 1px solid #f0f0f0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .logo {
            font-family: 'Dancing Script', cursive;
            font-size: 2.5rem;
            font-weight: 600;
            color: #2c2c2c;
            text-decoration: none;
            transition: all 0.3s ease;
        }
        
        .logo:hover {
            color: #d4914a;
            transform: translateY(-2px);
        }
        
        nav ul {
            display: flex;
            list-style: none;
            gap: 40px;
        }
        
        nav a {
            text-decoration: none;
            color: #2c2c2c;
            font-weight: 500;
            text-transform: uppercase;
            font-size: 0.85rem;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            position: relative;
        }
        
        nav a:hover {
            color: #d4914a;
        }
        
        nav a::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -5px;
            left: 50%;
            background: #d4914a;
            transition: all 0.3s ease;
        }
        
        nav a:hover::after {
            width: 100%;
            left: 0;
        }
        
        /* Main Layout */
        .main-layout {
            display: grid;
            grid-template-columns: 1fr 300px;
            gap: 60px;
            padding: 60px 0;
        }
        
        /* Blog Posts */
        .blog-posts {
            display: flex;
            flex-direction: column;
            gap: 80px;
        }
        
        .post {
            animation: fadeInUp 0.8s ease-out;
        }
        
        .post-header {
            margin-bottom: 20px;
        }
        
        .post-meta {
            display: flex;
            gap: 15px;
            margin-bottom: 15px;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 500;
        }
        
        .post-category {
            color: #d4914a;
        }
        
        .post-date {
            color: #888;
        }
        
        .post-title {
            font-family: 'Playfair Display', serif;
            font-size: 2.2rem;
            font-weight: 600;
            color: #2c2c2c;
            line-height: 1.3;
            margin-bottom: 20px;
            transition: color 0.3s ease;
        }
        
        .post-title:hover {
            color: #d4914a;
            cursor: pointer;
        }
        
        .post-image {
            width: 100%;
            height: 500px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 30px;
            transition: all 0.5s ease;
            cursor: pointer;
        }
        
        .post-image:hover {
            transform: scale(1.02);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        }
        
        .post-excerpt {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 30px;
        }
        
        .continue-reading {
            display: inline-block;
            padding: 12px 30px;
            background: #f8f8f8;
            color: #2c2c2c;
            text-decoration: none;
            border-radius: 30px;
            font-weight: 500;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .continue-reading:hover {
            background: #d4914a;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(212, 145, 74, 0.3);
        }
        
        .post-divider {
            height: 1px;
            background: linear-gradient(to right, transparent, #e0e0e0, transparent);
            margin: 40px 0;
        }
        
        /* Sidebar */
        .sidebar {
            position: sticky;
            top: 140px;
            height: fit-content;
        }
        
        .sidebar-section {
            background: #fdfdfd;
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            border: 1px solid #f5f5f5;
            transition: all 0.3s ease;
        }
        
        .sidebar-section:hover {
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            transform: translateY(-2px);
        }
        
        .sidebar-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 20px;
            color: #2c2c2c;
        }
        
        .search-box {
            width: 100%;
            padding: 15px 20px;
            border: 2px solid #f0f0f0;
            border-radius: 30px;
            font-size: 1rem;
            transition: all 0.3s ease;
            background: white;
        }
        
        .search-box:focus {
            outline: none;
            border-color: #d4914a;
            box-shadow: 0 0 0 3px rgba(212, 145, 74, 0.1);
        }
        
        .about-text {
            font-size: 0.95rem;
            line-height: 1.7;
            color: #666;
            margin-bottom: 20px;
        }
        
        .social-links {
            display: flex;
            gap: 15px;
        }
        
        .social-link {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: #f8f8f8;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            color: #666;
            font-weight: 600;
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }
        
        .social-link:hover {
            background: #d4914a;
            color: white;
            transform: translateY(-3px);
        }
        
        .related-posts {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        
        .related-post {
            display: flex;
            gap: 15px;
            text-decoration: none;
            color: inherit;
            padding: 10px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        
        .related-post:hover {
            background: #f8f8f8;
        }
        
        .related-post img {
            width: 60px;
            height: 60px;
            object-fit: cover;
            border-radius: 6px;
        }
        
        .related-post-content {
            flex: 1;
        }
        
        .related-post-title {
            font-size: 0.9rem;
            font-weight: 500;
            margin-bottom: 5px;
            line-height: 1.3;
        }
        
        .related-post-date {
            font-size: 0.75rem;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        /* Newsletter */
        .newsletter-input {
            width: 100%;
            padding: 15px 20px;
            border: 2px solid #f0f0f0;
            border-radius: 30px;
            font-size: 1rem;
            margin-bottom: 15px;
            background: white;
            transition: all 0.3s ease;
        }
        
        .newsletter-input:focus {
            outline: none;
            border-color: #d4914a;
            box-shadow: 0 0 0 3px rgba(212, 145, 74, 0.1);
        }
        
        .newsletter-btn {
            width: 100%;
            padding: 15px;
            background: #2c2c2c;
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .newsletter-btn:hover {
            background: #d4914a;
            transform: translateY(-2px);
        }
        
        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .main-layout {
                grid-template-columns: 1fr;
                gap: 40px;
            }
            
            .header-content {
                flex-direction: column;
                gap: 20px;
            }
            
            nav ul {
                gap: 20px;
            }
            
            .post-title {
                font-size: 1.8rem;
            }
            
            .post-image {
                height: 300px;
            }
            
            .sidebar {
                position: relative;
                top: auto;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <a href="#" class="logo">Giorgia - photography blog</a>
                <nav>
                    <ul>
                        <li><a href="#">Photo</a></li>
                        <li><a href="#">Travel</a></li>
                        <li><a href="#">Creations</a></li>
                        <li><a href="#">About</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <main class="container">
        <div class="main-layout">
            <div class="blog-posts">
"""

middle_html_file = """
            </div>

            <aside class="sidebar">
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
                    <div class="social-links">
                        <a href="#" class="social-link">IG</a>
                        <a href="#" class="social-link">FB</a>
                        <a href="#" class="social-link">TW</a>
                        <a href="#" class="social-link">YT</a>
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
"""

end_html_file = """
                    </div>
                </div>
            </aside>
        </div>
    </main>

    <script>
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
    </script>
</body>
</html>
"""

total_post = start_html_index

for post in blog_post:

    post_template = f"""
                <article class="post">
                    <div class="post-header">
                        <div class="post-meta">
                            <span class="post-category">Photography</span>
                            <span class="post-date">{post.date.strftime("%B %d, %Y")}</span>
                        </div>
                        <h2 class="post-title">{post.title}</h2>
                    </div>
                    {post.preview}
                    <a href="posts/{post.filename}" class="continue-reading">Continue Reading</a>
                    <div class="post-divider"></div>
                </article>

    """

    total_post = total_post + post_template


total_post = total_post + middle_html_file

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
total_post = total_post + end_html_file

current_dir = os.getcwd()
print(current_dir)
file_path = os.path.join(current_dir, 'index.html')

# Write to file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(total_post)

print(f"Document written to: {file_path}")