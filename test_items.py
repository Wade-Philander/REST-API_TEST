from models.items import ItemModel 
from base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        item = ItemModel('test', 19,99)

        self.assertIsNone(ItemModel.find_by_name('test')),"Found an item with name {}, but expected not to".format(item.name))

        item.save_to_db()

        self.assertIsNone(ItemModel.find_by_name('test'))

        item.delete_from_db()

        self.assertIsNone(ItemModel.find_by_name('test'))

