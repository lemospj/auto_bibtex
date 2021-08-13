# BibTex project Python scripts

## What are these scripts for?

BibTeX is arguably the most popular reference management software among mathematicians. When using LaTeX as a text editor, BibTeX allows one to store references in a `.bib` file and to automatically generate a reference section at the end of the text. However, if you have ever used BibTeX, you know that you must go through a slightly annoying process: you must find the relevant BibTeX entry online, copy it to your `.bib` file, and then change the label to an easily usable one. The scripts in the folder are a program that automates this process. It uses the Python web scraping package `BeautifulSoup` to search for a given publication on the MathSciNet website (you need to have access to MathSciNet in the first place in order to use this program); it will then copy the BibTeX entry to a `.bib` file indicated by the user, or create that `.bib` file and copy the entry.

It is not unlikely that someone has already come up with a better program having the same functionalities of this one, but, at the moment, I am not aware of this. In any case, I decided that the automation of this task would be an interesting small project to take on.

Comments and suggestions are welcome!

## How can I use the scripts?

Two things are required in order to successfully run these scripts:

1. You will need access to the MathSciNet database;
2. You will need Python installed on your computer.

If both of the above are true, then download the folder named `bib_scripts` to a location of your choice. Inside the folder, you will find a Python file called `auto_bib.py`. Run this script using the terminal, i.e. type `python <path_to_auto_bib.py>` in the terminal. The program will then start. Here's a breakdown of what will happen:

1. The program will let you know your current working directory. It will also ask you whether this is the location of your `.bib` (or of your future `.bib`file). You can reply with `y` (yes) or `n` (no) (upper case is fine). Any other reply will cause the process to terminate. If you replied `y`, then go to 2. If you replied `n`, you will be asked to indicate a valid folder for the `.bib` file. You can use relative paths. So, if the folder `bib_scripts` is in the folder where your `.bib` file lives, the path `..` will change the working directory to the one with the `.bib` file.
2. The program will look for `.bib` files in the location indicated in the previous step. If it finds no `.bib` files or finds more than one, it will prompt you to choose a name for the `.bib` file you want to use or create. If it finds exactly one `.bib` file, it will ask you whether you want to use this as the `.bib` file. If not, you will have to idicate a name for the `.bib` file.
3. The program will then access MathSciNet and require you to indicate the name of an author and the title of a publication. 
4. After the information above has been submitted, the program will either find no publications matching your search terms, or it will find exactly one, or will find more than one. 
   1. If it finds exactly one, it will ask you for the BibTeX entry label you want to use, and then write down the entry in the `.bib` file provided (it will create a `.bib` file if there is no such file with the indicated name).
   2. If it finds more than one, it print a list of several results, and ask for a choice. After the choice has been made, it will ask for the label and write down the BibTeX entry on the `.bib` file indicated.
5. Finally, the program will ask you whether you would like to start another search. If so, it will go back to step 3 (the `.bib` file to be used will be the one provided when the program ran for the first time).
