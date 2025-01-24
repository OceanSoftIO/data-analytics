# 🔥 CloudOps Automation at Scale 🦅

🌟 You can use [CloudOps Automation Runbooks](https://cloudops.oceansoft.io), built on Jupyter Notebooks, to quickly create SRE RunBooks for Runbook Automation and Cloud Infrastructure Management! 🌐

> [!IMPORTANT]
> **🏆 Mission**: Our mission is to simplify CloudOps Automation for DevOps and SRE teams by providing an extensive, community-driven repository of actions and runbooks that streamline day-to-day operations. 

> [!NOTE]
> **👁️ Vision**: Our vision is to be the 🥇 One-Stop Multi-Cloud Platform Engineering & Best Practices Solution for all CloudOps Automation needs, allowing DevOps and SRE teams to automate their workflows with ease, improve efficiency, and minimize toil.

[![🐍 Runbooks PyPI version](https://img.shields.io/pypi/v/runbooks)](https://pypi.org/project/runbooks/) ![🦾 GitHub Container Registry](https://img.shields.io/github/v/tag/nnthanh101/runbooks:latest?label=GHCR%20Version&color=blue&logo=docker)


<div align="left">
  <a href="https://www.linkedin.com/in/nnthanh" target="blank"><img align="center" src="https://img.shields.io/badge/-nnthanh-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/nnthanh/" alt="Nhat-Thanh Nguyen" height="25" width="100" /></a>
  <a href="https://github.com/nnthanh101/" target="blank"><img align="center" src="https://img.shields.io/github/followers/nnthanh101?label=Follow&style=social&link=https://github.com/nnthanh101/" alt="Thanh Nguyen" height="25" width="100" /></a>
  <a href="https://www.facebook.com/groups/platformengineering" target="blank"><img align="center" src="https://img.shields.io/badge/Facebook-blue?style=flat-square&logo=facebook&logoColor=white&link=[https://www.linkedin.com/in/nnthanh/](https://www.facebook.com/groups/platformengineering)" alt="Nhat-Thanh Nguyen" height="25" width="100" /></a>  
</div>

---

## 🛠️ Features

* 🥉 ✅**Lightning-Fast Toolchain**: Powered by 📦 `uv` - Next-generation Python dependency and build management, 💅 `ruff` - Linting and formatting at blazing speed, and 🧪 pytest - Robust testing framework with coverage reports.
* 🥈 ✅**Effortless CI/CD Pipelines**: 🛠️ Taskfile Automation - Say goodbye to manual SDLC repetitive tasks, 🐳 Containerized Workflows – 🛡️ Security-first practices and Multi-stage Wolfi-based Docker builds for scalable production-ready environments, and ⚙️ Auto-publish to `PyPI` and GitHub Container Registry (`GHCR`) with GitHub Actions.
* 🥇 ☑️**CloudOps Automation and FinOps Toolkit** – Pre-configured hybrid-cloud workflows and seamlessly integrations (jupyterlab, mkdocs, boto3, moto) for managing cloud infrastructure 🌐.  

| **Feature**              | **Toolchain**                            | **Purpose**                                        |
|--------------------------|-------------------------------------|----------------------------------------------------|
| 🛠️ Configuration         | `pyproject.toml`                 | Centralized configuration for dependencies, testing, and linting.  |
| 🧹 Task Automation       | [`Taskfile`](https://taskfile.dev/) | Automates repetitive tasks like linting, testing, and publishing.  |
| 📦 Python Dependencies   | [`uv`](https://docs.astral.sh/uv/)  | Lightning-fast dependency resolution, caching, and builds. |
| 💅 Linting & Formatting  | [`ruff`](https://docs.astral.sh/ruff/) | Enforces code quality standards, auto-formatting, and import sorting.  |
| 🧪 Testing Framework     | [`pytest`](https://docs.pytest.org/)  | Comprehensive unit tests, integration tests with coverage reporting.    |
| 🐳 Docker Integration    | Dockerfile + [`DevContainer`](https://containers.dev/)  | Optimized wolfi-based multi-stage builds for CI/CD and local development environments. |
| 🦾 CI/CD Pipelines       | [`GitHub Actions`](https://github.com/features/actions) | Automated builds, tests, and deployments to PyPI and GHCR. |
| 📝 Security Compliance   | [`chainguard/wolfi-base`](https://hub.docker.com/r/chainguard/wolfi-base) + SBOM + Attestations | Ensures compliance, vulnerability scanning, and security transparency. |

---

### WIP

- [ ] 📚 auto doc generation
- [ ] **CLI Tools** – Typer simplifies automation for AWS resources.  
- [ ] **Logging** – Loguru ensures structured logs for debugging. 
- [x] 🐳 CI/CD Optimized Docker Image runs when a new *release* is created pushing to gh registry
- [x] 🦾 GitHub actions:
    - [x] auto publish to [`pypi`](https://pypi.org/) on push on `main`
    - [ ] auto creating a new tag on push on `main`, sync versions
    - [x] run `tests` and `lint` on `dev` and `main` when a PR is open

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/nnthanh101/runbooks.git
cd runbooks
```

### 2. Install Dependencies and Run CI/CD Pipelines

```bash
echo "Install Python dependencies using UV"
task install

echo "Run CI/CD pipeline tasks: clean, lint, format, test, and build"
task ci

echo "Publish the project package to PyPI"
task publish
```

### 3. Run in DevContainer 🐳

1. Open the project in **VSCode**.  
2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.  
3. **Reopen in Container**:  
   **Command Palette `Ctrl+Shift+P` → Reopen in Container**.  

---

## Project Structure

> 🛠 End-to-end Production-grade project structure for successful 💎 CloudOps Automation and Visual Analytics FinOps projects 🚀

```
cloudops-automation/
├── .devcontainer/     ## Dev Container configurations
│   └── Dockerfile     ## Container image build file
├── .github/           ## CI/CD workflows
│   ├── workflows/     ## GitHub Actions workflows
│   └── templates/     ## Workflow templates
├── .vscode/           ## IDE-specific configurations
├── config/            ## Configuration files (YAML, JSON)
├── data               🔍 Where all your raw and processed data files are stored.
│   ├── external       <- Data from third-party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, unprocessed, immutable data dump.
│
├── docs               📓 A default mkdocs project; see mkdocs.org for details
│   ├── api/                 ## API documentation
│   ├── architecture/        ## Architecture diagrams
│   ├── tutorials/           ## Tutorials and guides
│   ├── getting-started.md   ## Quickstart guide
│   └── index.md             ## Overview documentation
│
├── logs/                    ## Log files for debugging
|
├── models             🧠 Store your trained and serialized models for easy access and versioning.
│
├── notebooks          💻 Jupyter notebooks for experiments and visualization.
│   ├── data_exploration.ipynb
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         runbooks and configuration for tools like black
│
├── src/                            ## 🧩 Source code for use in this project.
│   ├── runbooks/                   ## Main module for CloudOps Runbooks automation
│   │   ├── __init__.py             ## Package initializer
│   │   ├── calculator.py           ## [Python101] Calculator
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   ├── utils.py                ## Utility scripts (logging, configs)
│   │   └── cleanup.py              ## Cleanup automation runbook
│   ├── main.py     
├── test/                           ## Unit and integration tests
│   ├── conftest.py
│   ├── __init__.py
│   ├── test_calculator.py          ## [Python101] Test cases for calculator
│   ├── test_utils.py               ## Test cases for utils
│   └── test_exceptions.py         
├── templates/                      ## Terraform and CloudFormation templates
├── tools/                          ## Developer tools and scripts
├── .dockerignore                   ## Docker ignore file
├── .env                            ## Environment variables
├── .gitignore                      ## Git ignore file
├── .python-version                 ## Python version management
├── .gitignore
├── mkdocs.yml                      # Documentation generator configuration
├── README.md          🤝 Explain your project and its structure for better collaboration.
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            📊 Generated analysis (reports, charts, and plots) as HTML, PDF, LaTeX.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   🛠 The requirements file for reproducing the analysis environment, for easy environment setup.
└── Taskfile           <- Taskfile with convenience commands like `task data` or `task train`

```

### [Github Container Registry to store and manage Docker and OCI images](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

1. Check if the image exists in GitHub Packages:

```
docker pull ghcr.io/nnthanh101/runbooks:latest
```

2. If the image doesn't exist, build and push it:

```
docker build -t ghcr.io/nnthanh101/runbooks:latest .
docker login ghcr.io -u nnthanh -p GH_TOKEN
docker push ghcr.io/nnthanh101/runbooks:latest
```

3. Inspect

```
docker inspect ghcr.io/nnthanh101/runbooks:latest
```
