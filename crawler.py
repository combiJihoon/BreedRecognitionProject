from google_images_download import google_images_download  # importing the library

response = google_images_download.googleimagesdownload()  # class instantiation

celebrities = [
    "한지민",
    "강민경",
    "조세호",
    "서인국",
    "전현무",
    "김혜수",
    "백종원",
    "안소희",
    "뷔",
    "김범수",
    "수지",
    "비",
    "강다니엘",
    "박명수",
    "이상윤",
    "박보검",
    "고창석"
]


def downloadimages(query):
    arguments = {"keywords": query,
                 "format": "jpg",
                 "limit": 30,
                 "print_urls": True,
                 "size": "medium",
                 "aspect_ratio": "panoramic"}

    response.download(arguments)


for query in celebrities:
    downloadimages(query)
