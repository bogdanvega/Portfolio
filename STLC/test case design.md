### **1. Product Rating System**

**Test Design Techniques: Use Case Testing, Error Guessing**

### **Test Cases:**
1. **Decision Table Testing:**
    - **Test Case**: Verify that a logged-in user can rate a product that he previously bought.
        As a logged-in user of MarketMate, I am able to rate a product after I buy it.

| Step# | Action                                           | Expected outcome                                                                                                    | OK/NOK | URL                                                                      | Link to issue |
|------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1    | Go to home page MarketMate                       | Home page is loaded                                                                                                 |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2    | Click on profile page                            | Login page is loaded                                                                                                |  | /auth                                                                    |               |
| 3a   | Fill in 'test123@test.com' as email address      |                                                                                                                     |  |                                                                          |               |
| 3b   | Fill '123456' as password                        |                                                                                                                     |  |                                                                          |               |
| 4    | Click 'Sign In'                                  | You are successfully logged in and Home page is loaded                                                              |  |                                                                          |               |
| 5    | Click 'Shop'                                     | Shop page is loaded                                                                                                 |  |                                                                          |               |
| 6    | Click 'Add to Cart' under the 'Celery' vegetable | 'Item added to cart' message is displayed                                                                           |  |                                                                          |               |
| 7    | Go to cart page by clicking on Cart icon         | Checkout page is displayed                                                                                          |  |                                                                          |               |
| 8a   | Fill 'Baker street, 57' as Street Address        |                                                                                                                     |  |                                                                          |               |
| 8b   | Fill 'New York' as City                          |                                                                                                                     |  |                                                                          |               |
| 8c   | Fill '89210' as Postal Code                      |                                                                                                                     |  |                                                                          |               |
| 8d   | Fill '1111111111111111' as Card number           |                                                                                                                     |  |                                                                          |               |
| 8e   | Fill 'Test Test' as Name on card                 |                                                                                                                     |  |                                                                          |               |
| 8f   | Fill '02/2028' as Expiration                     |                                                                                                                     |  |                                                                          |               |
| 8g   | Fill '111' as Cvv                                |                                                                                                                     |  |                                                                          |               |
| 9    | Click 'Buy now'                                  | Successfully bought the item. Home page is loaded.                                                                  |  |                                                                          |               |
| 10   | Click 'Shop'                                     | Shop page is loaded                                                                                                 |  |                                                                          |               |
| 11   | Click 'Celery' to open product information       | Celery product information page is loaded                                                                           |  |                                                                          |               |
| 12   | Select a rating of 4 stars                       | 4 stars are filled in                                                                                               |  |                                                                          |               |
| 13   | Fill 'Fresh' in 'What is your view?' field       |                                                                                                                     |  |                                                                          |               |
| 14   | Click 'Send'                                     | Rating is displayed under the product information<br/>"You have already reviewed this product." message is displayed |  |                                                                          |               |

2. **Decision Table Testing:**
    - **Test Case**: Verify that a logged-in user cannot rate a product if the product was not bought.
        As a logged-in user of MarketMate, I should not be able to rate a product if I didn't buy it.

| Step# | Action                                          | Expected outcome                                                             | OK/NOK | URL                      | Link to issue |
|-------|-------------------------------------------------|------------------------------------------------------------------------------|--|--------------------------|---------------|
| 1     | Go to home page MarketMate                      | Home page is loaded                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                           | Login page is loaded                                                         |  | /auth                                                                          |               |
| 3a    | Fill in 'test123@test.com' as email address     |                                                                              |  |                          |               |
| 3b    | Fill '123456' as password                       |                                                                              |  |                          |               |
| 4     | Click 'Sign In'                                 | You are successfully logged in and Home page is loaded                       |  |                          |               |
| 5     | Click 'Shop'                                    | Shop page is loaded                                                          |  |                          |               |
| 6     | Click 'Gala Apples' to open product information | Gala Apples product information page is loaded                               |  |                          |               |
| 7     | Try to rate the product                         | "You need to buy this product to tell us your opinion!" message is displayed |  |                          |               |

3. **Decision Table Testing:**
    - **Test Case**: Verify that a user cannot rate a product being logged out.
        As a logged-out user of MarketMate, I should not be able to rate a product.

| Step# | Action                                     | Expected outcome                                                             | OK/NOK | URL                      | Link to issue |
|------|--------------------------------------------|------------------------------------------------------------------------------|--|--------------------------|---------------|
| 1    | Go to home page MarketMate                 | Home page is loaded                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2    | Click on profile page                      | Login page is loaded and no user is logged in                                |  | /auth                                                                          |               |
| 3    | Click 'Go to Home'                         | Home page is loaded                                                          |  |                          |               |
| 5    | Click 'Shop'                               | Shop page is loaded                                                          |  |                          |               |
| 6    | Click 'Kale' to open product information   | Kale product information page is loaded                                      |  |                          |               |
| 7    | Try to rate the product                    | "You need to buy this product to tell us your opinion!" message is displayed |  |                          |               |

4. **Use Case Testing:**
    - **Test Case**: Verify that a logged-in user cannot rate a product multiple times.
        As a logged-in user of MarketMate, I should not be able to rate a product more than one time.

    Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation, but it will make the test case steps longer.

