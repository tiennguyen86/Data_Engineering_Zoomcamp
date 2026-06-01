# Nhận đầu vào và tạo ra 1 số đầu ra
# Nhận dữ liệu đầu vào, biến đổi nó, rồi tạo ra dữ liệu đầu ra hữu ích.
# Đưa dữ liệu từ nơi nó đang nằm đến nơi nó cần đến, dưới dạng mà người dùng cần.

import sys
import pandas as pd


# Mục đích chương trình này làm sao để truyền tham số vào chương trình từ terminal



# python3 pypeline.py --Đối số
# Nhận tham số từ dòng lệnh
# Ví dụ:
# python3 pipeline.py 1

print("arguments:", sys.argv)

# Output
#  python3 pypeline.py 1
# arguments: ['pypeline.py', '1']
# Hello, Tiến!

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df["month"] = month

print(df.head())

df.to_parquet(f"output_month_{month}.parquet")

print(f"Hello, Tiến!, month: {month}")
