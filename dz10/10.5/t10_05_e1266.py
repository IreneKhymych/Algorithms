import sys

def max_length(n, tracks, index=0, current_sum=0):
    if current_sum > n:
        return 0
    if index == len(tracks):
        return current_sum
    take = max_length(n, tracks, index + 1, current_sum + tracks[index])
    skip = max_length(n, tracks, index + 1, current_sum)
    return max(take, skip)

def process_input():
    input_lines = sys.stdin.read().strip().split("\n")
    for line in input_lines:
        data = list(map(int, line.split()))
        n = data[0]
        tracks = data[2:]
        result = max_length(n, tracks)
        print("sum:", result)

if __name__ == "__main__":
    process_input()
