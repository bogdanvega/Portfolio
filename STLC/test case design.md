### **1. Product Rating System**

**Test Design Techniques: Decision Table Testing, Use Case Testing, Error Guessing**

### **Test Cases:**
1. **Decision Table Testing:**
    - **Test Case**: Verify that a logged-in user can rate a product that he previously bought.
        As a logged-in user of MarketMate, I am able to rate a product after I buy it.

| Step# | Action                                           | Expected outcome                                                                                                                                     | OK/NOK | URL                                                                      | Link to issue |
|-------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                       | Home page is loaded                                                                                                                                  |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                            | Login page is loaded                                                                                                                                 |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address      |                                                                                                                                                      |  |                                                                          |               |
| 3b    | Fill '123456' as password                        |                                                                                                                                                      |  |                                                                          |               |
| 4     | Click 'Sign In'                                  | You are successfully logged in and Home page is loaded                                                                                               |  |                                                                          |               |
| 5     | Click 'Shop'                                     | Shop page is loaded                                                                                                                                  |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 20 years)         |                                                                                                                                                      |  |                                                                          |               |
| 7     | Click 'Confirm'                                  | Message "You are of age. You can now view all products, even alcohol products." is displayed                                                         |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Celery' vegetable | 'Item added to cart' message is displayed                                                                                                            |  |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon         | Checkout page is displayed                                                                                                                           |  |                                                                          |               |
| 10a   | Fill 'Baker street, 57' as Street Address        |                                                                                                                                                      |  |                                                                          |               |
| 10b   | Fill 'New York' as City                          |                                                                                                                                                      |  |                                                                          |               |
| 10c   | Fill '89210' as Postal Code                      |                                                                                                                                                      |  |                                                                          |               |
| 10d   | Fill '1111111111111111' as Card number           |                                                                                                                                                      |  |                                                                          |               |
| 10e   | Fill 'Test Test' as Name on card                 |                                                                                                                                                      |  |                                                                          |               |
| 10f   | Fill '02/2028' as Expiration                     |                                                                                                                                                      |  |                                                                          |               |
| 10g   | Fill '111' as Cvv                                |                                                                                                                                                      |  |                                                                          |               |
| 11    | Click 'Buy now'                                  | Successfully bought the item. Home page is loaded.                                                                                                   |  |                                                                          |               |
| 12    | Click 'Shop'                                     | Shop page is loaded                                                                                                                                  |  |                                                                          |               |
| 13    | Click 'Celery' to open product information       | Celery product information page is loaded                                                                                                            |  |                                                                          |               |
| 14    | Select a rating of 4 stars                       | 4 stars are filled in                                                                                                                                |  |                                                                          |               |
| 15    | Fill 'Fresh' in 'What is your view?' field       |                                                                                                                                                      |  |                                                                          |               |
| 16    | Click 'Send'                                     | Rating with 4 star and "Fresh" message is displayed under the product information<br/>"You have already reviewed this product." message is displayed |  |                                                                          |               |
<img width="1918" height="825" alt="Screenshot 2026-02-04 122919" src="https://github.com/user-attachments/assets/96d97091-8fbb-488d-8f5a-0176d2fa5d90" />
<img width="1889" height="821" alt="Screenshot 2026-02-04 123033" src="https://github.com/user-attachments/assets/20299f48-6a22-403f-bc6f-d8459e06a5fa" />
<img width="1893" height="822" alt="Screenshot 2026-02-04 123119" src="https://github.com/user-attachments/assets/ce2204f4-35ee-4248-966c-07cf58e54e56" />
<img width="1891" height="814" alt="Screenshot 2026-02-04 123244" src="https://github.com/user-attachments/assets/4219669d-bb80-490a-bae3-307d625cfc5c" />


2. **Decision Table Testing:**
    - **Test Case**: Verify that a logged-in user cannot rate a product if the product was not bought.
        As a logged-in user of MarketMate, I should not be able to rate a product if I didn't buy it.

