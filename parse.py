# Class For Storing Rectangle Data
class Rectangle:
    def __init__(self, XStart, YStart, ZStart, Width, Height):
        self.XStart = XStart
        self.YStart = YStart
        self.ZStart = ZStart
        self.Width  = Width
        self.Height = Height
    
    def __str__(self):
        return "XStart: {}\nYStart: {}\nZStart: {}\nWidth: {}\nHeight: {}\n".format(self.XStart, self.YStart, self.ZStart, self.Width, self.Height)
    
class Substrate:
    def __init__(self, Height, Thickness, LossTangent, Permittivity, Rectangle):
        self.Height = Height
        self.Thickness = Thickness
        self.LossTangent = LossTangent
        self.Permittivity = Permittivity
        self.Rectangle = Rectangle

    def __str__(self):
        return "Height: {}\Thickness: {}\LossTangent: {}\nPermittivity: {}".format(self.Height, self.Thickness, self.LossTangent, self.Permittivity)

# Parse .pcb file
def parse(filename):

    f = open(filename, "r")
    lines = f.read().split('\n')

    # Extract Rectangle Data
    rectangle_data = []
    substrate_data = ""
    for line in lines:
        if (line.startswith("Rectangle")):
            rectangle_data.append(line.split(' ', 2)[2])
        elif (line.startswith("Substrate")):
            substrate_data = line.split('=', 1)[1]

    # Load Rectangle Data Into Class
    XMin = 0.0
    XMax = 0.0
    YMin = 0.0
    YMax = 0.0
    rectangles = []
    for rectangle in rectangle_data:
        parts = rectangle.split(' ')
        XOffset = float(parts[0])
        YOffset = float(parts[1])
        for part in parts[2:]:
            coords = part.split('|')
            XStart = float(coords[0]) + XOffset
            YStart = float(coords[1]) + YOffset
            Width = float(coords[2])
            Height = float(coords[3])
            XMin = min(XMin, XStart)
            XMax = max(XMax, XStart + Width)
            YMin = min(YMin, YStart)
            YMax = max(YMax, YStart + Height)
            rectangles.append(Rectangle(XStart, YStart, 0, Width, Height))
    
    # Load Substrate Data Into Class
    parts = substrate_data.split('|')
    Height = parts[2]
    Thickness = float(parts[5].split(' ')[0]) * 1e-6
    LossTangent = parts[3]
    Permittivity = parts[1]
    BoundingBox = Rectangle(XMin, YMin, 0, XMax - XMin, YMax - YMin)
    print(Permittivity)
    return rectangles, Substrate(Height, Thickness, LossTangent, Permittivity, BoundingBox)

if __name__ == '__main__':
    parse("design.pcb")