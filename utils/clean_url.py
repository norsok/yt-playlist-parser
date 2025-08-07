from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def clean_url(urls):
    cleaned_urls = []
    for url in urls:
        try:
            # Разбираем URL на компоненты
            parsed = urlparse(url['url'])
            
            # Разбираем параметры запроса
            query_params = parse_qs(parsed.query)
            
            # Если есть параметры запроса
            if query_params:
                # Получаем первый ключ параметра
                first_key = next(iter(query_params.keys()))
                # Оставляем только первый параметр
                new_query = {first_key: query_params[first_key]}
                # Собираем новый query
                new_query_str = urlencode(new_query, doseq=True)
                
                # Собираем URL обратно
                cleaned_url = urlunparse(
                    (parsed.scheme, parsed.netloc, parsed.path, 
                     parsed.params, new_query_str, parsed.fragment)
                )
                cleaned_urls.append(cleaned_url)
            else:
                cleaned_urls.append(url['url'])
        except Exception as e:
            print(f"Ошибка при обработке URL {url['url']}: {e}")
            cleaned_urls.append(url['url'])  # Возвращаем исходный URL в случае ошибки
    
    return cleaned_urls
 
# Исходный URL
# url = 'https://www.youtube.com/watch?v=X24V-yukt1k&list=PLosWRcTJZf2rFH_EY4p1B4VO2GGLJ2zlN&index=1&pp=iAQB'

# # Очищаем URL
# cleaned_url = clean_url(url)
# print(cleaned_url)