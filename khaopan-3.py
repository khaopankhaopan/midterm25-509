กว้าง = float(input("Input กว้าง (เมตร): "))
ยาว = float(input("Input ยาว (เมตร): "))
ลึก = float(input("Input ลึก (เมตร): "))

volume = กว้าง * ยาว * ลึก

time_per_cubic_meter = 15 / 60
total_time = volume * time_per_cubic_meter

print("Time to fill the pool: {:.2f} minutes".format(total_time))
