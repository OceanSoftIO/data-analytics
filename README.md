# 🔥 MLOps at Scale 🦅

🌟 An end-to-end full-stack Data Science and AI/ML project effectively implementing ML models, MLOps practices, scalable machine learning, and data storytelling. ✨

📚 `🛠️ Experiment (Design + Develop) --> 🚀 Production (Deploy + Iterate) ⚙️`: Full-Stack **Data Science** and Production-Grade **Machine Learning** at Scale are the fastest-growing fields in technology. This repository aims to develop professional and strong advanced analytics skills to compete in the age of digital and AI. 🏁

<div align="left">
  <a href="https://www.linkedin.com/in/nnthanh" target="blank"><img align="center" src="https://img.shields.io/badge/-nnthanh-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/nnthanh/" alt="Nhat-Thanh Nguyen" height="25" width="100" /></a>
  <a href="https://github.com/nnthanh101/" target="blank"><img align="center" src="https://img.shields.io/github/followers/nnthanh101?label=Follow&style=social&link=https://github.com/nnthanh101/" alt="Thanh Nguyen" height="25" width="100" /></a>
  <a href="https://www.facebook.com/groups/platformengineering" target="blank"><img align="center" src="https://img.shields.io/badge/Facebook-blue?style=flat-square&logo=facebook&logoColor=white&link=[https://www.linkedin.com/in/nnthanh/](https://www.facebook.com/groups/platformengineering)" alt="Nhat-Thanh Nguyen" height="25" width="100" /></a>  
</div>

---

🎯 End-to-end full-stack machine learning from experimental (design + development) to production (deployment + iteration) for iteratively building reliable production-grade AI/ML applications.

* [x] 💡 Agile CRISP-DM for Data Science and Machine Learning
  * [x] Cookiecutter Data Science (CCDS) V2: data science tooling and MLOps
  * [x] Agile Implementation of CRISP-DM for Data Science and Machine Learning
* [ ] ⚙️ MLOps
  * [ ] 💻 DevOps best practices for developing and deploying machine learning models.
  * [ ] ⚙️ Build an end-to-end machine learning system by connecting MLOps components such as tracking, testing, serving, and orchestration.
* [ ] 🚀 Dev to Prod:
  * [ ] 🐙 Develop robust CI/CD workflows to continuously train and deploy better models in a modular way that integrates with any stack.
  * [ ] 📈 Scale: ML workloads (data, training, tuning, and serving) are easily scalable, facilitating a quick and reliable transition from development to production without requiring code or infrastructure modifications.

---

## Deliverables 💎

|**:calendar:**|**:alarm_clock: Deliverables / Tasks Done**| **:link: Reference Links**|
|------|--------------------|---------------------|
|~~01~~| 🎓 **AWS Certified Data Analytics - Specialty (DAS)** (Collecting Streaming Data, Data Collection and Getting Data, Amazon Elastic Map Reduce (EMR), Using Redshift & Redshift Maintenance & Operations, AWS Glue, Athena, and QuickSight, ElasticSearch, AWS Security Services) ✅ | [A Cloud Guru - DAS](https://learn.acloud.guru/course/aws-certified-database-speciality-dbs-c01/dashboard) & [ACG Practice Exam](https://practice-exam.acloud.guru/9f55ebb2-12f8-4a55-a41b-fe5cb1917e30) & [UDemy Practice Exam](https://www.udemy.com/course/aws-certified-data-analytics-specialty-practice-exams-amazon/)|
|02| 🎓 **AWS Certified Machine Learning - Specialty (MLS-C01)** (Data Preparation, Data Analysis and Visualization, Modeling, Algorithms, Evaluation and Optimization, Implementation and Operations) ☑️ | [A Cloud Guru - MLS-C01](https://learn.acloud.guru/course/aws-certified-machine-learning-specialty/dashboard) & [ACG Practice Exam](https://practice-exam.acloud.guru/f87ac9a1-2d47-44f1-8e10-2a8e43959ef5) & [UDemy Practice Exam](https://www.udemy.com/course/aws-certified-machine-learning-specialty-practice-exams-amazon/) |  
|~~03~~| 🛠 Reproducible Local Development for Data Science and Machine Learning projects | [Data Science](https://github.com/nnthanh101/Data-Science) | 
|04| 👨‍💻 **Analytics-Experience Project:** Time Series Forecasting & Machine Learning Prediction | [Analytics-Experience Project](https://analytics-experience.pages.dev) |
|05| 📚 **MLOps** | [MLOps]() |
|06| 💹 **Analytics Dashboard:** Data Insights & Visual Analytics | [Visual Analytics]()|
|07| 🚀 **Scalable MLOps** MLOps at Production-grade Scale | [Scalable MLOps](#)|

--------

## Project Organization

> 🛠 Production-grade project structure for successful data-science or machine-learning projects 🚀

> 💎 End-to-end Data Science and Advanced Analytics Experience 🚀


```
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          🤝 Explain your project and its structure for better collaboration.
├── config/
│   └── logging.config.ini
├── data               🔍 Where all your raw and processed data files are stored.
│   ├── external       <- Data from third-party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, unprocessed, immutable data dump.
│
├── docs               📓 A default docusaurus | mkdocs project; see docusaurus.io | mkdocs.org for details
│
├── models             🧠 Store your trained and serialized models for easy access and versioning.
│
├── notebooks          💻 Jupyter notebooks for exploration and visualization.
│   ├── data_exploration.ipynb
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
│
├── pyproject.toml     <- Project configuration file with package metadata for analytics
│                         and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            📊 Generated analysis (reports, charts, and plots) as HTML, PDF, LaTeX.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   🛠 The requirements file for reproducing the analysis environment, for easy environment setup.
│
├── setup.cfg          <- Configuration file for flake8
│
├── src                💾 Source code for data processing, feature engineering, and model training.
│   ├── data/
│   │   └── data_preprocessing.py
│   ├── features/
│   │   └── feature_engineering.py
│   ├── models/
│   │   └── model.py
│   └── utils/
│       └── helper_functions.py
├── tests/
│   ├── test_data_preprocessing.py
│   ├── test_feature_engineering.py
│   └── test_model.py
├── setup.py           🛠 A Python script to make the project installable.
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── analytics          🧩 Source code for use in this project.
    │
    ├── __init__.py    <- Makes analytics a Python module
    │
    ├── data           <- Scripts to download, preprocess, or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make predictions.           
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results-oriented visualizations
        └── visualize.py
```