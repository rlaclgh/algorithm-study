def solution(bridge_length, weight, truck_weights):
    length = len(truck_weights)
    on_road_weight = 0
    on_road_trucks = []
    arrival_trucks = []
    locations =[] 
    for i in range(1, (bridge_length+1)*(len(truck_weights)+1)):
        on_road_weight = sum(on_road_trucks)
        if truck_weights and on_road_weight + truck_weights[0] <= weight:
            on_road_trucks.append(truck_weights.pop(0))
            locations.append(0)
        locations = [x+1 for x in locations]
        if locations[0] == bridge_length:
            locations.pop(0)
            arrival_trucks.append(on_road_trucks.pop(0))
        if len(arrival_trucks) == length:
            return i+1