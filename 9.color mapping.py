regions = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}
colors = ["Red", "Green", "Blue"]
def assign_colors(region, color_map):
    if region == len(regions):
        return True
    region_name = list(regions.keys())[region]
    for color in colors:
        if all(color_map.get(neighbor) != color for neighbor in regions[region_name]):
            color_map[region_name] = color
            if assign_colors(region + 1, color_map):
                return True
            color_map.pop(region_name)
    return False
color_map = {}
assign_colors(0, color_map)
print("Color Assignments:", color_map)
