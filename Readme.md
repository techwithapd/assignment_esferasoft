<!-- Documentation on how to access APIs  -->

Requirements are in requirements.txt -> please install them in a v-environment,
then run migrations and finally, runserver

Note: Please create at least 2 users first to test all APIs.

All API endpoints are prefixed with /api/.
http://127.0.0.1:8000/api/


1. User Registration -> POST /auth/register/ : (http://127.0.0.1:8000/api/auth/register/)

Body:
{
  "username": "amarpreet",
  "password": "Test@12345"
}


2. User Login -> POST /auth/login/ : (http://127.0.0.1:8000/api/auth/login/)

Body:
{
  "username": "amarpreet",
  "password": "Test@12345"
}


3. Product Creation -> POST /products/ : (http://127.0.0.1:8000/api/products/)

Headers:
Authorization: Bearer <access_token>

Body:
{
  "name": "HP pavillion laptop",
  "description": "2 years old, fully functional 15' laptop.",
  "starting_price": 10000,
  "end_time": "2025-08-05T18:00:00Z"
}


4. All Products Listing -> GET /products/ : (http://127.0.0.1:8000/api/products/)

Headers:
Authorization: Bearer <access_token>


5. Get Single Product Details -> GET /products/{id}/ : (http://127.0.0.1:8000/api/products/id/)

Headers:
Authorization: Bearer <access_token>



6. Place a Bid -> POST /bids/ : (http://127.0.0.1:8000/api/bids/)

Headers:
Authorization: Bearer <access_token>

Body:
{
    "amount": "1100.50",
    "product": "2"
}


7. Get All Bids List -> GET /bids/ : (http://127.0.0.1:8000/api/bids/)

Headers:
Authorization: Bearer <access_token>


8. Get a Bid Details -> GET /bids/{id}/ : (http://127.0.0.1:8000/api/bids/id/)

Headers:
Authorization: Bearer <access_token>

