# coding:utf-8
#@Time    :2019/4/6 14:42
class Production_steel(dict):
    @property
    def plan_uuid(self):
        return self["plan_uuid"]

    @plan_uuid.setter
    def id(self, plan_uuid):
        self["plan_uuid"] = plan_uuid

    @property
    def stell(self):
        return self["stell"]

    @stell.setter
    def id(self, stell):
        self["stell"] = stell

class PlanData(dict):
    @property
    def plan_uuid(self):
        return self["plan_uuid"]

    @plan_uuid.setter
    def id(self, plan_uuid):
        self["plan_uuid"] = plan_uuid

    @property
    def serial_number(self):
        return self["serial_number"]

    @serial_number.setter
    def id(self, serial_number):
        self["serial_number"] = serial_number

    @property
    def batch_number(self):
        return self["batch_number"]

    @batch_number.setter
    def id(self, batch_number):
        self["batch_number"] = batch_number

    @property
    def steel_grade(self):
        return self["steel_grade"]

    @steel_grade.setter
    def id(self, steel_grade):
        self["steel_grade"] = steel_grade

    @property
    def blocks_number(self):
        return self["blocks_number"]

    @blocks_number.setter
    def id(self, blocks_number):
        self["blocks_number"] = blocks_number

    @property
    def billet_thickness(self):
        return self["billet_thickness"]

    @billet_thickness.setter
    def id(self, billet_thickness):
        self["billet_thickness"] = billet_thickness

    @property
    def billet_width(self):
        return self["billet_width"]

    @billet_width.setter
    def id(self, billet_width):
        self["billet_width"] = billet_width

    @property
    def billet_length(self):
        return self["billet_length"]

    @billet_length.setter
    def id(self, billet_length):
        self["billet_length"] = billet_length

    @property
    def production_thickness(self):
        return self["production_thickness"]

    @production_thickness.setter
    def id(self, production_thickness):
        self["production_thickness"] = production_thickness

    @property
    def production_width(self):
        return self["production_width"]

    @production_width.setter
    def id(self, production_width):
        self["production_width"] = production_width

    @property
    def order(self):
        return self["order"]

    @order.setter
    def id(self, order):
        self["order"] = order

    @property
    def remarks(self):
        return self["remarks"]

    @remarks.setter
    def id(self, remarks):
        self["remarks"] = remarks

    @property
    def minute(self):
        return self["minute"]

    @minute.setter
    def id(self, minute):
        self["minute"] = minute

class Plan(dict):
    @property
    def plan_uuid(self):
        return self["plan_uuid"]

    @plan_uuid.setter
    def id(self, plan_uuid):
        self["plan_uuid"] = plan_uuid

    @property
    def plan_company(self):
        return self["plan_company"]

    @plan_company.setter
    def id(self, plan_company):
        self["plan_company"] = plan_company

    @property
    def plan_number(self):
        return self["plan_number"]

    @plan_number.setter
    def id(self, plan_number):
        self["plan_number"] = plan_number

    @property
    def plan_produceDate(self):
        return self["plan_produceDate"]

    @plan_produceDate.setter
    def id(self, plan_produceDate):
        self["plan_number"] = plan_produceDate