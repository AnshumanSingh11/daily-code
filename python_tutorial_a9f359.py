# --- Educational Code Tutorial: Procedural Abstract Art with Python Turtle ---
#
# Learning Objective:
# This tutorial will teach beginners how to procedurally generate unique and
# visually appealing abstract art using Python's `turtle` module. We'll focus
# on combining random movements with a curated random color palette to create
# diverse artistic outputs. This will introduce fundamental concepts of
# procedural generation and creative coding.

import turtle
import random

# --- Configuration ---
# We define these constants to make it easy to change the art's characteristics
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_SHAPES = 100  # How many drawing elements (lines, curves, etc.) we'll create
MAX_PEN_SIZE = 5  # The maximum thickness of our drawing lines
MIN_PEN_SIZE = 1  # The minimum thickness of our drawing lines
MAX_MOVE_DISTANCE = 50  # The maximum distance the turtle can move in one step
MIN_MOVE_DISTANCE = 5   # The minimum distance the turtle can move in one step
MAX_TURN_ANGLE = 360    # The maximum angle the turtle can turn
MIN_TURN_ANGLE = 0      # The minimum angle the turtle can turn

# --- Color Palettes ---
# We create a few pre-defined color palettes. This gives us control over the
# aesthetic and ensures colors work well together.
# Each palette is a list of RGB tuples (0-255).
COLOR_PALETTES = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)],  # Primary colors + Yellow
    [(255, 165, 0), (255, 192, 203), (139, 69, 19), (255, 255, 255)], # Warm tones + White
    [(0, 128, 128), (70, 130, 180), (106, 90, 205), (240, 230, 140)], # Cool tones + Beige
    [(50, 205, 50), (152, 251, 152), (0, 100, 0), (255, 215, 0)] # Greens + Gold
]

# --- Setup the Turtle Screen ---
screen = turtle.Screen()
# Set the size of the drawing window
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
# Set a background color for the canvas
screen.bgcolor("black")
# Turn off screen updates for faster drawing
screen.tracer(0)

# --- Create the Turtle ---
artist = turtle.Turtle()
# Set the turtle's speed to its fastest
artist.speed(0)
# Hide the turtle icon itself so it doesn't obstruct the art
artist.hideturtle()
# Set the initial pen size
artist.pensize(random.randint(MIN_PEN_SIZE, MAX_PEN_SIZE))
# Set the drawing mode for lines (solid is standard)
artist.mode("standard")

# --- Helper Function to Convert RGB to Turtle Color ---
def rgb_to_turtle_color(rgb_tuple):
    # Turtle expects colors in a 0-1 range for RGB, not 0-255.
    # This function converts our 0-255 tuples to the format turtle understands.
    r, g, b = rgb_tuple
    return (r / 255, g / 255, b / 255)

# --- Procedural Generation Logic ---
def generate_abstract_art():
    # Select a random color palette to use for this artwork
    current_palette = random.choice(COLOR_PALETTES)
    # Convert the chosen palette to turtle-compatible format
    turtle_palette = [rgb_to_turtle_color(color) for color in current_palette]

    # Move the turtle to a random starting position within the screen bounds
    artist.penup() # Don't draw while moving to the start
    start_x = random.randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2)
    start_y = random.randint(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2)
    artist.goto(start_x, start_y)
    artist.pendown() # Start drawing from this position

    # Loop to create multiple drawing elements (shapes/lines)
    for _ in range(NUM_SHAPES):
        # Randomly choose a color from our selected palette
        color = random.choice(turtle_palette)
        # Set the pen color for the turtle
        artist.pencolor(color)
        # Randomly set the pen size for variety
        artist.pensize(random.randint(MIN_PEN_SIZE, MAX_PEN_SIZE))

        # Choose a random direction to move
        direction = random.randint(MIN_TURN_ANGLE, MAX_TURN_ANGLE)
        artist.setheading(direction) # Point the turtle in a random direction

        # Choose a random distance to move
        move_distance = random.randint(MIN_MOVE_DISTANCE, MAX_MOVE_DISTANCE)
        # Move the turtle forward, drawing a line
        artist.forward(move_distance)

        # Introduce a random turn to change direction for the next segment
        turn_angle = random.randint(MIN_TURN_ANGLE, MAX_TURN_ANGLE)
        artist.right(turn_angle)

        # Optional: Occasionally lift the pen and move to a new random location
        # This creates disjointed elements and more abstract forms.
        if random.random() < 0.1: # 10% chance to reposition
            artist.penup()
            new_x = random.randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2)
            new_y = random.randint(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2)
            artist.goto(new_x, new_y)
            artist.pendown()

    # After all shapes are drawn, update the screen to show the final artwork
    screen.update()

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures the code only runs when the script is executed directly
    # (not when imported as a module).

    print("Generating abstract art...")
    generate_abstract_art()
    print("Art generation complete. Click the window to close.")

    # Keep the window open until it's manually closed
    screen.mainloop()