# HouseLayout3D 🏡


## Installation

```
conda create --name houselayout3d python=3.10 -y
conda activate houselayout3d

git clone git@github.com:HouseLayout3D/houselayout3d.git
cd houselayout3d
pip install -r requirements.txt

# On Mac
brew install git-lfs
# On Linux
sudo apt-get install git-lfs

git lfs
git clone https://huggingface.co/datasets/houselayout3d/HouseLayout3D data
```

Next, you van visualize the HouseLayout3D dataset as follows:

```
python visualize.py
python -m http.server 6008
```

Then open your browser and navigate to `http://localhost:6008`