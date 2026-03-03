#!/usr/bin/env python3
"""
Generate a simple emoji 😎 3D model in OBJ format
"""

# Face (sphere)
def generate_face():
    points = []
    faces = []
    
    # Simple sphere approximation - just use a flat circle with emoji features
    # Center
    cx, cy, cz = 0, 0, 0
    radius = 50
    
    # Generate face circle
    for i in range(37):
        angle = i * 10 * 3.14159 / 180
        x = cx + radius * (1 if i == 0 else 1)
        y = cy + radius * 0.8
        z = cz + 5
        points.append((x, y, z))
    
    # Sunglasses
    # Left lens
    points.extend([
        (-35, 5, 10), (-35, -5, 10), (-20, 5, 10), (-20, -5, 10),  # left lens
        (-35, 5, 15), (-35, -5, 15), (-20, 5, 15), (-20, -5, 15),
    ])
    
    # Right lens
    points.extend([
        (20, 5, 10), (20, -5, 10), (35, 5, 10), (35, -5, 10),
        (20, 5, 15), (20, -5, 15), (35, 5, 15), (35, -5, 15),
    ])
    
    # Smile
    for i in range(11):
        angle = (i - 5) * 0.15
        x = -15 + i * 3
        y = -20 - (15 - abs(i - 5)) * 0.8
        z = 8
        points.append((x, y, z))
    
    return points

# Let's create a simpler emoji - just use basic shapes
obj_content = """# Emoji 😎 3D Model
# Generated for 3D printing

# Sunglasses - Left lens (box)
v -35.0 5.0 10.0
v -35.0 -5.0 10.0
v -20.0 5.0 10.0
v -20.0 -5.0 10.0
v -35.0 5.0 15.0
v -35.0 -5.0 15.0
v -20.0 5.0 15.0
v -20.0 -5.0 15.0

# Sunglasses - Right lens (box)
v 20.0 5.0 10.0
v 20.0 -5.0 10.0
v 35.0 5.0 10.0
v 35.0 -5.0 10.0
v 20.0 5.0 15.0
v 20.0 -5.0 15.0
v 35.0 5.0 15.0
v 35.0 -5.0 15.0

# Face (thin plate)
v -50.0 40.0 2.0
v -50.0 -40.0 2.0
v 50.0 40.0 2.0
v 50.0 -40.0 2.0
v -50.0 40.0 3.0
v -50.0 -40.0 3.0
v 50.0 40.0 3.0
v 50.0 -40.0 3.0

# Smile (curved, using small boxes)
v -20.0 -20.0 8.0
v -20.0 -30.0 8.0
v -10.0 -20.0 8.0
v -10.0 -30.0 8.0
v -20.0 -20.0 9.0
v -20.0 -30.0 9.0
v -10.0 -20.0 9.0
v -10.0 -30.0 9.0

v -10.0 -18.0 8.0
v -10.0 -28.0 8.0
v 0.0 -18.0 8.0
v 0.0 -28.0 8.0
v -10.0 -18.0 9.0
v -10.0 -28.0 9.0
v 0.0 -18.0 9.0
v 0.0 -28.0 9.0

v 0.0 -16.0 8.0
v 0.0 -26.0 8.0
v 10.0 -16.0 8.0
v 10.0 -26.0 8.0
v 0.0 -16.0 9.0
v 0.0 -26.0 9.0
v 10.0 -16.0 9.0
v 10.0 -26.0 9.0

v 10.0 -18.0 8.0
v 10.0 -28.0 8.0
v 20.0 -18.0 8.0
v 20.0 -28.0 8.0
v 10.0 -18.0 9.0
v 10.0 -28.0 9.0
v 20.0 -18.0 9.0
v 20.0 -28.0 9.0

# Faces
f 1 2 4 3
f 5 6 8 7
f 1 2 6 5
f 3 4 8 7
f 1 3 7 5
f 2 4 8 6

f 9 10 12 11
f 13 14 16 15
f 9 10 14 13
f 11 12 16 15
f 9 11 15 13
f 10 12 16 14

f 17 18 20 19
f 21 22 24 23
f 17 18 22 21
f 19 20 24 23
f 17 19 23 21
f 18 20 24 22
"""

with open('/Users/sheeepsheepmac/Desktop/emoji_cool.obj', 'w') as f:
    f.write(obj_content)

print("Generated emoji_cool.obj")
