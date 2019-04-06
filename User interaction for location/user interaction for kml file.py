import simplekml

longitude=float(input("Enter longitude: "))
latitude=float(input("Enter longitude: "))

kml=simplekml.Kml()

kml.newpoint(name="Sample",coords=[(longitude,latitude)])

#here you have to set your own path to set the location for your kml file
kml.save("D:/udemy programs/user_points.kml")
