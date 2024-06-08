"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [0, 2, 6],
            "answer": 1,
        },
        {
            "input": [0, 4, 6],
            "answer": -1,
        },
        {
            "input": [0, 3, 6],
            "answer": 0,
        }
    ], 
    "Extra": [
        {
            "input": [1, 2, 4],
            "answer": 1,
        },
        {
            "input": [1000, 10000, 100000],
            "answer": 1,
        },
        {
            "input": [10, 12, 13],
            "answer": -1,
        }
    ]
}
