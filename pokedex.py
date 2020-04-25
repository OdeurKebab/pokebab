import os
import cv2
import numpy as np
from sklearn.svm import SVC
import pickle
import matplotlib.pyplot as plt

PATH = os.path.join(os.getcwd(), 'pokemondb')
MAX_SIZE = 485
SIZE = 64
POKEDEX = np.loadtxt(os.path.join(os.getcwd(), 'pokedex.csv'), delimiter=',', dtype=str)
POKEDEX = dict([(int(k), v) for k, v in POKEDEX])


def import_model(pkl_filename):
    pkl = open(pkl_filename, 'rb')
    model = pickle.load(pkl)
    pkl.close()
    return model


def file_to_img(f):
    img = cv2.imread(os.path.join(PATH, f), 0)
    img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT)
    _, mask = cv2.threshold(img, thresh=20, maxval=255, type=cv2.THRESH_BINARY)
    return mask


def make_img_squared(img):
    resized = np.ones((MAX_SIZE, MAX_SIZE), dtype='uint8')*255
    w, h = img.shape
    h_stride = (MAX_SIZE - w) // 2
    v_stride = (MAX_SIZE - h) // 2
    resized[h_stride:(w + h_stride), v_stride:(h + v_stride)] = img
    copy = np.zeros((SIZE, SIZE), dtype='uint8')
    copy = cv2.resize(src=resized.astype('uint8'), dst=None, dsize=copy.shape)
    return copy


def load_img(f):
    img = file_to_img(f)
    return make_img_squared(img).ravel()


def load_data():
    return dict(
        [(int(f[:-4]), load_img(f)) for f in os.listdir(PATH) if 'png' in f])


def data_augmentation(im):
    copies = []
    im.shape = (SIZE, SIZE)
    for scale in 0.5, 0.75, 1:
        copy = np.zeros((int(scale * MAX_SIZE), int(scale * MAX_SIZE)), dtype='uint8')
        copy = cv2.resize(src=im.astype('uint8'), dst=None, dsize=copy.shape)
        copies.append(make_img_squared(copy).ravel())
    return copies


if __name__ == '__main__':
    data = load_data()
    imgs, ids = [], []

    for id, im in data.items():
        for im_ in data_augmentation(im):
            imgs.append(im_)
            ids.append(id)

    del data

    model = SVC(verbose=True).fit(imgs, ids)

    svm_pkl_filename = 'svm.pkl'
    svm_pkl = open(svm_pkl_filename, 'wb')
    pickle.dump(model, svm_pkl)
    svm_pkl.close()

