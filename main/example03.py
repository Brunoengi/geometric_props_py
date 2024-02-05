
from geometricProps import GeometricProps

sectionBox = GeometricProps(
    [
        {'x':300, 'y':0},   
        {'x':300, 'y':250}, 
        {'x':320, 'y':270}, 
        {'x':598, 'y':270}, 
        {'x':598, 'y':296}, 
        {'x':0, 'y':300},   
        {'x':-598, 'y':296},
        {'x':-598, 'y':270},
        {'x':-320, 'y':270},
        {'x':-300, 'y':250},
        {'x':-300, 'y':0},  
        {'x':300, 'y':0},   
        {'x':275, 'y':25},  
        {'x':-275, 'y':25}, 
        {'x':-275, 'y':250},
        {'x':-255, 'y':270},
        {'x':255, 'y':270}, 
        {'x':275, 'y':250}, 
        {'x':275, 'y':25},  
        {'x':300, 'y':0},   
    ])

print("Xmax: ", round(sectionBox.Xmax, 2), ' cm')
print("Xmin: ", round(sectionBox.Xmin, 2), ' cm')
print("Ymin: ", round(sectionBox.Ymax, 2), ' cm')
print("Ymax: ", round(sectionBox.Ymin, 2), ' cm')
print("A: ", round(sectionBox.A, 2), ' cm²')
print("Sx: ", round(sectionBox.Sx, 2), ' cm³' )
print("Sy: ", round(sectionBox.Sy, 2), ' cm³' )
print("Ix: ", round(sectionBox.Ix, 2), ' cm⁴')
print("Iy: ", round(sectionBox.Iy, 2), ' cm⁴')
print("Ixy: ", round(sectionBox.Ixy, 2), ' cm⁴')
print("Xg: ", round(sectionBox.Xg, 2), ' cm')
print("Yg ", round(sectionBox.Yg, 2), ' cm')
print("Ixg: ", round(sectionBox.Ixg, 2), ' cm⁴')
print("Iyg: ", round(sectionBox.Iyg, 2), ' cm⁴')
print("Ixyg ", round(sectionBox.Ixyg, 2), ' cm⁴')
print('Y1: ', round(sectionBox.Y1,2), ' cm')
print('Y2: ', round(sectionBox.Y2, 2), ' cm')
print('W1: ', round(sectionBox.W1, 2), ' cm³')
print('W2: ', round(sectionBox.W2, 2), ' cm³')
print('h: ', round(sectionBox.h, 2), ' cm')