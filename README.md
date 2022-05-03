# Have Songs Gotten More Upbeat Over the Last Decade? 

This is my final dashboard for MA705, where I use many of the skills and tools I learned over the semester to create something that is useful, and that I am proud of. 

## Purpose of Dashboard 

Being an avid music fan myself, I was curious to see how trends in music have changed over the last decade. With apps like Instagram and TikTok becoming more popular, my driving question was whether songs have gotten more upbeat over the last decade. 

Using a publicly available dataset, I performed some minor cleaning and data munging using pandas and numpy tools to make the data easier to work with. Then, using Dash and Plotly I built a graph and table that updates itself based on user inputs. 

For example, if you're curious to see solo artists that make high tempo, upbeat songs & their relative BPM, you can filter for that and see how it has changed (or not changed!) over time. 

## Data Preparation 

First, I dropped all the NA columns to omit missing data. Then, I noticed that in a database of 1,000 songs, there were over 100 unique genres. While this may be due to the artists' creativity deciding to create a new genre for a song that eventually became popular, leaving it in that state would have made Plotly visualizations extremely cluttered. 

In order to combat this, I decided to group the genres into 9 key groups that could eventually be plotted. I also used pandas methods to create 2 new columns based on the numeric value of Energy and Danceability of a song. In its raw form, these columns had a number attached, and using pandas, I grouped them into low, medium, and high respectively. 

Also, to make the updating table more aesthetically pleasing, I renamed some columns to give them more understandable names. For example, 'acous' became 'softness'.

After this main part of data preparation, I used our template from class to convert a dataframe into an html table, used html components to create Dropdown lists, and included callbacks and functions to ensure that the graph and tables update according to user input. 

### Data Description 

A link to the data is available on the upper left hand corner of the Dashboard and here: 
https://www.kaggle.com/datasets/muhmores/spotify-top-100-songs-of-20152019

I used no other sources to build this dashboard. 

### Further Comments 

Thanks a ton for everything you taught us this semester. Looking back at when I was struggling to write a for loop in January, it's cool to see what I was able to build by just putting in the hours and practicing, doing the problem sets, and visiting office hours. See you in Time Series, and go Celtics!

