
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.model_selection import train_test_split

def preprocess_data(df, categorical_cols, numerical_cols, target_col):
    # Separar X e y
    X = df[categorical_cols + numerical_cols]
    y = df[target_col]
    
    # Codificación ordinal
    encoder = OrdinalEncoder()
    X[categorical_cols] = encoder.fit_transform(X[categorical_cols])
    
    # Escalado de variables numéricas
    scaler = StandardScaler()
    X[numerical_cols] = scaler.fit_transform(X[numerical_cols])
    
    # División en train y test
    return train_test_split(X, y, test_size=0.2, random_state=42)