| Step# | Action                                                | Expected outcome                                                | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------------------|-----------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                            | Home page is loaded                                             |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                                 | Login page is loaded                                            |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address           |                                                                 |  |                                                                          |               |
| 3b    | Fill '123456' as password                             |                                                                 |  |                                                                          |               |
| 4     | Click 'Sign In'                                       | You are successfully logged in and Home page is loaded          |  |                                                                          |               |
| 5     | Click 'Shop'                                          | Shop page is loaded                                             |  |                                                                          |               |
| 6     | Click 'Add to Cart' under the 'Cauliflower' vegetable | 'Item added to cart' message is displayed                       |  |                                                                          |               |
| 7     | Go to cart page by clicking on Cart icon              | Checkout page is displayed                                      |  |                                                                          |               |
| 8a    | Fill 'Baker street, 57' as Street Address             |                                                                 |  |                                                                          |               |
| 8b    | Fill 'New York' as City                               |                                                                 |  |                                                                          |               |
| 8c    | Fill '89210' as Postal Code                           |                                                                 |  |                                                                          |               |
| 8d    | Fill '1111111111111111' as Card number                |                                                                 |  |                                                                          |               |
| 8e    | Fill 'Test Test' as Name on card                      |                                                                 |  |                                                                          |               |
| 8f    | Fill '02/2028' as Expiration                          |                                                                 |  |                                                                          |               |
| 8g    | Fill '111' as Cvv                                     |                                                                 |  |                                                                          |               |
| 9     | Click 'Buy now'                                       | Successfully bought the item. Home page is loaded.              |  |                                                                          |               |
| 10    | Click 'Shop'                                          | Shop page is loaded                                             |  |                                                                          |               |
| 11    | Click 'Cauliflower' to open product information       | Cauliflower product information page is loaded                  |  |                                                                          |               |
| 12    | Select a rating of 5 stars                            | 5 stars are filled in                                           |  |                                                                          |               |
| 13    | Fill 'Tasty' in 'What is your view?' field            |                                                                 |  |                                                                          |               |
| 14    | Click 'Send'                                          | Rating is displayed under the product information               |  |                                                                          |               |
| 15    | Try to rate the product again                         | "You have already reviewed this product." message is displayed  |  |                                                                          |               |

5. **Use Case Testing:**
    - **Test Case**: Verify that a user can see the product rating from another user.
        As a user of MarketMate, I should be able to see a product rating from another user.

  Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation, but it will make the test case steps longer.

| Step# | Action                                              | Expected outcome                                       | OK/NOK | URL                                                                      | Link to issue |
|-------|-----------------------------------------------------|--------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                          | Home page is loaded                                    |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                               | Login page is loaded                                   |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address         |                                                        |  |                                                                          |               |
| 3b    | Fill '123456' as password                           |                                                        |  |                                                                          |               |
| 4     | Click 'Sign In'                                     | You are successfully logged in and Home page is loaded |  |                                                                          |               |
| 5     | Click 'Shop'                                        | Shop page is loaded                                    |  |                                                                          |               |
| 6     | Click 'Add to Cart' under the 'Asparagus' vegetable | 'Item added to cart' message is displayed              |  |                                                                          |               |
| 7     | Go to cart page by clicking on Cart icon            | Checkout page is displayed                             |  |                                                                          |               |
| 8a    | Fill 'Baker street, 57' as Street Address           |                                                        |  |                                                                          |               |
| 8b    | Fill 'New York' as City                             |                                                        |  |                                                                          |               |
| 8c    | Fill '89210' as Postal Code                         |                                                        |  |                                                                          |               |
| 8d    | Fill '1111111111111111' as Card number              |                                                        |  |                                                                          |               |
| 8e    | Fill 'Test Test' as Name on card                    |                                                        |  |                                                                          |               |
| 8f    | Fill '02/2028' as Expiration                        |                                                        |  |                                                                          |               |
| 8g    | Fill '111' as Cvv                                   |                                                        |  |                                                                          |               |
| 9     | Click 'Buy now'                                     | Successfully bought the item. Home page is loaded.     |  |                                                                          |               |
| 10    | Click 'Shop'                                        | Shop page is loaded                                    |  |                                                                          |               |
| 11    | Click 'Asparagus' to open product information       | Asparagus product information page is loaded           |  |                                                                          |               |
| 12    | Select a rating of 3 stars                          | 3 stars are filled in                                  |  |                                                                          |               |
| 13    | Fill 'Not very tasty' in 'What is your view?' field |                                                        |  |                                                                          |               |
| 14    | Click 'Send'                                        | Rating is displayed under the product information      |  |                                                                          |               |
| 15    | Click on profile page                               | Login page is loaded                                   |  |                                                                          |               |
| 16a   | Fill in 'test321@test.com' as email address         |                                                        |  |                                                                          |               |
| 16b   | Fill '654321' as password                           |                                                        |  |                                                                          |               |
| 17    | Click 'Sign In'                                     | You are successfully logged in and Home page is loaded |  |                                                                          |               |
| 18    | Click 'Shop'                                        | Shop page is loaded                                    |  |                                                                          |               |
| 19    | Click 'Asparagus' to open product information       | Asparagus product information page is loaded           |  |                                                                          |               |
| 20    | Scroll down and look for test123 user rating        | The 3 stars rating from user test123 is displayed      |  |                                                                          |               |


