def contains_title(title_viveo, speakers_names):
    # print('title_viveo ', title_viveo)
    # print('speakers_names ', speakers_names)
    title_viveo_lower = title_viveo.lower()
    for index, speaker in enumerate(speakers_names):
        if speaker.lower() in title_viveo_lower:
            return (True, index)
    return (False, -1)

speakers_names = [
    "Алексашенко",
    "Белковский",
    "Белковским",
    "Военный обзор",
    "Крутихин",
    "Крутихиным",
    "Курников",
    "Липсиц",
    "Милов",
    "Осечкин",
    "Осечкиным",
    "Пивоваров",
    "Пивоваровым",
    "Портников",
    "Федоров",
    "Шейтельман",
    "Фельштинский",
    "Фельштинским",
    "Шульман",
    "Яковина"
]