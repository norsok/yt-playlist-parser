from utils.contains_title import contains_title, speakers_names

def get_speaker_from_title(title):
    """
    Определяет имя спикера из заголовка видео.
    
    :param title: Заголовок видео
    :return: Строку с именем спикера или пустую строку
    """
    found, index = contains_title(title, speakers_names)

    if found:
        return f"{speakers_names[index]}"
    return ""