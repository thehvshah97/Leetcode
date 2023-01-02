from collections import defaultdict, deque
from typing import List


class EvaluateDivision:
    def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        evaluations = defaultdict(list)

        for i in range(len(equations)):
            x, y, v = equations[i][0], equations[i][1], values[i]
            evaluations[x].append([y, v])
            evaluations[y].append([x, 1 / v])

        results = []
        for i in range(len(queries)):
            a, b = queries[i]
            if a not in evaluations or b not in evaluations:
                results.append(float(-1))
                continue
            q = deque([(a, 1)])
            seen = set()
            while q:
                var, m = q.popleft()
                if var == b:
                    results.append(m)
                    q = []
                    continue

                for x, val in evaluations[var]:
                    if x in seen: continue
                    q.append((x, m * val))

                seen.add(var)
            if len(results) != i + 1:
                results.append(float(-1))

        return results


if __name__ == '__main__':
    print(EvaluateDivision.calcEquation([["a","b"],["b","c"]], [2.0, 3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
