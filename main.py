import os
from datetime import datetime, timedelta
import shutil

def process_videos(input_folder, move_files=False):
    for filename in os.listdir(input_folder):
        if not filename.endswith(".webm"):
            continue

        try:
            name_part, datetime_part = filename.rsplit(" ", 1)
            lastname, firstname = name_part.split(" ", 1)
            datetime_str = datetime_part.replace(".webm", "")

            dt = datetime.strptime(datetime_str, "%Y-%m-%d_%H%M%S")

            dt = dt - timedelta(hours=7)

            # Формируем название новой папки
            folder_name = f"{dt.strftime('%d.%m.%Y')} {lastname} {firstname}"
            folder_path = os.path.join(input_folder, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            src = os.path.join(input_folder, filename)
            dst = os.path.join(folder_path, filename)
            if move_files:
                shutil.move(src, dst)
            else:
                shutil.copy2(src, dst)

            print(f"Обработан: {filename} → {folder_name}")

        except Exception as e:
            print(f"Ошибка при обработке {filename}: {e}")


if __name__ == "__main__":
    input_path = "/Users/daniil/Documents/Работа"
    process_videos(input_path, move_files=True)