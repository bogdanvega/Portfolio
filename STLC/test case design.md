### **1. Product Rating System**

**Test Design Techniques: **

### **Test Cases:**
1. **Boundary Value Analysis:**
    - **Test Case**: Verify that a logged-in user can rate a product that he previously bought
        As a logged-in user of MarketMate, I am able to rate a product after I buy it.

| Step# | Action                                           | Expected outcome                                                                                                     | OK/NOK | URL                      | Link to issue |
|-------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--|--------------------------|---------------|
| 1     | Go to profile page MarketMate                    | Login page appears                                                                                                   |  | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Fill in the email and password                   |                                                                                                                      |  | /auth                    |               |
| 3a    | Fill in 'test123@test.com' as email address      |                                                                                                                      |  |                          |               |
| 3b    | Fill '123456' as password                        |                                                                                                                      |  |                          |               |
| 4     | Click 'Sign In'                                  | You are successfully logged in and Home page is loaded                                                               |  |                          |               |
| 5     | Click 'Shop'                                     | Shop page is loaded                                                                                                  |  |                          |               |
| 6     | Click 'Add to Cart' under the 'Celery' vegetable | 'Item added to cart' message is displayed                                                                            |  |                          |               |
| 7     | Go to cart page by clicking on Cart icon         | Checkout page is displayed                                                                                           |  |                          |               |
| 8     | Fill in the 'Shipment Address' and 'Payment'     |                                                                                                                      |  |                          |               |
| 8a    | Fill 'Baker street, 57' as Street Address        |                                                                                                                      |  |                          |               |
| 8b    | Fill 'New York' as City                          |                                                                                                                      |  |                          |               |
| 8c    | Fill '89210' as Postal Code                      |                                                                                                                      |  |                          |               |
| 8d    | Fill '1111111111111111' as Card number           |                                                                                                                      |  |                          |               |
| 8e    | Fill 'Test Test' as Name on card                 |                                                                                                                      |  |                          |               |
| 8f    | Fill '02/2028' as Expiration                     |                                                                                                                      |  |                          |               |
| 8g    | Fill '111' as Cvv                                |                                                                                                                      |  |                          |               |
| 9     | Click 'Buy now'                                  | Successfully bought the item. Home page is loaded.                                                                   |  |                          |               |
| 10    | Click 'Shop'                                     | Shop page is loaded                                                                                                  |  |                          |               |
| 11    | Click 'Celery' to open product information       | Celery product information page is loaded                                                                            |  |                          |               |
| 12    | Select a rating of 4 stars                       |                                                                                                                      |  |                          |               |
| 13    | Fill in the "What is your view?" field a comment |                                                                                                                      |  |                          |               |
| 13a   | Fill 'Fresh' as comment                          |                                                                                                                      |  |                          |               |
| 14    | Click 'Send'                                     | Rating is displayed under the product information<br/>"You have already reviewed this product." message is displayed |  |                          |               |

![image](https://github.com/user-attachments/assets/a593d7b6-456f-4094-9c8a-dc88f4b4ef4c)
