# DATA_ANNOTATION

## Installation

``` sh
# python3
python -m venv venv
pip install git+https://github.com/labelmeai/labelme
pip install -r requirements.txt
```

## Annotation

You can start your annotation process by using the instruction:
``` sh
python main.py
```
- In the qt pop-up window, right click and choose `Create Line` first to annotate corresponding points in the adjacent images.
- After choosing a line, select a tag listed below. You are expected to label 10-20 pairs of corresponding points, and click `Save` after completing the labeling.
- If there are very few or even no corresponding points between the two images, feel free to click `Save` button (or `x` if you don't want anything to be saved) to exit this group of annotations at any time.