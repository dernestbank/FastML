# FastML-app

This is a web app that uses the several libraies suchas lazypredict library to predict multiple machine learning models on a users data preoptimization. The goal is to fasttrack the ML piipeline with tools and libraries. 


# Demo

Launch the web app:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dernestbank/FastML/app.py)



# Reproducing this web app
To recreate this web app on your own computer, do the following.



###  Download and unzip contents from GitHub repo

Download and unzip contents from https://github.com/dernestbank/FastML

### change directory to the app directory
```
cd FastML-app
```
### Create conda environment
create a conda environment
```
conda create -n fastml python=3.7.9
```
activate env
```
conda activate fastml
```

### Install libraries
```
pip install -r requirements.txt
```



###  Launch the app

```
streamlit run app.py
```

# Roadmap for FastML
- [x]  One pager Multi-algorithm analysis
- [x] Publish demo app
- [ ] Add data manupulation ( column selection, data cleaning, data transformation, etc.)
- [ ] Addd a feature engineering step to the pipeline.
- [ ] Add a feature selection step to the 
- [ ] Add a model selection, optimization and hyperparameter tuning to the pipteline pipeline.
- [ ] Add a LLM feature

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[Dernest Bank](https://github.com/dernestbank)

## Acknowledgements
- [lazypredict](https://github.com/shankarpandala/lazypredict)
- [dataprofessor](https://github.com/dataprofessor)
- [streamlit](https://github.com/streamlit/streamlit)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)  
