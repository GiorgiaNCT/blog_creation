import os
from configs.blog_details import blog_post
from configs.common_content import get_script, HEADER_HTML, get_related_post

def create_posts():
    current_dir = os.getcwd()
    print(current_dir)

    os.makedirs("posts", exist_ok=True)
    ## Sort newest → oldest
    #posts_sorted = sorted(posts, key=lambda p: p.date, reverse=True)


    for post in blog_post:
        html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post.title}</title>
    <link rel="stylesheet" href="../style_post.css">
    <link rel="icon" type="image/png" href="img/logo.png">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Dancing+Script:wght@600&display=swap" rel="stylesheet">
        """ 

        html_template = html_template + HEADER_HTML    

        html_template = html_template + f"""

    <main class="container">
        <a href="../index.html" class="back-button">
            ← Back to Blog
        </a>
        
        <section class="hero-section">
            <div class="post-meta">
                <span class="post-category">{post.category}</span>
                <span class="post-date">{post.date.strftime("%B %d, %Y")}</span>
            </div>
            <h1 class="post-title">{post.blog_title}</h1>
            <p class="post-subtitle">{post.blog_subtitle}</p>
            <p class="post-intro">{post.blog_intro}</p>
        </section>

        <div class="gallery-container">
            <div class="gallery-grid">
        """
        
        for image in post.blog_content:
            html_template = html_template + f"""
                <div class="gallery-item">
                    {image}
                </div>
            """


        html_template = html_template + f"""
            </div>
        </div>

        <!-- Footer Section -->
        <div class="footer-section">
            <div class="post-tags">
                <a href="#" class="tag">{post.tags[0]}</a>
            </div>

            <div class="share-section">
                <h3 class="share-title">Share This Story</h3>
                <div class="share-buttons">
                    <a href="#" class="share-btn facebook">FB</a>
                    <a href="#" class="share-btn twitter">TW</a>
                    <a href="#" class="share-btn pinterest">PI</a>
                    <a href="#" class="share-btn instagram">IG</a>
                </div>
            </div>
        </div>
    </main>

    """

        html_template = html_template + """
<!-- Lightbox -->
    <div class="lightbox" id="lightbox">
        <button class="lightbox-close" id="lightboxClose">&times;</button>
        <button class="lightbox-nav lightbox-prev" id="lightboxPrev">‹</button>
        <div class="lightbox-content">
            <img src="" alt="" id="lightboxImg">
        </div>
        <button class="lightbox-nav lightbox-next" id="lightboxNext">›</button>
    </div>

    <script>
        // Wait for DOM to be fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            // Lightbox functionality
            const lightbox = document.getElementById('lightbox');
            const lightboxImg = document.getElementById('lightboxImg');
            const lightboxClose = document.getElementById('lightboxClose');
            const lightboxPrev = document.getElementById('lightboxPrev');
            const lightboxNext = document.getElementById('lightboxNext');
            const galleryItems = document.querySelectorAll('.gallery-item img');
            
            let currentIndex = 0;
            const images = Array.from(galleryItems).map(img => ({
                src: img.src,
                alt: img.alt
            }));

            console.log('Gallery items found:', galleryItems.length);

            // Open lightbox
            galleryItems.forEach((img, index) => {
                img.addEventListener('click', function(e) {
                    console.log('Image clicked:', index);
                    currentIndex = index;
                    openLightbox();
                });
            });

            function openLightbox() {
                console.log('Opening lightbox for image:', currentIndex);
                lightboxImg.src = images[currentIndex].src;
                lightboxImg.alt = images[currentIndex].alt;
                lightbox.classList.add('active');
                document.body.style.overflow = 'hidden';
            }

            function closeLightbox() {
                console.log('Closing lightbox');
                lightbox.classList.remove('active');
                document.body.style.overflow = 'auto';
            }

            // Close lightbox
            lightboxClose.addEventListener('click', function(e) {
                e.stopPropagation();
                closeLightbox();
            });

            lightbox.addEventListener('click', function(e) {
                if (e.target === lightbox) {
                    closeLightbox();
                }
            });

            // Navigation
            lightboxPrev.addEventListener('click', function(e) {
                e.stopPropagation();
                currentIndex = (currentIndex - 1 + images.length) % images.length;
                lightboxImg.src = images[currentIndex].src;
                lightboxImg.alt = images[currentIndex].alt;
            });

            lightboxNext.addEventListener('click', function(e) {
                e.stopPropagation();
                currentIndex = (currentIndex + 1) % images.length;
                lightboxImg.src = images[currentIndex].src;
                lightboxImg.alt = images[currentIndex].alt;
            });

            // Keyboard navigation
            document.addEventListener('keydown', function(e) {
                if (!lightbox.classList.contains('active')) return;
                
                if (e.key === 'Escape') {
                    closeLightbox();
                } else if (e.key === 'ArrowLeft') {
                    lightboxPrev.click();
                } else if (e.key === 'ArrowRight') {
                    lightboxNext.click();
                }
            });
        });
    </script>
</body>
</html>
        """

        """
        SCRIPT_HTML = get_script('')

        html_template = html_template + SCRIPT_HTML
        """
        file_path = os.path.join(current_dir, 'posts', post.filename)

        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_template)

        print(f"Document written to: {file_path}")
        
