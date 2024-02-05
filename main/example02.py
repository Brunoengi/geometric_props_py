
from geometricProps import GeometricProps

sectionTWithCorbels = GeometricProps(
    [
        {'x':30, 'y':0}, 
        {'x':30, 'y':40},
        {'x':10, 'y':60},
        {'x':10, 'y':120},
        {'x':40, 'y':130},
        {'x':40, 'y':150},
        {'x':-40, 'y':150},
        {'x':-40, 'y':130},
        {'x':-10, 'y':120},
        {'x':-10, 'y':60},
        {'x':-30, 'y':40},
        {'x':-30, 'y':0},
        {'x':30, 'y':0},
    ])

print("Xmax: ", round(sectionTWithCorbels.Xmax, 2), ' cm')
print("Xmin: ", round(sectionTWithCorbels.Xmin, 2), ' cm')
print("Ymin: ", round(sectionTWithCorbels.Ymax, 2), ' cm')
print("Ymax: ", round(sectionTWithCorbels.Ymin, 2), ' cm')
print("A: ", round(sectionTWithCorbels.A, 2), ' cm²')
print("Sx: ", round(sectionTWithCorbels.Sx, 2), ' cm³' )
print("Sy: ", round(sectionTWithCorbels.Sy, 2), ' cm³' )
print("Ix: ", round(sectionTWithCorbels.Ix, 2), ' cm⁴')
print("Iy: ", round(sectionTWithCorbels.Iy, 2), ' cm⁴')
print("Ixy: ", round(sectionTWithCorbels.Ixy, 2), ' cm⁴')
print("Xg: ", round(sectionTWithCorbels.Xg, 2), ' cm')
print("Yg ", round(sectionTWithCorbels.Yg, 2), ' cm')
print("Ixg: ", round(sectionTWithCorbels.Ixg, 2), ' cm⁴')
print("Iyg: ", round(sectionTWithCorbels.Iyg, 2), ' cm⁴')
print("Ixyg ", round(sectionTWithCorbels.Ixyg, 2), ' cm⁴')
print('Y1: ', round(sectionTWithCorbels.Y1,2), ' cm')
print('Y2: ', round(sectionTWithCorbels.Y2, 2), ' cm')
print('W1: ', round(sectionTWithCorbels.W1, 2), ' cm³')
print('W2: ', round(sectionTWithCorbels.W2, 2), ' cm³')
print('h: ', round(sectionTWithCorbels.h, 2), ' cm')