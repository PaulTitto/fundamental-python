"""
Tipe data Dictionary
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wive', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng['ayah'])
print('Data ini dikirimkan oleh server gojek untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-07-03',
    'driver_list': [{'nama': 'Eko', 'jarak': 10}, {'nama': 'DWi', 'jarak': 30},
                    {'nama': 'Tri', 'jarak': 100}, {'nama': 'catur', 'jarak': 1000}
     ]
}

print(data_dari_server_gojek)
print(f"\nDriver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"\nDriver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver Terdekat Berjarak #1{data_dari_server_gojek['driver_list'][0]['jarak']} meter")