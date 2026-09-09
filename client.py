class KnasterTarskiFixpointSolver:
    """Iterative least fixpoint computation on monotonic functions over finite lattices."""
    def solve_set_fixpoint(self, initial_set: list[int], max_size: int = 5) -> dict:
        curr = set(initial_set)
        steps = 0
        while len(curr) < max_size:
            steps += 1
            nxt = curr | {len(curr)}
            if nxt == curr:
                break
            curr = nxt

        return {
            "initial_elements": initial_set,
            "least_fixpoint": sorted(list(curr)),
            "iterations": steps
        }
