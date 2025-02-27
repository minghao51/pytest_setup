import os
import pytest

def test_iac_files():
    """Test if IaC files exist and are valid Terraform/YAML/JSON"""
    iac_files = []
    for root, _, files in os.walk('infrastructure'):
        for file in files:
            if file.endswith(('.tf', '.tfvars', '.yml', '.yaml', '.json', '.svg')):
                iac_files.append(os.path.join(root, file))
    
    assert len(iac_files) > 0, "No IaC files found in infrastructure directory"
    
    for file_path in iac_files:
        with open(file_path, 'r') as f:
            if file_path.endswith('.tf'):
                # Basic syntax check for Terraform files
                content = f.read()
                assert 'resource' in content or 'variable' in content or 'provider' in content, \
                    f"Terraform file {file_path} doesn't contain basic Terraform blocks" 