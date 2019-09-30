## Setup

 - run in python 3.7 or your virtual environment

cd InfiniteScrollPhoto
pip install -r requirement.txt
(chose y)
python app.py

## Run

## Requirement Analysis

We will like you to develop a single image gallery website using vue and flask, 
It require to load images from database. 
[Pinterest](www.pinterest.com.au)

0. Load image from database, use flask and vue

1. Infinite scroll
    Need to support auto load next batch of images when it reach the end

2. Slider that resize image
    Waterfall display need to support resize all images using slider

3. Re-order when image overlap after slider resizing:
    Automatically adjust number of rows when image size is too large/small
    
4. Responsive by window:
    Adjust number of rows when browser window get smaller