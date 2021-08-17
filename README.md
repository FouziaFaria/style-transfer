# Style Transfer using ML

<p align="center">
    <img src="neural_style/images/style-images/mosaic.jpg" height="200px">
    <img src="neural_style/images/content-images/elon.jpg" height="200px">
    <img src="neural_style/images/output-images/mosaic-elon.jpg" height="200px">
</p>

# Dependencies

[<img align="left" width="30px" src="https://streamlit.io/images/brand/streamlit-mark-color.png" />][Streamlit]

[<img align="left" width="30px" src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg" />][pytorch]

<br />

# Languages and Tools

[<img align="left" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" />][python]
[<img align="left" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" />][jupyter notebook]
[<img align="left" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png" />][Visual Studio Code]
[<img align="left" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png" />][git]
[<img align="left" width="26px" src="https://raw.githubusercontent.com/github/explore/78df643247d429f6cc873026c0622819ad797942/topics/github/github.png" />][github]
[<img align="left" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" />][terminal]

<br />

# References
Based on this fast neural style code:
[Fast Neural Style](https://github.com/pytorch/examples/tree/master/fast_neural_style)

# Installation
It is recommended to use a virtual environment before installing the dependencies

### Create conda environment
Therefore, we will create a conda environment called *performance*
```
conda create -n performance python=3.7.9
```
Then, we will login to the *performance* environement
```
conda activate performance
```

### Install prerequisite libraries

Download requirements.txt file

```
wget https://raw.githubusercontent.com/FouziaFaria/style-transfer/main/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```

# Usage
Download the pretrained models

<div align='center'>
  <img src='images/content-images/amber.jpg' height="174px">
</div>

<div align='center'>
  <img src='neural_style/images/style-images/candy.jpg' height="174px">
  <img src='neural_style/images/style-images/mosaic.jpg' height="174px">
  <img src='neural_style/images/style-images/rain-princess.jpg' height="174px">
  <img src='neural_style/images/style-images/rain-princess-cropped.jpg' height="174px">
  <br>
  <img src='images/style-images/rain-princess-cropped.jpg' height="174px">
  <img src='images/output-images/amber-rain-princess.jpg' height="174px">
  <img src='images/output-images/amber-udnie.jpg' height="174px">
  <img src='images/style-images/udnie.jpg' height="174px">
</div>

```console
python download_saved_models.py
```

Move the *saved_models* folder into the *neural_style* folder.

Run
```console
streamlit run app.py
```

[Streamlit]: https://streamlit.io/
[pytorch]: https://pytorch.org/
[python]: https://www.python.org/
[jupyter notebook]: https://jupyter.org/
[Visual Studio Code]: https://code.visualstudio.com/
[git]: https://git-scm.com/
[github]: https://github.com/
[terminal]: https://sourceforge.net/projects/windows-terminal.mirror/
