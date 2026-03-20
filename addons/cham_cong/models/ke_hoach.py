from odoo import models, fields

class KeHoach(models.Model):
    _name = 'cham_cong.ke_hoach'
    _description = 'Lịch Đăng Ký Ca Làm'

    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    ngay_lam_viec = fields.Date(string='Ngày làm', required=True)
    ca_lam_id = fields.Many2one('cham_cong.kieu_ke_hoach', string='Ca làm việc', required=True)