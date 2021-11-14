import subprocess
import os

def call_jp2a(image_dir, output_dir, width=30):
    
    for image in os.listdir(image_dir):
        code, ext = os.path.splitext(image)
        with open( os.path.join(output_dir, f'{code}.txt'), "w") as outfile:
            subprocess.Popen(['jp2a', f'--width={width}', '--chars= #', os.path.join(image_dir,image)], stdout=outfile)      # hack around with chars

def image_to_banner(image_file):
        result = subprocess.Popen(['jp2a', '--chars= #', image_file], stdout=subprocess.PIPE)
        return result.stdout.decode()


if __name__ == "__main__":

    image_dir = "fonts"
    output_dir = "banner_text"
    
    os.makedirs(output_dir, exist_ok=True)
    call_jp2a(image_dir, output_dir)
