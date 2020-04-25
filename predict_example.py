from pokedex import *


if __name__ == '__main__':
    svm = import_model('svm.pkl')
    #error = 0
    #for f in os.listdir(PATH):
    f = 'PokecordSpawn.jpg'
    img = load_img(f).reshape(SIZE, SIZE)
    plt.imshow(img)
    plt.show()
    pkmn_img = img.ravel().reshape(1, -1)
    pkmn_id = svm.predict(pkmn_img)

    # if pkmn_id[0] == int(f[:-4]):
    #     pass
    # else:
    print(POKEDEX[pkmn_id[0]])
    #     error += 1
    # print(error)

