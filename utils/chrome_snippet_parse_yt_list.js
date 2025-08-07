// Скрипт для парсинга списка видео в плейлисте YT
const play_list_items = document.querySelectorAll('.playlist-items #wc-endpoint.ytd-playlist-panel-video-renderer')

const play_list_url = []
play_list_items.forEach(item => play_list_url.push(item.href))

// Если нужно исключить ролики
const not_indexs = [0]
play_list_items.forEach((item, idx) => {
  if (!not_indexs.includes(idx)) play_list_url.push(item.href)
})

// console.log('play_list_url ', play_list_url)

// ================================

const video_title = document.querySelectorAll('.playlist-items #meta #video-title')

video_title.forEach(title => {
  // console.log('video_title ', title.title)
})
// console.log('video_title ', video_title)

// ================================

const video_channel = document.querySelectorAll('.playlist-items #meta #byline')

video_channel.forEach(channel => {
  console.log('channel ', channel.innerText)
})
// console.log('video_title ', video_title)
