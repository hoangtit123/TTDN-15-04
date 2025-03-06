from odoo import models, fields, api


class DatPhongHop(models.Model):
    _name = 'dat_phong_hop'
    _description = ' Quản lý phòng họp '

    ma_dat_phong = fields.Char("Mã đặt phòng", required=True)
    ngay_dat_phong = fields.Date("Ngày đặt phòng")
    bat_dau = fields.Datetime("Thời gian bắt đầu")
    ket_thuc = fields.Datetime("Thời gian kết thúc")
    ten_cuoc_hop = fields.Char("Tên cuộc họp")

    phong_hop_id = fields.Many2one('phong_hop', string="Phòng họp", required=True)


    