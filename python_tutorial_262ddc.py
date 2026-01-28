# Learning Objective: Procedurally Generate and Display Unique, Evolving Visual Patterns in a Grid

# This tutorial will guide you through creating a Python script that generates
# a grid of visually interesting patterns. We will use basic mathematical
# functions to define these patterns, making them unique and potentially
# evolving over time. This will help you understand:
# 1. How to use loops to create grids.
# 2. How simple mathematical formulas can create complex visuals.
# 3. How to map numerical values to visual properties (like color).
# 4. Basic image manipulation with the Pillow library.

# Import necessary libraries
from PIL import Image, ImageDraw  # Pillow library for image creation and drawing
import random                 # For introducing randomness

# --- Configuration ---
GRID_SIZE = 16       # Number of cells in each dimension of our grid
CELL_SIZE = 30       # Size of each cell in pixels
IMAGE_WIDTH = GRID_SIZE * CELL_SIZE
IMAGE_HEIGHT = GRID_SIZE * CELL_SIZE
BACKGROUND_COLOR = (255, 255, 255) # White background
PATTERN_COLOR_RANGE = ((0, 0, 0), (100, 100, 255)) # Range for pattern colors (dark grey to blue)

# --- Helper Functions ---

def get_pattern_value(row: int, col: int, time_factor: float) -> float:
    """
    Calculates a numerical value for a specific grid cell based on its
    row, column, and a time factor. This value will determine the pattern.
    The 'why' here is to use mathematical functions to create repeatable,
    but varied, patterns. Different functions will yield different visual styles.
    We're using sine waves and multiplication to create smooth, flowing patterns.
    The time_factor allows for animation/evolution of the patterns.
    """
    # Base value using a combination of row and column, scaled and shifted
    base_value = (row + col) * 0.1

    # Introduce some sinusoidal variation based on position and time
    # These sine waves add complexity and visual interest.
    pattern_noise = (
        (abs(row - col) * 0.2) +
        (row * 0.3) +
        (col * 0.4) +
        (time_factor * 0.5) # This makes the pattern evolve over time
    )

    # Use sine function to create oscillating values
    sine_wave_1 = math.sin(base_value + pattern_noise)
    sine_wave_2 = math.cos(pattern_noise * 1.5)

    # Combine and scale the results to get a value typically between -1 and 1
    # We then map this to a range suitable for coloring (e.g., 0 to 255).
    combined_value = (sine_wave_1 * 0.5) + (sine_wave_2 * 0.5)
    # Scale the combined value to be roughly between 0 and 1 for easier mapping
    scaled_value = (combined_value + 1) / 2
    return scaled_value

def map_value_to_color(value: float) -> tuple[int, int, int]:
    """
    Maps a numerical value (typically between 0 and 1) to an RGB color.
    The 'why' here is to translate our calculated pattern values into
    something we can actually see on screen. We'll interpolate between
    two defined colors based on the input value.
    """
    # Define the start and end colors for interpolation
    start_color = PATTERN_COLOR_RANGE[0]
    end_color = PATTERN_COLOR_RANGE[1]

    # Linearly interpolate between the start and end colors based on the value
    # This creates a smooth gradient of colors.
    r = int(start_color[0] + (end_color[0] - start_color[0]) * value)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * value)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * value)

    # Ensure color values are within the valid 0-255 range
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return (r, g, b)

def draw_grid_pattern(image: Image.Image, time_factor: float):
    """
    Draws the entire grid of patterns onto the given Pillow Image object.
    The 'why' is to iterate through each cell of our grid and apply
    the pattern generation and color mapping logic to draw it.
    """
    draw = ImageDraw.Draw(image) # Get a drawing context for the image

    # Loop through each row of the grid
    for row in range(GRID_SIZE):
        # Loop through each column in the current row
        for col in range(GRID_SIZE):
            # Calculate the pattern value for this specific cell
            pattern_val = get_pattern_value(row, col, time_factor)

            # Map the calculated value to an RGB color
            cell_color = map_value_to_color(pattern_val)

            # Calculate the pixel coordinates for the top-left and bottom-right
            # corners of the current cell.
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            # Draw a rectangle for the current cell with the determined color
            # This is the 'display' part - making the pattern visible.
            draw.rectangle([x1, y1, x2, y2], fill=cell_color)

# --- Main Execution ---

if __name__ == "__main__":
    # We will generate a sequence of images to show the evolving patterns.
    # This is a common way to create simple animations.

    num_frames = 60 # Number of frames to generate for the animation
    output_filename_base = "pattern_grid_" # Base name for output files

    print(f"Generating {num_frames} frames of evolving patterns...")

    for frame_num in range(num_frames):
        # Create a new blank image for each frame
        # The 'RGB' mode means it's a color image.
        image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), BACKGROUND_COLOR)

        # Calculate a time factor that changes with each frame.
        # This is crucial for making the patterns evolve. We normalize it
        # so that it's always between 0 and 1.
        current_time_factor = frame_num / num_frames

        # Draw the grid pattern onto the image using the current time factor
        draw_grid_pattern(image, current_time_factor)

        # Construct the filename for the current frame
        # We use zfill to ensure consistent padding (e.g., 001, 002, ... 060)
        output_filename = f"{output_filename_base}{str(frame_num + 1).zfill(3)}.png"

        # Save the generated image
        image.save(output_filename)
        print(f"Saved {output_filename}")

    print("\nGeneration complete!")
    print("You can now view the generated PNG files to see the evolving patterns.")
    print("Consider using a GIF maker tool to combine these PNGs into an animation.")