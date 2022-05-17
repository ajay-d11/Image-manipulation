from PIL import Image
import os
from PIL import Image, ImageFilter
from PIL import ImageEnhance

size_300 = (300, 300)

def manipulation():

    while True:
        user_choice = input("Which image would you like to modify? (image1, image2, image3, ... image10? ").lower()
        usershow = Image.open(user_choice + ".jpg")
        usershow.show()
        user_confirmation = input("Is this the correct image? yes or no? ").lower()
        if user_confirmation == "yes":
            break

    choice = input("How would you like to modify your image (resize, png, black/white, blur, or rotate? ").lower()

    if choice == "rotate":
        pic1 = Image.open(user_choice + ".jpg")
        pic2 = pic1.rotate(90).save('rotate/' + user_choice + '_rotate.jpg')
        pic2 = Image.open('rotate/' + user_choice + '_rotate.jpg')
        pic2.show()
        
    if choice == "resize":
    
        newsize = (200, 200)
        
        pic1 = Image.open(user_choice + ".jpg")
        pic2 = pic1.resize(newsize)
        pic2.show()
        pic2.save('resize/' + user_choice + '_rotate.jpg')

    if choice == "blur":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.show()
        pic2 = pic1.filter(ImageFilter.BLUR)
        pic2.show()
        pic2.save("blur/" + user_choice + "_rotate.jpg")

    if choice == "black/white":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.show()
        pic2 = pic1.convert('L') 
        pic2.show()
        pic2.save("black/white/" + user_choice + "_rotate.jpg")

    if choice == "png":
        pic1 = Image.open(user_choice + ".jpg")
        pic1.save("png/" + user_choice + "_png.png")
        pic1.show()

    else:
        print("Not a valid option")

        round2 = input("would you like to modify a new image? yes or no?")
        if round2 == "yes":
            manipulation()
        else: 
            print("Okay adios")


        

manipulation()