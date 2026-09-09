import sys
import json
from client import KnasterTarskiFixpointSolver

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "solve":
        solver = KnasterTarskiFixpointSolver()
        return solver.solve_set_fixpoint(params.get("init", []), params.get("max_size", 4))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
