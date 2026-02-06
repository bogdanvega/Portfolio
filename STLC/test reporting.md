### **1. Product Rating System**

**Test Design Techniques: Decision Table Testing, Use Case Testing, Error Guessing**

### Scenario 1: Logged-in user rates a product that he previously bought.

As a logged-in user of MarketMate, I am able to rate a product after I buy it.

| Step# | Action                                           | Expected outcome                                                                                                                                     | STATUS  | URL                                                                      | Link to issue                                          |
|-------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------|--------------------------------------------------------|
| 1     | Go to home page MarketMate                       | Home page is loaded                                                                                                                                  | OK      | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |                                                        |
| 2     | Click on profile page                            | Login page is loaded                                                                                                                                 | OK      | /auth                                                                    |                                                        |
| 3a    | Fill in 'test123@test.com' as email address      |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 3b    | Fill '123456' as password                        |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 4     | Click 'Sign In'                                  | You are successfully logged in and Home page is loaded                                                                                               | OK      |                                                                          |                                                        |
| 5     | Click 'Shop'                                     | Shop page is loaded                                                                                                                                  | OK      |                                                                          |                                                        |
| 6     | Fill Date of birth as (Today - 20 years)         |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 7     | Click 'Confirm'                                  | Message "You are of age. You can now view all products, even alcohol products." is displayed                                                         | OK      |                                                                          |                                                        |
| 8     | Click 'Add to Cart' under the 'Celery' vegetable | 'Item added to cart' message is displayed                                                                                                            | OK      |                                                                          |                                                        |
| 9     | Go to cart page by clicking on Cart icon         | Checkout page is displayed                                                                                                                           | OK      |                                                                          |                                                        |
| 10a   | Fill 'Baker street, 57' as Street Address        |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 10b   | Fill 'New York' as City                          |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 10c   | Fill '89210' as Postal Code                      |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 10d   | Fill '1111111111111111' as Card number           |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 10e   | Fill 'Test Test' as Name on card                 |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 10f   | Fill '02/2028' as Expiration                     |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 10g   | Fill '111' as Cvv                                |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 11    | Click 'Buy now'                                  | Successfully bought the items. Home page is loaded.                                                                                                  | OK, BUT |                                                                          | [#1](https://github.com/bogdanvega/Portfolio/issues/1) |
| 12    | Click 'Shop'                                     | Shop page is loaded                                                                                                                                  | OK      |                                                                          |                                                        |
| 13    | Click 'Celery' to open product information       | Celery product information page is loaded                                                                                                            | OK      |                                                                          |                                                        |
| 14    | Select a rating of 4 stars                       | 4 stars are filled in                                                                                                                                | OK      |                                                                          |                                                        |
| 15    | Fill 'Fresh' in 'What is your view?' field       |                                                                                                                                                      | OK      |                                                                          |                                                        |
| 16    | Click 'Send'                                     | Rating with 4 star and "Fresh" message is displayed under the product information<br/>"You have already reviewed this product." message is displayed | NOT OK  |                                                                          | [#2](https://github.com/bogdanvega/Portfolio/issues/2) |

<img width="1918" height="825" alt="Screenshot 2026-02-04 122919" src="https://github.com/user-attachments/assets/96d97091-8fbb-488d-8f5a-0176d2fa5d90" />
<img width="1889" height="821" alt="Screenshot 2026-02-04 123033" src="https://github.com/user-attachments/assets/20299f48-6a22-403f-bc6f-d8459e06a5fa" />
<img width="1893" height="822" alt="Screenshot 2026-02-04 123119" src="https://github.com/user-attachments/assets/ce2204f4-35ee-4248-966c-07cf58e54e56" />


2. **Decision Table Testing:**
    - **Test Case**: Verify that a logged-in user cannot rate a product if the product was not bought.
        + As a logged-in user of MarketMate, I should not be able to rate a product if I didn't buy it.

| Step# | Action                                          | Expected outcome                                                                              | STATUS | URL                      | Link to issue |
|-------|-------------------------------------------------|-----------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to home page MarketMate                      | Home page is loaded                                                                           | OK     | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on profile page                           | Login page is loaded                                                                          | OK     | /auth                                                                          |               |
| 3a    | Fill in 'test123@test.com' as email address     |                                                                                               | OK     |                          |               |
| 3b    | Fill '123456' as password                       |                                                                                               | OK     |                          |               |
| 4     | Click 'Sign In'                                 | You are successfully logged in and Home page is loaded                                        | OK     |                          |               |
| 5     | Click 'Shop'                                    | Shop page is loaded                                                                           | OK     |                          |               |
| 6     | Fill Date of birth as (Today - 20 years)        |                                                                                               | OK     |                          |               |
| 7     | Click 'Confirm'                                 | Message "You are of age. You can now view all products, even alcohol products." is displayed  | OK     |                          |               |
| 8     | Click 'Gala Apples' to open product information | Gala Apples product information page is loaded                                                | OK     |                          |               |
| 9     | Try to rate the product                         | "You need to buy this product to tell us your opinion!" message is displayed                  | OK     |                          |               |


<img width="1894" height="815" alt="Screenshot 2026-02-04 124750" src="https://github.com/user-attachments/assets/606b075d-d81b-4bf4-9b99-64bbe7b48fe7" />


3. **Decision Table Testing:**
    - **Test Case**: Verify that a user cannot rate a product being logged out.
        + As a logged-out user of MarketMate, I should not be able to rate a product.

| Step# | Action                                   | Expected outcome                                                                                           | OK/NOK | URL                      | Link to issue |
|-------|------------------------------------------|------------------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to home page MarketMate               | Home page is loaded                                                                                        | OK     | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on profile page                    | Login page is loaded and no user is logged in                                                              | OK     | /auth                                                                          |               |
| 3     | Click 'Go to Home'                       | Home page is loaded                                                                                        | OK     |                          |               |
| 5     | Click 'Shop'                             | Shop page is loaded                                                                                        | OK     |                          |               |
| 6     | Fill Date of birth as (Today - 20 years) |                                                                                                            | OK     |                          |               |
| 7     | Click 'Confirm'                          | Message "You are of age. You can now view all products, even alcohol products." is displayed               | OK     |                          |               |
| 8     | Click 'Kale' to open product information | Kale product information page is loaded                                                                    | OK     |                          |               |
| 9     | Try to rate the product                  | "You need to buy this product to tell us your opinion!" message is displayed                               | OK     |                          |               |

<img width="1883" height="801" alt="Screenshot 2026-02-04 125152" src="https://github.com/user-attachments/assets/0d8cd5d3-da67-49ee-b476-10c03bac0a64" />


4. **Use Case Testing:**
    - **Test Case**: Verify that a logged-in user cannot rate a product multiple times.
        + As a logged-in user of MarketMate, I should not be able to rate a product more than one time.

    Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation. But it will make the test case steps longer.

| Step# | Action                                                | Expected outcome                                                                             | STATUS  | URL                                                                      | Link to issue |
|-------|-------------------------------------------------------|----------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                            | Home page is loaded                                                                          | OK      | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on profile page                                 | Login page is loaded                                                                         | OK      | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address           |                                                                                              | OK      |                                                                          |               |
| 3b    | Fill '123456' as password                             |                                                                                              | OK      |                                                                          |               |
| 4     | Click 'Sign In'                                       | You are successfully logged in and Home page is loaded                                       | OK      |                                                                          |               |
| 5     | Click 'Shop'                                          | Shop page is loaded                                                                          | OK      |                                                                          |               |
| 6     | Fill Date of birth as (Today - 20 years)              |                                                                                              | OK      |                                                                          |               |
| 7     | Click 'Confirm'                                       | Message "You are of age. You can now view all products, even alcohol products." is displayed | OK      |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Cauliflower' vegetable | 'Item added to cart' message is displayed                                                    | OK      |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon              | Checkout page is displayed                                                                   | OK      |                                                                          |               |
| 10a   | Fill 'Baker street, 57' as Street Address             |                                                                                              | OK      |                                                                          |               |
| 10b   | Fill 'New York' as City                               |                                                                                              | OK      |                                                                          |               |
| 10c   | Fill '89210' as Postal Code                           |                                                                                              | OK      |                                                                          |               |
| 10d   | Fill '1111111111111111' as Card number                |                                                                                              | OK      |                                                                          |               |
| 10e   | Fill 'Test Test' as Name on card                      |                                                                                              | OK      |                                                                          |               |
| 10f   | Fill '02/2028' as Expiration                          |                                                                                              | OK      |                                                                          |               |
| 10g   | Fill '111' as Cvv                                     |                                                                                              | OK      |                                                                          |               |
| 11    | Click 'Buy now'                                       | Successfully bought the item. Home page is loaded.                                           | OK, BUT |                                                                          | [#1](https://github.com/bogdanvega/Portfolio/issues/1)              |
| 12    | Click 'Shop'                                          | Shop page is loaded                                                                          | OK      |                                                                          |               |
| 13    | Click 'Cauliflower' to open product information       | Cauliflower product information page is loaded                                               | OK      |                                                                          |               |
| 14    | Select a rating of 5 stars                            | 5 stars are filled in                                                                        | OK      |                                                                          |               |
| 15    | Fill 'Tasty' in 'What is your view?' field            |                                                                                              | OK      |                                                                          |               |
| 16    | Click 'Send'                                          | Rating is displayed under the product information                                            | NOT OK  |                                                                          | [#2](https://github.com/bogdanvega/Portfolio/issues/2)              |
| 17    | Try to rate the product again                         | "You have already reviewed this product." message is displayed                               | OK      |                                                                          |               |

<img width="1889" height="818" alt="Screenshot 2026-02-04 125414" src="https://github.com/user-attachments/assets/02329f39-9f00-46e4-b724-8d96a04d439f" />


5. **Use Case Testing:**
    - **Test Case**: Verify that a user can see the product rating from another user.
        + As a user of MarketMate, I should be able to see a product rating from another user.

  Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation. But it will make the test case steps longer.

| Step# | Action                                              | Expected outcome                                                                              | STATUS  | URL                                                                      | Link to issue |
|-------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                          | Home page is loaded                                                                           | OK      | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on profile page                               | Login page is loaded                                                                          | OK      | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address         |                                                                                               | OK      |                                                                          |               |
| 3b    | Fill '123456' as password                           |                                                                                               | OK      |                                                                          |               |
| 4     | Click 'Sign In'                                     | You are successfully logged in and Home page is loaded                                        | OK      |                                                                          |               |
| 5     | Click 'Shop'                                        | Shop page is loaded                                                                           | OK      |                                                                          |               |
| 6     | Fill Date of birth as (Today - 20 years)            |                                                                                               | OK      |                                                                          |               |
| 7     | Click 'Confirm'                                     | Message "You are of age. You can now view all products, even alcohol products." is displayed  | OK      |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Asparagus' vegetable | 'Item added to cart' message is displayed                                                     | OK      |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon            | Checkout page is displayed                                                                    | OK      |                                                                          |               |
| 10a   | Fill 'Baker street, 57' as Street Address           |                                                                                               | OK      |                                                                          |               |
| 10b   | Fill 'New York' as City                             |                                                                                               | OK      |                                                                          |               |
| 10c   | Fill '89210' as Postal Code                         |                                                                                               | OK      |                                                                          |               |
| 10d   | Fill '1111111111111111' as Card number              |                                                                                               | OK      |                                                                          |               |
| 10e   | Fill 'Test Test' as Name on card                    |                                                                                               | OK      |                                                                          |               |
| 10f   | Fill '02/2028' as Expiration                        |                                                                                               | OK      |                                                                          |               |
| 10g   | Fill '111' as Cvv                                   |                                                                                               | OK      |                                                                          |               |
| 11    | Click 'Buy now'                                     | Successfully bought the item. Home page is loaded.                                            | OK, BUT |                                                                          | [#1](https://github.com/bogdanvega/Portfolio/issues/1)               |
| 12    | Click 'Shop'                                        | Shop page is loaded                                                                           | OK      |                                                                          |               |
| 13    | Click 'Asparagus' to open product information       | Asparagus product information page is loaded                                                  | OK      |                                                                          |               |
| 14    | Select a rating of 3 stars                          | 3 stars are filled in                                                                         | OK      |                                                                          |               |
| 15    | Fill 'Not very tasty' in 'What is your view?' field |                                                                                               | OK      |                                                                          |               |
| 16    | Click 'Send'                                        | Rating is displayed under the product information                                             | NOT OK  |                                                                          | [#2](https://github.com/bogdanvega/Portfolio/issues/2)              |
| 17    | Click on profile page                               | Login page is loaded                                                                          | OK      |                                                                          |               |
| 18a   | Fill in 'test321@test.com' as email address         |                                                                                               | OK      |                                                                          |               |
| 18b   | Fill '654321' as password                           |                                                                                               | OK      |                                                                          |               |
| 19    | Click 'Sign In'                                     | You are successfully logged in and Home page is loaded                                        | OK      |                                                                          |               |
| 20    | Click 'Shop'                                        | Shop page is loaded                                                                           | OK      |                                                                          |               |
| 21    | Click 'Asparagus' to open product information       | Asparagus product information page is loaded                                                  | OK      |                                                                          |               |
| 22    | Scroll down and look for test123 user rating        | The 3 stars rating from user test123 is displayed                                             | OK      |                                                                          |               |

<img width="1887" height="817" alt="Screenshot 2026-02-04 125649" src="https://github.com/user-attachments/assets/f8803010-0ecc-4671-9834-c920b4b2e91a" />
<img width="1881" height="813" alt="Screenshot 2026-02-04 125713" src="https://github.com/user-attachments/assets/809a78a8-69d3-42c9-a08a-108ea2a61da5" />



6. **Error Guessing:**
    - **Test Case**: Verify system behavior when trying to rate a product without selecting a star.
        + As a user of MarketMate, I should not be able to rate a product without selecting a star.

  Could have used a dependency on Test Case #1 for this test case.
    To avoid dependencies, because they can cause problems in test execution, I'll avoid them in this situation. But it will make the test case steps longer.

| Step# | Action                                           | Expected outcome                                                                                    | OK/NOK  | URL                                                                      | Link to issue |
|-------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                       | Home page is loaded                                                                                 | OK      | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click on profile page                            | Login page is loaded                                                                                | OK      | /auth                                                                    |               |
| 3a    | Fill in 'test123@test.com' as email address      |                                                                                                     | OK      |                                                                          |               |
| 3b    | Fill '123456' as password                        |                                                                                                     | OK      |                                                                          |               |
| 4     | Click 'Sign In'                                  | You are successfully logged in and Home page is loaded                                              | OK      |                                                                          |               |
| 5     | Click 'Shop'                                     | Shop page is loaded                                                                                 | OK      |                                                                          |               |
| 6     | Fill Date of birth as (Today - 20 years)         |                                                                                                     | OK      |                                                                          |               |
| 7     | Click 'Confirm'                                  | Message "You are of age. You can now view all products, even alcohol products." is displayed        | OK       |                                                                          |               |
| 8     | Click 'Add to Cart' under the 'Ginger' vegetable | 'Item added to cart' message is displayed                                                           | OK      |                                                                          |               |
| 9     | Go to cart page by clicking on Cart icon         | Checkout page is displayed                                                                          | OK      |                                                                          |               |
| 10a   | Fill 'Baker street, 57' as Street Address        |                                                                                                     | OK      |                                                                          |               |
| 10b   | Fill 'New York' as City                          |                                                                                                     | OK      |                                                                          |               |
| 10c   | Fill '89210' as Postal Code                      |                                                                                                     | OK      |                                                                          |               |
| 10d   | Fill '1111111111111111' as Card number           |                                                                                                     | OK      |                                                                          |               |
| 10e   | Fill 'Test Test' as Name on card                 |                                                                                                     | OK      |                                                                          |               |
| 10f   | Fill '02/2028' as Expiration                     |                                                                                                     | OK      |                                                                          |               |
| 10g   | Fill '111' as Cvv                                |                                                                                                     | OK      |                                                                          |               |
| 11    | Click 'Buy now'                                  | Successfully bought the item. Home page is loaded.                                                  | OK, BUT |                                                                          |  [#1](https://github.com/bogdanvega/Portfolio/issues/1)             |
| 12    | Click 'Shop'                                     | Shop page is loaded                                                                                 | OK      |                                                                          |               |
| 13    | Click 'Ginger' to open product information       | Ginger product information page is loaded                                                           | OK      |                                                                          |               |
| 14    | Leave the star rating without selecting any star |                                                                                                     | OK      |                                                                          |               |
| 15    | Fill 'Too green' in 'What is your view?' field   |                                                                                                     | OK      |                                                                          |               |
| 16    | Click 'Send'                                     | Error message is displayed: "Invalid input for the field 'Rating'. Please check your input."        | OK      |                                                                          |               |


<img width="1884" height="816" alt="Screenshot 2026-02-04 125950" src="https://github.com/user-attachments/assets/1f905788-dc43-4749-a4e1-e58fedb4a347" />


### **2. Age Verification for Alcoholic Products**

**Test Design Techniques: Use Case Testing, Boundary Value Analysis, Equivalence Partitioning, Error Guessing**

### **Test Cases:**
1. **Use Case Testing:**
    - **Test Case**: Verify that the modal is displayed when user is accessing Shop.
        + As a user of MarketMate, I am prompted to enter my age when I'm navigating to Shop.

| Step# | Action                                      | Expected outcome                                            | OK/NOK | URL                                                                      | Link to issue |
|-|---------------------------------------------|-------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1 | Go to home page MarketMate                  | Home page is loaded                                         |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2 | Click on profile page                       | Login page is loaded                                        |  | /auth                                                                    |               |
| 3a | Fill in 'test123@test.com' as email address |                                                             |  |                                                                          |               |
| 3b | Fill '123456' as password                   |                                                             |  |                                                                          |               |
| 4 | Click 'Sign In'                             | You are successfully logged in and Home page is loaded      |  |                                                                          |               |
| 5 | Click 'Shop'                                | Shop page is loaded and Age Verification modal is displayed |  |                                                                          |               |

<img width="1884" height="816" alt="Screenshot 2026-02-04 130528" src="https://github.com/user-attachments/assets/e4c4eafc-da94-4188-9b3d-f013fb7b0d1e" />

2. **Boundary Value Analysis:**
    - **Test Case**: Verify that user with exactly 18 years old can view and buy alcoholic products.
        As a user of MarketMate, I am able to view and buy alcoholic products if I am exactly 18 years old.

| Step# | Action                                    | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                | Home page is loaded                                                                          |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click 'Shop'                              | Shop page is loaded and Age Verification modal is displayed                                  |  |                                                                          |               |
| 3     | Fill Date of birth as (Today - 18 years)  |                                                                                              |  |                                                                          |               |
| 4     | Click 'Confirm'                           | Message "You are of age. You can now view all products, even alcohol products." is displayed |  |                                                                          |               |
| 5     | Click 'Alcohol' Category on the left side | Alcoholic products are displayed                                                             |  |                                                                          |               |

<img width="1889" height="818" alt="Screenshot 2026-02-04 130642" src="https://github.com/user-attachments/assets/d506b85c-e206-42c7-b388-04ed06949b4a" />
<img width="1886" height="823" alt="Screenshot 2026-02-04 130709" src="https://github.com/user-attachments/assets/4eccc852-d3e3-41c9-b5c3-3d2e871b0113" />
<img width="1888" height="814" alt="Screenshot 2026-02-04 131543" src="https://github.com/user-attachments/assets/ac7e3a8a-7bcb-4898-a158-fbf58e335ed9" />


3. **Equivalence Partitioning:**
    - **Test Case**: Verify that user below 18 years old can not view and buy alcoholic products.
        As a user of MarketMate, I am not able to view and buy alcoholic products if I am below 18 years old.

| Step# | Action                                    | Expected outcome                                                                                                           | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                | Home page is loaded                                                                                                        |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click 'Shop'                              | Shop page is loaded and Age Verification modal is displayed                                                                |  |                                                                          |               |
| 3     | Fill Date of birth as (Today - 17 years ) |                                                                                                                            |  |                                                                          |               |
| 4     | Click 'Confirm'                           | Message "You are underage. You can still browse the site, but you will not be able to view alcohol products." is displayed |  |                                                                          |               |
| 5     | Click 'Alcohol' Category on the left side | Alcoholic products are not displayed                                                                                       |  |                                                                          |               |

<img width="1883" height="813" alt="Screenshot 2026-02-04 130822" src="https://github.com/user-attachments/assets/a0d7aaa8-fd06-476b-9ad2-dd634afba7bc" />
<img width="1892" height="819" alt="Screenshot 2026-02-04 130829" src="https://github.com/user-attachments/assets/f4183899-b238-4d14-9158-cf4e5e746a4a" />
<img width="1892" height="811" alt="Screenshot 2026-02-04 131443" src="https://github.com/user-attachments/assets/8795ca98-aa12-428b-bd1c-2d17eb486d98" />


4. **Error Guessing:**
    - **Test Case**: Verify that an invalid Date of Birth format is not accepted by the modal.
        + As a user of MarketMate, I get an error if I submit an invalid Date of Birth format.

| Step# | Action                                  | Expected outcome                                                                                                           | OK/NOK | URL                                                                      | Link to issue |
|-------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate              | Home page is loaded                                                                                                        |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click 'Shop'                            | Shop page is loaded and Age Verification modal is displayed                                                                |  |                                                                          |               |
| 3     | Fill Date of birth as '03/03/1998'      |                                                                                                                            |  |                                                                          |               |
| 4     | Click 'Confirm'                         | Message "Wrong birth date format used." is displayed |  |                                                                          |               |
| 5     | Click 'Alcohol' Category on the left side | Alcoholic products are not displayed                                                                                       |  |                                                                          |               |

<img width="1889" height="818" alt="Screenshot 2026-02-04 130959" src="https://github.com/user-attachments/assets/891896e9-ed7d-4d80-b554-8eec9eea78ec" />
<img width="1892" height="811" alt="Screenshot 2026-02-04 131443" src="https://github.com/user-attachments/assets/010c1ffe-dfaa-4e13-8242-1888ed527c67" />


5. **Error Guessing:**
    - **Test Case**: Verify that not filling the Birth Date is not accepted by the modal.
        As a user of MarketMate, I get an error if I confirm the age verification modal without filling Birth Date.

| Step# | Action                                            | Expected outcome                                                                                                           | OK/NOK | URL                                                                      | Link to issue |
|-------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                        | Home page is loaded                                                                                                        |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
| 2     | Click 'Shop'                                      | Shop page is loaded and Age Verification modal is displayed                                                                |  |                                                                          |               |
| 3     | Click 'Confirm' without filling the Date of Birth | Message "Wrong birth date format used." is displayed |  |                                                                          |               |
| 4     | Click 'Alcohol' Category on the left side         | Alcoholic products are not displayed                                                                                       |  |                                                                          |               |

<img width="1889" height="819" alt="Screenshot 2026-02-04 131316" src="https://github.com/user-attachments/assets/28874e58-d92e-4625-a3ea-2df5ba85c332" />
<img width="1892" height="811" alt="Screenshot 2026-02-04 131443" src="https://github.com/user-attachments/assets/0150384b-b93b-48a4-8864-1209fb0fa2e8" />


### **3. Shipping Cost Changes**

**Test Design Techniques: Use Case Testing, Boundary Value Analysis, Equivalence Partitioning, Error Guessing**

### **Test Cases:**
1. **Equivalence Partitioning:**
    - **Test Case**: Verify that free shipping is granted when order is above 20€.
        + As a user of MarketMate, I get free shipping when my order is above 20€.

| Step# | Action                                                                             | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                         | Home page is loaded                                                                          |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
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


<img width="1888" height="817" alt="Screenshot 2026-02-04 131929" src="https://github.com/user-attachments/assets/d38ebc17-4f70-466d-88dc-2f1d59e19358" />
<img width="1890" height="817" alt="Screenshot 2026-02-04 131904" src="https://github.com/user-attachments/assets/27987da0-8704-426e-9f9a-fc81ca85bcc8" />


2. **Boundary Value Analysis:**
    - **Test Case**: Verify that 5€ shipping cost is added to orders just below 20€.
        + As a user of MarketMate, I have to pay 5€ shipping cost when my order is just below 20€.

| Step# | Action                                                                                    | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                                | Home page is loaded                                                                          |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
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


<img width="1892" height="810" alt="Screenshot 2026-02-04 132019" src="https://github.com/user-attachments/assets/a65c1545-b04f-4da6-9a16-2b3d18927e12" />
<img width="1890" height="806" alt="Screenshot 2026-02-04 132047" src="https://github.com/user-attachments/assets/2e76356e-e469-41a6-8f7f-bbd16ce1acbd" />


3. **Use Case Testing:**
    - **Test Case**: Verify that shipping cost is calculated dynamically when items are added to the basket.
        As a user of MarketMate, I can see the shipping cost is calculated dynamically when items are added to the basket.

| Step# | Action                                                                                         | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                                     | Home page is loaded                                                                          |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
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


<img width="1886" height="805" alt="Screenshot 2026-02-04 132735" src="https://github.com/user-attachments/assets/bb6b8872-5445-40bf-8f9d-df23d2140945" />
<img width="1877" height="803" alt="Screenshot 2026-02-04 132923" src="https://github.com/user-attachments/assets/56f058e9-3ef1-49f0-8b29-d59a801ff0d2" />
<img width="1893" height="805" alt="Screenshot 2026-02-04 132827" src="https://github.com/user-attachments/assets/16c74589-c2c6-49e2-b3a8-5c8720655093" />


4. **Error Guessing:**
    - **Test Case**: Verify that free shipping cost is not kept after the Product Total drops below 20€.
        + As a user of MarketMate, I can see the shipping cost is being added back when Product Total drops below 20€.

| Step# | Action                                                                                         | Expected outcome                                                                             | OK/NOK | URL                                                                      | Link to issue |
|-------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--|--------------------------------------------------------------------------|---------------|
| 1     | Go to home page MarketMate                                                                     | Home page is loaded                                                                          |  | [https://grocerymate.masterschool.com/](https://grocerymate.masterschool.com/) |               |
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

<img width="1884" height="815" alt="Screenshot 2026-02-04 133103" src="https://github.com/user-attachments/assets/174b98c1-1856-456c-8720-e7d81e8e391e" />
<img width="1891" height="808" alt="Screenshot 2026-02-04 133114" src="https://github.com/user-attachments/assets/c04c5e31-a9f5-4bdb-bbdf-dac5860c9264" />
<img width="1885" height="807" alt="Screenshot 2026-02-04 133129" src="https://github.com/user-attachments/assets/91926864-4463-4b31-9025-370a3fa5aa14" />
<img width="1888" height="807" alt="Screenshot 2026-02-04 133158" src="https://github.com/user-attachments/assets/2a07af72-fcf7-4c68-a6ce-0f30101400e6" />

