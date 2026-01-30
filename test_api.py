"""
Test script to verify API functionality
"""
import pickle
import pandas as pd
import numpy as np

print("=" * 60)
print("TESTING API COMPONENTS")
print("=" * 60)

# Test 1: Load Model
print("\n1. Loading model...")
try:
    with open('water_consumption_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("   ✓ Model loaded successfully")
except Exception as e:
    print(f"   ✗ Error loading model: {e}")
    model = None

# Test 2: Load Municipality Encoder
print("\n2. Loading municipality encoder...")
try:
    with open('municipality_encoder.pkl', 'rb') as f:
        municipality_encoder = pickle.load(f)
    print("   ✓ Municipality encoder loaded successfully")
except Exception as e:
    print(f"   ✗ Error loading municipality encoder: {e}")
    municipality_encoder = None

# Test 3: Load Feature Columns
print("\n3. Loading feature columns...")
try:
    with open('feature_columns.pkl', 'rb') as f:
        feature_columns = pickle.load(f)
    print("   ✓ Feature columns loaded successfully")
    print(f"   Features: {feature_columns}")
except Exception as e:
    print(f"   ✗ Error loading feature columns: {e}")
    feature_columns = None

# Test 4: Load Data
print("\n4. Loading data...")
try:
    df = pd.read_csv('water_consumption_100000_rows_improved.csv')
    print(f"   ✓ Data loaded: {len(df)} rows")
    print(f"   Municipalities: {df['region_name'].unique()}")
except Exception as e:
    print(f"   ✗ Error loading data: {e}")
    df = None

# Test 5: Test Prediction
if model is not None and municipality_encoder is not None and feature_columns is not None and df is not None:
    print("\n5. Testing prediction for Kurnool...")
    try:
        municipality = 'Kurnool'
        temperature = 32
        humidity = 65
        rainfall = 0
        
        # Get recent data
        muni_data = df[df['region_name'] == municipality].sort_values('date').tail(30)
        
        if len(muni_data) > 0:
            avg_consumption = muni_data['water_consumption_liters'].mean() / 1_000_000
            municipality_code = municipality_encoder.transform([municipality])[0]
            population = int(muni_data['population'].mean())
            industrial_index = int(muni_data['industrial_activity_index'].mean())
            prev_day_avg = muni_data['water_consumption_liters'].mean()
            
            prev_day_normalized = prev_day_avg / 100_000_000
            latest_date = pd.to_datetime(muni_data['date'].iloc[-1])
            month = latest_date.month
            season_map = {'Winter': 0, 'Summer': 1, 'Monsoon': 2, 'Spring': 3}
            season_str = muni_data['season'].iloc[-1]
            season = season_map.get(season_str, 0)
            
            feature_dict = {
                'temperature_celsius': temperature,
                'humidity_percent': humidity,
                'rainfall_mm': rainfall,
                'is_weekend': 0,
                'is_holiday': 0,
                'municipality_encoded': municipality_code,
                'population_scaled': population / 1_000_000,
                'industrial_scaled': industrial_index,
                'prev_day_consumption_normalized': prev_day_normalized,
                'prev_7day_avg_normalized': prev_day_normalized,
                'consumption_variance': 1.0,
                'month': month,
                'season': season
            }
            
            X_pred = pd.DataFrame([feature_dict])[feature_columns]
            predicted_consumption_liters = model.predict(X_pred)[0]
            predicted_consumption = predicted_consumption_liters / 1_000_000
            
            print(f"   ✓ Prediction successful!")
            print(f"   Predicted consumption: {predicted_consumption:.2f} ML")
            print(f"   Average consumption: {avg_consumption:.2f} ML")
        else:
            print(f"   ✗ No data found for municipality")
    except Exception as e:
        print(f"   ✗ Prediction error: {e}")
        import traceback
        traceback.print_exc()

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)
