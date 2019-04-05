#@Time    :2019/3/31 17:02
class Item:
    @property
    def id(self):
        return self["_id"]

    @id.setter
    def id(self, id_):
        if not isinstance(id_, str):
            raise ValueError('param must be type of str')
        self["_id"] = id_