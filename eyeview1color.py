import pygame
import pandas as pd

# Load EOG data from CSV
df = pd.read_csv('eogdata.csv')

# Simulation parameters
width, height = 800, 600
eye_radius = 30
eyeball_radius = 30
retina_radius = 10
scaling_factor = 30

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Continuous Eye Movement Simulation")

# Initialize eye positions
left_eye_x, left_eye_y = width // 3, height // 2
right_eye_x, right_eye_y = 2 * width // 3, height // 2

# Clock to control the frame rate
clock = pygame.time.Clock()

# Define color palette
color_palette = [
    (0, 0, 128),  # Dark Blue (-10)
    (0, 0, 153),  # Blue (-9)
    (0, 0, 179),  # Light Blue (-8)
    (0, 0, 204),  # Lighter Blue (-7)
    (0, 0, 230),  # Lightest Blue (-6)
    (0, 128, 0),  # Dark Green (-5)
    (0, 153, 0),  # Green (-4)
    (0, 179, 0),  # Light Green (-3)
    (0, 204, 0),  # Lighter Green (-2)
    (0, 230, 0),  # Lightest Green (-1)
    (255, 255, 0),  # Yellow (0)
    (192, 192, 192),  # Light Grey (1)
    (128, 128, 128),  # Grey (2)
    (64, 64, 64),  # Dark Grey (3)
    (32, 32, 32),  # Darker Grey (4)
    (255, 192, 192),  # Light Red (5)
    (255, 128, 128),  # Red (6)
    (255, 64, 64),  # Dark Red (7)
    (255, 32, 32),  # Darker Red (8)
    (255, 0, 0)  # Darkest Red (9)
]

# Main loop
running = True
idx = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update eye movement based on EOG data
    horizontal_movement = df['EOG Horizontal'].iloc[idx] * scaling_factor

    # Update eyeball positions
    left_eyeball_x = left_eye_x - horizontal_movement
    right_eyeball_x = right_eye_x - horizontal_movement

    # Update retina positions based on EOG data
    left_retina_x = left_eye_x - horizontal_movement
    right_retina_x = right_eye_x - horizontal_movement

    # Clear the screen
    screen.fill((255, 255, 255))

    # Map the movement to color palette
    color_index = int(horizontal_movement + 10)  # Shift to positive range
    color_index = max(0, min(19, color_index))  # Ensure it's within the range
    color = pygame.Color(*color_palette[color_index])

    # Draw hollow eyeballs with color based on movement distance
    pygame.draw.circle(screen, color, (left_eye_x, left_eye_y), eye_radius, 1)
    pygame.draw.circle(screen, color, (right_eye_x, right_eye_y), eye_radius, 1)

    # Draw hollow outer circles (eyeballs) with color
    pygame.draw.circle(screen, color, (int(left_eyeball_x), left_eye_y), eye_radius, 1)
    pygame.draw.circle(screen, color, (int(right_eyeball_x), right_eye_y), eye_radius, 1)

    # Draw retina circles with color
    pygame.draw.circle(screen, color, (int(left_retina_x), left_eye_y), retina_radius)
    pygame.draw.circle(screen, color, (int(right_retina_x), right_eye_y), retina_radius)

    # Draw labels
    font = pygame.font.Font(None, 36)
    label_left = font.render('Left Eye', True, color)
    label_right = font.render('Right Eye', True, color)
    screen.blit(label_left, (left_eye_x - eye_radius, left_eye_y - 2 * eye_radius))
    screen.blit(label_right, (right_eye_x - eye_radius, right_eye_y - 2 * eye_radius))

    # Print information to the terminal
    print(f"Time: {df['Time'].iloc[idx]}, EOG Horizontal: {df['EOG Horizontal'].iloc[idx]}, Color: {color}")

    # Update the display
    pygame.display.flip()

    # Increment index for the next data point
    idx = (idx + 1) % len(df)

    # Control the frame rate
    clock.tick(30)  # Adjust the value to control the frame rate

pygame.quit()
