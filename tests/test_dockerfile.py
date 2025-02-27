import os

def test_dockerfile_exists():
    """Test if Dockerfile exists and contains essential commands"""
    docker_dir = 'docker'
    dockerfile_path = os.path.join(docker_dir, 'Dockerfile')
    
    # Check if docker directory exists
    assert os.path.isdir(docker_dir), "Docker directory not found"
    
    # Check if Dockerfile exists in docker directory
    assert os.path.isfile(dockerfile_path), f"Dockerfile not found in {docker_dir} directory"
    
    with open(dockerfile_path, 'r') as f:
        content = f.read().lower()
        
    essential_commands = ['from', 'workdir', 'copy', 'run']
    for command in essential_commands:
        assert command in content, f"Dockerfile missing essential command: {command}" 