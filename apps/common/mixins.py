from PIL import Image, ImageDraw, ImageFont

def overlay_grid_and_logo(input_image_path, output_image_path, grid_size=1, logo_path='img.png'):
    # Загрузка изображения
    original_image = Image.open(input_image_path)

    # Создание объекта ImageDraw для рисования на изображении
    draw = ImageDraw.Draw(original_image)

    # Наложение сетки
    width, height = original_image.size
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill="red", width=1, joint="curve")
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill="red", width=1, joint="curve")

    # Наложение логотипа
    logo = Image.open(logo_path)
    print(logo.size)
    logo_width, logo_height = 100, 100
    original_image.paste(logo, (width - logo_width, height - logo_height))

    # Сохранение результата
    original_image.save(output_image_path)

# if __name__ == "__main__":
#     input_image_path = "img_2.png"
#     output_image_path = "result.png"
#     logo_path = "img.png"
#
#     overlay_grid_and_logo(input_image_path, output_image_path, grid_size=10, logo_path=logo_path)