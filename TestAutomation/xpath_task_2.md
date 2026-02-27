## Task 2

Go the https://grocerymate.masterschool.com 

1. Write the XPath for the highlighted icon/button given in the image below.
![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c/38f4acec-5e04-4646-8f54-5edd021120da/image.png)

Solution:
//div[@class = 'headerIcon'][1]

2. Now, open https://grocerymate.masterschool.com/auth. 

Write the XPath of all input fields (Email address, Password), sign in button, Create a new account link, and Go to Home link

Solution:
Email address input field: //input[@type = 'email']
Password input field: //input[@type = 'password']
Sign in button: //button[@type = 'submit']
Create a new account link: //a[@class = 'switch-link']
Go to Home link: //a[@class = 'home-link']

3. Now, on the same link as in Part 2, click on Create a new account, you will see the following UI:
Write the XPath for all input fields (Full Name, Email address, Password), Sign Up button.

Solution:
Full Name input field: //input[@type = 'text']
Email address input field: //input[@type = 'email']
Password input field: //input[@type = 'password']
Sign Up button: //button[@type = 'submit']

4. Go to https://grocerymate.masterschool.com/store, you will see the following UI:
https://masterschool.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c%2F29c80beb-9478-4c6c-9ed0-104fe48162ad%2Fimage.png?table=block&id=7dfce969-52b8-468e-bb13-4999b6ddf1ed&spaceId=3a9085c4-df29-45e6-8bc7-6c9c0a25ea8c&width=2000&userId=&cache=v2
Write the XPath of **Confirm** button which you can see in the Modal. 

Solution:
//div[@class = 'modal-content']//button

5. Go to the **Shop** page, write the XPath for:
   a. Quantity input of Oranges

    Solution:
    //input[@name = 'quantity_66b3a57b3fd5048eacb4798f']

   b. Add to cart button for Oranges

    Solutions:
    //button[@class = 'btn btn-primary btn-cart'][1]
    //img[@alt = 'Oranges']/following-sibling::div//button[@class = 'btn btn-primary btn-cart']

   c. Add to wish list for Oranges
   
    Solution:
    //button[@class = 'btn btn-outline-dark '][1]
    //img[@alt = 'Oranges']/following-sibling::div//button[@class = 'btn btn-outline-dark ']