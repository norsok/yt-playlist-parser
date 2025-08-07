import yt_dlp
import time
# from yt_dlp.utils import DownloadError
from yt_dlp import DownloadError
import os
from config_loader import CONFIG as config
from youtube_url_list.url_list_1 import playList_urls
from utils.clean_url import clean_url
from utils.get_speaker_from_title import get_speaker_from_title

 


def download_youtube_audio(urls = [], output_path="."):
    """
    Скачивает аудио с YouTube в формате MP3 используя yt-dlp
    
    :param url: Ссылка на YouTube видео
    :param output_path: Папка для сохранения (по умолчанию текущая)
    :return: Путь к сохраненному MP3 файлу
    """

    # Настройки для скачивания аудио
    ydl_opts = {
        'format': 'bestaudio/best',  # Скачать лучшее аудио
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': config['audio_quality'], # 192
        }],
        'quiet': False,
        'retries': 10,  # Increase retry attempts
        'file_access_retries': 10,  # Specifically for file access issues
        'retry_sleep_functions': {'file_access': lambda x: 2},  # Wait 2 seconds between retries
        'updatetime': False,
    }

    # Скачиваем и конвертируем каждое видео
    total_count = 0
    ready_count = 0
    for index, url in enumerate(urls, start=1): 
        total_count += 1
        retries = 3
        while retries > 0:
            try:
                with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
                    info = ydl.extract_info(url, download=False)
                    title = info.get('title', '')
                    speaker_prefix = get_speaker_from_title(title)

                # Динамически формируем outtmpl с номером файла и именем спикера
                current_ydl_opts = ydl_opts.copy()
                current_ydl_opts['outtmpl'] = os.path.join(
                    output_path,
                    f'{config["date_in_title"]} {speaker_prefix} %(channel)s - %(title).{config["title_length"]}s.%(ext)s'
                    if config['isUse_date_in_title'] 
                    else f'{index} {speaker_prefix} %(title).{config["title_length"]}s.%(ext)s'
                )

                with yt_dlp.YoutubeDL(current_ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    mp3_file = os.path.splitext(filename)[0] + '.mp3'
                
                ready_count += 1
                print(f"Аудио успешно сохранено как: {mp3_file}")
                break
            except DownloadError as e:
                if "Unable to rename file" in str(e):
                    retries += 1
                    if retries == 0:
                        print(f"Ошибка при обработке {url}: {e}")
                    else:
                        print(f"Ошибка доступа к файлу, попытка {3-retries}/3...")
                        time.sleep(5)  # Wait 5 seconds before retry
                else:
                    print(f"Ошибка при обработке {url}: {e}")
                    break
            except Exception as e:
                print(f"Ошибка при обработке {url}: {e}")
                break

    print(f"____ Все видео обработаны! ____  / Кол-во: {ready_count} из {total_count}")

if __name__ == "__main__":
  print("Скачиваем аудио... Кол-во:", len(playList_urls))
  download_path = f"{config['download_root_path']}/{config['download_folder']}"
  cleaned_urls = clean_url(playList_urls)
  download_youtube_audio(cleaned_urls, download_path)