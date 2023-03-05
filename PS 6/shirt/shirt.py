import sys
from PIL import Image
from PIL import ImageOps


def main():
    input_pic, output_pic = get_pic()
    wear_shirt(input_pic, output_pic)


def get_pic():
    if len(sys.argv) < 3:
        sys.exit("Too Few Command-Line Arguments!")
    elif len(sys.argv) > 3:
        sys.exit("Too Many Command-Line Arguments!")

    if sys.argv[1][-3:] != sys.argv[2][-3:]:
        sys.exit("Input and Output Have Different Extensions!")

    if sys.argv[1][-4:] not in [".jpg", ".png"] and sys.argv[1][-5:] != ".jpeg":
        sys.exit("Invalid Input!")

    if sys.argv[2][-4:] not in [".jpg", ".png"] and sys.argv[2][-5:] != ".jpeg":
        sys.exit("Invalid Input!")

    return sys.argv[1], sys.argv[2]



def wear_shirt(input_pic, output_pic):
    try:

        # Open the Images
        shirt = Image.open("shirt.png")
        input_image = Image.open(input_pic)

        # Size of the Shirt Image
        size = shirt.size

        # Re-Size and Crop the Input Image According to the Size of the Shirt
        resized_input_image = ImageOps.fit(input_image, size = size)

        # Paste the Shirt to the Re-Sized Input Image
        resized_input_image.paste(shirt, mask = shirt)

        # Save
        resized_input_image.save(output_pic)

    except FileNotFoundError:
        sys.exit("The File Does Not Exist!")

if __name__ == "__main__":
    main()