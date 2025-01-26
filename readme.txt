1) Install TexLive with default paths.

2) Clone Repo into ~/Documents. See (https://castel.dev/post/lecture-notes-3/) for an explaination of the file structure. Basically, every semester needs a preamble.tex file, and every course needs a info.yaml file.

3) If making new semester, set ROOT to the path to the new semester directory in ~/Documents/math-notes/gilles-system/scripts-gilles/config.py

4) If making a new course, create a new dir in the semester folder, populate that folder with an info.yaml document, then run ~/Documents/math-notes/gilles-system/scripts-gilles/init-all-courses.py which will populate the necessary files to use the keyboard shortcuts that we are about to set up.

4) Check to make sure ~/Documents/math-notes/gilles-system/current_course works. If not run (ln -s ~/Documents/math-notes/bachelors/****CURRENT-SEMESTER-DIR****/****CURRENT-COURSE-DIR**** ~/Documents/math-notes/gilles-system/current_course) 

5) Test the programs in ~/Documents/math-notes/gilles-system/scripts-gilles in terminal

6) If programs working, set up short cuts to run the rofi-lectures (alt+l), rofi-courses (alt + k), and rofi-lectures-view (alt + j)


