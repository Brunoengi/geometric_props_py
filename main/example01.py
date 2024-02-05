
from geometricProps import GeometricProps

rectangulo = GeometricProps(
    [
        {'x':0, 'y':0}, 
        {'x':20, 'y':0},
        {'x':20, 'y':60},
        {'x':0, 'y':60},
        {'x':0, 'y':0},
    ])

print("Xmax: ", round(rectangulo.Xmax, 2), ' cm')
print("Xmin: ", round(rectangulo.Xmin, 2), ' cm')
print("Ymin: ", round(rectangulo.Ymax, 2), ' cm')
print("Ymax: ", round(rectangulo.Ymin, 2), ' cm')
print("A: ", round(rectangulo.A, 2), ' cm²')
print("Sx: ", round(rectangulo.Sx, 2), ' cm³' )
print("Sy: ", round(rectangulo.Sy, 2), ' cm³' )
print("Ix: ", round(rectangulo.Ix, 2), ' cm⁴')
print("Iy: ", round(rectangulo.Iy, 2), ' cm⁴')
print("Ixy: ", round(rectangulo.Ixy, 2), ' cm⁴')
print("Xg: ", round(rectangulo.Xg, 2), ' cm')
print("Yg ", round(rectangulo.Yg, 2), ' cm')
print("Ixg: ", round(rectangulo.Ixg, 2), ' cm⁴')
print("Iyg: ", round(rectangulo.Iyg, 2), ' cm⁴')
print("Ixyg ", round(rectangulo.Ixyg, 2), ' cm⁴')
print('Y1: ', round(rectangulo.Y1,2), ' cm')
print('Y2: ', round(rectangulo.Y2, 2), ' cm')
print('W1: ', round(rectangulo.W1, 2), ' cm³')
print('W2: ', round(rectangulo.W2, 2), ' cm³')
print('h: ', round(rectangulo.h, 2), ' cm')