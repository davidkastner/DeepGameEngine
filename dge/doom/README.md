Install Vizdoom
conda install -c conda-forge boost cmake sdl2
git clone https://github.com/mwydmuch/ViZDoom.git --recurse-submodules
cd ViZDoom
python setup.py build && python setup.py install