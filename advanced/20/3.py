import asyncio

import requests
from bs4 import BeautifulSoup


async def get__content(url_to_fetch):
    return requests.get(url_to_fetch).content


async def info(movie):
    all_a_tag = movie.find_all('a')
    all_li_tag = movie.find_all('li')

    movie_name = all_a_tag[1].text
    url_to_fetch = all_a_tag[1]['href']
    movie_date = all_li_tag[0].text

    response_item = await get__content(url_to_fetch)
    soup_item = BeautifulSoup(response_item, 'lxml')
    img_tag = soup_item.find('img')

    print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = requests.get(url).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id="showing-soon")
    tasks = [asyncio.create_task(info(each_movie)) for each_movie in all_movies.find_all('div', class_="item")]
    await asyncio.gather(*tasks)


asyncio.run(main())
