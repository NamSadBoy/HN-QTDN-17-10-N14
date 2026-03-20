from odoo import models, fields

class ThuongPhat(models.Model):
    _name = 'tinh_luong.thuong_phat'
    _description = 'Quản lý Thưởng / Phạt thủ công'

    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    ngay_ghi_nhan = fields.Date(string='Ngày ghi nhận', required=True, default=fields.Date.context_today)
    loai = fields.Selection([
        ('thuong', 'Thưởng (+)'),
        ('phat', 'Phạt (-)')
    ], string='Loại', required=True, default='thuong')
    so_tien = fields.Float(string='Số tiền', required=True)
    ly_do = fields.Char(string='Lý do', required=True)