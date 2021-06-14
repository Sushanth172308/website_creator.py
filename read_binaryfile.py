file = open('Tiger_image.jpg', 'rb')
data = file.read()
file.close()


file = open('new_image.jpg', 'wb')
file.write(data)
file.close()