from manim import *
import numpy as np

def create_gradient_background(scene, start_color, end_color):
    background = Rectangle(
        width=1200,
        height=800,
        fill_opacity=0.15,
        stroke_width=0,
    ).set_color_by_gradient(start_color, end_color)
    scene.play(FadeIn(background))
    return background

class PortfolioAnimation(Scene):
    def construct(self):
        # Set a subtle gradient background for the entire animation
        bg = create_gradient_background(self, "#032B43", "#176087")
        
        # Introduction Scene
        self.play_intro()
        self.wait(1)
        
        # Education Scene
        self.play_education()
        self.wait(1)
        
        # Projects Timeline
        self.play_projects()
        self.wait(1)
        
        # Skills Visualization
        self.play_skills()
        self.wait(1)

        # Personal Interests
        self.play_interests()
        self.wait(1)

        # Website Showcase
        self.play_website()
        self.wait(1)
        
        # Closing Scene
        self.play_outro()
        
    def play_intro(self):
        # Create particle effect
        particles = VGroup(*[
            Dot(radius=0.05).move_to([
                np.random.uniform(-7, 7),
                np.random.uniform(-4, 4),
                0
            ]).set_color(color) 
            for color in [BLUE, PURPLE, TEAL, "#FF69B4"]  # Added pink for contrast
            for _ in range(30)
        ])
        
        # Animate particles
        self.play(
            LaggedStart(*[
                Create(p) for p in particles
            ], lag_ratio=0.1)
        )
        
        name = Text("Atilla Çolak", font_size=72)
        name.set_color_by_gradient("#FF69B4", BLUE, PURPLE)  # Added pink gradient
        
        # Create typing effect for name
        self.play(AddTextLetterByLetter(name), run_time=1.5)
        
        # Animate particles converging towards name
        self.play(
            *[p.animate.move_to(
                name.get_center() + np.array([
                    np.random.uniform(-2, 2),
                    np.random.uniform(-1, 1),
                    0
                ])
            ) for p in particles],
            run_time=1.5
        )
        
        subtitle = Text("Software Developer", font_size=48)
        subtitle.next_to(name, DOWN)
        self.play(FadeIn(subtitle, shift=UP))
        
        # Disperse particles
        self.play(
            *[p.animate.move_to([
                np.random.uniform(-7, 7),
                np.random.uniform(-4, 4),
                0
            ]) for p in particles],
            run_time=1.5
        )
        
        self.play(
            FadeOut(name, shift=UP),
            FadeOut(subtitle, shift=UP),
            FadeOut(particles)
        )
        
    def play_education(self):
        title = Text("Education", font_size=64).set_color_by_gradient(TEAL, BLUE, PURPLE)
        title.to_edge(UP)
        
        # Create animated underline
        underline = Line(color=TEAL)
        underline.match_width(title)
        underline.next_to(title, DOWN, buff=0.1)
        
        self.play(Write(title))
        self.play(Create(underline))
        
        uni = Text("Delft University of Technology", font_size=48, color="#FF69B4")
        degree = Text("BSc Computer Science and Engineering", font_size=36)
        
        # Create animated GPA counter
        gpa_text = Text("GPA: ", font_size=36, color=TEAL).align_to(LEFT)
        gpa_number = DecimalNumber(
            0,
            num_decimal_places=1,
            include_sign=False,
            font_size=36,
            color=GREEN
        ).next_to(gpa_text, RIGHT)
        
        gpa_group = VGroup(gpa_text, gpa_number)
        education_group = VGroup(uni, degree, gpa_group).arrange(DOWN, buff=0.5).shift(UP)
        
        self.play(FadeIn(uni, shift=RIGHT))
        self.play(FadeIn(degree, shift=RIGHT))
        self.play(FadeIn(gpa_text, shift=RIGHT))
        
        # Animate GPA counter
        self.play(
            ChangeDecimalToValue(gpa_number, 7.9),
            run_time=2,
            rate_func=smooth
        )
        
        # Create pulsing highlight
        highlight = Circle(radius=0.7, color=GREEN, stroke_width=3)
        highlight.surround(gpa_group)
        
        self.play(Create(highlight))
        self.play(
            highlight.animate.scale(1.2).set_color(TEAL),
            rate_func=there_and_back
        )
        
        self.play(
            FadeOut(VGroup(title, underline, uni, degree, gpa_group, highlight), shift=UP)
        )
        
    def play_projects(self):
        title = Text("Notable Projects (and Work)", font_size=56).set_color_by_gradient(TEAL, PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Create animated timeline with flowing particles
        timeline = Line(LEFT * 5, RIGHT * 5, color=GRAY)
        timeline.shift(DOWN)
        self.play(Create(timeline))

        # Create flowing particles along timeline
        particles = VGroup(*[
            Dot(radius=0.05, color=TEAL)
            .move_to(timeline.get_start())
            for _ in range(10)
        ])

        self.play(
            LaggedStart(*[
                MoveAlongPath(p, timeline) for p in particles
            ], lag_ratio=0.1)
        )

        projects = [
            ("ANDL", "Co-founder building responsible AI", "2024", "#FF69B4"),
            ("Hivello", "Data Analyst", "2024", TEAL),
            ("My HeartSpace", "Lead Dev", "2024", BLUE),
            ("Others", "Many Solo Projects", "2021-...", PURPLE),
        ]

        dots = VGroup()
        labels = VGroup()

        for i, (name, desc, year, color) in enumerate(projects):
            x_pos = timeline.get_left() + (i * 3.2) * RIGHT

            # Create interactive dot
            dot = Dot(x_pos, color=color).scale(1.5)  # Slightly larger dot for better visibility
            dots.add(dot)

            # Create label with improved styling
            label = VGroup(
                Text(name, font_size=24, color=color, weight=BOLD),  # Use bold font for project name
                Text(desc, font_size=20, color=WHITE),  # Slightly smaller and white for description
                Text(year, font_size=16, color=GRAY)  # Smaller year text
            ).arrange(DOWN, buff=0.15)  # Adjust spacing for better separation

            # Center the labels directly above the dots
            label.move_to(dot.get_center() + UP * 0.8)
            labels.add(label)

            # Animate dot appearance with ripple effect
            ripple = Circle(radius=0.3, color=color).move_to(dot.get_center())
            self.play(
                Create(dot),
                Create(ripple),
                ripple.animate.scale(3).fade(1),
                Write(label),
                run_time=0.8
            )

        self.wait(2)
        self.play(
            FadeOut(VGroup(title, timeline, dots, labels, particles), shift=UP)
        )

        
    def play_skills(self):
        title = Text("Technical Skills", font_size=64).set_color_by_gradient(TEAL, PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Define skills data for the bar chart
        skills = [
            ("Web Dev", 95, "#FF69B4"),
            ("Backend", 90, TEAL),
            ("Frontend", 90, BLUE),
            ("Data Analysis", 85, PURPLE),
            ("Systems", 75, "#FF69B4"),
            ("AI/ML", 70, TEAL)
        ]
        
        # Extracting values and labels
        values = [level for _, level, _ in skills]
        labels = [skill for skill, _, _ in skills]

        # Create bar chart
        chart = BarChart(
            values=values,
            bar_names=labels,
            y_range=[0, 100, 20],
            y_length=5,
            x_length=12,
            x_axis_config={"font_size": 24},
            bar_colors=[color for _, _, color in skills]
        )
        
        # Add chart to the scene
        self.play(Create(chart))
        
        # Create labels for each bar
        bar_labels = chart.get_bar_labels(font_size=24)

        # Add labels to the scene
        self.play(Write(bar_labels))

        # Wait for a moment to let the audience absorb the information
        self.wait(2)

        # Enhanced exit animation
        self.play(
            FadeOut(VGroup(title, chart, bar_labels), shift=UP)
        )

    def play_interests(self):
        title = Text("Beyond Coding", font_size=64).set_color_by_gradient(TEAL, PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Create interactive interest cards with hover effects
        interests = [
            ("♟️ Chess", "2300+ Online Rating", TEAL),
            ("🎵 Music Production", "Piano and Beatmaking", "#FF69B4"),
        ]

        cards = VGroup()
        for i, (icon_title, desc, color) in enumerate(interests):
            # Create card with gradient background
            card_bg = RoundedRectangle(
                height=2.5,
                width=4,
                corner_radius=0.5,
                stroke_color=color,
                fill_color=color,
                fill_opacity=0.1
            )
            
            content = VGroup(
                Text(icon_title, font_size=36, color=color),
                Text(desc, font_size=24)
            ).arrange(DOWN, buff=0.3)
            content.move_to(card_bg.get_center())
            
            # Create pulsing effect
            pulse = card_bg.copy().scale(1.1)
            pulse.set_fill(opacity=0)
            
            card_group = VGroup(card_bg, content, pulse)
            cards.add(card_group)

        cards.arrange(RIGHT, buff=1).shift(UP)
        
        for card in cards:
            self.play(
                Create(card[0]),
                Write(card[1]),
                run_time=0.8
            )
            # Add pulsing animation
            self.play(
                card[2].animate.scale(1.1).set_stroke(opacity=0),
                rate_func=there_and_back,
                run_time=0.8
            )
        
        self.wait(1)
        self.play(
            FadeOut(VGroup(title, cards), shift=UP)
        )

    def play_website(self):
        title = Text("Visit atillas.co", font_size=64).set_color_by_gradient(TEAL, PURPLE)
        title.to_edge(UP)
        self.play(Write(title))

        # Create interactive website showcase
        features = [
            ("📚 Book Summaries", "Deep dives into tech & philosophy", TEAL),
            ("💻 Project Showcase", "Live demos & code explanations", "#FF69B4"),
            ("...", "Whatever more I added since this video", BLUE),
        ]

        feature_group = VGroup()
        for i, (feature, desc, color) in enumerate(features):
            # Create feature card with hover effect
            card = VGroup(
                Text(feature, font_size=32, color=color),
                Text(desc, font_size=24, color=GRAY)
            ).arrange(DOWN, buff=0.2)
            
            # Add background highlight
            highlight = Rectangle(
                width=card.width + 0.5,
                height=card.height + 0.3,
                fill_color=color,
                fill_opacity=0.1,
                stroke_color=color,
                stroke_opacity=0.5
            )
            highlight.move_to(card)
            
            feature_group.add(VGroup(highlight, card))

        feature_group.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        feature_group.shift(UP * 0.5)

        for item in feature_group:
            self.play(
                Create(item[0]),
                Write(item[1]),
                run_time=0.7
            )
            # Add hover animation
            self.play(
                item[0].animate.scale(1.05),
                rate_func=there_and_back,
                run_time=0.3
            )

        self.wait(1)
        self.play(
            FadeOut(VGroup(title, feature_group), shift=UP)
        )
        
    def play_outro(self):
        contact = VGroup(
            Text("Let's Connect!", font_size=64).set_color_by_gradient(BLUE, PURPLE),
            Text("atilla.colak@outlook.com", font_size=36),
            Text("atillas.co", font_size=36, color=BLUE),
            Text("github.com/atillaColak", font_size=36)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(contact))
        
        # Create animated circle with gradient
        circle = Circle(radius=4).set_color_by_gradient(BLUE, PURPLE)
        circle.surround(contact)
        self.play(Create(circle))
        self.play(
            circle.animate.scale(1.2).rotate(PI),
            rate_func=there_and_back
        )
        
        self.wait(2)