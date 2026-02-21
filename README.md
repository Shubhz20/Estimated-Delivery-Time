# Swiggy Delivery Time Prediction

This project is a Machine Learning case study that predicts food delivery times for Swiggy based on various factors like location, ratings, and price.

## 📌 Project Overview

Imagine you order food on an app like Swiggy. The app tells you it will arrive in "35 mins". How does it know that?
This project builds a **Decision Tree Regressor** model that learns from past delivery data to estimate these times.

## 📊 Dataset Details

The model is trained on a dataset of **8,680** restaurant orders.

- **Source**: `swiggy.csv`
- **Features Used**:
  - **City**: The city where the restaurant is located (9 unique cities).
  - **Area**: Specific locality (833 unique areas).
  - **Price**: Approximate cost for two people.
  - **Avg ratings**: Average customer rating (out of 5).
  - **Total ratings**: Number of ratings received.
- **Target Variable**: `Delivery time` (in minutes).

## 🔍 Key Insights from Data

Before training, we analyzed the data and found:

- **Average Delivery Time**: ~54 minutes.
- **Fastest Delivery**: 20 minutes.
- **Longest Delivery**: 109 minutes.
- **Top Cities by Restaurant Count**:
  1.  Kolkata (1346)
  2.  Mumbai (1277)
  3.  Chennai (1106)
  4.  Pune (1090)
  5.  Hyderabad (1075)

## ⚙️ How It Works

1.  **Data Loading & Cleaning**: We load the data and remove rows with missing values to ensure quality.
2.  **Preprocessing**:
    - Numerical features (`Price`, `Ratings`) are used as is.
    - Categorical features (`City`, `Area`) are converted into numbers using **One-Hot Encoding**, resulting in **845 input features**.
3.  **Model Training**:
    - Algorithm: **Decision Tree Regressor**
    - Configuration: `max_depth=10` (to balance learning and overfitting).
    - Split: 80% Training Data (6944 samples) / 20% Testing Data (1736 samples).
4.  **Evaluation**:
    - We test the model on unseen data to check its accuracy.

## 📈 Model Performance

- **Mean Absolute Error (MAE)**: **8.77 min**
  - _Interpretation_: On average, the model's prediction is off by about ±9 minutes from the actual delivery time.
- **R² Score**: **0.4039**
  - _Interpretation_: The model explains about 40% of the variability in delivery times based on the available data.

## 🛠️ Tools Used

- **Python**: Core programming language.
- **Pandas**: For data manipulation and analysis.
- **Scikit-Learn**: For building and evaluating the machine learning model.
- **Jupyter Notebook**: For interactive development and data visualization.

## 📁 Project Structure

```text
.
├── Harshit_Agrawal_Swiggy_Case_Study.ipynb  # Main analysis & model building notebook
├── swiggy.csv                               # Dataset (not included in repo)
└── README.md                                # Project documentation
```

## 🧪 Feature Engineering Ideas (Future)

To improve the model's R² score, the following features could be explored:

- **Time of Day**: Orders at lunch/dinner peaks might take longer.
- **Day of Week**: Weekends vs. Weekdays.
- **Weather Conditions**: Rain or extreme heat impacting delivery speed.
- **Cuisine Type**: Some foods (like Pizza) may have specific preparation times.
- **Distance**: Actual distance between the restaurant and the delivery point.

## 🚀 Future Roadmap

- [ ] Implement **Random Forest Regressor** to compare performance.
- [ ] Use **XGBoost** or **LightGBM** for better predictive power.
- [ ] Perform **Hyperparameter Tuning** using GridSearchCV.
- [ ] Add data visualizations (Heatmaps, correlation plots).

## 🚀 How to Run

1.  Clone this repository.
2.  Ensure you have Python installed with `pandas` and `scikit-learn`.
3.  Place the `swiggy.csv` dataset in the root directory.
4.  Open the notebook `Harshit_Agrawal_Swiggy_Case_Study (1).ipynb` in Jupyter Notebook or Google Colab.
5.  Run all cells to see the analysis and predictions in action!

## 🤝 Contributing

Contributions are welcome! If you have ideas to improve the model or find any bugs, feel free to open an issue or submit a pull request.

## 👤 Author

**Harshit Agrawal**

- [GitHub](https://github.com/harshitagrawal) _(Update with your actual link)_

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
