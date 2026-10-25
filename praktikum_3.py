nilai = 70
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

lulus = syarat_nilai or syarat_kehadiran

print("Nilai:", nilai)
print("Kehadiran:", kehadiran)
print("Memenuhi syarat nilai:", syarat_nilai)
print("Memenuhi syarat kehadiran:", syarat_kehadiran)
print("Status lulus:", lulus)