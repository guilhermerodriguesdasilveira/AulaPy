#distancia euclidiana
x = [ 1.952 , 1.213 ,330000 ] #carro1
y = [ 1.720 , 1.940 ,23230 ]  #carro2
z = [ 2.073 , 1.803 ,92000 ]  #carro3

dist_euclidiana = sum([(xi - yi)**2 for xi, yi in zip(x, y)])**0.5
print(dist_euclidiana)


#distancia hamming
a='banheira'
b='torneira'

def hamming(a, b):
    total = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            total+=1
    return total
print( hamming(a, b) )


#distancia Manhattan
x = [ 1.952 , 1.213 ,330000 ] #carro1
y = [ 1.720 , 1.940 ,23230 ]  #carro2
dist_manhattan = sum([abs(xi - yi) for xi, yi in zip(x, y)])
print(dist_manhattan)


#distancia Minkowski
p = 3
x = [ 1.952 , 1.213 ,330000 ] #carro1
y = [ 1.720 , 1.940 ,23230 ]  #carro2
dist_minkowski = sum([abs(xi - yi)**p for xi, yi in zip(x, y)])**(1/p)
print(dist_minkowski)