| Step# | Action                                          | Expected outcome                                                                              | OK/NOK | URL                      | Link to issue |
|-------|-------------------------------------------------|-----------------------------------------------------------------------------------------------|--|--------------------------|---------------|
| 1     | Go to home page MarketMate                      | Home page is loaded                                                                           |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                           | Login page is loaded                                                                          |  | /auth                                                                          |               |
| 3a    | Fill in 'test123@test.com' as email address     |                                                                                               |  |                          |               |
| 3b    | Fill '123456' as password                       |                                                                                               |  |                          |               |
| 4     | Click 'Sign In'                                 | You are successfully logged in and Home page is loaded                                        |  |                          |               |
| 5     | Click 'Shop'                                    | Shop page is loaded                                                                           |  |                          |               |
| 6     | Fill Date of birth as (Today - 20 years)        |                                                                                               |  |                          |               |
| 7     | Click 'Confirm'                                 | Message "You are of age. You can now view all products, even alcohol products." is displayed  |  |                          |               |
| 8     | Click 'Gala Apples' to open product information | Gala Apples product information page is loaded                                                |  |                          |               |
| 9     | Try to rate the product                         | "You need to buy this product to tell us your opinion!" message is displayed                  |  |                          |               |

3. **Decision Table Testing:**
    - **Test Case**: Verify that a user cannot rate a product being logged out.
        As a logged-out user of MarketMate, I should not be able to rate a product.

| Step# | Action                                   | Expected outcome                                                             | OK/NOK | URL                      | Link to issue |
|-------|------------------------------------------|------------------------------------------------------------------------------|--|--------------------------|---------------|
| 1     | Go to home page MarketMate               | Home page is loaded                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                    | Login page is loaded and no user is logged in                                |  | /auth                                                                          |               |
| 3     | Click 'Go to Home'                       | Home page is loaded                                                          |  |                          |               |
| 5     | Click 'Shop'                             | Shop page is loaded                                                          |  |                          |               |
| 6     | Fill Date of birth as (Today - 20 years) |                                                                              |  |                          |               |
| 7     | Click 'Confirm'                          | Message "You are of age. You can now view all products, even alcohol products." is displayed                                                                             |  |                          |               |
| 8     | Click 'Kale' to open product information | Kale product information page is loaded                                      |  |                          |               |
| 9     | Try to rate the product                  | "You need to buy this product to tell us your opinion!" message is displayed |  |                          |               |

4. **Use Case Testing:**
    - **Test Case**: Verify that a logged-in user cannot rate a product multiple times.
        As a logged-in user of MarketMate, I should not be able to rate a product more than one time.

    Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation. But it will make the test case steps longer.

| Step# | Action                                                | Expected outcome                                                | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------------------|-----------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                            | Home page is loaded                                             |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                                 | Login page is loaded                                            |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address           |                                                                 |  |                                                                          |               |
| 3b    | Fill '123456' as password                             |                                                                 |  |                                                                          |               |
| 4     | Click 'Sign In'                                       | You are successfully logged in and Home page is loaded          |  |                                                                          |               |
| 5     | Click 'Shop'                                          | Shop page is loaded                                             |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 20 years)              |                                                                 |  |                                                                          |               |
| 7     | Click 'Confirm'                                       | Message "You are of age. You can now view all products, even alcohol products." is displayed                                                                |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Cauliflower' vegetable | 'Item added to cart' message is displayed                       |  |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon              | Checkout page is displayed                                      |  |                                                                          |               |
| 10a   | Fill 'Baker street, 57' as Street Address             |                                                                 |  |                                                                          |               |
| 10b   | Fill 'New York' as City                               |                                                                 |  |                                                                          |               |
| 10c   | Fill '89210' as Postal Code                           |                                                                 |  |                                                                          |               |
| 10d   | Fill '1111111111111111' as Card number                |                                                                 |  |                                                                          |               |
| 10e   | Fill 'Test Test' as Name on card                      |                                                                 |  |                                                                          |               |
| 10f   | Fill '02/2028' as Expiration                          |                                                                 |  |                                                                          |               |
| 10g   | Fill '111' as Cvv                                     |                                                                 |  |                                                                          |               |
| 11    | Click 'Buy now'                                       | Successfully bought the item. Home page is loaded.              |  |                                                                          |               |
| 12    | Click 'Shop'                                          | Shop page is loaded                                             |  |                                                                          |               |
| 13    | Click 'Cauliflower' to open product information       | Cauliflower product information page is loaded                  |  |                                                                          |               |
| 14    | Select a rating of 5 stars                            | 5 stars are filled in                                           |  |                                                                          |               |
| 15    | Fill 'Tasty' in 'What is your view?' field            |                                                                 |  |                                                                          |               |
| 16    | Click 'Send'                                          | Rating is displayed under the product information               |  |                                                                          |               |
| 17    | Try to rate the product again                         | "You have already reviewed this product." message is displayed  |  |                                                                          |               |

