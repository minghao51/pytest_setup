import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.utils import setup_project_structure

def test_project_structure():
    """Test if essential project directories exist"""
    setup_project_structure()
    required_dirs = [
        'data',
        # 'data/raw',
        # 'data/processed',
        'notebooks',
        'infrastructure',
        'src'
    ]
    for dir_name in required_dirs:
        assert os.path.isdir(dir_name), f"Directory '{dir_name}' not found"

# def test_data_directory():
#     """Test if data directory contains files and has proper structure"""
#     data_dir = 'data'
#     assert os.path.isdir(data_dir), "Data directory not found"
#     # assert os.path.isdir(os.path.join(data_dir, 'raw')), "Data/raw directory not found"
#     # assert os.path.isdir(os.path.join(data_dir, 'processed')), "Data/processed directory not found"
    
#     # Check if data directory is not empty
#     has_files = False
#     for root, _, files in os.walk(data_dir):
#         if files:
#             has_files = True
#             break
    
#     assert has_files, "Data directory is empty" 