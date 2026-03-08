def birthdayCakeCandles(candles):
  tallest=max(candles)
  count=candles.count(tallest)
  print(count)

n = int(input())
candles = list(map(int, input().split()))
print(birthdayCakeCandles(candles))
