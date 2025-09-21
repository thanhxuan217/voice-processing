# Python version: 3.10
# Hướng dẫn chạy code để tạo sách daisy
Bước 1: Chuẩn bị file audio và doc
1.1 Tạo thư mục audio và tải file .mp3 vào thư mục, đặt tên dưới dạng: Thuy-Hu-{hoi}.mp3
Ví dụ: audio/Thuy-Hu-68.mp3
1.2 Tạo thư mục chứa file doc chứa các file docx của các hồi tương ứng, đặt tên dưới dạng: Hoi{hoi}.docx
Ví dụ: doc/Hoi1.docx
Bước 3: Cài đặt môi trường và các thư viện cần thiết
# $ conda create --name <env> --file requirements.txt
Bước 4: Tải model LLMA về máy 
# Mục đích của bước này là LLM correct chính tả dựa trên reference từ file docx
# $ ollama pull llama3
Bước 5: Mở file dasy_pipeline.py và chỉnh sửa range (Range này chứa số các hồi)
Ví dụ như bạn chỉ muốn test hồi 1, hãy chỉnh range thành range = range(1, 2)
Nhóm đã có để 1 đoạn file test cho hồi 1
Bước 6: Kiểm thử book bằng Easy Reader
