from geometricProps import GeometricProps

retangulo = GeometricProps(
    [
        {'x':0, 'y':0}, 
        {'x':60, 'y':0},
        {'x':60, 'y':60},
        {'x':0, 'y':20},
        {'x':0, 'y':0},
    ])

print("O valor máximo referente ao eixo X é", retangulo.Xmax)
print("O valor mínimo referente ao eixo X é", retangulo.Xmin)

print("O valor máximo referente ao eixo Y é", retangulo.Ymax)
print("O valor mínimo referente ao eixo Y é", retangulo.Ymin)

print("O valor da área é: ", retangulo.A)
print("O valor do momento estático em relação ao eixo x é: ", retangulo.Sx)
print("O valor do momento estático em relação ao eixo y é: ", retangulo.Sy)

print("O valor do momento de inérica em relação ao eixo x é: ", retangulo.Ix)
print("O valor do momento de inérica em relação ao eixo y é: ", retangulo.Iy)
print("O valor do momento de inérica em relação ao eixo xy é: ", retangulo.Ixy)

print("O valor do centroide em relação ao eixo x é: ", retangulo.Xg)
print("O valor do centroide em relação ao eixo y é: ", retangulo.Yg)

print("O valor da inércia em relação ao centroide em x é: ", retangulo.Ixg)
print("O valor da inércia em relação ao centroide em y é: ", retangulo.Iyg)
print("O valor da inércia em relação ao centroide em xy é: ", retangulo.Ixyg)

print('A distância vertical Y1 entre o centro de gravidade e o ponto mais baixo ao longo do eixo vertical da seção transversal analisada é:', retangulo.Y1)
print('A distância vertical Y2 entre o ponto mais alto ao longo do eixo vertical e o centro de gravidade analisada é:', retangulo.Y2)

print('O módulo resistente W1 (Módulo de elasticidade para flexão (ou módulo de flexão) em relação ao eixo vertical.) é: ', retangulo.W1)
print('O módulo resistente W1 (Módulo de elasticidade para flexão (ou módulo de flexão) em relação ao eixo vertical.) é: ', retangulo.W2)

print('A altura da peça é: ', retangulo.h)