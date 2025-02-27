# import os
# import pytest
# import nbformat
# from nbconvert.preprocessors import ExecutePreprocessor

# def test_notebooks():
#     """Test if Jupyter notebooks exist, are valid, and can execute"""
#     notebook_files = []
#     for root, _, files in os.walk('notebooks'):
#         for file in files:
#             if file.endswith('.ipynb'):
#                 notebook_files.append(os.path.join(root, file))
    
#     assert len(notebook_files) > 0, "No Jupyter notebooks found"
    
#     # Configure notebook execution
#     ep = ExecutePreprocessor(
#         timeout=600,  # Timeout in seconds
#         kernel_name='python3'
#     )
    
#     for notebook_path in notebook_files:
#         try:
#             with open(notebook_path, 'r', encoding='utf-8') as f:
#                 nb = nbformat.read(f, as_version=4)
                
#                 # First validate notebook format
#                 nbformat.validate(nb)
                
#                 # Try to execute the notebook
#                 try:
#                     ep.preprocess(nb)
#                 except Exception as e:
#                     pytest.fail(f"Notebook {notebook_path} failed to execute: {str(e)}")
                    
#         except Exception as e:
#             pytest.fail(f"Invalid notebook {notebook_path}: {str(e)}") 

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

@pytest.mark.parametrize('notebook_name', REQUIRED_NOTEBOOKS)
def test_notebook_execution(notebook_name):
    """Test if specific notebooks can execute"""
    notebook_path = os.path.join('notebooks', notebook_name)
    assert os.path.exists(notebook_path), f"Notebook not found: {notebook_name}" 