from odoo import models, fields

class DanhMucBangCap(models.Model):
    _name = 'nhan_su.bang_cap'
    _description = 'Danh mục Bằng cấp / Chứng chỉ'

    name = fields.Char(string='Tên Bằng cấp', required=True)
    code = fields.Char(string='Mã định danh')