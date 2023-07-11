# Anime Data Crawling

Project crawl dữ liệu về anime từ trang web https://animevietsub.moe/ <br>
Project sử dụng công cụ Python Scrapy framework.

## How to run

Cài đặt Python Scrapy framework: <br>
```
  pip install scrapy
```
Project hiện tại có thể crawl data về anime bộ và anime lẻ.

**Đối với anime bộ** <br>
Sử dụng start_urls, output file và vòng lặp dưới đây trong *movie.py* 
```
  start_urls = ["https://animevietsub.moe/anime-bo/"]

  'anime_series.json' : {'format' : 'json', 'overwrite' : True}

  for i in range(1, 124):
    next_page_url = 'https://animevietsub.moe/anime-bo/trang-' + str(i) + '.html'
    yield response.follow(next_page_url, callback=self.parse)
```
Trong đó, range vòng lặp là *(trang bắt đầu, trang kết thúc)* cần crawl, có thể thay đổi tùy ý. 

Đồng thời thay đổi file đầu ra tương ứng trong *setting.py*
```
  'anime_series.json': {'format': 'json'}
```

**Đối với anime lẻ** <br>
Sử dụng start_urls, output file và vòng lặp dưới đây trong file *movie.py* 
```
  start_urls = ["https://animevietsub.moe/anime-le/"]
  'anime_movie.json' : {'format' : 'json', 'overwrite' : True}

  for i in range(1, 41):
    next_page_url = 'https://animevietsub.moe/anime-le/trang-' + str(i) + '.html'
    yield response.follow(next_page_url, callback=self.parse)
```
File đầu ra trong *setting.py*
```
  'anime_movie.json': {'format': 'json'}
```
**Cách chạy**
Di chuyển đến folder anime <br>
Chạy lệnh
```
  scrapy crawl movie
```
