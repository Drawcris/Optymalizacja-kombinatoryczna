from ortools.linear_solver import pywraplp

def CreateModel():
    data = {}
    data["constriant_coeffs"] = [
        [3, 4],
        [3, 2]
    ]
    data["bounds"] = [5000, 4000]
    data["obj_coeffs"] = [3, 3.4]
    data["num_vars"] = 2
    data["num_constraints"] = 2
    return data

def main():
    data = CreateModel()
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return
    infinity = solver.infinity()
    x = {}
    for j in range(data["num_vars"]):
        x[j] = solver.IntVar(0, infinity, "x[%i]" % j)
    print("Numver of variables: =", solver.NumVariables())
    for i in range(data["num_constraints"]):
        constriant = solver.RowConstraint(0, data["bounds"][i], "")
        for j in range(data["num_vars"]):
            constriant.SetCoefficient(x[j], data["constriant_coeffs"][i][j])
    print("Num of constraints: =", solver.NumConstraints())

    objective = solver.Objective()
    for j in range(data["num_vars"]):
        objective.SetCoefficient(x[j], data["obj_coeffs"][j])
    objective.SetMaximization()

    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Objective value =", solver.Objective().Value())
        for j in range(data["num_vars"]):
            print(x[j].name(), " = ", x[j].solution_value())
        print()
        print(f"Problem solved in {solver.wall_time():d} milliseconds.")
        print(f"Problem solved in {solver.iterations():d} iterations.")
        print(f"Problem solved in {solver.nodes():d} branch-and-bound nodes.")
    else:
        print("The problem does not have an optimal solution.")

if __name__ == "__main__":
    main()
