import random
from bokeh.plotting import figure, show

class probability(object):
    """This class have been created just to refresh back my ability to code. It's not useful, it's not well written.
    The pourpose of this class is to give the user some method for basic probability computation.
    """

    def __init__(self) -> None:
        self.p = figure(title="Distribution", x_axis_label="x", y_axis_label="y")
        super().__init__()


    def uniform_random_variable(self, min, max) -> float:
        return random.uniform(min, max)

    def normal_random_variable(self, mu, sigma) -> float:
        return random.normalvariate(mu, sigma)

    def gauss_random_variable(self, mu, sigma) -> float:
        return random.gauss(mu, sigma)
        
        
    def print_distribution(self, probability_function, a, b, n) -> None:
        """Generate a graph to show the given probability function
        """
        data = [probability_function(a,b) for i in range(n)]
        print(len(data))
        n_bin = round(n/200)
        minima, maxima = min(data), max(data)
        binsize = (maxima - minima)/n_bin
        positions = [minima + (i+0.5)*binsize for i in range (n_bin)]
        frequency = [len([x for x in data if minima + i*binsize <= x < minima + (i+1)*binsize]) for i in range(n_bin)]
        
        self.p.line(positions, frequency, legend_label="Distribution for "+ probability_function.__name__, line_width=2)
        show(self.p)





if __name__ == "__main__":
    p = probability()
    p.print_distribution(p.gauss_random_variable, 0, 1, 100000)
    p.print_distribution(p.normal_random_variable, 0, 1, 100000)
    "uhuh"
