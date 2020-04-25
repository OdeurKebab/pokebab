from pokedex import *


if __name__ == '__main__':
    #images, pokemons = load_data()
    svm = import_model('svm.pkl')

    for f in sorted(os.listdir(PATH)):
        pkmn_img = load_img(f).ravel().reshape(1, -1)
        pkmn_id = svm.predict(pkmn_img)
        print(POKEDEX[pkmn_id[0]] == POKEDEX[int(f[:-4])])

