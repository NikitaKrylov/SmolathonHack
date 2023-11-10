from django.contrib.auth.models import User
from django.test import TestCase
from datetime import datetime, timedelta
from posts.models import EventPost
from posts.repository.smoladmin import SmoladminRepository, CategoryCardItem
from posts.utils.travel import generate_travel_route


class SmoladminRepositoryTestCase(TestCase):
    repository: SmoladminRepository = SmoladminRepository()

    # def test_get_sub_categories(self):
    #     response = self.repository.get_all_subcategories_card()
    #     # print(response)
    #
    # def test_get_items(self):
    #     response = self.repository._get_items(CategoryCardItem("asd", 'sdsd', 'https://www.smoladmin.ru/o-smolenske/turizm/obekty-obschestvennogo-pitaniya/restorany/'))
    #     print(response)
    #     EventPost.objects.bulk_create(response)
    #
    #     print(EventPost.objects.all())

    #
    def test_get_all_items(self):
        response = self.repository.get_subcategories()

        items = []
        for i in response:
            print(f"Parse {i}...")
            items += self.repository.get_items_from_subcategory(i)

        print(len(items))
        self.assertIsNotNone(EventPost.objects.first().images)
        print(list(map(lambda x: x.images.first().file.url, items)))


        print(EventPost.objects.all())
        print(EventPost.objects.count())


#
# class GenerateTravelRouteTestCase(TestCase):
#
#     def setUp(self) -> None:
#         User.objects.create(
#             username='user',
#             email='user@example.com',
#             password='password'
#         )
#
#     def test_generate_route(self):
#         user = User.objects.first()
#         now = datetime.now().date()
#         end = now + timedelta(days=5)
#         route = generate_travel_route(user, now, end)
#         self.assertIsNotNone(route)
#
#         print(route)
#         print(route.days.all())


