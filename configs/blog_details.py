from configs.post_class import Post
from datetime import date

blog_post_old = {
    'cdmx_dia_de_los_muertos_2024.html': {
        'title':'CDMX Celebrates Día de los Muertos 2024',
        'title_blog': 'CDMX Celebrates Día de los Muertos 2024',
        'subtitle_post': 'Dia del los muerto parade',
        'tags': ['Photo'],
        'text_blog':"""
                    <p>Mexico City during Día de los Muertos is nothing short of magical. The streets come alive with vibrant colors, intricate altars, and the haunting beauty of Catrinas—those elegant skeletal figures that have become synonymous with this sacred celebration of life and death.</p>
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/6-DSCF5719.jpg" alt="Woman with flower" class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/9243c3184388fd8b4e9cc18c9409fbe6a1bedd35/2-DSCF5769.jpg" alt="Mask " class="featured-image">

"""
    }
}

blog_post = [
    Post(
        filename='cdmx_dia_de_los_muertos_2024_new.html',
        title='CDMX Celebrates Día de los Muertos 2024',
        blog_title='CDMX Celebrates Día de los Muertos 2024',
        blog_subtitle='Dia del los muerto parade',
        blog_content="""
                    <p>Mexico City during Día de los Muertos is nothing short of magical. The streets come alive with vibrant colors, intricate altars, and the haunting beauty of Catrinas—those elegant skeletal figures that have become synonymous with this sacred celebration of life and death.</p>
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/6-DSCF5719.jpg" alt="Woman with flower" class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/9243c3184388fd8b4e9cc18c9409fbe6a1bedd35/2-DSCF5769.jpg" alt="Mask " class="featured-image">
        """,
        preview="""
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/6-DSCF5719.jpg" alt="Tokyo street in rain" class="post-image">
                    <p class="post-excerpt">
                        Last year I experienced the vibrant Día de los Muertos parade in Mexico, where music, colors, and tradition filled the streets. It was a powerful celebration of life, memory, and culture.
                    </p>
        """,
        tags=['Photo'],
        date=date(2025, 9, 15)
    ),
    Post(
        filename='tepito_market.html',
        title='Inside Tepito: Mexico City’s Legendary Market',
        blog_title='Inside Tepito: Mexico City’s Legendary Market',
        blog_subtitle='Tepito market',
        blog_content="""
                    <p>Step into Tepito, Mexico City’s most legendary market, where history, tradition, and street culture collide. This tour unveils the hidden stories and vibrant spirit behind its bustling alleys.</p>
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c406f3db5d277bbb565d9583591f9b93de2edba1/tepito/40-DSCF5415.jpg" alt="Woman with flower" class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c406f3db5d277bbb565d9583591f9b93de2edba1/tepito/42-DSCF5406.jpg" alt="Mask " class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c406f3db5d277bbb565d9583591f9b93de2edba1/tepito/44-DSCF5403.jpg" alt="Mask " class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c406f3db5d277bbb565d9583591f9b93de2edba1/tepito/45-DSCF5400.jpg" alt="Mask " class="featured-image">
        """,
        preview="""
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/42-DSCF5406.jpg" alt="Portrait of elderly hands" class="post-image">
                    <p class="post-excerpt">
                        Step into Tepito, Mexico City’s most legendary market, where history, tradition, and street culture collide. This tour unveils the hidden stories and vibrant spirit behind its bustling alleys.
                    </p>
        """,
        tags=['Photo'],
        date=date(2025, 9, 13)
    ),
    Post(
        filename='cdmx_by_night.html',
        title='CDMX After Dark: Nighttime Stories in the City',
        blog_title='CDMX After Dark: Nighttime Stories in the City',
        blog_subtitle='City by night',
        blog_content="""
                    <p>The streets of Mexico City come alive after dark, revealing lights, shadows, and hidden corners. A nighttime journey through CDMX captured through my lens.</p>
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/9f96cf159138287f43ba1fe4db104b1fed37fdea/23-DSCF5579.jpg" alt="Woman with flower" class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c1cbed055d0e17eaf97b88e33d55a03f89a45d88/21-DSCF5584.jpg" alt="Mask " class="featured-image">
        """,
        preview="""
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/9f96cf159138287f43ba1fe4db104b1fed37fdea/23-DSCF5579.jpg" alt="Portrait of elderly hands" class="post-image">
                    <p class="post-excerpt">
                       The streets of Mexico City come alive after dark, revealing lights, shadows, and hidden corners. A nighttime journey through CDMX captured through my lens.
                    </p>
        """,
        tags=['Photo'],
        date=date(2025, 9, 12)
    ),
]