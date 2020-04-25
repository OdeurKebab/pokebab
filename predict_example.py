from pokedex import *


if __name__ == '__main__':
    #images, pokemons = load_data()
    svm = import_model('svm.pkl')

    pkmn_img = load_img('004.png').ravel().reshape(1, -1)

    print(pkmn_img.shape)
    pkmn_id = svm.predict(pkmn_img)
    print(POKEDEX[pkmn_id[0]])

