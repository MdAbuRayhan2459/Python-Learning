class Geopoint:
    def __init__(self,name, latitude, longitude,type_):
        self.name = name
        self.latitude= latitude
        self.longitude = longitude
        self.type_ = type_


    def print_info(self):
        print(f"Name:{self.name}")
        print(f"Latitude: {self.latitude}")
        print(f"Longtitude:{self.longitude}")
        print(f"Type:{self.type_}")


import math
def haversine(lat1, lon1, lat2, lon2):
 R = 6371
 dlat = math.radians(lat2 - lat1)
 dlon = math.radians(lon2 - lon1)
 a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) \
 * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
 return R * 2 * math.asin(math.sqrt(a))





class GeoSystem:


    def __init__(self ):
       self.places =[]

    def add_place(self,point):
       self.places.append(point)




    def find_nearest(self,lat, lon):
        if not self.places:
            return None
        nearest_place = None
        shortest_distance= 100000000
        for place in self.places :
           d = haversine(lat,lon, place.latitude,place.longitude)
        #    print(f"Checking {place.name}: {distance:.2f} km")
           if d< shortest_distance:
              shortest_distance = d
              nearest_place = place

        return nearest_place



    def find_nearest_by_type(self,lat,lon,type_):
        nearest_place = None
        shortest_distance = 10000000
        # found= False
        for place in self.places:
            if place.type_.lower()== type_.lower():
                # found =True
                d = haversine(lat,lon,place.latitude,place.longitude)
                if d<shortest_distance:
                    shortest_distance=d
                    nearest_place=place
        return nearest_place
    
        # if found:
        #     return nearest_place
        # else:
        #     return None
    def find_within_radius(self, lat,lon, radius_km):
        places_in_radius=[]

        for place in self.places:
            d= haversine(lat,lon,place.latitude, place.longitude)
            if d<= radius_km:
                places_in_radius.append(place)
                
        return places_in_radius
          

    def group_by_type(self):
        Groups = {}
        for place in self.places:
            place_type = place.type_
            if place_type not in Groups:
                Groups[place_type]=[]
            Groups[place_type].append(place.name)
        return Groups
        
    def find_farthest_pair(self):
        max_d=0
        farthest_pair=(None,None)
        for i in range( len(self.places)):
            for j in range(i+1,len(self.places)):
                place1=self.places[i]
                place2=self.places[j]
                d = haversine(place1.latitude,place1.longitude,place2.latitude,place2.longitude)
                if d>max_d:
                    max_d=d
                    farthest_pair=(place1, place2)
        return farthest_pair,max_d


       

    def center_point(self):
        if not self.places:
            return None
        total_latitude = 0
        total_longitude=0
        count=0
        for place in self.places:
            total_latitude=total_latitude+place.latitude
            total_longitude=total_longitude+place.longitude
            count+=1
            center_latitude=total_latitude/count
            center_longitude=total_longitude/count
        return(center_latitude,center_longitude)






places = [
    Geopoint("Central Park", 40.7851, -73.9683, "Park"),
    Geopoint("City Hospital", 40.7401, -73.9902, "Hospital"),
    Geopoint("Union Market", 40.7347, -74.0027, "Market"),
    Geopoint("Green School", 40.7218, -73.9977, "School"),
    Geopoint("Sunrise School", 40.7295, -73.9854,"School"),
    ]







def main_menu():
    geo = GeoSystem()


    for p in places:
        geo.add_place(p)


    while True:
        print("GeoExplorer Menu:")
        print("1. Add a new place")
        print("2. Find nerest place to a location")
        print('3. Find nearest place of a specific type')
        print('4. Show all places within radius')
        print('5. Group places by type')
        print('6. Show two farthest places')
        print('7. Show center point')
        print('8. Exit')
        # choice = int(input("Enter your choice: "))
        while True:
            try:
                choice=int(input("Enter your choice: "))
                if choice<1 or choice>8:
                    print("please enter a number between 1 and 8.")
                    continue
                break
            except ValueError:
                print("Inalid input please enter a number between 1 and 8.")


        if choice == 1:
            name = input("enter place name: ")
            lat = float(input("enter latitude: "))
            lon = float(input("enter longitude:"))
            type_ = input("enter place type: ")
            geo.add_place(Geopoint(name,lat,lon,type_))
            print("Place added!")

        elif choice == 2:
            lat = float(input("enter latitude: "))
            lon = float(input("enter longitude: "))
            nearest=geo.find_nearest(lat,lon)
            if nearest:
                print(f"Nearest place: {nearest.name} ({nearest.latitude},{nearest.longitude},{nearest.type_})")
            else:
                print("not available")
        


        elif choice==3:
            lat = float(input("enter latitude:  "))
            lon = float(input("enter longitude: "))
            type_ = input("enter place type: ")
            nearest = geo.find_nearest_by_type(lat,lon,type_)
            if nearest:
                print(f"Nearest {type_}: {nearest.name} ({nearest.latitude},{nearest.longitude})")
            else:
                print(f"No place is available of type {type_}")
            

        elif choice==4:
            lat = float(input("enter latitude: "))
            lon = float(input("enter longitude: "))
            radius =float(input("enter radius in km: "))
            result = geo.find_within_radius(lat,lon,radius)
            if result:
              print(f"Place within {radius} km:")
              for place in result:
                 print(f"- {place.name} ({place.type_})")
            else:
               print("no places found within the radius")
        

        elif choice==5:
            groups = geo.group_by_type()
            print("Grouped by type:")
            for type_,names in groups.items():
               print(f"{type_}:{','.join(names)}")
        

        elif choice==6:
            (place_1,place_2),dist= geo.find_farthest_pair()
            if place_1 and place_2:
                print(f"Farthest places:{place_1.name}<-->{place_2.name} Distance: {dist:.1f} km")
            else:
                print("not available")


        elif choice==7:
            center = geo.center_point()
            if center:
                print(f"Center point: {center[0]:.4f},{center[1]:.4f}")
            else:
                print('not available')

        elif choice==8:
            print("Exiting GeoExplorer.Goodbye!")
            break
        # else:
        #     print("Please choose a number between 1-8")
            
if __name__ == "__main__":
    main_menu()


