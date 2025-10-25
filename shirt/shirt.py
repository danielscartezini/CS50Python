from PIL import Image, ImageOps
from sys import exit, argv

def main():
    check_cli_argvs()

    # open the image
    try:
        image = Image.open(argv[1])
    except FileNotFoundError:
        exit("Input does not exist")
    # open the shirt
    shirt = Image.open("shirt.png")
    # get the size of the shirt
    size = shirt.size
    # resize muppet image to fit the shirt
    muppet = ImageOps.fit(image, size)
    #past the shirt in image
    muppet.paste(shirt, shirt)
    #create output image
    muppet.save(argv[2])

def check_cli_argvs():
    if len(argv) != 3:
        exit(f'Expected three command line arguments, not {len(argv)}')

    # .jpg, .jpeg, or .png
    valid_extensions = (".jpg", ".jpeg", ".png")

    is_argv_1_valid = argv[1].lower().endswith(valid_extensions)
    is_argv_2_valid = argv[2].lower().endswith(valid_extensions)

    if not is_argv_1_valid or not is_argv_2_valid:
        exit(f'Expected .jpg, .jpeg, or .png not "{argv[1]}, {argv[2]}"')

    elif argv[1].split(".")[1]!= argv[2].split(".")[1]:
        exit("The extensions must be the same.")

if __name__ == "__main__":
    main()
