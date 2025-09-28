import os
from configs.blog_details import blog_post
from configs.common_content import SCRIPT_HTML, get_related_post

start_html_index = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giorgia Photo Blog</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&family=Dancing+Script:wght@600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style_post.css">
    <link rel="icon" type="image/png" href="img/logo.png">
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <a href="index.html" class="logo">Giorgia - photography blog</a>
                <nav>
                    <ul>
                        <li><a href="#" class="filter-link" data-filter="all">Home</a></li>
                        <li><a href="#" class="filter-link" data-filter="Photos">Photos</a></li>
                        <li><a href="#" class="filter-link" data-filter="Creations">Creations</a></li>
                    </ul>
                </nav>
                <button class="sidebar-toggle" aria-label="Toggle sidebar">☰</button>
            </div>
        </div>
    </header>

    <main class="container">
        <div class="main-layout">
            <div class="blog-posts">
"""


total_post = start_html_index 

for post in blog_post:

    post_template = f"""
                <article class="post" data-category="{post.category}">
                    <div class="post-header">
                        <div class="post-meta">
                            <span class="post-category">Photography</span>
                            <span class="post-date">{post.date.strftime("%B %d, %Y")}</span>
                        </div>
                        <h2 class="post-title">
                            <a href="posts/{post.filename}" class="post-link">{post.title}</a>
                        </h2>
                    </div>
                    {post.preview}
                    <a href="posts/{post.filename}" class="continue-reading">Continue Reading</a>
                    <div class="post-divider"></div>
                </article>

    """

    total_post = total_post + post_template


total_post = total_post + """
            </div>
"""

SIDEBAR_HTML_COMMON = get_related_post()
total_post = total_post + SIDEBAR_HTML_COMMON

total_post = total_post + """
                    </div>
                </div>
            </aside>
        </div>
    </main>
"""

total_post = total_post + SCRIPT_HTML

current_dir = os.getcwd()
print(current_dir)
file_path = os.path.join(current_dir, 'index.html')

# Write to file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(total_post)

print(f"Document written to: {file_path}")