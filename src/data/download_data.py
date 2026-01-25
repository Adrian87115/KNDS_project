import kagglehub
import shutil
import os
from pathlib import Path

def main():
    
    project_dir = Path(__file__).resolve().parents[2]
    raw_data_dir = project_dir.joinpath('data', 'raw')
    print(f"Data directory: {raw_data_dir}")

    path = kagglehub.dataset_download("ahsan81/hotel-reservations-classification-dataset")

    downloaded_files = os.listdir(path)
    csv_file = [f for f in downloaded_files if f.endswith('.csv')][0]
    source_path = os.path.join(path, csv_file)
    
    destination_path = raw_data_dir.joinpath(csv_file)

    shutil.copy(source_path, destination_path)

    print("-" * 30)
    print(f"Data downloaded and saved to: {destination_path}")
    print("-" * 30)

if __name__ == '__main__':
    main()