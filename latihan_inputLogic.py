
nama = input('Nama Pegawai :')
jabatan = str(input('Jabatan :'))
agama = input('Agama :')
status = input('Status Pernikahan :')
#hitung gaji dkk
if jabatan == 'Manager': gapok = 15000000
elif jabatan =='Asisten Manager': gapok = 10000000
elif jabatan == 'Supervisor': gapok = 7000000
elif jabatan == 'Staff': gapok = 4000000
else: gapok - 0
tunjab = 0.3 * gapok
bpjs = 0.1 * gapok
tunkel = (0, 0.1 * gapok)[status == 'Ya']
gator = gapok + tunjab + bpjs + tunkel
zakat = (0, 0.025 * gator)[agama == 'Islam' and gator >= 7000000]
takehomepay = gator - zakat

print('Nama Pegawai\t\t: %s'
    '\nJabatan\t\t\t: %s'
    '\nAgama\t\t\t: %s'
    '\nStatus Pernikahan\t: %s'
    '\nGaji Pokok\t\t: Rp. %i'
    '\nTunjangan Jabatan\t: Rp. %i'
    '\nTunjangan Keluarga\t: Rp. %i'
    '\nBPJS\t\t\t: Rp. %i'
    '\nZakat Profesi\t\t: Rp. %.2f'
    '\nTake Home Pay\t\t: Rp. %.2f'
    %(nama,jabatan,agama,status,gapok,tunjab,
    tunkel,bpjs,zakat,takehomepay)
)
