import subprocess

def test_app():
    result = subprocess.run(['python3', 'app.py'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout