import os
def main():
    for count, filename in enumerate(os.listdir("images/")):
        destino = "robot" + str(count)+ ".jpg"
        fonte = "images/" + filename
        destino = "images_dest/" + destino

        os.rename(fonte, destino)

if __name__ == '__main__':
    main()

'''for count, filename in enumerate(os.listdir("images/")):
        destino = "robot" + str(count)+ ".jpg"
        fonte = "images/" + filename
        destino = "images_dest/" + destino

        os.rename(fonte, destino)'''
