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
        filename='oaxaca.html',
        title='Mercado de Abastos: Oaxaca',
        blog_title='Mercado de Abastos: Oaxaca',
        blog_subtitle='Walking through Oaxaca’s vibrant market, one frame at a time.',
        blog_content="""
                    <p>On a warm morning, I wandered through the Mercado de Abastos in Oaxaca — absorbing colors, voices, textures. Each stall, each face, each fragment of light became a frame. This is more than a market; it’s a story in motion.</p>
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2909.jpg" alt="Stall with fruits" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2920.jpg" alt="Colorful fabrics" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2929.jpg" alt="Market corridor" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2933.jpg" alt="Vendor arranging goods" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2939.jpg" alt="Close up of produce" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2949.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2955.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2961.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2971.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2971.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2975.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2983.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2994.jpg" alt="Shadows in aisle" class="featured-image">
    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2997.jpg" alt="Shadows in aisle" class="featured-image">

        """,
        preview="""
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2933.jpg"  alt="Market entrance" class="post-image">
                    <p class="post-excerpt">
                         On a warm morning, I wandered through the Mercado de Abastos in Oaxaca — absorbing colors, voices, textures. Each stall, each face, each fragment of light became a frame.
                    </p>
        """,
        main_photo="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/0937ed97f9a7141033d738dddb6ed293ec28d5b8/Oaxaca/DSCF2933.jpg" ,
        category="Photos",
        tags=['Photo'],
        date=date(2025, 10, 11)
    ),
    Post(
        filename='films_mexico_v2.html',
        title='Unfolding Mexico: A 35mm Journey',
        blog_title='Unfolding Mexico: A 35mm Journey',
        blog_subtitle='A journey through Mexico’s colors, textures, and spirit — captured only on film.',
        blog_content="""
                    <p>Shot entirely on analog film, this collection reveals Mexico in its most timeless form, where imperfections become part of the story. Each frame carries the warmth of the country’s light, its vibrant streets, and the soul of its people.</p>
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c1cbed055d0e17eaf97b88e33d55a03f89a45d88/scan/000007760011.jpg" alt="Woman with flower" class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c1cbed055d0e17eaf97b88e33d55a03f89a45d88/scan/000007760018.jpg" alt="Mask " class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c1cbed055d0e17eaf97b88e33d55a03f89a45d88/scan/000007760019.jpg" alt="Mask " class="featured-image">
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c1cbed055d0e17eaf97b88e33d55a03f89a45d88/scan/000007760025.jpg" alt="Mask " class="featured-image">
        """,
        preview="""
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c1cbed055d0e17eaf97b88e33d55a03f89a45d88/scan/000007760011.jpg" alt="Tokyo street in rain" class="post-image">
                    <p class="post-excerpt">
                    Shot entirely on analog film, this collection reveals Mexico in its most timeless form, where imperfections become part of the story. Each frame carries the warmth of the country’s light, its vibrant streets, and the soul of its people.
                    </p>
        """,
        main_photo="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c1cbed055d0e17eaf97b88e33d55a03f89a45d88/scan/000007760011.jpg",
        category="Photos",
        tags=['Photo'],
        date=date(2025, 9, 15)
    ),
    Post(
        filename='catrinas_photoshoot.html',
        title='Catrinas in CDMX: A Día de los Muertos Photoshoot',
        blog_title='Catrinas in CDMX: A Día de los Muertos Photoshoot',
        blog_subtitle='A vibrant homage to Día de los Muertos in CDMX, where Catrinas embody elegance and tradition. This photoshoot captures the spirit of remembrance and celebration.',
        blog_content="""
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/60-DSCF3191.jpg" alt="Catrina Day of the Dead makeup" class="featured-image">

                    <p>Mexico City during Día de los Muertos is nothing short of magical. The streets come alive with vibrant colors, intricate altars, and the haunting beauty of Catrinas—those elegant skeletal figures that have become synonymous with this sacred celebration of life and death.</p>

                    <p>This photoshoot was born from a deep fascination with Mexican culture and the profound beauty found in their approach to mortality. Unlike many cultures that fear death, Mexicans embrace it as a natural part of life's cycle, celebrating their departed loved ones with joy, color, and remembrance.</p>

                    <h3>The Art of Transformation</h3>
                    
                    <p>Working with local makeup artists in CDMX was an incredible experience. Each Catrina look took hours to complete, with artists meticulously painting intricate designs that honor traditional Day of the Dead aesthetics while adding their own contemporary flair. The attention to detail was extraordinary—from the delicate flower patterns around the eyes to the ornate designs that seemed to dance across the models' faces.</p>

                    <div class="image-gallery">
                        <div>
                            <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/58-DSCF5165.jpg" alt="Catrina portrait with flowers" class="gallery-image">
                            <p class="image-caption">The intricate makeup process takes several hours, with artists carefully crafting each detail by hand.</p>
                        </div>
                    </div>

                    <div class="quote">
                        "Death is not the opposite of life, but a part of it. In Mexico, we don't mourn the dead—we celebrate their journey and keep their memory alive through art, food, and tradition."
                    </div>

                    <h3>Cultural Significance</h3>
                    
                    <p>The Catrina, originally created by artist José Guadalupe Posada and later immortalized by Diego Rivera, represents the democratic nature of death—it comes to rich and poor alike. During our shoot, I was struck by how the models embodied this spirit, transforming into these ethereal beings that seemed to bridge the world of the living and the dead.</p>
                    
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/f54ee20ceaa0c3c54585d38fee1982d309d0e0fa/55-DSCF5246.jpg" alt="Catrina 2" class="featured-image">
                    
                    <p>Each photograph in this series aims to capture not just the visual beauty of the Catrina tradition, but the deeper cultural significance it holds. These images are a testament to Mexico's unique relationship with mortality—one that finds beauty in the macabre and celebrates life through the acknowledgment of death.</p>

                    <h3>Behind the Scenes</h3>
                    
                    <p>Shooting in Mexico City's historic center provided the perfect backdrop for this project. The colonial architecture, with its weathered stones and baroque details, complemented the timeless elegance of the Catrina aesthetic. We worked primarily during the golden hour, when the warm light softened the dramatic makeup and created an otherworldly atmosphere.</p>
                    
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/f54ee20ceaa0c3c54585d38fee1982d309d0e0fa/62-DSCF3180.jpg" alt="Catrina 2" class="featured-image">
                    
                    <p>The collaboration with local artists was invaluable—not only for their technical expertise but for their cultural knowledge and respect for the traditions we were documenting. This wasn't just a photoshoot; it was a cultural exchange that deepened my understanding of Mexican heritage and the beautiful complexity of Día de los Muertos.</p>

        """,
        preview="""
                    <img src="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/60-DSCF3191.jpg" alt="Swiss Alps at golden hour" class="post-image">
                    <p class="post-excerpt">
                        A vibrant homage to Día de los Muertos in CDMX, where Catrinas embody elegance and tradition. This photoshoot captures the spirit of remembrance and celebration.                    
                    </p>
        """,
        main_photo="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/60-DSCF3191.jpg",
        category="Photos",
        tags=['Photo'],
        date=date(2025, 9, 15)
    ),
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
        main_photo="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/6-DSCF5719.jpg",
        category="Photos",
        tags=['Photo'],
        date=date(2025, 9, 14)
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
        main_photo="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/c7d77ee569e8cec6157c55ece5012372cb3bb1c3/42-DSCF5406.jpg",
        category="Photos",
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
        main_photo="https://raw.githubusercontent.com/GiorgiaNCT/photo_blog/9f96cf159138287f43ba1fe4db104b1fed37fdea/23-DSCF5579.jpg",
        category="Creations",
        tags=['Photo'],
        date=date(2025, 9, 12)
    )
]