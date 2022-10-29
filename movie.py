class Movie:
    def __init__(self, title, year):
        self.__avgRev = None
        self.__title = title
        self.__year = year
        self.__review = []

    def addReview(self, review):
        """this function takes the review value from the current line being read and adds it to the review list for
        the corresponding movie object"""

        # if the value of the review is valid it is added to the review list for the movie object
        if 1 <= int(review) <= 5:

            self.__review.append(review)

    def shortReview(self):
        """this function is responsible for giving each movie object their average review value, it also properly
        formats the output string that is to be printed"""

        # this calls the private method that will calculate the average review value for the movie
        self.__calcAvg()

        # once the average review has been calculated the following line is created and returned to the movie database
        movie = '{} ({}): {:.1f}/5'.format(self.__title, self.__year, self.__avgRev)

        return movie

    def longReview(self):
        """the long review method is responsible for outputting the long review of the corresponding movie,
        using a for loop I can determine how many of each review values there are in the review list and properly
        format the required output"""

        # create variables representing the numner of times the value of the review has been seen in the review list
        num5 = 0

        num4 = 0

        num3 = 0

        num2 = 0

        num1 = 0

        # calls the calcAvg method
        self.__calcAvg()

        # creates a for loop that will go through the review list and determine how many times each value has been seen
        for i in range(len(self.__review)):

            if int(self.__review[i]) == 5:

                num5 += 1

            elif int(self.__review[i]) == 4:

                num4 += 1

            elif int(self.__review[i]) == 3:

                num3 += 1

            elif int(self.__review[i]) == 2:

                num2 += 1

            elif int(self.__review[i]) == 1:

                num1 += 1

        # creates a variable that is the output string that is to be returned to main file and be printed
        movie = '{} ({})\nAverage review: {}/5\n*****: {}\n**** : {}\n***  : {}\n**   : {}\n' \
                '*    : {}'.format(self.__title, self.__year, self.__avgRev, num5, num4, num3, num2, num1)

        return movie

    def __calcAvg(self):
        """this function is responsible for calculating the average movie review value for the corresponding movie
        object, it goes through the review list and takes each review value and divides it by the total number of items
        in the list, which gives it the average review value"""

        # create the counter and the total review variables that will be used to calculate the average
        counter = 0

        totalRev = 0

        # this extracts every review corresponding to the movie and adds them together, also keeps track of the number
        # of items
        for i in range(len(self.__review)):

            totalRev += int(self.__review[i])

            counter += 1

        # if there is one or more reviews for the movie then the average is calculated
        if counter != 0:

            self.__avgRev = totalRev / counter

        # if there are no reviews for the movie then the average is set to be 0
        else:
            self.__avgRev = 0.000
