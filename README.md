**Description**
This repo contains an investigation into building a regression model to predict delivery duration. 

The original project can be found here: https://platform.stratascratch.com/data-projects/delivery-duration-prediction?utm_source=youtube&utm_medium=click&utm_campaign=YT+classical+ML+doordash+project.

Associated article can be found here: https://medium.com/@jimin.kang821/building-a-regression-model-delivery-duration-prediction-ab1435952419

**File Structure**
- datasets: contains data for model training & evaluation
- models: contains trained & serialized models
- notebooks: Jupyter notebooks containing investigation logic
    - eda.ipynb -> initial data cleaning/prep, feature engineering, & exploratory data analysis
    - modeling.ipynb -> building models with various regression algorithms & serialize best performing model
    - final_evaluation.ipynb -> evaluate final model on holdout test set
- utils: python files containing helper functions referenced in notebooks
    - feature_eng_utils.py -> functions for feature engineering
    - custom_transformers.py -> custom transformers used for preprocessing workflows

**Environment Setup**
This project was developed using Python 3.10. However, you should be able to run these notebooks with any version of Python 3. 

The required dependencies for this project are listed in requirements.txt. For more information on creating an environment from a requirements file, check out the following: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/