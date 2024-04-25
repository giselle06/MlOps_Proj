# SLEEP HEALTH ANALYSIS 
![Static Badge](https://img.shields.io/badge/MLOps_Project-Data_Science?logoColor=FFBE98)

This Project is based on a Sleep Health Dataset. It is a MLOps Project predicting the sleep health of a person based on their habits and various other factors. From model building to CI/CD pipeline to deployment it contains all the elements needed for a complete MLOps Project. Please refer [Project Guidelines](README.md) and [Project Report]() for further details.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


## Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/License-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Authors

[@Niyati25](https://www.github.com/Niyati25)

[@giselle06](https://www.github.com/giselle06)

[@cassiuscolaco](https://github.com/cassiuscolaco)

[@](https://www.github.com/)


## Feedback

If you have any feedback, please reach out to us at unigoa.ac.in


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Lessons Learned

What did you learn while building this project? What challenges did you face and how did you overcome them?


### Hi, we are group of young data science students trying to do our MLOps Semester End Mini Project

# Project Guidelines
**_Assignment 1_**
**Title: Building a Machine Learning Pipeline with PyCaret**
* Objective: 
     - The objective of this lab is to build a machine learning pipeline for a dataset using PyCaret, including data preprocessing, model selection, and evaluation.
* Requirements:
     - Python installed on your system
     - Basic knowledge of Python and machine learning concepts
* Tasks:
     - Install PyCaret:
          Install PyCaret using pip: pip install pycaret.
     - Load the Dataset:
          Download a dataset (e.g., from Kaggle or UCI Machine Learning Repository) or use a sample dataset provided with PyCaret.
          Load the dataset into a Pandas DataFrame.
     - Initialize PyCaret:
          Import PyCaret: import pycaret.
          Initialize PyCaret with the dataset: exp = pycaret.classification.setup(data, target='target_column_name').
     - Compare Models:
          Use pycaret.classification.compare_models() to compare multiple models and select the best performing ones based on a chosen metric (e.g., accuracy, precision, recall).
     - Create a Model:
          Choose a model from the list of best performing models.
          Create the model using pycaret.classification.create_model().
     - Tune the Model:
          Fine-tune the model hyperparameters using pycaret.classification.tune_model().
     - Evaluate the Model:
          Evaluate the model on the test dataset using pycaret.classification.plot_model() and pycaret.classification.evaluate_model().
     - Finalize the Model:
          Finalize the model using pycaret.classification.finalize_model().
     - Save and Deploy the Model (Optional):
          Save the trained model using pycaret.classification.save_model() for future use.
          Deploy the model using a deployment platform (e.g., Flask, Heroku) if desired.
     - **Submission:**
          Submit the Python code and any relevant output (e.g., evaluation metrics, plots) for review.
          Note: This lab can be done for regression or clustering tasks by using pycaret.regression or pycaret.clustering             instead of pycaret.classification. [Here](MLOps_Proj/notebooks/mlops_see.ipynb)
       
**_Assignment 2_**
**Title: Continuous Integration with GitHub Actions**
* Objective: 
     - The objective of this lab is to set up a basic continuous integration (CI) workflow using GitHub Actions for a simple Python project.
* Requirements:
     - A GitHub account
     - Basic knowledge of Git and GitHub
     - A simple Python project (e.g., a script, a small web application, or a library)
* Tasks:
     - Setting up the Repository:
          Create a new public repository on GitHub.
          Clone the repository to your local machine.
          Create a basic Python project in the repository (e.g., a simple Python script).
     - Creating a Workflow:
          Inside the repository, create a new directory named .github/workflows.
          Inside this directory, create a YAML file (e.g., ci.yml) for your CI workflow.
     - Defining the Workflow:
          Define a basic workflow that:
          Triggers on pushes to the main branch.
          Checks out the code.
          Sets up Python (use a matrix to test against multiple Python versions if possible).
          Installs dependencies (e.g., using pip).
          Runs your Python script or tests (e.g., using pytest).
     - Committing and Pushing Changes:
          Commit your workflow file (ci.yml) to the main branch.
          Push your changes to GitHub.
     - Testing the Workflow:
          Go to the &quot;Actions&quot; tab in your GitHub repository to see the workflow running.
          Verify that the workflow runs successfully.
     - *Optional Enhancements:*
     Add additional steps to your workflow, such as linting the code, checking for code formatting, or
     deploying the application (if applicable).
     - **Submission:**
     Share the link to your GitHub repository for evaluation. [Here](.github/workflows)


## Run Locally

Clone the project

```bash
  git clone https://github.com/giselle06/MlOps_Proj
```

Go to the project directory

```bash
  cd Mlops_Project
```

Install dependencies

```bash
  pip install pycaret[full]
  pip install 

```



