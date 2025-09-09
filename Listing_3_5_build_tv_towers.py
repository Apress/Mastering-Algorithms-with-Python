def build_tv_towers(sets_and_costs):
    I = set()
    all_neighbors = set()
    for cur_set, _ in sets_and_costs:
        all_neighbors |= cur_set
    total_cost = 0
    selected_sets = []
    while I != all_neighbors:
        per_new_element_costs = []
        for cur_set, cur_cost in sets_and_costs:
            new_element_set = cur_set - I 
            if new_element_set:
                per_new_element_costs.append((cur_cost / len(new_element_set), cur_set, cur_cost))
        min_cost, new_set, cur_cost = min(per_new_element_costs, key = lambda x: x[0])
        total_cost += cur_cost
        I |= new_set
        selected_sets.append(new_set)
        sets_and_costs.remove((new_set, cur_cost))
    return total_cost, selected_sets
        
if __name__ == "__main__":
    sets_and_costs = [({"A", "B", "C"}, 10),
                      ({"B", "D"}, 15),
                      ({"C", "D", "E"}, 12),
                      ({"A"}, 5)]
    print (build_tv_towers(sets_and_costs))