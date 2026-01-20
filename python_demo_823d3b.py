# Fractal Art Generation with Recursion and Turtle Graphics

# Learning Objective:
# This tutorial will teach you how to generate intricate fractal art
# using the power of recursion and Python's built-in turtle graphics module.
# We'll focus on understanding how recursive functions break down complex
# problems into smaller, self-similar steps, and how this translates to
# visually stunning fractal patterns.

import turtle

# --- Configuration ---
# These variables control the appearance and behavior of our fractal.
# You can experiment with changing these values to see different results!

# The angle of branching in degrees.
BRANCH_ANGLE = 25

# The scaling factor for each subsequent branch.
# A value less than 1 makes branches shorter.
BRANCH_SCALE = 0.7

# The initial length of the main trunk.
INITIAL_LENGTH = 100

# The number of recursive calls for each branch.
# This determines the depth and complexity of the fractal.
RECURSION_DEPTH = 9

# Speed of the turtle drawing. 0 is fastest, 1-10 are slow to fast.
DRAW_SPEED = 0

# Color of the branches.
BRANCH_COLOR = "green"

# --- Recursive Function ---

def draw_fractal_tree(t, length, depth):
    """
    Recursively draws a fractal tree.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        length (float): The current length of the branch to draw.
        depth (int): The current recursion depth.
    """

    # Base Case: When the recursion depth reaches 0, we stop drawing.
    # This is crucial to prevent infinite recursion.
    if depth == 0:
        return

    # Draw the current branch: Move the turtle forward by 'length'.
    t.forward(length)

    # Save the current turtle state (position and heading).
    # We need this to return to this point after drawing sub-branches.
    current_pos = t.position()
    current_heading = t.heading()

    # --- Recursive Step: Draw left sub-branch ---
    # Turn left by the specified angle.
    t.left(BRANCH_ANGLE)
    # Recursively call draw_fractal_tree for the left branch.
    # The length of the new branch is the current length scaled down.
    # The depth is reduced by 1 for the next level of recursion.
    draw_fractal_tree(t, length * BRANCH_SCALE, depth - 1)

    # Restore the turtle's state to draw the right sub-branch.
    # This is important because the left branch drawing might have moved
    # the turtle to a different position and heading.
    t.penup()  # Lift the pen to avoid drawing while repositioning
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown() # Put the pen down to continue drawing

    # --- Recursive Step: Draw right sub-branch ---
    # Turn right by the specified angle.
    t.right(BRANCH_ANGLE)
    # Recursively call draw_fractal_tree for the right branch.
    draw_fractal_tree(t, length * BRANCH_SCALE, depth - 1)

    # After drawing both sub-branches, we need to backtrack to the
    # starting position of the current branch so that the parent branch
    # can continue drawing.
    t.penup()
    t.goto(current_pos)
    t.setheading(current_heading)
    t.pendown()

# --- Main Execution ---

def create_fractal_art():
    """
    Sets up the turtle screen and initiates the fractal drawing process.
    """
    # Create a screen object.
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Set the window size.
    screen.bgcolor("lightblue")         # Set the background color.
    screen.title("Recursive Fractal Tree Art") # Set the window title.

    # Create a turtle object.
    artist = turtle.Turtle()
    artist.speed(DRAW_SPEED)           # Set the drawing speed.
    artist.color(BRANCH_COLOR)         # Set the initial color.
    artist.penup()                     # Lift the pen to move to starting position.
    artist.goto(0, -250)               # Move to the bottom center of the screen.
    artist.left(90)                    # Point the turtle upwards.
    artist.pendown()                   # Put the pen down to start drawing.

    # Start the recursive drawing process.
    draw_fractal_tree(artist, INITIAL_LENGTH, RECURSION_DEPTH)

    # Hide the turtle when drawing is complete.
    artist.hideturtle()
    # Keep the window open until it's manually closed.
    screen.mainloop()

# --- Example Usage ---
# To run this code, simply call the create_fractal_art() function.
if __name__ == "__main__":
    create_fractal_art()