import bank


class TestBank:
    
    def test_bank_0_10_10(self):
        assert bank.bank_cost(0, 10, 10) == 0
    
    def test_bank_100_10_0(self):
        assert bank.bank_cost(100, 10, 0) == 100

    def test_bank_100_0_10(self):
        assert bank.bank_cost(100, 0, 10) == 1000

    def test_bank_100_10_3(self):
        assert bank.bank_cost(100, 10, 3) == 364.1


class TestYourCash:

    def test_your_cash_100_0(self):
        assert bank.your_cash(100, 0) == 100

    def test_your_cash_0_10(self):
        assert bank.your_cash(0, 10) == 0

    def test_your_cash_250_3(self):
        assert bank.your_cash(250, 5) == 1250


class TestBankCash:

    def test_bank_cash_100_10_0(self):
        assert bank.bank_cash(100, 10, 0) == 0

    def test_bank_cash_0_10_10(self):
        assert bank.bank_cash(0, 10, 10) == 0

    def test_bank_cash_100_0_10(self):
        assert bank.bank_cash(100, 0, 10) == 0

    def test_bank_cash_100_10_1(self):
        assert bank.bank_cash(100, 10, 1) == 10

    def test_bank_cash_300_10_2(self):
        assert bank.bank_cash(300, 10, 2) == 93
