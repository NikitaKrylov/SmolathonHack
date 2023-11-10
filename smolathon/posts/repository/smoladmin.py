import os
import urllib.request
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup
from collections import namedtuple
from django.core.files import File

from mediacore.models import ImageFile
from posts.models import EventPost

CategoryCardItem = namedtuple("CategoryCardItem", ['category', 'subcategory', 'link'])

CategoryItem = namedtuple("CategoryItem", ['name', 'url'])


class SmoladminRepository:
    urls = [
        ("https://www.smoladmin.ru/o-smolenske/turizm/obekty-obschestvennogo-pitaniya/", 'Питание'),
        ("https://www.smoladmin.ru/o-smolenske/turizm/dosug1/", 'Досуг'),
        ("https://www.smoladmin.ru/o-smolenske/turizm/dostoprimechatelnosti/", 'Достопримечательности'),
    ]
    _base_url = "https://www.smoladmin.ru"
    st_accept = "text/html"
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }

    def get_subcategories(self):
        items = [
            CategoryCardItem("Гостинницы", "Гостинницы", "https://www.smoladmin.ru/o-smolenske/turizm/gostinicy/")
        ]

        for url, category in self.urls:
            response = requests.get(url, headers=self.headers)
            soap = BeautifulSoup(response.text, features="html.parser")

            for subcategory_card in soap.findAll('div', class_='category__title'):
                subcategory_title = subcategory_card.find('a').text
                subcategory_url = self._base_url + subcategory_card.find('a').get('href')
                items.append(CategoryCardItem(category, subcategory_title, subcategory_url))

        return items
        # return [self._get_items(i) for i in items]

    def get_items_from_subcategory(self, category_item: CategoryCardItem):
        response = requests.get(category_item.link, headers=self.headers)
        soup = BeautifulSoup(response.text, features="html.parser")
        items = []

        page_count = 1
        pages_list = soup.find('div', class_='b-pageline')
        if pages_list:
            page_count = int(pages_list.findAll('a', class_=None)[-1].text)

        for i in range(1, page_count + 1):
            page_url = category_item.link + f'?page={i}'
            page_items = self.get_all_items_from_page(category_item, page_url)
            items += page_items
        return items

    def get_item_from_page(self, category_item: CategoryCardItem, body: BeautifulSoup) -> EventPost:
        title = body.find('p', class_='culture__title').find('a').text.strip()

        params = body.find('div', class_='culture__wrap').findAll('p', class_='culture__param')
        address = params[0].text
        phone = params[1].text.replace('телефон: ', '')
        if len(params) >= 3:
            site = params[2].text.replace('сайт: ', '').replace('https://www.smoladmin.ru', '')
        else:
            site = None

        post = EventPost(
            title=title,
            category=category_item.category,
            subcategory=category_item.subcategory,
            address=address,
            phone=phone,
            site=self._base_url + site if site else ''

        )
        post.save()

        image_url = self._base_url + body.find('img')['src']
        result = urllib.request.urlretrieve(image_url)

        with open(result[0], 'rb') as file:
            image_file = ImageFile(event_post=post)
            image_file.file.save(os.path.basename(image_url), File(file))
            image_file.save()

        return post

    def get_all_items_from_page(self, category_item: CategoryCardItem, page_url: str) -> List[EventPost]:
        items = []
        response = requests.get(page_url, headers=self.headers)
        soup = BeautifulSoup(response.text, features="html.parser")

        for body in soup.findAll('div', class_='culture__item'):
            try:
                item = self.get_item_from_page(category_item, body)
                items.append(item)
            except Exception as e:
                print(f"skip page item: '{e}'")

        return items




