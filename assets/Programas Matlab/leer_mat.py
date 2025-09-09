import scipy.io
import h5py

filename = "assets/Programas Matlab/TFG workspace.mat"

try:
    data = scipy.io.loadmat(filename)
    print("Variables disponibles:", data.keys())
except NotImplementedError:
    print("El archivo es .mat v7.3, usando h5py...")
    with h5py.File(filename, "r") as f:
        print("Variables disponibles:", list(f.keys()))
