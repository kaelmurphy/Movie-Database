from movie import Movie


class MovieDatabase:

    def __init__(self):
        self.__movieList = []
        self.__testList = []

    def addMovie(self, title, year):
        """this method takes the title and the year of the current movie and determines whether or not it is
        already in the database or not, if it is not in the database it is added to the database, if it is already
        in the database then nothing will happen"""

        # create a new movie with the title and year so we can determine whether it is in the database already
        newMovie = '{} {}'.format(title, year)

        # if the new movie is not in the database already then it is added to self.__movieList and self.__testList
        if newMovie not in self.__testList:

            # this line creates the new movie as an object by calling the Movie class
            newMovie = Movie(title, year)

            self.__testList.append('{} {}'.format(title, year))

            # this line adds the movie object to the database
            self.__movieList.append(newMovie)

        else:

            pass

        # returns the database so we can access it from the main file
        return self.__movieList

    def findMovie(self, title, year):
        """this function takes the title and the year of the current movie and checks the database to see whether it
        already exists or not, if it exists then the movie object is returned for a review to be added to it, if the
        movie doesn't exist in the database then the line from the file is ignored"""

        # set findmovie equal to the title and year of the movie
        findMovie = '{} {}'.format(title, year)

        # see whether findMovie is in the database, using a for loop allows us to find the index of the movie in the
        # test database and return the movie object with the same index from the movie object database
        for i in range(len(self.__testList)):

            if findMovie == self.__testList[i]:

                returnMovie = self.__movieList[i]

                # returns the corresponding movie object if the movie is in the database
                return returnMovie

            else:

                pass

        # returns false if the movie is not in the database, this way we can skip this line of the input file
        if findMovie not in self.__testList:

            return False

    def showAll(self):
        """when the showall function is called, all the movies in the database are given a short review by calling
        the shortReview method from the movie class, the movies are then sorted by title and year and returned in
        a list to the main file"""

        # create a list with all the movies and their average reviews to be returned to the main file
        showAllList = []

        # this for loop goes through all the objects in the database and for each object calls the shortreview method
        for i in range(len(self.__movieList)):

            # adds the short review of each movie in the database to a list that is returned
            showAllList.append(self.__movieList[i].shortReview())

        # sorts all the short reviews alphabetically and by year of release
        showAllList.sort()

        # this will print off all the items in the showall list
        for j in range(len(showAllList)):

            print(showAllList[j])
