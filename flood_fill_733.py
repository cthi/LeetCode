class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        def floodFill_h(image, sr, sc, newColor, ogColor, seen, N, M):
            if sr > N - 1 or sc > M - 1 or sr < 0 or sc < 0 or (sr, sc) in seen or image[sr][sc] != ogColor:
                return

            seen.add((sr, sc))
            image[sr][sc] = newColor

            for x, y in dirs:
                floodFill_h(image, sr + x, sc + y, newColor, ogColor, seen, N , M)

        floodFill_h(image, sr, sc, newColor, image[sr][sc], set(), len(image), len(image[0]))
        return image
