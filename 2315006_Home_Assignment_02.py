# Grid dimensions
N = 4
M = 4

# Land use grid
land_use = [['R', 'C', 'E', 'R'],
['R', 'R', 'C', 'E'],
['I', 'R', 'R', 'C'],
['E', 'C', 'I', 'R']]

# Population grid
population = [[120, 40, 0, 200],
  [100, 180, 30, 0],
  [80, 160, 140, 60],
  [0, 30, 50, 190]]

# Temperature grid
temperature = [[32, 36, 30, 34],
   [35, 37, 33, 31],
   [40, 38, 39, 35],
   [28, 30, 41, 36]]


bus_stops = [(0, 0), (2, 3)]
service_centers = [(0, 1), (2, 2)]
waste_center = (1, 0)


# test case 2
# N=5
# M=4

# land_use = [['R', 'C', 'I', 'R'],
#             ['R', 'R', 'C', 'R'],
#             ['I', 'E', 'R', 'C'],
#             ['R', 'C', 'E', 'R'],
#             ['I', 'C', 'C', 'R']]

# population = [[150, 50, 90, 250],
#               [120, 130, 40, 100],
#               [80, 0, 140, 60],
#               [170, 20, 0, 190],
#               [100, 30, 20, 160]]

# temperature = [[32, 36, 30, 34],
#                 [35, 37, 33, 31],
#                 [40, 38, 39, 35],
#                 [28, 30, 41, 36],
#                 [28, 30, 41, 36]]

# num_bus_stop=3
# bus_stops = [(1, 1), (4, 2), (3,3)]
# waste_center = (3, 1)
# Num_service= 4
# service_centers = [(0, 0), (1, 1), (2,2), (3,3)]



# test case 3

# N=3
# M=3

# land_use = [['R', 'C', 'I'],
#             ['R', 'E', 'C'],
#             ['R', 'R', 'E']]

# population = [[120, 40, 100],
#               [110, 0, 50],
#               [200, 160, 0]]

# temperature = [[32, 36, 30],
#                 [35, 37, 33],
#                 [40, 38, 29]]

# num_bus_stop=2
# bus_stops = [(0, 0), (2, 1)]
# waste_center = (2, 0)
# Num_service= 2
# service_centers = [(2, 0), (2, 1)]




def show_summary_of_each_zone():
    land_use_count = {'R': 0, 'C': 0, 'E': 0, 'I': 0}
    population_sum = {'R': 0, 'C': 0, 'E': 0, 'I': 0} # Initialize population sums for each land type
    total_population =0
    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            land_type = land_use[i][j]
            pop = population[i][j]
            land_use_count[land_type] += 1
            population_sum[land_type] += pop
            total_population += pop
    print("Land Use summary")
    for land_type in land_use_count:
        count = land_use_count[land_type]
        total_pop = population_sum[land_type]
        avg_pop = total_pop/count if count > 0 else 0
        pop_percent = (total_pop/total_population)*100
        print(f"{land_type}: {count} cells, Total Population: {total_pop}, Avg: {avg_pop:.2f}")
        print(f"Population in {land_type} zones: {total_pop} ({pop_percent:.2f}% of total)")

import math
def euclidean_distance(a1,b1):
    return math.sqrt((a1[0] - b1[0]) ** 2 + (a1[1] - b1[1]) ** 2)



def find_bus_stop_accessibility():
    residential_cells =[]
    total_population = 0
    population_affected = 0
    far_cells = []
    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            if land_use[i][j] == 'R':
                residential_cells.append((i, j))
    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            total_population += population[i][j]
    for i,j in residential_cells:
        min_distance = 10000000

        for bus in bus_stops:
            distance = euclidean_distance((i, j), bus)
            min_distance = min(min_distance, distance)
        if min_distance>1.5:
            far_cells.append((i,j))
            population_affected+= population[i][j]

        affected_percent = (population_affected/ total_population)*100 if total_population > 0 else 0
    print(f"The cells more than 1.5 units away from nearest bus stopage : {far_cells}")
    print(f"Population affected: {population_affected} ({affected_percent:.2f}%) ")
    # print(total_population)
import itertools

