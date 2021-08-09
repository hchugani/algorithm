
class MinDistance:
    """
    https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0
    https://en.wikipedia.org/wiki/Levenshtein_distance

    for j from 1 to n:
      for i from 1 to m:
          if s[i] = t[j]:
            substitutionCost := 0
          else:
            substitutionCost := 1

          d[i, j] := minimum(d[i-1, j] + 1,                   // deletion
                             d[i, j-1] + 1,                   // insertion
                             d[i-1, j-1] + substitutionCost)  // substitution

  return d[m, n]

    Explaination

    D[i, j] =  max(i, j) if i=0 or j = 0
            =  min(D[i-1, j-1]+1, D[i][j-1], D[i-1][j]) if ai != bn
            = min D[i-1, j-1], D[i][j-1], D[i-1][j]) if ai -= bn
    """

    def findMinDistance(self, s1: str, s2: str):
        # converst s1 to s2
        n = len(s1)
        m = len(s2)
        dist = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n+1):
            dist[i][0] = i
        for j in range(m+1):
            dist[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                x = dist[i-1][j]+1 # deletion
                y = dist[i][j-1]+1 # insertion
                z = dist[i-1][j-1]
                if s1[i-1]!=s2[j-1]:
                    z +=1 # substituion
                dist[i][j] = min(x, y, z)
        return dist[n][m]


if __name__ == "__main__":
    md = MinDistance()
    print(md.findMinDistance("horse", "ros"))
    print(md.findMinDistance("zoologicoarchaeologist", "zoogeologist"))

