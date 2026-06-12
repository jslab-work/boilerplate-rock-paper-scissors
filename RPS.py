# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    counters = {"R": "P", "P": "S", "S": "R"}

    if len(opponent_history) < 4:
        return "S"

    def predict(n):
        if len(opponent_history) < n + 1:
            return None

        patterns = {}
        recent = opponent_history[-100:]

        for i in range(len(recent) - n):
            key = tuple(recent[i:i+n])
            nxt = recent[i+n]
            if key not in patterns:
                patterns[key] = {"R": 0, "P": 0, "S": 0}
            patterns[key][nxt] += 1

        key = tuple(opponent_history[-n:])
        if key in patterns:
            return max(patterns[key], key=patterns[key].get)
        return None

    prediction = predict(3) or predict(2) or opponent_history[-1]
    return counters[prediction]
