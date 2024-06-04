import os
import numpy as np
from data_handler import DataHandler

def main():
    # Test with numpy arrays
    X_np = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y_np = np.array([1, 2, 3])
    data_handler_np = DataHandler()
    data_handler_np.from_numpy(X_np, y_np)
    print("Numpy Features:\n", data_handler_np.get_features())
    print("Numpy Labels:\n", data_handler_np.get_labels())

    # Test with an Excel file in the data folder
    xlsx_file_path = os.path.join(os.path.dirname(__file__), '../../data', 'test_data.xlsx')
    print("xlsx_file_path: \n", os.path.abspath(xlsx_file_path))

    if os.path.exists(xlsx_file_path):
        data_handler_xlsx = DataHandler()
        data_handler_xlsx.from_xlsx(xlsx_file_path)
        print("Excel Features:\n", data_handler_xlsx.get_features())
        print("Excel Labels:\n", data_handler_xlsx.get_labels())
    else:
        print(f"File not found: {xlsx_file_path}")

if __name__ == "__main__":
    main()