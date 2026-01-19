import matplotlib.pyplot as plt

file1_data = []
plane1 = []

with open("file1.txt") as f:
    for i in f:
        file1_data.append(float((i)))

fuel_plane1 = 0
k_plane1 = 0

for i in range(len(file1_data) - 1):
    fuel_plane1 += file1_data[i] - file1_data[i + 1]
    k_plane1 += 1
    plane1.append([fuel_plane1,k_plane1])

file2_data = []
plane2 = []

with open("file2.txt") as f:
    for i in f:
        file2_data.append(float((i)))

fuel_plane2 = 0
k_plane2 = 0

for i in range(len(file2_data) - 1):
    fuel_plane2 += file2_data[i] - file2_data[i + 1]
    k_plane2 += 1
    plane2.append([fuel_plane2,k_plane2])

x1 = []
y1 = []

x1_2 = []
y1_2 = []

for i in plane1:
    y1.append(i[0])
    x1.append(i[1])
    if i[1] > 250:
        y1_2.append(i[0])
        x1_2.append(i[1])

x2 = []
y2 = []

x2_2 = []
y2_2 = []

for i in plane2:
    y2.append(i[0])
    x2.append(i[1])
    if i[1] > 250:
        y2_2.append(i[0])
        x2_2.append(i[1])

mass_dif = []
for i in range(1,299):
    mass_dif.append([plane1[i][0] - plane2[i][0],i])

x_mass = []
y_mass = []

for i in mass_dif:
    x_mass.append(i[1])
    y_mass.append(i[0])

plt.figure(1)
plt.title('Общий график')
plt.xlabel('Время(с)')
plt.ylabel('Масса потраченного топлива(кг)')
plt.plot(x1, y1, color='red')
plt.plot(x2, y2, color='blue')

plt.figure(2)
plt.title('Детальный график')
plt.xlabel('Время(с)')
plt.ylabel('Масса потраченного топлива(кг)')
plt.plot(x1_2, y1_2, color='red')
plt.plot(x2_2, y2_2, color='blue')

plt.figure(3)
plt.title('График разницы массы самолетов')
plt.xlabel('Время(с)')
plt.ylabel('Масса (кг)')
plt.plot(x_mass, y_mass, color='green')
plt.show()
