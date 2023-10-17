

import shutil
import os

source_folder = 'C:/Users/Quinn/Desktop/py/New_files/path/to/module/folder'
destination_folder = 'C:/Users/Quinn/Desktop/py/New_files/path/to/test/folder'

file_to_copy = 'order.py'
source_file_path = os.path.join(source_folder, file_to_copy)
destination_file_path = os.path.join(destination_folder, file_to_copy)
shutil.copy(source_file_path, destination_file_path)

class OrderTestCase(TestCase):
    def test_order_id_is_increment(self):
        initial_counter = Order.counter
        order_1 = Order([])
        self.assertEqual(order_1.order_id, f"order-{initial_counter}")
        order_2 = Order([])
        self.assertEqual(order_2.order_id, f"order-{initial_counter}")