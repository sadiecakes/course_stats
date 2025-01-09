# Write your solution here
def retrieve_all(website):
    data = json.loads(website.read())
#    num_dicts = len([item for item in data if isinstance(item, dict)])
#    dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8, dict9, dict10, dict11, dict12, dict13 = data
    tuple_list = []

    for dictionary in data:
        if dictionary["enabled"] == True:
            sum = 0
            for num in dictionary["exercises"]:
                sum += num
            tuple_list += [dictionary["fullName"], dictionary["name"], dictionary["year"], sum]
    result_tuples = []
    for i in range(0, len(tuple_list), 4):
        result_tuples.append(tuple(tuple_list[i:i+4]))
    
    return result_tuples

if __name__ == "__main__":
    import urllib.request
    import json

    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    my_request = urllib.request.urlopen(url)
    result = retrieve_all(my_request)
    print(result)
