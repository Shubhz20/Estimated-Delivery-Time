import utils
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_model():
    """Trains the Swiggy Delivery Time prediction model."""
    logging.info("Loading dataset...")
    try:
        df = utils.load_data()
    except FileNotFoundError:
        logging.error("swiggy.csv not found. Please place it in the project root.")
        return

    logging.info(f"Data loaded successfully with {len(df)} samples.")
    
    X_encoded = utils.prepare_features(df)
    y = df['Delivery time']
    
    logging.info(f"Features prepared. Encoded feature count: {X_encoded.shape[1]}")
    
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
    logging.info(f"Training set: {len(X_train)} samples. Test set: {len(X_test)} samples.")
    
    logging.info("Training Decision Tree Regressor (max_depth=10)...")
    model = DecisionTreeRegressor(max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    logging.info("Evaluating model on test data...")
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    logging.info(f"Evaluation Complete | MAE: {mae:.2f} mins | R² Score: {r2:.4f}")

if __name__ == "__main__":
    train_model()
