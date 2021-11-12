from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
import json

class FoodCalorieViewSetTests(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user_1 = get_user_model().objects.create_user('yuvraj', password='yuvraj123')
        cls.user_2 = get_user_model().objects.create_user('adarsh', password='adarsh123')
        cls.token_1 = Token.objects.create(user=cls.user_1)
        cls.token_2 = Token.objects.create(user=cls.user_2)
        cls.data_full_1 = { 'consumed_at': '2021-11-12T11:44:19Z', 'name': 'Dahi Papdi', 'calorie': 13, 'is_inactive': False}
        cls.data_full_2 = { 'consumed_at': '2021-11-12T11:45:19Z', 'name': 'Dahi Papdi1', 'calorie': 13, 'is_inactive': False}
        cls.data_full_1_with_id = { 'consumed_at': '2021-11-12T11:44:19Z', 'name': 'Dahi Papdi', 'calorie': 13, 'id' : 1, 'is_inactive': False}
        cls.data_full_2_with_id = { 'consumed_at': '2021-11-12T11:45:19Z', 'name': 'Dahi Papdi1', 'calorie': 13, 'id' : 2, 'is_inactive': False}
        cls.data_consumed_at_missing = { 'name': 'Dahi Papdi', 'calorie': 13, 'is_inactive': False }
        cls.data_name_missing = { 'consumed_at': '2021-11-12T11:45:19Z', 'calorie': 13, 'is_inactive': False }
        cls.data_calorie_missing = { 'consumed_at': '2021-11-12T11:45:19Z', 'name': 'Dahi Papdi', 'is_inactive': False }
        cls.data_food_calorie_list = [cls.data_full_1, cls.data_full_2]
        cls.data_food_calorie_list_with_ids = [cls.data_full_1_with_id, cls.data_full_2_with_id]
        return super().setUpTestData()


    def test_food_calorie_create(self):
        url = reverse('foodcalories-list')
        
        response = self.client.post(url, FoodCalorieViewSetTests.data_full_1)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_1.key)
        
        response = self.client.post(url, FoodCalorieViewSetTests.data_full_1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.post(url, FoodCalorieViewSetTests.data_name_missing)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, FoodCalorieViewSetTests.data_consumed_at_missing)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(url, FoodCalorieViewSetTests.data_calorie_missing)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    
    def test_get_all_food_calorie(self):
        url = reverse('foodcalories-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_1.key)
        self.client.post(url, FoodCalorieViewSetTests.data_full_1)
        self.client.post(url, FoodCalorieViewSetTests.data_full_2)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), FoodCalorieViewSetTests.data_food_calorie_list_with_ids)

        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_2.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [])
        

    def test_food_calorie_get(self):
        url = reverse('foodcalories-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_1.key)
        self.client.post(url, FoodCalorieViewSetTests.data_full_1)
        self.client.post(url, FoodCalorieViewSetTests.data_full_2)

        response = self.client.get(reverse('foodcalories-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), FoodCalorieViewSetTests.data_full_1_with_id)

        response = self.client.get(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), FoodCalorieViewSetTests.data_full_2_with_id)

        response = self.client.get(reverse('foodcalories-detail', args=[3]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(reverse('foodcalories-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_2.key)
        response = self.client.delete(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_food_calorie_delete(self):
        url = reverse('foodcalories-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_1.key)
        self.client.post(url, FoodCalorieViewSetTests.data_full_1)
        self.client.post(url, FoodCalorieViewSetTests.data_full_2)

        response = self.client.delete(reverse('foodcalories-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('foodcalories-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(reverse('foodcalories-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.delete(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_2.key)
        response = self.client.delete(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_food_calorie_patch(self):
        url = reverse('foodcalories-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_1.key)
        self.client.post(url, FoodCalorieViewSetTests.data_full_1)
        self.client.post(url, FoodCalorieViewSetTests.data_full_2)

        response = self.client.patch(reverse('foodcalories-detail', args=[1]), { 'calorie' : 78})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('foodcalories-detail', args=[1]))
        self.assertEqual(json.loads(response.content)['calorie'], 78)

        response = self.client.patch(reverse('foodcalories-detail', args=[1]), { 'calorie' : 10 , 'name' : 'Salad'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('foodcalories-detail', args=[1]))
        data = json.loads(response.content)
        self.assertEqual(data['calorie'], 10)
        self.assertEqual(data['name'], 'Salad')
        
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.patch(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_2.key)
        response = self.client.patch(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_food_calorie_put(self):
        url = reverse('foodcalories-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_1.key)
        self.client.post(url, FoodCalorieViewSetTests.data_full_1)

        response = self.client.put(reverse('foodcalories-detail', args=[1]), { 'calorie' : 78})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.put(reverse('foodcalories-detail', args=[1]), FoodCalorieViewSetTests.data_full_2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(reverse('foodcalories-detail', args=[1]))
        data = dict(FoodCalorieViewSetTests.data_full_2_with_id)
        data['id'] = 1
        self.assertEqual(json.loads(response.content), data)
        
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.put(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + FoodCalorieViewSetTests.token_2.key)
        response = self.client.put(reverse('foodcalories-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

