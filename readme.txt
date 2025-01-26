IF YOU ONLY WANT TO READ MY NOTES, just download the .tex files from inside course folders or try downloading master.pdf in any course. Be careful! master.pdf may or may not be up to date depending on my last compilation before the last commit.

1) Install TexLive with default paths.

2) NOTE: STEP (2) CAN BE DONE CONCURRENTLY WITH (1)! Install Zathura (PDF Viewer), Vim (text editor), VimPlug (Vim plugin manager), VimTex (Vim plug in), and Ultisnips (Vim plug in). Make sure that your ~/.vimrc file contains at least the contents of ~/Documents/math-notes/gilles-system/minimal-vimrc. If you have no .vimrc folder in ~, we recommend copy and pasting ~/Documents/math-notes/gilles-system/minimal-vimrc to ~ and making sure to rename it ".vimrc". 

2) Clone Repo into ~/Documents. See (https://castel.dev/post/lecture-notes-3/) for an explaination of the file structure. Basically, every semester needs a preamble.tex file, every course needs a info.yaml file to automatically compile and populate the dir with the master document components, and you must have a system link to the working course dir in ~.

3) If making new semester, set ROOT to the path to the new semester directory in ~/Documents/math-notes/gilles-system/scripts-gilles/config.py

4) If making a new course, create a new dir in the semester folder, populate that folder with an info.yaml document, then run ~/Documents/math-notes/gilles-system/scripts-gilles/init-all-courses.py which will populate the dir with the necessary files to compile the master document and use the keyboard shortcuts that we are about to set up.

4) Check to make sure ~/current_course exists and works. If not run (ln -s ~/Documents/math-notes/bachelors/****CURRENT-SEMESTER-DIR****/****CURRENT-COURSE-DIR**** ~/current_course) 

5) Test the programs in ~/Documents/math-notes/gilles-system/scripts-gilles in terminal

6) If programs working, set up short cuts to run the rofi-lectures (alt+l), rofi-courses (alt + k), and rofi-lectures-view (alt + j)

7) Read through all shortcuts in the semester dir preamble.tex file or in ~/Documents/math-notes/gilles-system/gilles-snips/latex-snippets/tex.snippets


