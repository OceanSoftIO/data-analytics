# How to Use `Runbooks`

> This part of the project documentation focuses on a
**problem-oriented** approach. You'll tackle common
tasks that you might have, with the help of the code
provided in this project.

This section dives **deeper** into **how to use the public `runbooks` package** available on [PyPI](https://pypi.org/project/runbooks/) and the **Docker image** hosted on [GitHub Container Registry (GHCR)](https://github.com/nnthanh101/packages/container/package/runbooks).  

We will cover **installation**, **usage examples**, and **integration** into Python and containerized environments, ensuring **best practices** in Python and DevOps workflows.  

---

## 1. How to Use PyPI `runbooks`

### **Step 1.1. Install from PyPI**  

#### **Install the Package**  
Run the following command to install the `runbooks` package from **PyPI**:  
```bash
pip install runbooks
```

#### **Verify the Installation**  
Check that the package is installed successfully:  
```bash
pip show runbooks
```

**Expected Output**:  
```
Name: runbooks
Version: 0.1.5
Summary: CloudOps Automation for DevOps and SRE teams.
Author-email: runbooks maintainers <nnthanh101@gmail.com>
Location: /home/os/.local/lib/python3.12/site-packages
Requires: boto3, loguru, moto, requests, tqdm, typer
```



---

### **Step 1.2. Use Python Scripts with Installed `runbooks`**  

#### **Example 1: Using the Calculator CLI**  
```bash
runbooks calculate + 5 10
```

**Output**:  
```
Result: 15.0
```

#### **Example 2: Using the Toolkit CLI**  
```bash
runbooks toolkit add 5 10
```

**Output**:  
```
Result: 15.0
```

---

### **Step 1.3. Use the Python API in Scripts**  

#### **Step 1: Import and Initialize Components**  
```python
from runbooks.calculator import Calculator
from runbooks.toolkit import add, subtract, multiply, divide
from runbooks.exceptions import InvalidOperationError
from runbooks.utils import validate_input

# Initialize the calculator with precision
calc = Calculator(precision=2)
```

#### **Step 2: Perform Operations (Calculator)**  
```python
try:
    result = calc.add(5, 10)
    print(f"Addition Result: {result}")  # Output: 15.0
except InvalidOperationError as e:
    print(f"Error: {e}")
```

#### **Step 3: Perform Operations (Toolkit)**  
```python
try:
    print(add(5, 10))        # Output: 15.0
    print(subtract(10, 5))   # Output: 5.0
    print(multiply(5, 2))    # Output: 10.0
    print(divide(10, 2))     # Output: 5.0
except Exception as e:
    print(f"Error: {e}")
```

--- 

## **2. How to Use `runbooks` Docker from DockerHub (and GHCR)**

### **Step 1: Pull the Image from GHCR**  
```bash
docker pull nnthanh101/runbooks:latest
```

### **Step 2: Verify the Image**  
```bash
docker images
```

**Expected Output**:  
```
REPOSITORY            TAG               IMAGE ID       CREATED        SIZE
nnthanh101/runbooks   latest            ca55512f7d5d   28 hours ago   2.43GB
```

### **Step 3: Run Commands Using Docker**  

**Calculator Use-Case:**  
```bash
docker run --rm nnthanh101/runbooks:latest runbooks calculate + 5 10
```

**Output**:  
```
Result: 15.0
```

**Toolkit Use-Case:**  
```bash
docker run --rm nnthanh101/runbooks:latest runbooks toolkit add 5 10
```

**Output**:  
```
Result: 15.0
```

---

## **3. Advanced Usage: Environment Variables & Configurations**  

### **Step 1: Configure Logging**  
The `runbooks` package uses logging configuration from `DEFAULT_CONFIG` in `src/runbooks/config.py`.  

**Example Configuration**:  
```python
DEFAULT_CONFIG = {
    "log_file": "runbooks.log",
    "debug": True,
    "precision": 2
}
```

**Set Environment Variables in Docker**:  
```bash
docker run --rm -e LOG_FILE=custom.log -e DEBUG=true nnthanh101/runbooks:latest
```

---

## **4. Automate Deployment and CI/CD with GHCR and PyPI**  

### **Step 1: Build and Push to GHCR**  

1. **Build the Docker Image**:  
```bash
docker build -t nnthanh101/runbooks:latest .
```

2. **Log in to GHCR**:  
```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
```

3. **Push the Image**:  
```bash
docker push nnthanh101/runbooks:latest
```

---

### **Step 2: Publish Python Package to PyPI**  

1. **Build Package**:  
```bash
task build
```

2. **Upload to PyPI**:  
```bash
task publish
```

---

## **5. Documentation with MkDocs**

### **Step 1: Install MkDocs**  
```bash
pip install mkdocs mkdocs-material mkdocstrings
```

### **Step 2: Serve Documentation**  
```bash
mkdocs serve
```

**Access URL**: `http://127.0.0.1:8000`

---

## **6. Best Practices for SDLC and CI/CD**

### **Taskfile Commands**  
- **Linting**:  
  ```bash
  task lint
  ```

- **Testing**:  
  ```bash
  task test
  ```

- **Build & Publish**:  
  ```bash
  task build
  task publish
  ```

---

## **7. FAQ and Troubleshooting**  

### **1. Installation Issues (PyPI)**  
**Error**:  
```bash
ERROR: No matching distribution found for runbooks
```

**Solution**:  
Ensure Python version is **3.11+**:  
```bash
python --version
```

---

### **2. Docker Permission Denied**  
**Error**:  
```bash
permission denied while trying to connect to the Docker daemon
```

**Solution**:  
Add the user to the Docker group:  
```bash
sudo usermod -aG docker $USER
```

---

### **3. Logs Not Appearing**  
**Issue**: Logs are missing in the output.  

**Solution**: Check log file permissions and paths:  
```bash
ls -l runbooks.log
```

---

## **8. Summary**

This template establishes **best practices** for Python projects with **Dockerized CI/CD pipelines** and **multi-platform distribution via PyPI and GHCR**. It supports:

- **Scalable DevOps workflows** with modular design.
- **Secure containerized deployments** with GHCR.
- **Automated testing and linting pipelines** using Taskfile and GitHub Actions.
- **Comprehensive documentation** with MkDocs and docstrings for maintainability.

**By following this guideline**, your Python-based DevOps tools will meet **enterprise-grade standards**, ensuring **high performance, reliability, and security**.