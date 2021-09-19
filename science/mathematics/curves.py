def mapExtremes(data, percentage=0.03):
    """
        will map the data from the datastream into extremes.
        extremes with values within the given percentage will be added

        :arg data: datastream to map
        :type data: list
        :arg percentage: percentage values have to be within each other to be considered the same value
        :type percentage: float

        :return:
                {
                    1456.03: 3,
                    1569.98: 5,
                },

                {
                    45.98: 15,
                    156.54: 3,
                }
    """
    peaks = {}
    valleys = {}


    simular_max = inf
    simular_min = inf
    for _ in range(len(data)):
        if len(data) == 0: break
        max_ = max(data)
        min_ = min(data)

        for key in peaks:
            if abs(key-max_) < simular_max:
                simular_max = key
        if simular_max < max_ * (1+percentage) and simular_max > max_ * (1-percentage):
            if simular_max in peaks:
                peaks[simular_max] += 1
            else: peaks[max_] = 1
            data.remove(max_)
        else:
            peaks[max_] = 1
            data.remove(max_)

        if min_ == max_: continue

        for key in valleys:
            if abs(key-min_) < simular_min:
                simular_min = key
        if simular_min < min_ * (1+percentage) and simular_min > min_ * (1-percentage):
            if simular_min in valleys:
                valleys[simular_min] += 1
            else: valleys[simular_min] = 1
            data.remove(min_)
        else:
            valleys[min_] = 1
            data.remove(min_)