5. **Use Case Testing:**
    - **Test Case**: Verify that a user can see the product rating from another user.
        As a user of MarketMate, I should be able to see a product rating from another user.

  Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation. But it will make the test case steps longer.

| Step# | Action                                              | Expected outcome                                                                              | OK/NOK | URL                                                                      | Link to issue |
|-------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                          | Home page is loaded                                                                           |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                               | Login page is loaded                                                                          |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address         |                                                                                               |  |                                                                          |               |
| 3b    | Fill '123456' as password                           |                                                                                               |  |                                                                          |               |
| 4     | Click 'Sign In'                                     | You are successfully logged in and Home page is loaded                                        |  |                                                                          |               |
| 5     | Click 'Shop'                                        | Shop page is loaded                                                                           |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 20 years)            |                                                                                               |  |                                                                          |               |
| 7     | Click 'Confirm'                                     | Message "You are of age. You can now view all products, even alcohol products." is displayed  |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Asparagus' vegetable | 'Item added to cart' message is displayed                                                     |  |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon            | Checkout page is displayed                                                                    |  |                                                                          |               |
| 10a   | Fill 'Baker street, 57' as Street Address           |                                                                                               |  |                                                                          |               |
| 10b   | Fill 'New York' as City                             |                                                                                               |  |                                                                          |               |
| 10c   | Fill '89210' as Postal Code                         |                                                                                               |  |                                                                          |               |
| 10d   | Fill '1111111111111111' as Card number              |                                                                                               |  |                                                                          |               |
| 10e   | Fill 'Test Test' as Name on card                    |                                                                                               |  |                                                                          |               |
| 10f   | Fill '02/2028' as Expiration                        |                                                                                               |  |                                                                          |               |
| 10g   | Fill '111' as Cvv                                   |                                                                                               |  |                                                                          |               |
| 11    | Click 'Buy now'                                     | Successfully bought the item. Home page is loaded.                                            |  |                                                                          |               |
| 12    | Click 'Shop'                                        | Shop page is loaded                                                                           |  |                                                                          |               |
| 13    | Click 'Asparagus' to open product information       | Asparagus product information page is loaded                                                  |  |                                                                          |               |
| 14    | Select a rating of 3 stars                          | 3 stars are filled in                                                                         |  |                                                                          |               |
| 15    | Fill 'Not very tasty' in 'What is your view?' field |                                                                                               |  |                                                                          |               |
| 16    | Click 'Send'                                        | Rating is displayed under the product information                                             |  |                                                                          |               |
| 17    | Click on profile page                               | Login page is loaded                                                                          |  |                                                                          |               |
| 18a   | Fill in 'test321@test.com' as email address         |                                                                                               |  |                                                                          |               |
| 18b   | Fill '654321' as password                           |                                                                                               |  |                                                                          |               |
| 19    | Click 'Sign In'                                     | You are successfully logged in and Home page is loaded                                        |  |                                                                          |               |
| 20    | Click 'Shop'                                        | Shop page is loaded                                                                           |  |                                                                          |               |
| 21    | Click 'Asparagus' to open product information       | Asparagus product information page is loaded                                                  |  |                                                                          |               |
| 22    | Scroll down and look for test123 user rating        | The 3 stars rating from user test123 is displayed                                             |  |                                                                          |               |


6. **Error Guessing:**
    - **Test Case**: Verify system behavior when trying to rate a product without selecting a star.
        As a user of MarketMate, I should not be able to rate a product without selecting a star.

  Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation. But it will make the test case steps longer.

