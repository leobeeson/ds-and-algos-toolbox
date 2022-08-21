# Towers of Hanoi: source -> https://www.youtube.com/watch?v=rf6uf3jNjbo&list=PLpXOY-RxVRTM_-Lvss2ezy1lVl6VUrzW2&index=2&ab_channel=Reducible
def print_move(from_: int, to_:int) -> None:
    print(f"{from_} -> {to_}")

def towers_of_hanoi(n: int, from_: int, to_:int) -> None:
    if n == 1:
        print_move(from_, to_)
    else:
        proxy_ = 6 - from_ - to_
        towers_of_hanoi(n - 1, from_, proxy_)
        print_move(from_, to_)
        towers_of_hanoi(n-1, proxy_, to_)


towers_of_hanoi(4, 1, 3)
