### **1. Product Rating System**

**Test Design Techniques: **

### **Test Cases:**
1. **Boundary Value Analysis:**
    - **Test Case**: Verify that a logged-in user can rate a product that he previously bought
        As a logged-in user of MarketMate, I am able to rate a product after I buy it

| Step# | Action                                      | Expected outcome                                                                                   | OK/NOK | URL                      | Link to issue |
|-------|---------------------------------------------|-----------------------------------------------------------------------------------------------------|--------|--------------------------|---------------|
| 1     | Go to profile page MarketMate               | Login page appears                                                                                  | OK     | [https://findmate.masterschool.com/](https://findmate.masterschool.com/) |               |
| 2     | Fill in the email and password              |                                                                 | OK     | /auth                    |               |
| 3a    | Fill in 'test123@test.com' as email address |                                                                                                     |        |                          |               |
| 3b    | Fill '123456' as password                   |                                                                                                     |        |                          |               |
| 4     | Click Sign In                               |                | OK     |                          |               |
| 5     | Click on log in                             | You are successfully logged in                                                                      | OK     |                          |               |

![image](https://github.com/user-attachments/assets/a593d7b6-456f-4094-9c8a-dc88f4b4ef4c)
