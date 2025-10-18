for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print('-')

# nested loop while
string = "-"
bar = 1
# Looping Baris
while bar <= 5:
    kol = bar
# Looping Kolom
    while kol > 0:
        string += "*"
        kol = kol - 1
    string += "\n"
    bar = bar + 1
print (string)

# string = "-"
# bar = 1
# # Looping Baris
# while bar <= 5:
#     kol = bar
# # Looping Kolom
#     while kol > 0:
#         string += "*"
#         kol = kol - 1
#     string += "\n"
#     bar = bar + 1
# print (string)

a = 6
for i in range(0, a):
    for j in range(0, a - 1):
        print('*', end='')
    a -= 1
    print('')

a = 5
s = a - 1 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ', end='')
    s -= 1
    for j in range(0, i + 1):
        print('* ', end='')
    print('')