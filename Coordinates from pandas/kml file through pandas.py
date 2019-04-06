import simplekml,pandas

#here you have to set your own path to set the location for your csv file
df=pandas.read_csv("D:/udemy programs/1_pandas.csv")

kml=simplekml.Kml()

for lon,lat in zip(df["Longitude"],df["Latitude"]):
    kml.newpoint(coords=[(lon,lat)])

#here you have to set your own path to set the location for your kml file
kml.save("D:/udemy programs/pandas_csv_points.kml")

