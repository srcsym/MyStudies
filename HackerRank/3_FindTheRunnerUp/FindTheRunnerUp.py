n = int(input())
arr = map(int, input().split())

ParticipantsList = (list(arr))

k = max(ParticipantsList)

while max(ParticipantsList) == k:
    ParticipantsList.remove(max(ParticipantsList))

print(max(ParticipantsList))
