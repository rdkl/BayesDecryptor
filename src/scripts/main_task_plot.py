import collections
from itertools import izip

import matplotlib.pyplot as plt
import numpy as np


##############################################################################
class DataLoader(object):
    # Line format: ["number of iterations" "parameter" "values_list"] 
    def __init__(self, path_to_file="../../data/main_task_5_2.txt"):
        self.__data = collections.Counter()
        
        with open(path_to_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split()
                
                if len(line) < 2:
                    continue
                
                try:
                    number_of_iterations = int(line[1])
                    parameter = int(line[0])
                    values_list = [float(item) for item in line[2:]]
                
                except:
                    raise TypeError("Unknown data format in %s" \
                                    % (" ".join(line)))
                
                if not parameter in self.__data:     
                    self.__data[parameter] = \
                        collections.Counter()
                        
                self.__data[parameter][number_of_iterations] = values_list
                    
    #-------------------------------------------------------------------------
    def plot_by_parameter(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        for parameter in self.__data:
            mean, std = self.extract_data_by_parameter(parameter)
            ax.annotate("%.2f" % std, xy = (parameter + 10, mean))
            plt.plot(parameter, mean, marker="o")
            print mean
        
        plt.ylim([0, 1])
        plt.xlabel("parameter")
        plt.ylabel("Error ratio")
        plt.grid(True)
        plt.show(True)
    
    #-------------------------------------------------------------------------
    def plot_by_parameter_and_iterations(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        
        iteration_number_keys = set({})
        for parameter in self.__data:
            for item in self.__data[parameter].keys():
                iteration_number_keys.add(item)
        
        plot_data = {item : [[], [], []] for item in iteration_number_keys}
        
        for parameter in self.__data:
            for it in self.__data[parameter].keys():
                mean, std = \
                    self.extract_data_by_parameter_and_iteration_number(
                                                                parameter,
                                                                it)
                ax.annotate("%.2f" % std, xy = (parameter + 10, mean))
                plot_data[it][0] += [parameter]
                plot_data[it][1] += [mean]
                plot_data[it][2] += [std]                        
        
        for item in plot_data:
            sorted_lists = sorted(izip(plot_data[item][0], 
                                       plot_data[item][1],
                                       plot_data[item][2]), 
                                  reverse=True, 
                                  key=lambda x: x[0])
            plot_data[item][0], plot_data[item][1], plot_data[item][2] = \
                [[x[i] for x in sorted_lists] for i in range(3)]
            
            self.errorfill(plot_data[item][0], plot_data[item][1],
                      plot_data[item][2], label=item) 
                      # marker="o",  )
            
        ax.legend()
        plt.ylim([0, 1])
        plt.xlabel("parameter")
        plt.ylabel("Error ratio")
        plt.grid(True)
        plt.show(True)
    
    #-------------------------------------------------------------------------
    def extract_data_by_parameter(self, parameter):
        
        values_list = []
        
        for item in self.__data[parameter]:
            values_list += self.__data[parameter][item]
        
        return np.mean(values_list), np.std(values_list)
    
    #-------------------------------------------------------------------------
    def extract_data_by_parameter_and_iteration_number(self, parameter,
                                                       it):
        values_list = self.__data[parameter][it]
        return np.mean(values_list), np.std(values_list)
    
    #-------------------------------------------------------------------------
    def errorfill(self, x, y, yerr, label="", color=None, alpha_fill=0.1, 
                  ax = None):
        x = np.array(x)
        y = np.array(y)
        yerr = np.array(yerr)
        ax = ax if ax is not None else plt.gca()
        if color is None:
            color = ax._get_lines.color_cycle.next()
        if np.isscalar(yerr) or len(yerr) == len(y):
            ymin = y - yerr
            ymax = y + yerr
        elif len(yerr) == 2:
            ymin, ymax = yerr
        ax.plot(x, y, color=color, label=label)
        ax.fill_between(x, ymax, ymin, color=color, alpha=alpha_fill)
        
    #-------------------------------------------------------------------------
##############################################################################

if __name__ == "__main__":
    dl = DataLoader()
    dl.plot_by_parameter_and_iterations()