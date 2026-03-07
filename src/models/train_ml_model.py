
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_ml_model(df):

    X = df[['temperature_c','humidity_percent','wind_speed_mps','month','dayofyear']]
    y = df['rainfall_mm']

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train,y_train)

    score = model.score(X_test,y_test)

    return model, score
