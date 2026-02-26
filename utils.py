import pandas as pd

def load_data(filepath='swiggy.csv'):
    """Loads dataset and handles missing values.
    
    Args:
        filepath (str): Path to the dataset CSV file.
        
    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    df = pd.read_csv(filepath)
    return df.dropna()

def prepare_features(df):
    """Prepares features for the decision tree model.
    One-hot encodes categorical 'City' and 'Area' columns.
    
    Args:
        df (pd.DataFrame): Input dataframe.
        
    Returns:
        pd.DataFrame: DataFrame with categorical variables encoded.
    """
    X = df[['Price', 'Avg ratings', 'Total ratings', 'Area', 'City']]
    return pd.get_dummies(X, columns=['Area', 'City'])
