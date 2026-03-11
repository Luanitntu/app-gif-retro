#!/bin/bash

SH_DIR="$(dirname "$(readlink -f "$0")")"
GAMEDIR="$SH_DIR/GifViewerData"
cd "$GAMEDIR"

echo "--- SEARCHING FOR PYGAME ---" > log_final.txt

# 1. TÌM PORTMASTER
PM_DIR="/mnt/mmc/MUOS/PortMaster"
if [ ! -d "$PM_DIR" ]; then
    PM_DIR="/mnt/sdcard/MUOS/PortMaster"
fi

echo "Scanning inside: $PM_DIR" >> log_final.txt

# 2. QUÉT TÌM FOLDER 'pygame' (Chó nghiệp vụ hoạt động)
# Lệnh này sẽ tìm bất kỳ thư mục nào tên là "pygame" nằm trong PortMaster
TARGET_PYGAME=$(find "$PM_DIR" -type d -name "pygame" 2>/dev/null | head -n 1)

if [ -n "$TARGET_PYGAME" ]; then
    echo "FOUND PYGAME AT: $TARGET_PYGAME" >> log_final.txt
    
    # Lấy thư mục cha của nó để nạp vào Python
    PARENT_DIR=$(dirname "$TARGET_PYGAME")
    echo "Adding to path: $PARENT_DIR" >> log_final.txt
    
    export PYTHONPATH="$PARENT_DIR:$PYTHONPATH"
    
    # Một số bản Pygame cần thêm cả đường dẫn libs đi kèm
    if [ -d "$PARENT_DIR/pygame.libs" ]; then
        export LD_LIBRARY_PATH="$PARENT_DIR/pygame.libs:/usr/lib:$LD_LIBRARY_PATH"
    fi
else
    echo "CRITICAL: Quet sach se van khong thay Pygame dau ca!" >> log_final.txt
    echo "Listing pylibs content for debug:" >> log_final.txt
    ls -R "$PM_DIR/pylibs" >> log_final.txt
    
    # DỰ PHÒNG: Nếu không thấy, thử dùng lại libs cũ (nếu bạn chưa xóa)
    if [ -d "$GAMEDIR/libs" ]; then
        echo "Fallback to local libs..." >> log_final.txt
        export PYTHONPATH="$GAMEDIR/libs:$PYTHONPATH"
        export LD_LIBRARY_PATH="$GAMEDIR/libs/pygame.libs:/usr/lib:$LD_LIBRARY_PATH"
    fi
fi

# 3. CẤU HÌNH
export SDL_AUDIODRIVER=dummy
export SDL_GAMECONTROLLERCONFIG="$sdl_controllerconfig"

# 4. CHẠY
$ESUDO chmod 666 /dev/uinput
/usr/bin/python3 main.py >> log_final.txt 2>&1

sync
exit 0