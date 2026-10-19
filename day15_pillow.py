from PIL import Image   
img=Image.open("resized_image.jpg")
# img.show()
# print("Width:", img.width)
# print("Height:", img.height)
# print("Format:", img.format)
# print("Size:", img.size)
resized_image=img.resize((300,220))
resized_image.save("resized_image.jpg")

rotated_img = img.rotate(90)
rotated_img.save("rotated_photo90.jpg")

rotated_img.show()