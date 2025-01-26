import random
import colorsys


def generate_random_palette(num_colors=6):
    base_hue = random.random()
    golden_ratio = 0.618033988749895

    colors = []
    for i in range(num_colors - 1):
        hue = (base_hue + golden_ratio * i + random.uniform(-0.05, 0.05)) % 1.0
        saturation = min(1.0, max(0.5, 0.7 + random.uniform(-0.2, 0.2)))
        value = min(1.0, max(0.5, 0.9 + random.uniform(-0.3, 0.1)))
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        colors.append([int(x * 255) for x in rgb])

    # Add complementary color
    complement_hue = (base_hue + 0.5 + random.uniform(-0.05, 0.05)) % 1.0
    rgb = colorsys.hsv_to_rgb(complement_hue, 0.8, 0.8)
    colors.append([int(x * 255) for x in rgb])

    return colors


# Generate 10 random palettes
for i in range(10):
    palette = generate_random_palette()
    print(f"\nPalette {i + 1}:")
    for color in palette:
        print(f"RGB: {color}")