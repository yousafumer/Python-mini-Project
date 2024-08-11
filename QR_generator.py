import qrcode
img = qrcode.make("https://www.youtube.com/watch?v=Mrplj7qJ2m4")

img.save("text.png")
