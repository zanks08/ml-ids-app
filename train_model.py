from utils.preprocess import load_data
import xgboost as xgb
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# 1. Load the training data
X, y = load_data("data/KDDTrain+.txt")

# 2. Encode y labels (train labels)
le = LabelEncoder()
y = le.fit_transform(y)

# 3. Create the model (NEW TUNED PARAMETERS)
model = xgb.XGBClassifier(
    n_estimators=800,
    max_depth=15,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    gamma=0.2,
    reg_alpha=0.1,
    reg_lambda=1.0,
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42
)

# 4. Train the model
model.fit(X, y)

# 5. Save the trained model
joblib.dump(model, "model/ids_model.pkl")

print("✅ Model trained and saved successfully as 'ids_model.pkl'!")

# 6. Load the test data
X_test, y_test = load_data("data/KDDTest+.txt")

# 7. Encode y_test labels
y_test = le.transform(y_test)

# 8. Predict
y_pred = model.predict(X_test)

# 9. Evaluate
print("\n📊 Model Evaluation on Test Data:\n")
print(classification_report(y_test, y_pred))

