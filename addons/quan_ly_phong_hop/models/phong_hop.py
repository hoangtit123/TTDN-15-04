from odoo import models, fields, api


class PhongBan(models.Model):
    _name = 'phong_hop'
    _description = 'Bảng chứa thông tin phòng họp'

    ma_phong_hop = fields.Char("Mã phòng họp", required=True)
    ten_phong_hop = fields.Char("Tên phòng họp", required=True)

    dat_phong_hop_ids = fields.One2many('dat_phong_hop', 'phong_hop_id', string="Lịch đặt phòng")