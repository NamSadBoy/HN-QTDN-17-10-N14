from odoo import models, fields

class KieuKeHoach(models.Model):
    _name = 'cham_cong.kieu_ke_hoach'
    _description = 'Kiểu Kế Hoạch (Ca Làm Việc)'

    name = fields.Char(string='Tên ca (VD: Ca Sáng)', required=True)
    gio_vao = fields.Float(string='Giờ vào ca (VD: 8.0 = 8h00)', required=True)
    gio_ra = fields.Float(string='Giờ ra ca (VD: 17.5 = 17h30)', required=True)
    phut_cho_phep_muon = fields.Float(string='Số phút cho phép muộn', default=0)