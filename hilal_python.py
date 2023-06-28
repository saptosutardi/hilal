#ditulis oleh dr. Sapto Sutardi
#dokter dan penyuka teknologi

import ephem
import math
from datetime import datetime, timedelta

# Membuat observer (pengamat)
observer = ephem.Observer()
observer.lon = '116:08'  # Long: 116:08
observer.lat = '-08:36'  # Lat: -08:36
observer.elevation = 0   # Ketinggian pengamat dalam meter
observer.pressure = 0    # Tekanan atmosfer dalam mbar
observer.horizon = '-0:34'  # Horizon yang digunakan (-0:34 merupakan nilai yang sering digunakan untuk hilal)

# Menentukan tanggal pengamatan
date = '2023/06/18'

# Menghitung waktu terbenam matahari berdasarkan waktu lokal
sun = ephem.Sun()
observer.date = date
sunset = observer.next_setting(sun)
sunset_local_time = ephem.localtime(sunset).time().strftime("%H:%M")

# Menghitung waktu terbenam bulan berdasarkan waktu lokal
moon = ephem.Moon()
observer.date = date
moonset = observer.next_setting(moon)
moonset_local_time = ephem.localtime(moonset).time().strftime("%H:%M")

# Menghitung ketinggian bulan saat matahari tenggelam
observer.date = sunset
moon.compute(observer)
moon_altitude_deg = round(math.degrees(float(moon.alt)), 1)

# Menghitung waktu konjungsi (bertemunya bulan dan matahari)
conjunction = observer.previous_transit(moon)
conjunction_local_time = ephem.localtime(conjunction).time().strftime("%H:%M")

# Menghitung usia bulan (selisih waktu antara tenggelam bulan dan waktu konjungsi)
moonset_time = datetime.strptime(moonset_local_time, "%H:%M")
conjunction_time = datetime.strptime(conjunction_local_time, "%H:%M")
moon_age_timedelta = moonset_time - conjunction_time
moon_age_hours = moon_age_timedelta.seconds // 3600
moon_age_minutes = (moon_age_timedelta.seconds // 60) % 60
moon_age = "{:02d}:{:02d}".format(moon_age_hours, moon_age_minutes)

# Menghitung selisih waktu antara moonset_local_time dan sunset_local_time
moonset_time = datetime.strptime(moonset_local_time, "%H:%M")
sunset_time = datetime.strptime(sunset_local_time, "%H:%M")
time_diff = moonset_time - sunset_time
time_diff_hours = time_diff.seconds // 3600
time_diff_minutes = (time_diff.seconds // 60) % 60
time_diff_str = "{:02d}:{:02d}".format(time_diff_hours, time_diff_minutes)

# Menampilkan hasil
print("Waktu terbenam matahari (waktu lokal):", sunset_local_time)
print("Waktu terbenam bulan (waktu lokal):", moonset_local_time)
print("Ketinggian bulan saat matahari tenggelam:", moon_altitude_deg, "derajat")
print("Usia bulan:", moon_age)
print("Selisih waktu antara moonset dan sunset:", time_diff_str)
