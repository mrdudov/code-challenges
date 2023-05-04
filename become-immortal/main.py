from algorithm import elder_age


def main():
    assert elder_age(8,5,1,100) == 5
    assert elder_age(8,8,0,100007) == 224
    assert elder_age(25,31,0,100007) == 11925
    assert elder_age(5,45,3,1000007) == 4323
    assert elder_age(31,39,7,2345) == 1586
    assert elder_age(545,435,342,1000007) == 808451
    assert elder_age(28827050410, 35165045587, 7109602, 13719506) == 5456283

    elder_age()

if __name__ == "__main__":
    main()
