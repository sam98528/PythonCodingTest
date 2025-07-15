# PythonCodingTest

## Input 받기

- Single Input

```python
  a = input() # str
  b = int(input()) #int
```

- Multiple Input

```python
# multiple int split with whiteSpace
  a,b,c = map(int, input().split())
# multiple int split with comma (,)
a,b,c = map(int, input().split(,))
a,b = [(sys.stdin.readline()) for _ in range(2)]
```
