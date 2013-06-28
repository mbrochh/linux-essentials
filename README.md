# Linux Essentials

These are going to be the slides for a tutorial about Linux essentials that 
I am working on. Stay tuned.

An outline of the course can be found [here](https://docs.google.com/document/d/11VN5YN98WG53VHFAbzLuGNLyFw-iaNC78igHOJpjN5o)
and if you are intereseted in this course, please let me know [here](https://docs.google.com/forms/d/1R2BJN4yqS7QzPugk_Qu8Ve5z-x6EevoTPRlsw1RyH3s/viewform).


## Usage

In order to view these slides, just go to http://mbrochh.github.io/linux-essentials


## Installation

In order to work on the slides, do the following:

    git clone git@github.com:mbrochh/linux-essentials.git
    mkvirtualenv -p python2.7 linux-essentials
    workon linux-essentials
    pip install -r requirements.txt

Now you should have all necessary Python software installed. Make sure to 
install observr and run the file system watcher:

    ./source-watcher.sh

If you don't want to use the file system watcher, you can trigger a build via

    fab build

Now make your changes in the source directory. When you are done, review your
changes:

    open presentation/index.html
