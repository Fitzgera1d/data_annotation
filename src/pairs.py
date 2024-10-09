from collections import defaultdict
from pathlib import Path
from PIL import Image
import subprocess

def get_pairs(pair_file):
    with open(pair_file, "r") as f:
        content = f.read()

    lines = content.strip().split('\n')
    _pairs = [line.split(' ') for line in lines]
    pairs = defaultdict(set)
    for key, value in _pairs:
        pairs[key].add(value)
    return pairs

# labelme xx.jpg --labels xx,xx,xx -output xxx.json --nodata
def run_labelme(img_file, output_path, match_num, skip_exist=True):

    if Path(output_path).exists() and skip_exist:
        return
    labels = ','.join([f'{num:02d}' for num in range(match_num)])

    subprocess.run([
            'labelme', img_file, 
            '--labels', labels,
            '--output', output_path,
            '--nodata',
        ], stdout=subprocess.PIPE, text=True)
    
def merge_pair(img1_path, img2_path, output_path):
    img1_path = Path(img1_path).resolve()
    img2_path = Path(img2_path).resolve()

    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    width1, height1 = img1.size
    width2, height2 = img2.size

    total_width = width1 + width2
    max_height = max(height1, height2)

    new_img = Image.new('RGB', (total_width, max_height), (255, 255, 255))

    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (width1, 0))

    Path(output_path).mkdir(parents=True, exist_ok=True)
    new_img_path = output_path / f'{img1_path.stem}+{img2_path.stem}+{width1}.jpg'
    new_img.save(new_img_path)
    return new_img_path