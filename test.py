from joblib import load

pipeline = load('outputs/ml_pipeline/predict_sale_price/v1/best_regressor_pipeline.pkl')
print(type(pipeline))
print(pipeline.named_steps)  # This should list the steps in the pipeline
