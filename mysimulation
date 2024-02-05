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

# Main loop
running = True
idx = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update eye movement based on EOG data
    horizontal_movement = df['EOG Horizontal'].iloc[idx] * scaling_factor

    # Clear the screen
    screen.fill((255, 255, 255))

    # Set color based on movement distance
    if -10 <= horizontal_movement <= -8:
        color = "#000080"  # Dark Blue (-10 to -8)
    elif -8 < horizontal_movement <= -6:
        color = "#000099"  # Blue (-8 to -6)
    elif -6 < horizontal_movement <= -4:
        color = "#0000B3"  # Light Blue (-6 to -4)
    elif -4 < horizontal_movement <= -2:
        color = "#0000CC"  # Lighter Blue (-4 to -2)
    elif -2 < horizontal_movement < 0:
        color = "#0000E6"  # Lightest Blue (-2 to 0)
    elif 0 <= horizontal_movement < 2:
        color = "#00E600"  # Lightest Green (0 to 2)
    elif 2 <= horizontal_movement <= 4:
        color = "#00CC00"  # Lighter Green (2 to 4)
    elif 4 < horizontal_movement <= 6:
        color = "#00B300"  # Light Green (4 to -6)
    elif 6 < horizontal_movement <= 8:
        color = "#009900"  # Green (6 to 8)
    elif 8 < horizontal_movement <= 10:
        color = "#008000"  # Dark Green (8 to 10)
    else:
        color = "#FF0000"  # Darkest Red (outside of range)

    # Draw hollow eyeballs with color based on movement distance
    pygame.draw.circle(screen, pygame.Color(color), (left_eye_x, left_eye_y), eye_radius, 1)
    pygame.draw.circle(screen, pygame.Color(color), (right_eye_x, right_eye_y), eye_radius, 1)

    # Draw hollow outer circles (eyeballs) with color
    pygame.draw.circle(screen, pygame.Color(color), (int(left_eye_x - horizontal_movement), left_eye_y), eye_radius, 1)
    pygame.draw.circle(screen, pygame.Color(color), (int(right_eye_x - horizontal_movement), right_eye_y), eye_radius, 1)

    # Draw retina circles with color
    pygame.draw.circle(screen, pygame.Color(color), (int(left_eye_x - horizontal_movement), left_eye_y), retina_radius)
    pygame.draw.circle(screen, pygame.Color(color), (int(right_eye_x - horizontal_movement), right_eye_y), retina_radius)

    # Draw labels
    font = pygame.font.Font(None, 36)
    label_left = font.render('Left Eye', True, pygame.Color(color))
    label_right = font.render('Right Eye', True, pygame.Color(color))
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
