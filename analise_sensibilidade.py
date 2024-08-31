import matplotlib.pyplot as plt

class AlphaMethod:
    def __init__(self, well_start):
        self.well_start = well_start
        self.pull_test = []  
    
    def fill_specific_variables(self):
        pass  

class SensitivityAnalysis(AlphaMethod):
    def __init__(self, well_start, min_load, max_load, interval_load):
        super().__init__(well_start)
        self.min_load = min_load
        self.max_load = max_load
        self.interval_load = interval_load
        self.load_capacities = []
        self.fill_specific_variables()
        self.calculate_load_capacities()

    def fill_specific_variables(self):
        self.pull_test = self.well_start.pull_test

    def get_load_capacity_time(self):
        return [[0.0, self.pull_test]]

    def calculate_load_capacities(self):
        min_load = self.min_load
        load_intervals = [min_load]
        
        while load_intervals[-1] + self.interval_load <= self.max_load:
            load_intervals.append(load_intervals[-1] + self.interval_load)
        
        if load_intervals[-1] != self.max_load:
            load_intervals.append(self.max_load)
        self.load_capacities = []
        
        for load in load_intervals:
            capacities = [self.get_adjusted_capacity(load, pull_test_value[1]) for pull_test_value in self.pull_test]
            self.load_capacities.append([load, capacities])

    def get_adjusted_capacity(self, load, pull_test_value):
        return pull_test_value + (load - min_load)

# Lista pull_test da planilha
pull_test = [
    [1, 89312.16572],
    [2, 113262.9729],
    [3, 127273.2969],
    [4, 137213.78],
    [5, 144924.2178],
    [6, 151224.1041],
    [7, 156550.5821],
    [8, 161164.5872],
    [9, 165234.4282],
    [10, 168875.0249],
    [11, 172168.3453],
    [12, 175174.9113],
    [13, 177940.6838],
    [14, 180501.3893],
    [15, 182885.349],
    [16, 185115.3944],
    [17, 187210.2],
    [18, 189185.2353],
    [19, 191053.4584],
    [20, 192825.8321],
    [21, 194511.7133],
    [22, 196119.1525],
    [23, 197655.1258],
    [24, 199125.7184],
    [25, 200536.2698],
    [26, 201891.491],
    [27, 203195.5594],
    [28, 204452.1964],
    [29, 205664.7317],
    [30, 206836.1561],
    [31, 207969.1662],
    [32, 209066.2015],
    [33, 210129.4765],
    [34, 211161.0072],
    [35, 212162.6341],
    [36, 213136.0425],
    [37, 214082.7787],
    [38, 215004.2656],
    [39, 215901.815],
    [40, 216776.6393],
    [41, 217629.8607],
    [42, 218462.5205],
    [43, 219275.5865],
    [44, 220069.9596],
    [45, 220846.4802],
    [46, 221605.933],
    [47, 222349.0522],
    [48, 223076.5256],
    [49, 223788.9985],
    [50, 224487.077]
]

class TestSensitivityAnalysis(SensitivityAnalysis):
    def fill_specific_variables(self):
        self.pull_test = pull_test

# Exemplo que o usuário fornece os valores
min_load = 40000
max_load = 140000.0
interval_load = 10000.0
well_start = 0
# Criando a instância para o teste
analysis = TestSensitivityAnalysis(well_start, min_load, max_load, interval_load)

#print("Load Capacities:")
#for entry in analysis.load_capacities:
#    print(entry)

# Plotando os resultados
def plot_load_capacities(load_capacities):
    pull_test_times = [entry[0] for entry in pull_test]
    for idx, interval in enumerate(load_capacities):
        load_interval = interval[0]
        capacities = interval[1]
        plt.plot(pull_test_times, capacities, marker='o', label=f'Load Interval {load_interval}')

    plt.xlabel('Time')
    plt.ylabel('Capacity')
    plt.title('Sensitivyanalitic ')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_load_capacities(analysis.load_capacities)