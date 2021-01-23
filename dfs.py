from collections import defaultdict


class Graph:

	def __init__(self,vertices):

		self.V=vertices
		self.graph=defaultdict(list)

	def addEdge(self,u,v):
		if u<=self.V and v<=self.V:
			self.graph[u].append(v)

	def dfs(self,u,explored):
		for i in self.graph[u]:
			if i not in explored:
				explored.add(i)
				print(str(i)+" --> ")
				self.dfs(i,explored)


	def dfs_main(self,u):
		explored=set()
		explored.add(u)
		print(str(u) + " --> ")
		self.dfs(u,explored)

	












g=Graph(7)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(3,7)
#g.addEdge(1,4)

g.dfs_main(1)












