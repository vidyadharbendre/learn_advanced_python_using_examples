# simpleinterest/test_simpleinterest.py
from simpleinterest import SimpleInterest

def test_simpleinterest():
    simint = SimpleInterest(1000, 2, 4)

    # Test the initial principle
    assert simint.get_principle() == 1000, "Initial principle should be 100"

    # Test the initial time
    assert simint.get_time() == 2, "Initial time should be 2"

    # Test the initial rate
    assert simint.get_rate() == 4, "Initial rate should be 4"

    # Test the initial simpleinterest
    assert simint.calculate_simple_interest() == 80.0, "Initial simple interest should be 12"

    simint.display_simple_interest()

    simint.set_principle(10000)
    # Test the initial principle
    assert simint.get_principle() == 10000, "Initial principle should be 1000"

    # Test the initial simpleinterest
    assert simint.calculate_simple_interest() == 800.0, "Initial simple interest should be 12"

    simint.display_simple_interest()
    


if __name__ == "__main__":
    test_simpleinterest()
    print("All tests passed.")
