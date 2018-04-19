# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase



class RandomTestCase(TestCase):
	
	def test_one_plus_one1(self):
		self.assertEqual(1+1, 2)

