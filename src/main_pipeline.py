
from data.load_data import load_weather_data
from features.feature_engineering import build_features
from models.train_ml_model import train_ml_model
from visualization.rainfall_plots import rainfall_trend_plot

def main():

    df = load_weather_data("data/raw/weather_timeseries.csv")

    df_features = build_features(df)

    model, score = train_ml_model(df_features)

    print("Model performance:", score)

    rainfall_trend_plot(df_features)

if __name__ == "__main__":
    main()
