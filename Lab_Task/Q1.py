def solve_8_puzzle(start_state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
def manhattan_distance(state):
        distance = 0
        for i in range(len(state)):
              if state[i]==0:
                    current_row, current_col = divmod(i, 3)
                    target_row, target_col = divmod(8, 3)
                    distance += abs(current_row - target_row) + abs(current_col - target_col)
                    return distance
              def get_blank_index(state):
                    return state.index(0)
              def get_possible_moves(state):
                    moves=[(0,1),(0,-1),(1,0),(-1,0)]
                    blank_index=get_blank_index(state)
                    blank_row,blank_col=divmod(blank_index,3)
                    possible_moves=[]
                    for move in moves:
                        new_row,new_col=blank_row+move[0],blank_col+move[1]
                        if 0<=new_row<3 and 0<=new_col<3:
                            possible_moves.append((new_row,new_col))
                            return possible_moves
                        def swap(state ,index1,index2):
                            new_state=state[:]
                            new_state[index1],new_state[index2]=new_state[index2],new_state[index1]
                            return new_state
                        open_set=[(initial_state ,0,manhattan_distance(initial_state))]
                        closed_set=set()
                        while open_set:
                            current_state, g, h = min(open_set, key=lambda x: x[1] + x[2])
                            open_set.remove((current_state, g, h))
                            closed_set.add(tuple(current_state))
                            if current_state == goal_state:
                                path=[]
                                while parent is not None:
                                    path.append(current_state)
                                    current_state, parent = parent
                                    path.reverse()
                                    return path
                                blank_index = get_blank_index(current_state)
                                possible_moves = get_possible_moves(current_state)
                                for move in possible_moves:
                                     new_state =swap(current_state,blank_index,move[0]*3+move[1])
                                     if tuple(new_state) not in closed_set:
                                         open_set.append((new_state,g+1,manhattan_distance(new_state)))
                                         parent=(current_state, parent)
                                         return None
                                     state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
                                     solution_path=solve_8_puzzle(state)
                                     if solution_path:
                                         print("solution found")
                                for state in solution_path:
                                         print(state)
                            else:
                                        print("solution not found")
                        