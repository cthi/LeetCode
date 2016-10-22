import re

class Solution():
    def deserialize(self, s):
        tokens = re.findall(r"\[|\]|-?[0-9]+", s)
        return self.deserialize_h(tokens)

    def deserialize_h(self, tokens):
        if len(tokens) == 1:
            return int(tokens[0])
            
        counter = 0
        indicies = []

        for i, token in enumerate(tokens):
          if i == 0 or i == len(tokens) - 1:
            continue
          if token == '[':
            if counter == 0:
              indicies.append(i)
            counter += 1
          elif token == ']':
            counter -= 1 
            if counter == 0:
              indicies.append(i)
          else:
            if counter == 0:
              indicies.append(i)

        res = []
        i = 0

        while i < len(indicies):
          token = tokens[indicies[i]]
          if token[0] == '-' or token.isdigit():
            res.append(int(token))
            i += 1
          else:
            res.append(self.deserialize_h(tokens[indicies[i]: indicies[i + 1] + 1]))
            i += 2
        
        return res

