from odoo import models, fields, api


class ChucVu(models.Model):
    _name = 'thiet_bi'
    _description = 'Bảng chứa thông tin thiết bị'

    ma_thiet_bi = fields.Char("Mã thiết bị", required=True)
    ten_thiet_bi = fields.Char("Tên thiết bị", required=True)
    