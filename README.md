
# Music Finder 🎵

A Python-based app to practice dataset manipulation and Python programming, made for keeping my sanity during finals week! This project was both a fun experiment and a way to sharpen my skills using large datasets and GUI's.



## What It Does

The music finder application allows users to explore new music through artists who made a top 5000 greatest hits of all time list and their genres. 

- Step 1: Login to use the application, or create a new account.
- Step 2: Choose genres from a drop-down menu or add your own.
- Step 3: The app analyzes a dataset of a top 5000 greatest hits of all time dataset to find artists that match your selected genres.
- Step 4: It generates a personalized playlist featuring those artists to explore new music!

Whether you're a music enthusiast or someone looking to create custom playlists,  this app can serve as a useful tool for you.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.

`OPENAI_API_KEY='your_key'`



## Installation

After cloning the repository to your local device you must install the required dependencies.

```bash
  pip install os python-dotenv csv pandas tkinter openai
```
    
Enter the directory of your repository and run
```bash
  python main.py
```