## The assignment

****Write down which critical questions you can ask as a tester. Think of at least 3 questions per new feature. In the next session we will discuss these questions; after this you will receive the details of the requirements. 

## **The software**

You will test a webshop, which can be found here: https://grocerymate.masterschool.com/

The webshop has the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)

**You are going to test the new developed features. The new features are written below.**

## New features

### **1. Product Rating System**

**Vague requirement:** 
Users should be able to rate products with a 5-star system and have the option to add written feedback.

**Questions:**
1. Can a user submit a rating without being logged in, and if not, what feedback is shown?
2. Can the user still rate a product even if he didn't buy it yet?
3. Can a user rate the same product multiple times, and if yes, does the latest rating overwrite the previous one?
4. Are there any validations on the written feedback (minimum/maximum length, forbidden characters, profanity)?
5. How is the average rating calculated and updated when new ratings are added?
6. Are ratings immediately visible to other users, or is there a moderation step?
7. What happens if the user submits a rating but the network request fails?

**Detailed Requirement:**


### **2. Age Verification for Alcoholic Products**

**Vague requirement:** 
Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category asking if the user is 18+. Users must input their age before accessing the alcoholic products.

**Questions:**
1. When exactly does the age verification modal appear (on category click, page load, direct URL access)?
2. How should the age verification modal be implemented? (e.g., date of birth input (text field or selecting from a Calendar pop-up), age input)
3. If the age verification modal is date of birth input, what format should the date of birth be in? (e.g., MM/DD/YYYY)
4. What happens if the user enters an age under 18 — are they blocked, redirected, or shown a warning?
5. Is the age verification remembered for the session or future visits, and how long does it persist?
6. What input validation exists for the age field (non-numeric values, negative numbers, extremely high values)?
7. Does the age verification behave differently for logged-in vs. non-logged-in users?
8. What happens if the user closes the modal without entering their age?

**Detailed Requirement:**


### **3. Shipping Cost Changes**

**Vague requirement:** 
Free shipping for orders above a certain amount. Orders below this amount will incur a shipping fee.

**Questions:**
1. What is the exact threshold amount for free shipping, and is it inclusive or exclusive of that value?
2. Is the shipping cost recalculated dynamically when items are added or removed from the basket?
3. Is the free shipping threshold based on product subtotal, discounts, or final total including taxes?
4. Is the shipping fee clearly displayed before checkout and updated in real time?
5. What happens if a user qualifies for free shipping, then removes items and drops below the threshold?
6. Are shipping costs handled correctly across different payment methods?
7. Is the shipping fee applied consistently on the checkout page, order summary, and confirmation screen?

**Detailed Requirement:**
