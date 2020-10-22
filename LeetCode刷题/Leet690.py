import queue


class Solution:
    def getImportance(self, employees, id):
        emap = {e.id: e for e in employees}
        sum = 0
        q = queue.SimpleQueue()
        q.put(emap[id])
        while not q.empty():
            emp = q.get()
            sum += emp.importance
            for i in emp.subordinates:
                q.put(emap[i])
        return sum
