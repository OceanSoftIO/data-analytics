### 0.2.0 (2025-01-12)

##### New Features

* [ ] ...

##### New Documentation

##### Refactor

##### Bug Fixes


---

### 0.1.5 (2025-01-05)

##### New Features

* [x] 1st-Init [Cookiecutter Data Science & Machine Learning](https://github.com/drivendataorg/cookiecutter-data-science)
* [x] 1st-Init Project Documentation using `mkdocs`

##### CloudOps/FinOps Project Template 

Features:
- [x] 🛠️ configuration in a single file [`pyproject.toml`](pyproject.toml)
- [x] 📦 [`uv`](https://docs.astral.sh/uv/) as package manager
- [x] 💅 [`ruff`](https://docs.astral.sh/ruff/) for linting and formatting
- [x] 🧪 [`pytest`](https://docs.pytest.org/en/stable/) 
- [x] 🧹 [`Taskfile`](Taskfile) with code quality checks
- [x] 📚 Auto API Document Generation
- [ ] **CLI Tools** – Typer simplifies automation for AWS resources.  
- [x] **Logging** – Loguru ensures structured logs for debugging. 
- [x] 🐳 CI/CD Optimized Docker Image runs when a new *release* is created pushing to gh registry
- [x] 🦾 GitHub actions:
    - [x] auto publish to [`pypi`](https://pypi.org/) on push on `main`
    - [ ] auto creating a new tag on push on `main`, sync versions
    - [x] run `tests` and `lint` on `dev` and `main` when a PR is open
