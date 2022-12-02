class mapAnalyser:

        def __init__:
                self.lines = []
                self.matrice = {}
                self.keys = {}
                self.position = None

        def createMatrice(lines):
                y = 0
                for line in self.lines:
                        x = 0
                        for car in line:
                                if car == '#':
                                        matrice[(x,y)] = 0
                                elif car in ['.', '@'] or (car.asalpha() and car.islower()):
                                        matrice[(x,y)] = 1
                                elif car.asalpha() and car.isupper():
                                        matrice[(x,y)] = -1
                                
                                if car == '@':
                                        self.position = (x,y)
                                if car.asalpha() and car.isupper():
                                        self.keys[(x,y)] = car
                                x += 1
                        y += 1