| Step# | Action                                           | Expected outcome                                                                              | OK/NOK | URL                                                                      | Link to issue |
|-------|--------------------------------------------------|-----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                       | Home page is loaded                                                                           |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                            | Login page is loaded                                                                          |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address      |                                                                                               |  |                                                                          |               |
| 3b    | Fill '123456' as password                        |                                                                                               |  |                                                                          |               |
| 4     | Click 'Sign In'                                  | You are successfully logged in and Home page is loaded                                        |  |                                                                          |               |
| 5     | Click 'Shop'                                     | Shop page is loaded                                                                           |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 20 years)         |                                                                                               |  |                                                                          |               |
| 7     | Click 'Confirm'                                  | Message "You are of age. You can now view all products, even alcohol products." is displayed                                                                                              |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Ginger' vegetable | 'Item added to cart' message is displayed                                                     |  |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon         | Checkout page is displayed                                                                    |  |                                                                          |               |
| 10a   | Fill 'Baker street, 57' as Street Address        |                                                                                               |  |                                                                          |               |
| 10b   | Fill 'New York' as City                          |                                                                                               |  |                                                                          |               |
| 10c   | Fill '89210' as Postal Code                      |                                                                                               |  |                                                                          |               |
| 10d   | Fill '1111111111111111' as Card number           |                                                                                               |  |                                                                          |               |
| 10e   | Fill 'Test Test' as Name on card                 |                                                                                               |  |                                                                          |               |
| 10f   | Fill '02/2028' as Expiration                     |                                                                                               |  |                                                                          |               |
| 10g   | Fill '111' as Cvv                                |                                                                                               |  |                                                                          |               |
| 11    | Click 'Buy now'                                  | Successfully bought the item. Home page is loaded.                                            |  |                                                                          |               |
| 12    | Click 'Shop'                                     | Shop page is loaded                                                                           |  |                                                                          |               |
| 13    | Click 'Ginger' to open product information       | Ginger product information page is loaded                                                     |  |                                                                          |               |
| 14    | Leave the star rating without selecting any star |                                                                                               |  |                                                                          |               |
| 15    | Fill 'Too green' in 'What is your view?' field   |                                                                                               |  |                                                                          |               |
| 16    | Click 'Send'                                     | Error message is displayed: "Invalid input for the field 'Rating'. Please check your input."  |  |                                                                          |               |


### **2. Age Verification for Alcoholic Products**

**Test Design Techniques: Use Case Testing, Boundary Value Analysis, Equivalence Partitioning, Error Guessing**

### **Test Cases:**
1. **Use Case Testing:**
    - **Test Case**: Verify that the modal is displayed when user is accessing Shop.
        As a user of MarketMate, I am prompted to enter my age when I'm navigating to Shop.

| Step# | Action                                      | Expected outcome                                            | OK/NOK | URL                                                                      | Link to issue |
|-|---------------------------------------------|-------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1 | Go to home page MarketMate                  | Home page is loaded                                         |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2 | Click on profile page                       | Login page is loaded                                        |  | /auth                                                                    |               |
| 3a | Fill in 'test123@test.com' as email address |                                                             |  |                                                                          |               |
| 3b | Fill '123456' as password                   |                                                             |  |                                                                          |               |
| 4 | Click 'Sign In'                             | You are successfully logged in and Home page is loaded      |  |                                                                          |               |
| 5 | Click 'Shop'                                | Shop page is loaded and Age Verification modal is displayed |  |                                                                          |               |

2. **Boundary Value Analysis:**
    - **Test Case**: Verify that user with exactly 18 years old can view and buy alcoholic products.
        As a user of MarketMate, I am able to view and buy alcoholic products if I am exactly 18 years old.

| Step# | Action                                    | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                | Home page is loaded                                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click 'Shop'                              | Shop page is loaded and Age Verification modal is displayed                                  |  |                                                                          |               |
| 3     | Fill Date of birth as (Today - 18 years)  |                                                                                              |  |                                                                          |               |
| 4     | Click 'Confirm'                           | Message "You are of age. You can now view all products, even alcohol products." is displayed |  |                                                                          |               |
| 5     | Click 'Alcohol' Category on the left side | Alcoholic products are displayed                                                             |  |                                                                          |               |


3. **Equivalence Partitioning:**
    - **Test Case**: Verify that user below 18 years old can not view and buy alcoholic products.
        As a user of MarketMate, I am not able to view and buy alcoholic products if I am below 18 years old.

