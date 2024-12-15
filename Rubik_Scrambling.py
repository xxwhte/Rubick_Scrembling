from rubikencryptor.rubikencryptor import RubikCubeCrypto
from PIL import Image


input_image = Image.open('4.png')
encryptor = RubikCubeCrypto(input_image)
encrypted_image1 = encryptor.encrypt(alpha=3, iter_max=4, key_filename='key1.txt')
encrypted_image1.save('encrypted_image1.png')

input_image_1 = Image.open('encrypted_image1.png')
encryptor = RubikCubeCrypto(input_image_1)
encrypted_image2 = encryptor.encrypt(alpha=7, iter_max=10, key_filename='key2.txt')
encrypted_image2.save('encrypted_image2.png')


decryptor = RubikCubeCrypto(encrypted_image2)
decrypted_image2 = decryptor.decrypt(key_filename='key2.txt')
decrypted_image2.save('decrypted_image2.png')
decryptor = RubikCubeCrypto(decrypted_image2)
decrypted_image1 = decryptor.decrypt(key_filename='key1.txt')
decrypted_image1.save('decrypted_image1.png')
