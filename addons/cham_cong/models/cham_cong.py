from odoo import models, fields, api
from datetime import timedelta

class ChamCongChiTiet(models.Model):
    _name = 'cham_cong.chi_tiet'
    _description = 'Dữ liệu Chấm Công (Check-in/out)'

    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    ngay_cham_cong = fields.Date(string='Ngày', required=True, default=fields.Date.context_today)
    
    check_in = fields.Datetime(string='Giờ Check-in')
    check_out = fields.Datetime(string='Giờ Check-out')
    
    # Các trường tự động tính toán (Readonly)
    ke_hoach_id = fields.Many2one('cham_cong.ke_hoach', string='Ca áp dụng', compute='_compute_logic_cham_cong', store=True)
    di_muon = fields.Boolean(string='Đi muộn', compute='_compute_logic_cham_cong', store=True)
    ve_som = fields.Boolean(string='Về sớm', compute='_compute_logic_cham_cong', store=True)
    tien_phat = fields.Float(string='Tiền phạt', compute='_compute_logic_cham_cong', store=True)
    la_ngay_le = fields.Boolean(string='Là Ngày Lễ', compute='_compute_logic_cham_cong', store=True)

    @api.depends('employee_id', 'ngay_cham_cong', 'check_in', 'check_out')
    def _compute_logic_cham_cong(self):
        for record in self:
            # 1. Tự động kiểm tra xem ngày này có phải ngày lễ không
            ngay_le = self.env['cham_cong.ngay_le'].search([('ngay', '=', record.ngay_cham_cong)], limit=1)
            record.la_ngay_le = bool(ngay_le)

            # 2. Tìm xem hôm nay nhân viên này đăng ký ca nào
            ke_hoach = self.env['cham_cong.ke_hoach'].search([
                ('employee_id', '=', record.employee_id.id),
                ('ngay_lam_viec', '=', record.ngay_cham_cong)
            ], limit=1)
            record.ke_hoach_id = ke_hoach.id if ke_hoach else False

            # 3. Tính toán đi muộn / về sớm / Phạt tiền
            muon = False
            som = False
            phat = 0.0

            if ke_hoach and ke_hoach.ca_lam_id:
                ca = ke_hoach.ca_lam_id
                
                # Odoo lưu giờ chuẩn UTC, ta cộng thêm 7 tiếng (Múi giờ VN) để so sánh cho đúng
                if record.check_in:
                    in_time = record.check_in + timedelta(hours=7)
                    float_in = in_time.hour + (in_time.minute / 60.0)
                    if float_in > (ca.gio_vao + ca.phut_cho_phep_muon / 60.0):
                        muon = True
                        phat += 100000  # Phạt 100k
                
                if record.check_out:
                    out_time = record.check_out + timedelta(hours=7)
                    float_out = out_time.hour + (out_time.minute / 60.0)
                    if float_out < ca.gio_ra:
                        som = True
                        phat += 100000  # Phạt 100k

            record.di_muon = muon
            record.ve_som = som
            record.tien_phat = phat