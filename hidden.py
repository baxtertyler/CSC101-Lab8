# CPE 101-01
# LAB 8: File i/o
# Name: Tyler Baxter
# Section: 03

# runs all the functions for the code
# none -> none
def main():
    input_image = open("hidden.ppm", 'r')
    output_image = open('discover.ppm', 'w')
    header(input_image, output_image)
    decode_image(input_image, output_image)


# writes the header for the new image
# image, image -> none
def header(original, new):
    new.write(original.readline())
    new.write(original.readline())
    new.write(original.readline())


# decodes the image by multiplying the red pixel by 10 (or set to 255 if red * 10 > 255)
# image, image -> none
def decode_image(original, new):
    while 1 == 1:
        p_val = original.readline()
        if p_val == "":
            break
        original.readline()
        original.readline()
        new_p_val = int(p_val) * 10
        if new_p_val >= 225:
            new_p_val = 255
        new.write(str(new_p_val) + '\n')
        new.write(str(new_p_val) + '\n')
        new.write(str(new_p_val) + '\n')


if __name__ == '__main__':
    main()


