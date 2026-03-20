from odoo import models, fields

class NhanVien(models.Model):
    _inherit = 'hr.employee'

    he_so_luong = fields.Float(string='Hệ số lương', related='job_id.he_so_luong', store=True, readonly=False, tracking=True)
    luong_co_ban = fields.Float(string='Lương cơ bản', related='job_id.luong_co_ban_mac_dinh', store=True, readonly=False, tracking=True)
    
    tham_gia_bao_hiem = fields.Boolean(string='Tham gia BHXH', default=False, tracking=True)
    so_so_bhxh = fields.Char(string='Số sổ BHXH')
    muc_luong_dong_bao_hiem = fields.Float(string='Mức lương đóng BHXH')

    bang_cap_ids = fields.One2many('nhan_su.nhan_vien.bang_cap', 'employee_id', string='Danh sách Bằng cấp')
    lich_su_cong_tac_ids = fields.One2many('nhan_su.lich_su_cong_tac', 'employee_id', string='Lịch sử công tác')