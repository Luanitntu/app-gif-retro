# Hướng dẫn cài đặt cho muOS (RG35XX H)

## Cấu trúc thư mục đề xuất:
`/mnt/mmc/MUOS/application/GifViewer/`
├── `main.py`
├── `launcher.sh`
└── `images/`
    └── `earth.gif`

## Các bước cài đặt:
1. Copy toàn bộ thư mục `GifViewer` vào đường dẫn `/mnt/mmc/MUOS/application/` trên thẻ nhớ SD1.
2. Cấp quyền thực thi cho file launcher: `chmod +x launcher.sh` (thường muOS tự xử lý nếu chạy qua Explorer).
3. Truy cập **Applications** -> **GifViewer** trên máy để chạy.

## Lưu ý về thư viện:
Máy cần có sẵn `python3`, `pygame` và `pillow`. Nếu chưa có, bạn có thể cần cài đặt qua Task Manager hoặc Script cài đặt của cộng đồng muOS.
