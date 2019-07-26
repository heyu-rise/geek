# Python并发编程之Futures https://time.geekbang.org/column/article/102562
import time
from concurrent import futures

import requests


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    # for url in sites:
    #     download_one(url)
    # with futures.ProcessPoolExecutor() as pool:
    #     pool.map(download_one, sites)
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
        for future in to_do:
            future.result()


def main():
    sites = [
        'https://movie.douban.com/subject/26884354/',
        'https://movie.douban.com/subject/26931786/',
        'https://movie.douban.com/subject/30171425/',
        'https://movie.douban.com/subject/26848167/',
        'https://movie.douban.com/subject/26884354/',
        'https://movie.douban.com/subject/1291561/',
        'https://movie.douban.com/subject/30211551/',
        'https://movie.douban.com/subject/26794701/',
        'https://movie.douban.com/subject/30140229/'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
