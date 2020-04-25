from pokedex import *


if __name__ == '__main__':
    svm = import_model('svm.pkl')
    error = 0
    for f in os.listdir(PATH):
        img = load_img(f)
        pkmn_img = img.ravel().reshape(1, -1)
        pkmn_id = svm.predict(pkmn_img)
        if pkmn_id[0] == int(f[:-4]):
            pass
        else:
            print(POKEDEX[int(f[:-4])])
            error += 1
    print(error)

