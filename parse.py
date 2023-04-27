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

# Parse .pcb file
def parse(filename):
    f = open(filename, "r")
    lines = f.read().split('\n')

    # Extract Rectangle Data
    rectangle_data = []
    for line in lines:
        if (line.startswith("Rectangle")):
            rectangle_data.append(line.split(' ', 2)[2])    

    # Load Data Into Class
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
            rectangles.append(Rectangle(XStart, YStart, 0, Width, Height))
    return rectangles

if __name__ == '__main__':
    parse("design.pcb")