| Step# | Action                                    | Expected outcome                                                                                                           | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                | Home page is loaded                                                                                                        |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click 'Shop'                              | Shop page is loaded and Age Verification modal is displayed                                                                |  |                                                                          |               |
| 3     | Fill Date of birth as (Today - 17 years ) |                                                                                                                            |  |                                                                          |               |
| 4     | Click 'Confirm'                           | Message "You are underage. You can still browse the site, but you will not be able to view alcohol products." is displayed |  |                                                                          |               |
| 5     | Click 'Alcohol' Category on the left side | Alcoholic products are not displayed                                                                                       |  |                                                                          |               |

4. **Error Guessing:**
    - **Test Case**: Verify that an invalid Date of Birth format is not accepted by the modal.
        As a user of MarketMate, I get an error if I submit an invalid Date of Birth format.

| Step# | Action                                  | Expected outcome                                                                                                           | OK/NOK | URL                                                                      | Link to issue |
|-------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate              | Home page is loaded                                                                                                        |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click 'Shop'                            | Shop page is loaded and Age Verification modal is displayed                                                                |  |                                                                          |               |
| 3     | Fill Date of birth as '03/03/1998'      |                                                                                                                            |  |                                                                          |               |
| 4     | Click 'Confirm'                         | Message "You are underage. You can still browse the site, but you will not be able to view alcohol products." is displayed |  |                                                                          |               |
| 5     | Click 'Alcohol' Category on the left side | Alcoholic products are not displayed                                                                                       |  |                                                                          |               |

5. **Error Guessing:**
    - **Test Case**: Verify that an invalid Date of Birth format is not accepted by the modal.
        As a user of MarketMate, I get an error if I submit an invalid Date of Birth format.

| Step# | Action                                            | Expected outcome                                                                                                           | OK/NOK | URL                                                                      | Link to issue |
|-------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                        | Home page is loaded                                                                                                        |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click 'Shop'                                      | Shop page is loaded and Age Verification modal is displayed                                                                |  |                                                                          |               |
| 3     | Click 'Confirm' without filling the Date of Birth | Message "You are underage. You can still browse the site, but you will not be able to view alcohol products." is displayed |  |                                                                          |               |
| 4     | Click 'Alcohol' Category on the left side         | Alcoholic products are not displayed                                                                                       |  |                                                                          |               |


### **3. Shipping Cost Changes**

**Test Design Techniques: Use Case Testing, Boundary Value Analysis, Equivalence Partitioning, Error Guessing**

### **Test Cases:**
1. **Equivalence Partitioning:**
    - **Test Case**: Verify that free shipping is granted when order is above 20€.
        As a user of MarketMate, I get free shipping when my order is above 20€.

| Step# | Action                                                                             | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                         | Home page is loaded                                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                                                              | Login page is loaded                                                                         |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address                                        |                                                                                              |  |                                                                          |               |
| 3b    | Fill '123456' as password                                                          |                                                                                              |  |                                                                          |               |
| 4     | Click 'Sign In'                                                                    | You are successfully logged in and Home page is loaded                                       |  |                                                                          |               |
| 5     | Click 'Shop'                                                                       | Shop page is loaded and Age Verification modal is displayed                                  |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 19 years)                                           |                                                                                              |  |                                                                          |               |
| 7     | Click 'Confirm'                                                                    | Message "You are of age. You can now view all products, even alcohol products." is displayed |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Gala Apples' vegetable                              | 'Item added to cart' message is displayed                                                    |  |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon                                           | Checkout page is displayed                                                                   |  |                                                                          |               |
| 10    | Click on the + sign 10 times for the Gala Apples to bring the Product Total to 22€ | Total is 22€ with Shipment 0€                                                                |  |                                                                          |               |


2. **Boundary Value Analysis:**
    - **Test Case**: Verify that 5€ shipping cost is added to orders just below 20€.
        As a user of MarketMate, I have to pay 5€ shipping cost when my order is just below 20€.

