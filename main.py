import math

bok_a = 10.4

pole_kw = (bok_a * bok_a)

print(pole_kw)

bok_a = 3
bok_b = 7
bok_c = 5
wys_c = 2

pole_kw = (bok_a*bok_a)
pole_tr = (bok_b*bok_b*math.sqrt(3)/4)
pole_pr = (bok_a*bok_c)
pole_tr = (bok_c*wys_c)

print(pole_kw, pole_tr, pole_pr, pole_tr)

bok_x = 6
bok_y = 8
bok_z = 9

wys_alfa = 7.89
promien_alfa = 3.34

wys_beta = 9.6
promien_beta = 2.7

obj_prostopadloscian = (bok_x * bok_y * bok_z)
obj_walec = (math.pi * promien_alfa * promien_alfa * wys_alfa)
obj_stozek = (math.pi * promien_beta * promien_beta * wys_beta /3)

print (obj_prostopadloscian, obj_walec, obj_stozek)