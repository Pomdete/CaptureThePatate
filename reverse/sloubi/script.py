
output = '4B}mCuCNJmeVhvCzQusFHS7{2gCBCrQW'
flag = ''
for i in range(32):
    flag += output[(i * 17 + 51) % 32]

print(flag)