#!/usr/bin/env python3
"""
Script to create a circular version of the Isonga logo with blue background
"""

from PIL import Image, ImageDraw
import os

# Paths
logo_path = "core/static/img/isongalogo.png"
output_path = "core/static/img/isongalogo.png"

# Create circular logo with blue background
size = 256
bg_color = "#1d8fe1"  # Primary blue from your site

# Open original logo
logo = Image.open(logo_path).convert("RGBA")

# Create circular base with background
circular = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(circular)

# Draw blue circle
draw.ellipse([0, 0, size-1, size-1], fill=bg_color)

# Resize and center logo
logo_size = int(size * 0.7)
logo_resized = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

x = (size - logo_size) // 2
y = (size - logo_size) // 2

circular.paste(logo_resized, (x, y), logo_resized)

# Save
circular.save(output_path, "PNG")
print(f"✓ Circular logo created and saved to: {output_path}")
