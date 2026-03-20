from odoo import models, fields

class ChungChiBangCap(models.Model):
    _name = 'nhan_su.nhan_vien.bang_cap'
    _description = 'Bằng cấp của Nhân viên'

    employee_id = fields.Many2one('hr.employee', string='Nhân viên', ondelete='cascade')
    bang_cap_id = fields.Many2one('nhan_su.bang_cap', string='Loại Bằng cấp', required=True)
    ngay_cap = fields.Date(string='Ngày cấp')
    noi_cap = fields.Char(string='Nơi cấp')