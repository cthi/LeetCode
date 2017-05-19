from collections import defaultdict


class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        dead = []
        ppid_table = defaultdict(list)

        for i, x in enumerate(ppid):
            ppid_table[x].append(i)

        self.killProcess_h(pid, ppid_table, kill, dead)

        return dead

    def killProcess_h(self, pid, ppid_table, kill, dead):
        dead.append(kill)

        if kill in ppid_table:
            for pos in ppid_table[kill]:
                self.killProcess_h(pid, ppid_table, pid[pos], dead)
