import random
import time
from bokeh.plotting import figure, show
from bokeh.palettes import Dark2_5 as palette
import itertools
import math

class probability(object):
    """This class have been created just to refresh back my ability to code. It's not useful, it's not well written.
    The pourpose of this class is to give the user some method for basic probability computation.
    """

    def __init__(self) -> None:
        self.clear_graphs()
        super().__init__()


    def uniform_random_variable(self, min, max) -> float:
        return random.uniform(min, max)

    def normal_random_variable(self, mu, sigma) -> float:
        return random.normalvariate(mu, sigma)

    def gauss_random_variable(self, mu, sigma) -> float:
        return random.gauss(mu, sigma)

    def gaussian_distribution(self, x, mu, sigma) -> float:
        """Generate random point according to gaussian distribution """ 
        return 1/math.sqrt(2*math.pi*sigma**2) * math.exp(-(x-mu)**2/(2*sigma**2))
        
    def prepare_graph(self, probability_function, n, *args) -> None:
        #region comments
        """Generate a graph for the given probability function. Use show_graph to show on browser.
        
        Parameters:
        n (int): number of points to generate
        probability_function (func): the function to plot
        args (float): the parameters to use in func

        Returns:
        None
        """
        #endregion

        data = [probability_function(*args) for i in range(n)]
        n_bin = 50 #round(n*0.05)
        minima, maxima = min(data), max(data)
        binsize = (maxima - minima)/n_bin
        positions = [minima + (i+0.5)*binsize for i in range (n_bin)]
        frequencies = [len([x for x in data if minima + i*binsize <= x < minima + (i+1)*binsize]) for i in range(n_bin)]       
        self.p.line(positions, frequencies, legend_label="Distribution for "+ probability_function.__name__, line_width=2, color= next(self.colors))


    def show_graphs(self):
        """Open a browser page with the required graph"""
        show(self.p)
        #a clear graph would otherwise interact with the show.
        time.sleep(0.5)

    def clear_graphs(self):
        """Clear all generated ghraphs"""
        self.p = figure(title="Distribution", x_axis_label="x", y_axis_label="y")
        self.colors = itertools.cycle(palette)



if __name__ == "__main__":
    p = probability()
    n = 10000000
    p.prepare_graph(p.gauss_random_variable, n, 0, 1)
    p.prepare_graph(p.normal_random_variable, n, 0, 1)
    p.show_graphs()
    p.clear_graphs()
    p.prepare_graph(p.normal_random_variable, n, 0, 1)
    p.show_graphs()
