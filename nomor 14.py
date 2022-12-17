data = [0.883, 0.407, 0.363, 0.273, 0.368, 0.917, 0.673, 0.07, 0.452, 0.233,
 0.988, 0.901, 0.172, 0.237, 0.974, 0.324, 0.878, 0.698, 0.626, 0.997,
  0.206, 0.731, 0.216, 0.06, 0.453, 0.766, 0.732, 0.273, 0.876, 0.872]

R = []

# print(f"data : {data}")
#Mengurutkan data
data.sort()
R = data #Memindahkan data yang telah terurut
# print(f"data : {data}")
# print(f"R : {R}")

sementara = []
for i in range(len(data)) :
    sementara.append(round((i+1)/len(data) - R[i],2))
# print(f"D_p = {sementara}")
#Mencari D_plus
D_plus = max(sementara)
print(f"D_plus = {D_plus}")

sementara = []
for i in range(len(data)) :
    sementara.append(round(R[i] - (i)/len(data),2))
# print(f"D_m = {sementara}")
#Mencari D_min
D_min = max(sementara)
print(f"D_min = {D_min}")

D = max(D_plus,D_min)
print(f"D = {D}")