Goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
ACTIONS ={
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}
def breath_first_search(start_state):
    queue = [(start_state, [])]
    visited = set()
    while queue:
        state, path = queue.pop(0)
        if state == Goal_state:
            return path
        visited.add(tuple(state))
        blank_index = state.index(0)
        for action in ACTIONS[blank_index]:
            new_state = state[:]
            new_state[blank_index], new_state[action] = new_state[action], new_state[blank_index]
            if tuple(new_state) not in visited:
                queue.append((new_state, path + [new_state]))
                initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]
                solution_path = breath_first_search(initial_state)
                if solution_path:
                    print("solution found")
                    for state in solution_path:
                        print(state)
                else:
                    print("solution not found")