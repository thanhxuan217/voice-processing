import os

# Thư mục gốc
base_dir = "./output"

# Tạo thư mục cho 18 hồi
for i in range(1, 19):
    # Tên thư mục: ./output/hoi{i}/[Thuỷ Hử] Hồi {i}
    dir_path = os.path.join(base_dir, f"hoi{i}", f"[Thuỷ Hử] Hồi {i}")
    
    # Tạo thư mục (bao gồm cả các thư mục cha nếu chưa có)
    os.makedirs(dir_path, exist_ok=True)

print("Đã tạo xong thư mục cho 18 hồi!")