def simulate_waste_collection():
    residential_cells =[]
    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            if land_use[i][j] == 'R' and (i,j)!= waste_center:
                residential_cells.append((i, j))
    best_route = []
    min_total_distance = 10000000
    for perm in itertools.permutations(residential_cells):
        route = [waste_center]+ list(perm) + [waste_center]
        total_distance = 0
        for i in range(len(route)-1):
            total_distance += euclidean_distance(route[i], route[i+1])
        if total_distance<min_total_distance:
            min_total_distance = total_distance
            best_route = route
    # waste_center = (1, 0)
    # route = [waste_center]
    # remaining_cells = residential_cells[:]
    # total_distance = 0

    
    # total_distance += euclidean_distance(route[-1], waste_center)
    print("Optimal Route: ",best_route)
    print(f"Total Distance: {min_total_distance:.2f} units")


def analyze_service_area():
    far_cells = []
    parks_needed = []
    # total_population = 0
    # covered_R_cells = set()
    
    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            if land_use[i][j] == 'R':
                # nearest_center = None
                min_distance = 10000000
                for center in service_centers:
                    distance = euclidean_distance((i, j),center)
                    if distance < min_distance:
                        min_distance = distance
                        # nearest_center = center
                if min_distance>1.5: #find cells that are more than 1.5 units away from nearest service centers
                        far_cells.append((i, j)) 
    print(f"Cells more than 1.5 units away from nearest service centers: {far_cells}")
    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            if land_use[i][j]=='E': #check empty cells
                for cx,cy in far_cells:
                    if euclidean_distance((i,j),(cx,cy))<=2.5: #find parks within 2.5units from each resodential cell
                        parks_needed.append((i,j))
                        break
                # nearby_R_cells = set()
                # for k in range(len(land_use)):
                #     for l in range(len(land_use[k])):
                #         if (land_use[k][l] =='R' or land_use[k][l]) and euclidean_distance((i,j),(k,l))<=2.5:
                #             # if (i,j) not in parks_needed:
                #             nearby_R_cells.add((k,l))
                # if nearby_R_cells:
                #     parks_needed.append((i, j))
                #     covered_R_cells.update(nearby_R_cells)
                                
    parks_needed = list(set(parks_needed))
    if parks_needed:
        print(f"Minimum number of parks : {len(parks_needed)}  {parks_needed}")
    else:
        print("Empty area for parks are not sufficient!")

def detect_heat_risks():
    heat_risk_cells =[]
    land_types =['R','C','I','E']
    land_avg_tmp = {'R':[],'C':[],'I':[],'E':[]}
    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            land_type = land_use[i][j]
            temp = temperature[i][j]
            land_avg_tmp[land_type].append(temp)

    highest_avg_tmp = 0
    highest_tmp_land_type = None
    for land_type in land_avg_tmp: # check each land type
        if land_avg_tmp[land_type]: # if there are temperatures recorded for this land type
            avg_temp = sum(land_avg_tmp[land_type])/len(land_avg_tmp[land_type]) 
            if avg_temp>highest_avg_tmp:
                highest_avg_tmp= avg_temp
                highest_tmp_land_type= land_type


    for i in range(len(land_use)):
        for j in range(len(land_use[i])):
            if (land_use[i][j] in ['R','C'] and temperature[i][j]>36 and population[i][j]>100): #if the land type is residential or commercial and temperature is above 36 and population is above 100
                heat_risk_cells.append((i, j))


    print(f"{highest_tmp_land_type} zones have heighest average temperature: {highest_avg_tmp} deg Celcius")
    print(f"UHI risk cellls: {heat_risk_cells}")            

def main():
    while True:
        print("Welcome to SmartCity Planner!")
        print("1. Show Zoning Summary")
        print("2. Check Bus Stop Accessibility")
        print("3. Simulate Waste Collection Routes")
        print("4. Analyze Service Area Coverage")
        print("5. Detect UHI Risks")
        print("6. Exit")
        while True:
            try:
                choice=int(input("Enter your choice: "))
                if choice<1 or choice>6:
                    print("please enter a number between 1 and 6.")
                    continue
                break
            except ValueError:
                print("Inalid input please enter a number between 1 and 8.")
        if choice == 1:
            show_summary_of_each_zone()
        elif choice == 2:
            find_bus_stop_accessibility()
        elif choice == 3:
            simulate_waste_collection()
        elif choice == 4:
            analyze_service_area()
        elif choice == 5:
            detect_heat_risks()
        elif choice == 6:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()