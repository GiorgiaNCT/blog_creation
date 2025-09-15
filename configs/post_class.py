from dataclasses import dataclass
from datetime import date

@dataclass
class Post:
    filename: str
    title: str
    blog_title: str
    blog_subtitle: str
    blog_content: str
    preview: str
    tags: list[str]
    date: date