from impl.Grid import Grid

g = Grid(7)

g.grid[1][1].makeSet('a')

g.draw()

g.grid[1][1].moveBaton('a','v','v',1)

g.grid[1][2].moveBaton('a','v','h',1)

g.draw()

g.grid[1][1].trySendMessage()

g.draw()

g.grid[1][2].trySendMessage()

g.run()

g.draw()

g.grid[1][1].moveBaton('a','h','v', -1)

g.draw()

g.grid[1][1].trySendMessage()

g.run()

g.draw()

g.grid[1][0].moveBaton('a','h','v', -1)

g.run()

g.draw()

g.grid[1][-1].moveBaton('a','h','h', -1)

g.run()

g.draw()

g.grid[0][-1].moveBaton('a','h','h', 1)

g.run()

g.grid[1][-1].moveBaton('a','h','h', 1)

g.run()

g.grid[2][-1].moveBaton('a','h','h', 1)

g.run()

g.grid[3][-1].moveBaton('a','h','h', 1)

g.run()

g.draw()

g.grid[2][2].moveBaton('a','v','v', 1)

g.run()

g.grid[2][3].moveBaton('a','v','v', 1)

g.run()

g.grid[2][4].moveBaton('a','v','v', 1)

g.run()

g.grid[2][5].moveBaton('a','v','v', 1)

g.run()

g.grid[2][6].moveBaton('a','v','v', 1)

g.run()

g.grid[2][0].moveBaton('a','v','v', 1)

g.run()

g.draw()

g.grid[2][1].makeMessage('a','v','hello!')

g.step()

g.draw()

g.step()

g.draw()

g.step()

g.draw()

g.step()

g.draw()

g.grid[4][-1].makeMessage('a','h','konichiwa!')

g.step()

g.draw()

g.step()

g.draw()

g.step()

g.draw()

g.step()

g.draw()

g.grid[4][-1].moveBaton('a','h','h',-1)

g.run()

g.draw()

g.grid[3][-1].moveBaton('a','h','h',-1)

g.run()

g.draw()

g.grid[2][-1].makeMessage('a','h','gutentag!')

g.run()

g.grid[2][-1].moveBaton('a','h','h',-1)

g.run()

g.draw()

g.grid[1][-1].makeMessage('a','h','bonjour!')

g.run()
