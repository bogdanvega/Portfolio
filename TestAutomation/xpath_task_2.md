## Task 2

Go the https://grocerymate.masterschool.com 

1. Write the XPath for the highlighted icon/button given in the image below.
   
![image.png](https://img.notionusercontent.com/s3/prod-files-secure%2F3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c%2F38f4acec-5e04-4646-8f54-5edd021120da%2Fimage.png/size/w=2000?exp=1772533542&sig=MtNGoBWNwDihhjTynVPMZVkIUY5hzafHxDq9e0kh6h8&id=52261467-913b-430f-9cdf-b2d799135482&table=block)

   **Solution:**
   - //div[@class = 'headerIcon'][1]

2. Now, open https://grocerymate.masterschool.com/auth.
   
   ![image.png](https://img.notionusercontent.com/s3/prod-files-secure%2F3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c%2Fcc352327-dcdd-485b-af91-87626247bbd9%2Fimage.png/size/w=2000?exp=1772533892&sig=bfnej8RTseznyKrUVhLYmLrEjlHx4GJC4-EnzRiOZOQ&id=5eeb7c6b-9aba-4105-b820-5fcae7a1adf3&table=block)
   
   Write the XPath of all input fields (Email address, Password), sign in button, Create a new account link, and Go to Home link.

   **Solution:**
   - Email address input field: //input[@type = 'email']
   - Password input field: //input[@type = 'password']
   - Sign in button: //button[@type = 'submit']
   - Create a new account link: //a[@class = 'switch-link']
   - Go to Home link: //a[@class = 'home-link']

3. Now, on the same link as in Part 2, click on Create a new account, you will see the following UI:
   
   ![image.png](https://img.notionusercontent.com/s3/prod-files-secure%2F3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c%2F1e193326-679b-4739-96c8-36af2dc7c43e%2Fimage.png/size/w=2000?exp=1772533941&sig=D1jfiBMLWRHqqzKI6h09xROIVqPf0ENZXklHVGO79A8&id=faf82c81-fe8f-4121-91cb-5dac3e3aa24f&table=block)
   
   Write the XPath for all input fields (Full Name, Email address, Password), Sign Up button.

   **Solution:**
   - Full Name input field: //input[@type = 'text']
   - Email address input field: //input[@type = 'email']
   - Password input field: //input[@type = 'password']
   - Sign Up button: //button[@type = 'submit']

4. Go to https://grocerymate.masterschool.com/store, you will see the following UI:
   
   ![image.png](https://img.notionusercontent.com/s3/prod-files-secure%2F3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c%2F29c80beb-9478-4c6c-9ed0-104fe48162ad%2Fimage.png/size/w=2000?exp=1772533987&sig=JncTV6dt0N6niqOz0xkqGRl73oXW9AQWheUnVOi0U4A&id=7dfce969-52b8-468e-bb13-4999b6ddf1ed&table=block)
   
   Write the XPath of **Confirm** button which you can see in the Modal. 

   **Solution:**
   - //div[@class = 'modal-content']//button

5. Go to the **Shop** page, write the XPath for:
   
   a. Quantity input of Oranges

   **Solution:**
   - //div[@class = 'product-card']//input[@type = 'number'][1]

   b. Add to cart button for Oranges

   **Solutions:**
   - //button[@class = 'btn btn-primary btn-cart'][1]
   - //img[@alt = 'Oranges']/following-sibling::div//button[@class = 'btn btn-primary btn-cart']

   c. Add to wish list for Oranges
   
   **Solution:**
   - //button[@class = 'btn btn-outline-dark '][1]
   - //img[@alt = 'Oranges']/following-sibling::div//button[@class = 'btn btn-outline-dark ']
