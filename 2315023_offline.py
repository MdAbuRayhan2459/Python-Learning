import math
def haversine(lat1,lon1,lat2,lon2):
    R=6371
    dlat=math.radians(lat2-lat1)
    dlon=math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) \
* math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    distance= R *2*math.asin(math.sqrt((a)))
    return distance

class Geopoint:
    def __init__(self,name,latitude,longitude,type_):
        self.name=name
        self.latitude=latitude
        self.longitude=longitude
        self.type_=type_
    def print_info(self):
        print(f"name:{self.name}")
        print(f"latitude:{self.latitude}")
        print(f"longtitude:{self.longitude}")
        print(f"type:{self.type_}")
class Geosystem:
    def __init__(self):
        self.places=[]
    def add_place(self,point):
        self.places.append(point)
    def find_nearest(self,lat,lon):
        if len(self.places)== 0:
            return None
        nearest_place=self.places[0]
        minimum_distance=haversine(lat,lon,nearest_place.latitude,nearest_place.longitude)
        for place in self.places[1:]:
            distance=haversine(lat,lon,place.latitude,place.longitude)
            if distance< minimum_distance:
                distance=minimum_distance
                nearest_place=place
        return nearest_place
    def find_within_radius(self,lat,lon,radius_km):
        find_result = []
        for place in self.places [0:]:
            distance =haversine(lat,lon,place.latitude,place.longitude)
            if distance <= radius_km:
                find_result.append(place)
            return find_result
    def find_nearest_of_type (self,latitude,longitude,type_):
        if len(self.places)==0:
            return None
        nearest_place=self.places[0]
        minimum_distance=haversine(latitude,longitude,nearest_place.latitude,nearest_place.longitude)
        for place in self.places[1:]:
            if place.lower() == type_.lower():
                 distance=haversine(latitude,longitude,place.latitude,place.longitude)
                 if distance< minimum_distance:
                      distance=minimum_distance
                      nearest_place=place 
                 return nearest_place
    def group_by_type (self):
        group={

        }
        for place in self.places [0:]:
            type_=place.type
            if type_ in group:
                group [type_].append(place)
            else:
                group [type_]= [place]
        return group
    def find_farthest_pair (self):
        if len(self.places)<2:
            return None
        maximum_distance=0
        place1=None
        place2=None
        for i in range(len(self.places)):
            for j in range (i+1,self.places):
                p1=self.places[i]
                p2=self.places[j]
                distance= haversine(p1.latitude,p1.lontitudw,p2.latitude,p2.longitude)
                if distance > maximum_distance:
                    maximum_distance=distance
                    place1=p1
                    place2=p2
        return place1,place2,maximum_distance
    def center_point (self):
        if len(self.places)==0:
            return None
        sum_latitutde = 0
        sum_longitude = 0
        x=len(self.places)
        for place in self.places[0:]:
            sum_latitutde +=place.latitude
            sum_longitude += place.longitude
        centre_latitude=sum_latitutde/x
        centre_longitude=sum_longitude/x
        return (centre_latitude,centre_longitude)
sample_places = [
     Geopoint("Central Park", 40.7851, -73.9683, "Park"),
     Geopoint("City Hospital", 40.7401, -73.9902, "Hospital"),
     Geopoint("Union Market", 40.7347, -74.0027, "Market"),
     Geopoint("Green School", 40.7218, -73.9977, "School"),
     Geopoint("Sunrise School", 40.7295, -73.9854, "School"),
     ]
def menu():
    gs=Geosystem()
    for place in sample_places:
        gs.add_place(place)
    while True:
        print("/n GeoExplorer Menu:")
        print("1. Add a new place")
        print("2. Find nearest place to a location")
        print("3. Find nearest place of a specific type")
        print("4. Show all places within radius")
        print("5. Group places by type")
        print("6. Show two farthest places")
        print("7. Show center point")
        print("8. Exit")

        choice= input("Enter choice from the menu:")
        if choice== "1":
            name= input("Enter name:")
            latitude = float(input("Enter the latitude value:"))
            longitude = float(input("Enter the longitude value:"))
            type_=input("Enter place type:")
            point= Geopoint(name,latitude,longitude,type_)
            gs.add_place(point)
            print("Added")
        
        elif choice== "2":
            latitude = float(input("Enter the latitude value:"))
            longitude = float(input("Enter the longitude value:"))
            nearest_distance_place=gs.find_nearest(latitude,longitude)
            if nearest_distance_place:
                print("Nearest place:",(nearest_distance_place.name,nearest_distance_place.latitude,nearest_distance_place.longitude))
            else:
                print("No place found")

        elif choice == "3":
            latitude = float(input("Enter the latitude value:"))
            longitude = float(input("Enter the longitude value:"))
            type_=input("Enter place type:")
            find=gs.find_nearest_of_type(latitude,longitude,type_)
            if find:
                    print("Nearest place(Type):",(nearest_distance_place.name,nearest_distance_place.latitude,nearest_distance_place.longitude))
            else:
                print("No place found")
        elif choice == "4":
            latitude = float(input("Enter the latitude value:"))
            longitude = float(input("Enter the longitude value:"))
            radius = float(input("Enter the radius in km :"))
            nearby_place=gs.find_within_radius(latitude,longitude,radius)
            if nearby_place:
                print("Place is within (km):",radius,"km")
            else:
                print("No place found")
        elif choice == "5":
            type_group=gs.group_by_type()
            if type_group:
                print("Group by type:")
                for type_,places in type_group.item():
                    name=",".join(place.name for place in places)
                    print("Type:",name)
                else:
                    print("No place found for grouping")
        elif choice == "6":
            result=gs.find_farthest_pair()
            if result:
                place1,place2,distance =result
                print("Farthest places:",(place1.name,place2.name),"Distance:",distance)
        elif choice=="7":
            centre=gs.center_point()
            if centre:
                print("Centre point:",centre )
            else:
                print("There is no places to calculate the centre")
        elif choice=="8":
            print("Exit")
            break
        else:
            print("Choice is invailed,Please input again.")
if __name__=="__main__":
    menu()
