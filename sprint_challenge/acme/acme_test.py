#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_values(self):
        """Test default values being set and types"""
        prod = Product('Test Product')
        self.assertTrue(isinstance(prod.name,str))
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)
        self.assertTrue(isinstance(prod.identifier,int))

    def test_stealability_and_explode(self):
        """Tests stealability and explode function properly"""
        prod = Product(name='Test Product',
                       price=15,
                       weight=18,
                       flammability=70)
        self.assertTrue(prod.stealability() == "Kind stealable...")
        self.assertTrue(prod.explode() == "...BABOOM!!")

class AcmeReportTests(unittest.TestCase):
    """Making sure Acme Inventory Reports run well!"""

    def test_default_num_products(self):
        """Tests default number of products that are generated"""
        self.assertTrue(len(generate_products()) == 30)

    def test_legal_names(self):
        """Tests that generated names for a default batch of products are all valid possible names"""
        prods = generate_products()
        for _ in prods:
            self.assertIn(_.name[0], ADJECTIVES)
            self.assertIn(_.name[1], NOUNS)

if __name__ == '__main__':
    unittest.main()