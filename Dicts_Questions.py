import pprint

dictionary1 = {}
dictionary1["Christoph"] = {"Name": "Knorr", "Age": 35, "Employer": "CQ"}
dictionary1["Gundolf"] = {"Name": "Stoll", "Age": 60, "Employer": "IBW"}
dictionary1["Bennet"] = {"Name": "Wiegert", "Age": 40, "Employer": "SCM"}
pprint.pprint(dictionary1)
dictionary1["Gundolf"].update({"Age": 61})
pprint.pprint(dictionary1)
dictionary1["Gundolf"].update({"Vacation": "Yes"})
pprint.pprint(dictionary1)
dictionary1["Gundolf"].pop("Vacation")
pprint.pprint(dictionary1)