| Step# | Action                                                                                    | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                                | Home page is loaded                                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                                                                     | Login page is loaded                                                                         |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address                                               |                                                                                              |  |                                                                          |               |
| 3b    | Fill '123456' as password                                                                 |                                                                                              |  |                                                                          |               |
| 4     | Click 'Sign In'                                                                           | You are successfully logged in and Home page is loaded                                       |  |                                                                          |               |
| 5     | Click 'Shop'                                                                              | Shop page is loaded and Age Verification modal is displayed                                  |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 19 years)                                                  |                                                                                              |  |                                                                          |               |
| 7     | Click 'Confirm'                                                                           | Message "You are of age. You can now view all products, even alcohol products." is displayed |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Pink Lady Apples' vegetable                                | 'Item added to cart' message is displayed                                                    |  |                                                                          |               |
| 9     | Click 'Add to Cart' under the 'Birchwood Quarter Pounders' vegetable                      | 'Item added to cart' message is displayed                                                    |  |                                                                          |               |
| 10    | Go to cart page by clicking on Cart icon                                                  | Checkout page is displayed                                                                   |  |                                                                          |               |
| 11    | Click on the + sign for the Pink Lady Apples 6 times to bring the Product Total to 19.99€ | Total is 24.99€ with Shipment 5€                                                             |  |                                                                          |               |

3. **Use Case Testing:**
    - **Test Case**: Verify that shipping cost is calculated dynamically when items are added to the basket.
        As a user of MarketMate, I can see the shipping cost is calculated dynamically when items are added to the basket.

| Step# | Action                                                                                         | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                                     | Home page is loaded                                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                                                                          | Login page is loaded                                                                         |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address                                                    |                                                                                              |  |                                                                          |               |
| 3b    | Fill '123456' as password                                                                      |                                                                                              |  |                                                                          |               |
| 4     | Click 'Sign In'                                                                                | You are successfully logged in and Home page is loaded                                       |  |                                                                          |               |
| 5     | Click 'Shop'                                                                                   | Shop page is loaded and Age Verification modal is displayed                                  |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 19 years)                                                       |                                                                                              |  |                                                                          |               |
| 7     | Click 'Confirm'                                                                                | Message "You are of age. You can now view all products, even alcohol products." is displayed |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Ginger' vegetable                                               | 'Item added to cart' message is displayed                                                    |  |                                                                          |               |
| 9     | Click 'Add to Cart' under the 'Large Flat Mushrooms'                                           | 'Item added to cart' message is displayed                                                    |  |                                                                          |               |
| 10    | Go to cart page by clicking on Cart icon                                                       | Checkout page is displayed with Product Total 1.70€ and Shipment 5€                          |  |                                                                          |               |
| 11    | Click on the + sign for the Large Flat Mushrooms 17 times to bring the Product Total to 20.40€ | Total is 20.40€ with Shipment 0€                                                             |  |                                                                          |               |

4. **Error Guessing:**
    - **Test Case**: Verify that free shipping cost is not kept after the Product Total drops below 20€.
        As a user of MarketMate, I can see the shipping cost is being added back when Product Total drops below 20€.

| Step# | Action                                                                                         | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                                     | Home page is loaded                                                                          |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Click on profile page                                                                          | Login page is loaded                                                                         |  | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address                                                    |                                                                                              |  |                                                                          |               |
| 3b    | Fill '123456' as password                                                                      |                                                                                              |  |                                                                          |               |
| 4     | Click 'Sign In'                                                                                | You are successfully logged in and Home page is loaded                                       |  |                                                                          |               |
| 5     | Click 'Shop'                                                                                   | Shop page is loaded and Age Verification modal is displayed                                  |  |                                                                          |               |
| 6     | Fill Date of birth as (Today - 19 years)                                                       |                                                                                              |  |                                                                          |               |
| 7     | Click 'Confirm'                                                                                | Message "You are of age. You can now view all products, even alcohol products." is displayed |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Ginger' vegetable                                               | 'Item added to cart' message is displayed                                                    |  |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Large Flat Mushrooms'                                           | 'Item added to cart' message is displayed                                                    |  |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon                                                       | Checkout page is displayed with Product Total 1.70€ and Shipment 5€                          |  |                                                                          |               |
| 10    | Click on the + sign for the Large Flat Mushrooms 17 times to bring the Product Total to 20.40€ | Total is 20.40€ with Shipment 0€                                                             |  |                                                                          |               |
| 12    | Click on the - sign for the Large Flat Mushrooms to bring the Product Total to 19.30€          | Total is 24.30€ with Shipment 5€                                                             |  |                                                                          |               |
