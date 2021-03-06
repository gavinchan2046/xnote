# -*- coding:utf-8 -*-
# @author xupingmao <578749341@qq.com>
# @since 2020/01/24 16:39:45
# @modified 2020/02/15 19:47:12

import sys
import time
import unittest
sys.path.insert(1, "lib")
sys.path.insert(1, "core")
import xauth

# cannot perform relative import
try:
    import test_base
except ImportError:
    from tests import test_base

BaseTestCase = test_base.BaseTestCase

app = test_base.init()

class TestXauth(BaseTestCase):

    def test_check_invalid_names(self):
        self.assertTrue(xauth.is_valid_username("t1234"))
        self.assertFalse(xauth.is_valid_username("public"))

    def test_add_user(self):
        xauth.add_user("u123456", "123456")
        users = xauth.refresh_users()
        self.assertEqual(2, len(users))

