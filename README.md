# BibTex project Python scripts

## What are these scripts?

I have been working on a mini project whose aim is to create a Python program which, given an author and a title of a publication, will look in MathSciNet for articles corresponding to these parameters. Once the required publication has been found, the program will either create a `.bib` file with the BibTeX entry associated to this publication in a location indicated by the user, or will add the BibTeX entry to an existing `.bib` file provided by the user. These scripts contain the code I have written.

## What can the program do at the moment?

As far as I am aware, the program is working at the moment, **provided that you have access to the MathSciNet database**. If you run the function `auto_bib()` in the file `auto_bib.py`, you will be prompted to insert a location for your `.bib` file, an author, a title and the BibTeX label you wish to use. If the program happens to find a single publication matching your search parameters, it will assume that is the one you were looking for and add the entry to the `.bib` file. Otherwise, it will either inform you that no publications have been found, or ask you to choose among an indexed list of publications. After a BibTeX entry has been added to the `.bib` file, you will have the opportunity to add more. At some point in the future I may add some extra functionalities to the program.

It is quite possible that a program like this one already exists. Nevertheless, I decided to undertake this small project mostly because I thought it had the potential to be a fun exercise.

If you find a bug, please let me know! Suggestions and comments regarding the code are very welcome!

## Further work

A few things are still left to be done. Most importantly, this program does not check whether the entry we are trying to add to the `.bib` file already exists. It would however be desirable to add this functionality. 
