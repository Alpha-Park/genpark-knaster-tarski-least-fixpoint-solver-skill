from client import KnasterTarskiFixpointSolver

def main():
    print("=== Knaster-Tarski Least Fixpoint Solver ===")
    solver = KnasterTarskiFixpointSolver()
    res = solver.solve_set_fixpoint([], max_size=4)
    print("Fixpoint Result:", res)
    assert res["least_fixpoint"] == [0, 1, 2, 3]

    print("Knaster-Tarski Solver verified successfully!")

if __name__ == "__main__":
    main()
