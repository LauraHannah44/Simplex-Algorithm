class Tableau:
    def __init__(self):
        self.size = {"eq": int(input("eq: ")),"var": int(input("var: "))}
        self.vars = []

        self.var_labels = ["P"]

        for var_num in range(self.size["var"]):
            self.var_labels.append("x{}".format(var_num))

        for slack_num in range(self.size["eq"] - 1):
            self.var_labels.append("s{}".format(slack_num))

        self.var_labels.append("val")

        for eq_num in range(self.size["eq"]):

            self.vars.append([int(eq_num == 0)])
            for var in self.var_labels[1:1+self.size["var"]]:
                self.vars[eq_num].append(int(input("eq.{}, var.{}: ".format(eq_num, var))))
            
            for slack_num in range(self.size["eq"] - 1):
                self.vars[eq_num].append(int(eq_num == slack_num + 1))

            self.vars[eq_num].append(int(input("eq.{} val: ".format(eq_num))))


    def display(self):
        for eq_num in range(self.size["eq"]):
            print(" | ".join(map(str, self.vars[eq_num])))

        for eq_num in range(self.size["eq"]):

            string = []
            for var_num, var_name in enumerate(self.var_labels[0:-1]):
                string.append(str(self.vars[eq_num][var_num]) + var_name)

            print(" + ".join(string) + " = {}".format(self.vars[eq_num][-1]))


    def interpret(self):
        pass

    
    def pivot(self, pivot):
        divisor = self.vars[pivot["eq"]][pivot["var"]]

        for var_num in range(1 + self.size["var"] + self.size["eq"] - 1 + 1):
            self.vars[pivot["eq"]][var_num] /= divisor
        
        for eq_num in range(self.size["eq"]):

            if eq_num != pivot["eq"]:
                multiplier = self.vars[eq_num][pivot["var"]]
            
                for var_num in range(1 + self.size["var"] + self.size["eq"] - 1 + 1):
                    self.vars[eq_num][var_num] -= multiplier * self.vars[pivot["eq"]][var_num]



tableau = Tableau()
tableau.display()
tableau.pivot({"eq": int(input("pivoteq: ")), "var": int(input("pivotvar: "))})
tableau.display()