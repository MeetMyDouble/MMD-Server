HOW To : 

On ubuntu : Install all these dependencies :

build-essential cmake gfortran git wget curl graphicsmagick libgraphicsmagick1-dev libatlas-dev  libavcodec-dev libavformat-dev libgtk2.0-dev libjpeg-dev  liblapack-dev libswscale-dev pkg-config python3-dev python3-numpy software-properties-common zip

installing dlib : 

git clone https://github.com/davisking/dlib.git
cd dlib
mkdir build; cd build; cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1; cmake --build .
cd ..
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA (with super user rights)


installing face_recognition


pip3 install face_recognition (it'll take a while during "Running setup.py bdist_wheel for dlib")

