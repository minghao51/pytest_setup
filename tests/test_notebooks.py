import os
import pytest

REQUIRED_NOTEBOOKS = [
    'test101.ipynb',
    # 'model_training.ipynb',
    # 'evaluation.ipynb'
]

def test_notebooks_exist():
    """Test if required notebooks exist"""
    notebook_dir = 'notebooks'
    assert os.path.isdir(notebook_dir), "Notebooks directory not found"
    
    existing_notebooks = set()
    for root, _, files in os.walk(notebook_dir):
        for file in files:
            if file.endswith('.ipynb'):
                existing_notebooks.add(file)
    
    missing_notebooks = set(REQUIRED_NOTEBOOKS) - existing_notebooks
    assert not missing_notebooks, f"Required notebooks missing: {missing_notebooks}"

# @pytest.mark.parametrize('notebook_name', REQUIRED_NOTEBOOKS)
# def test_notebook_execution(notebook_name):
#     """Test if specific notebooks can execute"""
#     notebook_path = os.path.join('notebooks', notebook_name)
#     assert os.path.exists(notebook_path), f"Notebook not found: {notebook_name}" 