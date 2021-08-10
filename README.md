# Streamlit Style Transfer App

## References
Based on this fast neural style code:
[Fast Neural Style](https://github.com/pytorch/examples/tree/master/fast_neural_style)

[Streamlit website](https://www.streamlit.io/)

## Installation
It is recommended to use a virtual environment before installing the dependencies
```console
pip install streamlit
pip install torch torchvision
```

## Usage
Download the pretrained models
```console
python download_saved_models.py
```

Move the *saved_models* folder into the *neural_style* folder.

Run
```console
streamlit run main.py
```
