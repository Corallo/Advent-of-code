#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=1, year=2023,session=session_id)
#data= "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
data = data.split("\n")
#data = ["8four419eighteight1bpv"]
matches = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6,
           "seven":7, "eight":8, "nine":9, "1":1, "2":2,
              "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,"9":9 }

answer = 0
for line in data:
    first_idx = len(line)

    for key, value in matches.items():
        if key in line:
            idx =  line.index(key)
            if idx < first_idx:
                first_idx = idx
                first = value

    last_idx = 0
    for key, value in matches.items():
        if key in line:
            idx = line.rindex(key)
            if idx > last_idx:
                last_idx = idx
                last = value
    print(first, last)
    answer += first*10 + last



print(answer)
submit(answer, part="b", day=1, year=2023, session=session_id)
