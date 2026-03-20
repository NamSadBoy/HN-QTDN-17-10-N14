from odoo import models, fields

class LichSuCongTac(models.Model):
    _name = 'nhan_su.lich_su_cong_tac'
    _description = 'Lịch sử công tác'

    employee_id = fields.Many2one('hr.employee', string='Nhân viên', ondelete='cascade')
    tu_ngay = fields.Date(string='Từ ngày', required=True)
    den_ngay = fields.Date(string='Đến ngày')
    phong_ban_id = fields.Many2one('hr.department', string='Phòng ban')
    chuc_vu_id = fields.Many2one('hr.job', string='Chức vụ')
    ghi_chu = fields.Text(string='Ghi chú')