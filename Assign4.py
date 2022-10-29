# Kael Murphy
# CS1026B Asssignment 4

from movie import Movie
from moviedb import MovieDatabase

COMMAND = 0
TITLE = 1
YEAR = 2
REVIEW = 3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'


def readFile(input):
    """This file takes in the user input as a parameter
        it is responsible for reading the lines from the input file, determining which command is being used,
        and for outputting the required things when the show or print commands are read in the file"""

    # I created a datalist, which calls the moviedatabase class and creates the empty database which will be
    # filled up throughout the duration of the program
    dataList = MovieDatabase()

    # this with open statement opens and reads the lines of the file, it goes one line at a time and the line is saved
    # as fh
    with open(input, 'r') as fh:

        for line in fh:

            data = line.strip().split('-')

            command = data[COMMAND]

            # this sets the values of title and year to their corresponding values read in the input file
            if command != SHOW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]

            # if the command read from the file is NEW, we will try to add a new movie to the database
            if command == NEW_COMMAND:

                # this calls the add movie method from the moviedb class, it will add a movie to the database
                dataList.addMovie(title, year)

            # if the command read from the file is REV, we will add the review to the corresponding movie object
            elif command == REVIEW_COMMAND:

                # sets review equal to the value of the review given in the file
                review = data[REVIEW]

                # this line will find the corresponding movie to the review in the movie database by calling findMovie()
                addReview = dataList.findMovie(title, year)

                # if the movie is in the database, a review will be added to the corresponding movie object
                if addReview is not False:

                    # calls the add review method from the movie class
                    addReview.addReview(review)

                else:

                    pass

            # if the command read from the file is SHO, we will show all of the movies in the database with their
            # corresponding average reviews
            elif command == SHOW_COMMAND:

                # this calls the show all method from the movie database
                dataList.showAll()

            # the final command that can be read from a line is PRI, we will show a long review for the corresponding
            # movie if it is in the databse, if it isn't then we will do nothing
            elif command == PRINT_COMMAND:

                # set longreview equal to the corresponding movie object using the find movie method described earlier
                longReview = dataList.findMovie(title, year)

                # if the movie is in the database then the long review is printed
                if longReview != False:

                    # prints the long review of a movie after it calls the long review method from the movie class
                    print(longReview.longReview())

                # if the movie isn't in the database then nothing is done
                else:

                    pass


def main():
    userInput = 'movie.txt'
    readFile(userInput)


main()
