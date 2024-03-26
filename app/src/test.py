import streamlit as st
from manim import *
import os

"""
# Manim on Streamlit

I'm trying to run a Streamlit app that uses Manim to render a simple animation.

"""

class ExampleOfAnimation(Scene):
    def construct(self):
        circle = Circle(color=WHITE)
        square = Square(color=BLUE)

        self.play(Create(circle))
        self.wait()

        self.play(Transform(circle, square))
        self.wait()

        self.play(FadeOut(square))
        self.wait()


# Define the Streamlit app
def main():
    custom_scene = ExampleOfAnimation()

    # Create a button to run the Manim animation
    if st.button("Run Animation"):

        # Render the animation using Manim
        video_file = open(os.path.join('media', 'videos', '1080p60', 'ExampleOfAnimation.mp4'), 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
if __name__ == "__main__":
    main()