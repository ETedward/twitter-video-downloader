# Twitter Videos Downloader

Twitter-videos-downloader deals with high quantities of video downloads at the same time, using the youtube-dl library.

## Purpose

The purpose of twitter-videos-downloader is to aid the BBC Africa Eye investigations team in collecting open source materials. For years, the open source 
team has worked with high quantities first person video sources from Twitter. For example
in "Three Killings in Kampala" over 400 videos were downloaded for the investigation. The previous methodology
was to download each video one by one from Twitter. Instead, this program allows investigators to 
download hundreds of twitter videos from their URLs at once, saving valuable time for our open source team.

## Installation

First use the package manager [pip](https://pip.pypa.io/en/stable/) to install youtube-dl such that it is available to be called in the command line.
Then install the following two requirements for the python program: 
1) pandas // a data analytics library
2) os // operating system, should be installed already in most systems.
Both of these packages can be installed with pip

## Usage

This program usage is simple and meant for all investigators, including non-technical investigators to use!


After installation, first download all the files in this github repository.
Then run open the input.csv spreadsheet and copy all the URLs of the videos for downloading 
into the input column, the first (and only) column.
Then run the program by typing python command.py in your terminal, or alternatively python3 command.py depending
on your python version. 

## Additional Features
As requested, the output names of the downloaded videos file now correspond
to the row of the video URL in the input.csv file.
Instead of a random string, the output video file name now follows the form of 
"E" + the incrementing row number + "_" + the date the video was uploaded to twitter.

Contributions are always welcome. 
For additional features and any questions on usage, you can contact 
Edward on Twitter @edward_the6 or Github @ETedward

