from PIL import Image

with Image.open("./png_files/test.png") as im:

    # Provide the target width and height of the image
    width=11460#11480
    height=12260#12280
    im_resized = im.resize((width, height),resample=Image.Resampling.NEAREST)#use nearest to avoid resize creating interpolated values
    im_resized.save('./png_files/test_resized.png')