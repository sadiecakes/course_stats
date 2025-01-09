Retrieving the list of active courses

At the address https://studies.cs.helsinki.fi/stats-mock/api/courses you will find basic information about some of the courses offered by the University of Helsinki Department of Computer Science, in JSON format.

Please write a function named retrieve_all(), which retrieves the data of all the courses which are currently active (the field enabled has the value true). These should be returned as a list of tuples, in the following format:
Sample output

[
    ('Full Stack Open 2020', 'ofs2019', 2020, 201),
    ('DevOps with Docker 2019', 'docker2019', 2019, 36),
    ('DevOps with Docker 2020', 'docker2020', 2020, 36),
    ('Beta DevOps with Kubernetes', 'beta-dwk-20', 2020, 28)
]

Each tuple contains the following fields from the original data:

    the name of the course: fullName
    name
    year
    the sum of the values listed in exercises

NB: It is essential that you retrieve the data with the function urllib.request.urlopen, or the automated tests may not work correctly.

NB2: The tests are designed so that they slightly modify the data retrieved from the internet, to make sure you do not hard-code your return values.
