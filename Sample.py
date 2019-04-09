class Sample:
    def __init__(self, observation_list):
        self.observation_list = observation_list

        dimension = 0
        for observation in observation_list:
            dimension += len(observation)

        self.dimension = dimension

