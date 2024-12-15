import numpy as np
import cv2
import random
from rubikencryptor.rubikencryptor import RubikCubeCrypto
from PIL import Image


# Первый алгоритм: блочное скремблирование

def split_blocks(image, block_size):
    blocks = []
    height, width, channels = image.shape
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = image[i:i + block_size, j:j + block_size]
            blocks.append(block)
    return blocks


def scramble_blocks(blocks, key):
    random.seed(key)
    random.shuffle(blocks)
    return blocks


def reconstruct_image(blocks, image_shape, block_size):
    height, width, channels = image_shape
    image = np.zeros(image_shape, dtype=np.uint8)
    block_idx = 0
    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            image[i:i + block_size, j:j + block_size] = blocks[block_idx]
            block_idx += 1
    return image


def save_key(key, filename):
    with open(filename, 'w') as key_file:
        key_file.write(str(key))


def load_key(filename):
    with open(filename, 'r') as key_file:
        return int(key_file.read().strip())


def descramble_blocks(blocks, key):
    random.seed(key)
    block_idx = list(range(len(blocks)))
    random.shuffle(block_idx)

    ordered_blocks = [None] * len(blocks)
    for i, idx in enumerate(block_idx):
        ordered_blocks[idx] = blocks[i]

    return ordered_blocks


# Второй алгоритм: Скремблирование с помощью алгоритма кубика рубика

def rubik_encrypt(image_path, output_path, key_file):
    input_image = Image.open(image_path)
    encryptor = RubikCubeCrypto(input_image)
    encrypted_image = encryptor.encrypt(alpha=4, iter_max=5, key_filename=key_file)
    encrypted_image.save(output_path)


def rubik_decrypt(image_path, output_path, key_file):
    encrypted_image = Image.open(image_path)
    decryptor = RubikCubeCrypto(encrypted_image)
    decrypted_image = decryptor.decrypt(key_filename=key_file)
    decrypted_image.save(output_path)


def main():
    block_size = 150  # Размер блока

    image = cv2.imread('4.png')
    if image is None:
        print("Ошибка при загрузке изображения")
        return

    # Блочное скремблирование
    blocks = split_blocks(image, block_size)
    key1 = random.randint(0, 2 ** 32 - 1)
    save_key(key1, 'key1.txt')
    scrambled_blocks = scramble_blocks(blocks, key1)
    scrambled_image = reconstruct_image(scrambled_blocks, image.shape, block_size)
    cv2.imwrite('block_scrambled_image.png', scrambled_image)

    # Скремблирование c помощью рубика
    rubik_encrypt('block_scrambled_image.png', 'rubik_scrambled_image.png', 'key2.txt')

    # Дескремблирование c помощью рубика
    rubik_decrypt('rubik_scrambled_image.png', 'rubik_descrambled_image.png', 'key2.txt')

    # Дескремблирование блоков
    descrambled_image_rubik = cv2.imread('rubik_descrambled_image.png')
    descrambled_blocks = descramble_blocks(split_blocks(descrambled_image_rubik, block_size), key1)
    final_image = reconstruct_image(descrambled_blocks, image.shape, block_size)
    cv2.imwrite('final_image.png', final_image)

    print("Процесс завершён. Финальное изображение сохранено как 'final_image.png'.")


if __name__ == '__main__':
    main()
