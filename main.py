class JOperator:
    capacity = [None, 5, 3, 2]

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __repr__(self):
        return str(self.i) + " => " + str(self.j)

    def is_applicable(self, state):
        a = state.a
        # 5.1 alkalmazĂĄsi elĹfeltĂŠtel
        return a[self.i] > 0 and a[self.j] < JOperator.capacity[self.j]

    def apply(self, state):
        a = state.a
        new = JState()
        b = new.a
        # 5.2 hatĂĄsdefinĂ­ciĂł
        m = min(a[self.i], JOperator.capacity[self.j] - a[self.j])
        for k in (1, 2, 3):
            b[k] = a[k] + m if k == self.j else a[k] - m if k == self.i else a[k]
        return new


class JState:
    # 5.
    operators = [JOperator(i, j) for i in [1, 2, 3] for j in [1, 2, 3] if not i == j]

    def __init__(self):
        # 3. kezdoallapot
        self.a = [None, 5, 0, 0]

    def is_goal(self):
        # 4. celfeltetel
        return self.a[1] == 4

    def __str__(self):
        return self.a.__str__()

    def __repr__(self):
        return self.a.__repr__()

    def __eq__(self, other):
        return self.a.__eq__(other.a)

    def successors(self):
        result = []
        for op in JState.operators:
            if op.is_applicable(self):
                result.append((op.apply(self), op))
        return result


# start = JState()
# print(JOperator(1, 3).apply(start).is_goal())
# print(start.successors())

def search(start):
    class Node:
        count = 0
        def __init__(self, state, creator, parent):
            self.state = state
            self.creator = creator
            self.parent = parent
            Node.count = Node.count + 1 # ez itt időbonyolultság lesz. Garbage kollektoros nyelvek esetén nehéz tárbonyolultságot írni

    # 1
    leaves = [Node(start, None, None)]
    expanded = []


    # 2. feltétel vizsgálat
    while len(leaves) > 0:
        # 3.
        selected = leaves.pop(0)  # ez egy mélységi kereső --> FIFO <== a pop operátor alapértelmezetten az utolsó helyre rakja az elemet
        # 4.
        if selected.state.is_goal():
            print(Node.count)
            return selected  # VÉGE, megoldást találtunk
        # 5.
        if selected.state not in expanded:
            expanded.append(selected.state)
            for successor in selected.state.successors():
                leaves.append(Node(successor[0], successor[1], selected)) # az append az utolsó elemet veszi ki ==> verem adatszerkezet

    return None  # VÉGE, nem találtunk megoldást


print(search(JState()).creator)

goal = search(JState())
if not goal == None:
    solution = []
    while not goal.parent == None:
        solution.insert(0, goal.creator)
        goal = goal.parent
    print(solution)

