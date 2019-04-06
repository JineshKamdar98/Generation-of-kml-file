import simplekml

k1=simplekml.Kml()

k1.newpoint(name="Sample",coords=[(10,10)])

k1.newpoint(name="Sample",coords=[(15,15)])


#here you have to set your own path to set the location for your kml file
k1.save("D:/udemy programs/points.kml")


