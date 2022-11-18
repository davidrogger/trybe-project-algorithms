def study_schedule(permanence_period, target_time):
    counter = 0
    try:
        for period in permanence_period:
            start, end = period
            if start <= target_time <= end:
                counter += 1
    except TypeError:
        return None
    else:
        return counter
