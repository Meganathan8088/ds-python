class MeansEndAnalysis:
    def __init__(self, operators):
        self.operators = operators

    # Check whether an operator can be applied
    def applicable(self, state, operator):
        for key, value in operator["precond"].items():
            if state.get(key) != value:
                return False
        return True

    # Apply an operator and return the new state
    def apply(self, state, operator):
        new_state = state.copy()
        new_state.update(operator["effect"])
        return new_state

    # Solve using recursive search
    def solve(self, current, goal, visited=None):

        if visited is None:
            visited = set()

        print(f"Current State: {current}")

        # Check if goal is reached
        if all(current.get(k) == v for k, v in goal.items()):
            return []

        # Convert dictionary to tuple so it can be stored in a set
        state_tuple = tuple(sorted(current.items()))

        if state_tuple in visited:
            return None

        visited.add(state_tuple)

        # Try every operator
        for op in self.operators:
            if self.applicable(current, op):
                new_state = self.apply(current, op)

                plan = self.solve(new_state, goal, visited)

                if plan is not None:
                    return [op["name"]] + plan

        return None


# ---------------- Main Program ----------------

if __name__ == "__main__":

    operators = [
        {
            "name": "Buy_Car",
            "precond": {
                "has_money": True,
                "has_car": False
            },
            "effect": {
                "has_car": True
            }
        },
        {
            "name": "Drive_Car",
            "precond": {
                "has_car": True,
                "at_home": True
            },
            "effect": {
                "at_work": True,
                "at_home": False
            }
        }
    ]

    initial_state = {
        "has_money": True,
        "has_car": False,
        "at_home": True,
        "at_work": False
    }

    goal_state = {
        "at_work": True
    }

    mea = MeansEndAnalysis(operators)

    plan = mea.solve(initial_state, goal_state)

    if plan is not None:
        print("\nPlan Found:")
        for step in plan:
            print(step)
    else:
        print("\nNo solution found.")