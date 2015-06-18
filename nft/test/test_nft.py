# -*- coding: utf-8 -*-

import unittest
import nft


class TestTable(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_table(self):
        pass


class TestChain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_chain(self):
        pass


class TestRule(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rule(self):
        pass


def suite():
    suite_table = unittest.TestLoader().loadTestsFromTestCase(TestTable)
    suite_chain = unittest.TestLoader().loadTestsFromTestCase(TestChain)
    suite_rule = unittest.TestLoader().loadTestsFromTestCase(TestRule)
    return unittest.TestSuite([suite_table, suite_chain, suite_rule])


def run_tests():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    if result.errors or result.failures:
        return 1
    return 0

if __name__ == "__main__":
    unittest.main()