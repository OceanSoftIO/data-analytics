```
python3 -m venv venv
source venv/bin/activate

pip install numpy
```

```
python3 -c "import numpy as np; print(np.array([1, 2, 3]) + np.array([4, 5, 6]))"
```

$ python3

```python
import numpy as np
result = np.array([1, 2, 3]) + np.array([4, 5, 6])
print(result)
```

## 

runbooks.validate_input() 

runbooks.add(5,2)

## uv

```
uv venv ~/.venv
# source ~/.venv/bin/activate

uv pip install pytest pytest-cov ruff

uv pip list

# uv sync --frozen --no-install-project --no-dev --compile-bytecode
# uv sync --all-extras --dev
# uv pip install --compile-bytecode .
```

## test_*.py using pytest

* [ ] 1. Run Tests

    ```
    pytest tests/test_file_manager.py --cov=src/runbooks --cov-report=term-missing -v

    ```

* [ ] 2. Install Package

    ```
    pip install -e .
    ```

* [ ] 3. Execute CLI Tool

    ```
    runbooks test_folder test_file.txt
    ```
