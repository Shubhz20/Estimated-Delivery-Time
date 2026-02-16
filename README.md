# Swiggy Delivery Time Prediction

This project is a simple Machine Learning case study that predicts how long a food delivery will take on Swiggy.

## What is this project?

Imagine you order food on an app like Swiggy. The app tells you it will arrive in "35 mins". How does it know that?
This project builds a computer program (a model) that learns from past delivery data to guess these times.

## How does it work?

The project follows these easy steps:

1.  **Read the Data**: We load a file (`swiggy.csv`) containing information about thousands of past orders (like restaurant location, price, ratings, and how long the delivery actually took).
2.  **Clean the Data**: We remove any incomplete records so our model doesn't get confused.
3.  **Understand the Data**: We look at things like:
    - Which cities have the most orders?
    - What is the average delivery time?
    - How does the price or rating affect the time?
4.  **Prepare the Data**: Computers understand numbers better than words. We convert city names and areas into numbers (a process called "One-Hot Encoding").
5.  **Train the "Brain"**: We use a technique called **Decision Tree Regression**. Think of it like a flowchart the computer makes:
    - _Is the distance far? -> Yes -> Add 20 mins._
    - _Is the traffic bad? -> No -> Subtract 5 mins._
      It learns these rules by itself from the data!
6.  **Test the Model**: We hide some data from the computer and ask it to predict the time. Then we compare its guess to the real answer to see how accurate it is.

## Tools Used

- **Python**: The programming language.
- **Pandas**: For organizing data into tables (like Excel).
- **Scikit-Learn**: For building the machine learning model.

## How to Run it

You need a tool like **Jupyter Notebook** or **Google Colab**.

1.  Open the file `Harshit_Agrawal_Swiggy_Case_Study (1).ipynb`.
2.  Run the code blocks one by one to see the results!
