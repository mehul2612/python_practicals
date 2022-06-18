class Phone:
    def make_call(self):
        print("I am making a call")

    def play_game(self):
        print("I am playing a game")

    def set_color(self,color):
        self.color=color

    def set_cost(self,cost):
        self.cost=cost

    def show_color(self):
        return self.color

    def shoe_cost(self):
        return self.cost



p1=Phone()
p1.make_call()
p1.play_game()
p1.set_color("red")
p1.set_cost(5000)
print(p1.show_color())
print(p1.shoe_cost())