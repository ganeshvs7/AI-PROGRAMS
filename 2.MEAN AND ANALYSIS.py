print("GANESH V S  24BECS157 ")
print("mean end analysis")
class MeanEndAnalysis:
    def __init__(self, operators):
        self.operators = operators
    
    def solve(self, current , goal):
        print (f"current state: {current}||goal state: {goal} ")
        if current == goal:
            print("Goal state reached!")
            return []
        #find difference between current and goal state
        diff = self.find_difference(current, goal)
        if not diff:
            return []
        #find operator that can resolve the difference
        op=self.select_operator(diff)
        if not op:
            print("No operator found to resolve the difference.")
            return None
        #check preconditions of the operator
        preconditions_path=self.solve(current,op['precond'])
        if preconditions_path is None:
            print("Preconditions not satisfied.")
            return None
        #apply the operator to get the new state
        new_state=op['effect']
        remainaing_path=self.solve(new_state,goal)
        if remainaing_path is None:
            print("Failed to reach the goal state.")
            return None
        return preconditions_path + [op['name']] + remainaing_path
    
    def find_difference(self, current, goal):
        for key in goal:
            if current.get(key) != goal.get(key):
                return {key: goal[key]}
        return None
    
    def select_operator(self, diff):
        key, val = next(iter(diff.items()))
        for op in self.operators:
            if op['effect'].get(key) == val:    
                return op
        return None


# example usage
if __name__ == "__main__":
    operators = [
        {'name': 'drive_car',
         'precond':{'has_car': True,'at_home': True},
         'effect':{'at_work': True, 'at_home': False}
        },
        {
            'name':'buy_car',
            'precond':{'has_money': True, 'at_home': True},
            'effect':{'has_car': True}
        }
    ]
    current_state = {'has_money': True, 'has_car': False, 'at_home': True}
    goal_state = {"at_work": True}
    mea = MeanEndAnalysis(operators)
    plan = mea.solve(current_state,goal_state)
    print("\nExecution plan:",plan)






