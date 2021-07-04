anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)

print(f'halo {anak[0]}')

# for untuk list

for a in anak:
    print(f'halo {a}')


print('\nSapa Semua anak : cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')