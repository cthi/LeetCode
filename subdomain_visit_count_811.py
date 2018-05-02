class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        class Node:
            def __init__(self):
                self.visits = 0
                self.children = {}
        
        def traverse(name, node, output):
            if not node:
                return
            
            output.append(str(node.visits) + " "  + name)
            
            for child_name, child in node.children.items():
                if name:
                    traverse(child_name + '.' + name, child, output)
                else:
                    traverse(child_name, child, output)
    
        root = Node()
        
        for entry in cpdomains:
            visits, domains = entry.split()
            node = root
            for path in reversed(domains.split('.')):
                if path not in node.children:
                    node.children[path] = Node()
                
                node.children[path].visits += int(visits)
                node = node.children[path]
                
        output = []
        traverse("", root, output)
        return output[1:]
