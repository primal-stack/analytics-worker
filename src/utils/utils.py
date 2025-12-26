import os
import logging
import pandas as pd
import numpy as np

def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        logging.error(f"Failed to load data from {file_path}: {str(e)}")
        raise

def save_data(df: pd.DataFrame, file_path: str):
    try:
        df.to_csv(file_path, index=False)
    except Exception as e:
        logging.error(f"Failed to save data to {file_path}: {str(e)}")
        raise

def create_directory(directory_path: str):
    try:
        os.makedirs(directory_path, exist_ok=True)
    except Exception as e:
        logging.error(f"Failed to create directory {directory_path}: {str(e)}")
        raise

def get_files(directory_path: str) -> list:
    try:
        return [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    except Exception as e:
        logging.error(f"Failed to list files in {directory_path}: {str(e)}")
        raise