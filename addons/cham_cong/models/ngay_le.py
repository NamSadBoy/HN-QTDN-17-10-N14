from odoo import models, fields

class NgayLe(models.Model):
    _name = 'cham_cong.ngay_le'
    _description = 'Danh mục Ngày Lễ'

    name = fields.Char(string='Tên ngày lễ', required=True)
    ngay = fields.Date(string='Ngày', required=True)
    he_so_luong = fields.Float(string='Hệ số lương (Mặc định x2)', default=2.0)