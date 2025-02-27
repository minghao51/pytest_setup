import os

def setup_project_structure():
    """Create essential project directories if they don't exist"""
    required_dirs = [
        'data',
        # 'data/raw',
        # 'data/processed',
        'notebooks',
        'infrastructure',
        'src',
        'docker'
    ]
    for dir_name in required_dirs:
        os.makedirs(dir_name, exist_ok=True) 

if __name__ =="__main__":
    setup_project_structure()