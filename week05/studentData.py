studentData = {
    "name":"Mary",
    "module":
        [{
        "courseName":"Programming",
        "grade":45
        },{
        "courseName":"History",
        "grade":99
        }]
}
print ("Student \t: {}".format(studentData["name"]))
for modules in studentData["module"]:
    print("{} \t: {}".format(modules["courseName"],modules["grade"]))
               
              