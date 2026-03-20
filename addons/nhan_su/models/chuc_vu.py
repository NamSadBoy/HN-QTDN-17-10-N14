from odoo import models, fields

class ChucVu(models.Model):
    _inherit = 'hr.job'

    he_so_luong = fields.Float(string='Hệ số lương', default=1.0, tracking=True)
    luong_co_ban_mac_dinh = fields.Float(string='Lương cơ bản (Mặc định)', tracking=True)