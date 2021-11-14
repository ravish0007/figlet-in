import pyvips
import os

def generate_char(code, directory, font='Arial', dpi=500, width=1080):
    image = pyvips.Image.text(chr(code),  font=font, dpi=dpi)
    image.write_to_file(os.path.join(directory, f'{hex(code)}.jpg'))

def generate_text(text, file_path, font='Arial', dpi=500, width=1080):
    image = pyvips.Image.text(text,  font=font, dpi=dpi)
    image.write_to_file(file_path)

if __name__ == '__main__':

    os.makedirs('fonts', exist_ok=True)
    generate_char(65)
