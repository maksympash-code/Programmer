from pytube import YouTube

video_url = "https://youtu.be/GxEi5NMxmFs?si=kDEhUGIxqqkQ74Gh"
save_location = r"D:\Програмування\Відео"

yt = YouTube(video_url)

# Вивід наявних стрімів для налагодження
print("Доступні стріми:")
for stream in yt.streams:
    print(stream)

# Фільтрація потрібного стріму
stream = yt.streams.filter(res="720p", progressive = True).first()

if stream:
    print("Завантаження:", stream)
    stream.download(save_location)
    print("Завантаження завершено!")
else:
    print("Стрім з заданими параметрами не знайдено.")
