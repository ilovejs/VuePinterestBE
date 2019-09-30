## Setup

 - Run in Python 3.7 or your virtual environment
 - Flask 1.1.1 (latest) with Flask-cors installed
 
cd InfiniteScrollPhoto
pip install -r requirement.txt
python app.py

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
    
## Anti-pattern Explanation:

1. Why I don't use sqlite database to store image.
   
   It's not common in industry case, store image as binary file through database network will cause extra read work load.
   
   Better choice is to return with CDN prefix in url so that, CDN gateway can pick the closest server to load image.
   
   Each user would request 13 times for initial load, database can't easily scale for that (tps and network latency)
   
   Also, put ORM in flask for binary format is quite tedious and anti-pattern.
   