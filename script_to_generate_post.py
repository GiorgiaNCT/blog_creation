import os
from configs.blog_details import blog_post
from configs.common_content import STYLE_HTML, SCRIPT_HTML, HEADER_HTML, get_related_post
title = 'titolo'
titolo_blog = 'PROVA'
test_blog_post = 'blablabla'
subtitle_post = 'sottotitolo'
tags_post = 'tags1'

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
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Dancing+Script:wght@600&display=swap" rel="stylesheet">
    """ 
    
    html_template = html_template + STYLE_HTML

    # Adjust image paths for posts directory
    adjusted_header = HEADER_HTML.replace('img/', '../img/')
    html_template = html_template + adjusted_header

    html_template = html_template + f"""

    <main class="container">
        <a href="../index.html" class="back-button">
            ← Back to Blog
        </a>
        
        <div class="post-layout">
            <article class="article-main">
                <div class="post-header">
                    <div class="post-meta">
                        <span class="post-category">{post.category}</span>
                        <span class="post-date">{post.date.strftime("%B %d, %Y")}</span>
                    </div>
                    <h1 class="post-title">{post.blog_title}</h1>
                    <p class="post-subtitle">{post.blog_subtitle}</p>
                </div>

                <div class="post-content">
                    {post.blog_content}
                </div>

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
            </article>
    """

    SIDEBAR_HTML_COMMON = get_related_post()
    html_template = html_template + SIDEBAR_HTML_COMMON

    html_template = html_template + """
                    </div>
                </div>
            </aside>
        </div>
    </main>

    """

    html_template = html_template + SCRIPT_HTML

    print(html_template)
    file_path = os.path.join(current_dir, 'posts', post.filename)

    # Write to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"Document written to: {file_path}")

