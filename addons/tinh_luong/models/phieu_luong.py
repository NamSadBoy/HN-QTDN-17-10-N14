from odoo import models, fields, api

class PhieuLuong(models.Model):
    _name = 'tinh_luong.phieu_luong'
    _description = 'Phiếu Lương Nhân Viên'

    name = fields.Char(string='Mã phiếu lương', compute='_compute_name', store=True)
    employee_id = fields.Many2one('hr.employee', string='Nhân viên', required=True)
    
    # Kỳ tính lương
    tu_ngay = fields.Date(string='Từ ngày', required=True)
    den_ngay = fields.Date(string='Đến ngày', required=True)

    # 1. Dữ liệu từ Nhân sự
    luong_co_ban = fields.Float(string='Lương cơ bản', related='employee_id.luong_co_ban', store=True)
    
    # 2. Dữ liệu từ Chấm công (Tự động tính)
    so_ngay_cong_thuong = fields.Float(string='Ngày công thường', compute='_compute_luong', store=True)
    so_ngay_cong_le = fields.Float(string='Ngày công Lễ (x2)', compute='_compute_luong', store=True)
    tien_phat_di_muon = fields.Float(string='Phạt đi muộn/về sớm', compute='_compute_luong', store=True)
    
    # 3. Dữ liệu từ Thưởng/Phạt thủ công
    tien_thuong_khac = fields.Float(string='Thưởng khác (+)', compute='_compute_luong', store=True)
    tien_phat_khac = fields.Float(string='Phạt khác (-)', compute='_compute_luong', store=True)

    # 4. Bảo hiểm
    tien_tru_bhxh = fields.Float(string='Trừ BHXH (8%)', compute='_compute_luong', store=True)
    tien_tru_bhyt = fields.Float(string='Trừ BHYT (1.5%)', compute='_compute_luong', store=True)
    tien_tru_bhtn = fields.Float(string='Trừ BHTN (1%)', compute='_compute_luong', store=True)

    # 5. TỔNG KẾT
    tong_thu_nhap = fields.Float(string='Tổng thu nhập', compute='_compute_luong', store=True)
    thuc_lanh = fields.Float(string='Thực lãnh (Net)', compute='_compute_luong', store=True)
    
    trang_thai = fields.Selection([
        ('nhap', 'Bản nháp'),
        ('da_duyet', 'Đã chốt lương')
    ], string='Trạng thái', default='nhap', tracking=True)

    @api.depends('employee_id', 'tu_ngay', 'den_ngay')
    def _compute_name(self):
        for rec in self:
            if rec.employee_id and rec.tu_ngay:
                rec.name = f"Lương {rec.employee_id.name} - Tháng {rec.tu_ngay.month}/{rec.tu_ngay.year}"

    @api.depends('employee_id', 'tu_ngay', 'den_ngay', 'luong_co_ban')
    def _compute_luong(self):
        for rec in self:
            if not (rec.employee_id and rec.tu_ngay and rec.den_ngay):
                rec.so_ngay_cong_thuong = rec.so_ngay_cong_le = rec.tien_phat_di_muon = 0
                rec.tien_thuong_khac = rec.tien_phat_khac = 0
                rec.tien_tru_bhxh = rec.tien_tru_bhyt = rec.tien_tru_bhtn = 0
                rec.tong_thu_nhap = rec.thuc_lanh = 0
                continue

            # 1. Lấy dữ liệu Chấm công
            cham_cong_ids = self.env['cham_cong.chi_tiet'].search([
                ('employee_id', '=', rec.employee_id.id),
                ('ngay_cham_cong', '>=', rec.tu_ngay),
                ('ngay_cham_cong', '<=', rec.den_ngay)
            ])
            
            cong_thuong = 0.0
            cong_le = 0.0
            phat_muon = 0.0
            
            for cc in cham_cong_ids:
                phat_muon += cc.tien_phat
                if cc.la_ngay_le:
                    cong_le += 1.0
                else:
                    cong_thuong += 1.0
                    
            rec.so_ngay_cong_thuong = cong_thuong
            rec.so_ngay_cong_le = cong_le
            rec.tien_phat_di_muon = phat_muon

            # 2. Lấy dữ liệu Thưởng / Phạt thủ công
            thuong_phat_ids = self.env['tinh_luong.thuong_phat'].search([
                ('employee_id', '=', rec.employee_id.id),
                ('ngay_ghi_nhan', '>=', rec.tu_ngay),
                ('ngay_ghi_nhan', '<=', rec.den_ngay)
            ])
            
            thuong = sum(tp.so_tien for tp in thuong_phat_ids if tp.loai == 'thuong')
            phat = sum(tp.so_tien for tp in thuong_phat_ids if tp.loai == 'phat')
            
            rec.tien_thuong_khac = thuong
            rec.tien_phat_khac = phat

            # 3. Tính tiền bảo hiểm (Nếu có tham gia)
            luong_bh = rec.employee_id.muc_luong_dong_bao_hiem if rec.employee_id.tham_gia_bao_hiem else 0.0
            rec.tien_tru_bhxh = luong_bh * 0.08
            rec.tien_tru_bhyt = luong_bh * 0.015
            rec.tien_tru_bhtn = luong_bh * 0.01
            tong_tru_bh = rec.tien_tru_bhxh + rec.tien_tru_bhyt + rec.tien_tru_bhtn

            # 4. Tính toán số tiền cuối cùng (Giả định 1 tháng có 26 ngày công chuẩn)
            luong_1_ngay = rec.luong_co_ban / 26.0
            
            tong_thu_nhap = (luong_1_ngay * cong_thuong) + (luong_1_ngay * cong_le * 2) + thuong
            thuc_lanh = tong_thu_nhap - phat_muon - phat - tong_tru_bh

            rec.tong_thu_nhap = tong_thu_nhap
            rec.thuc_lanh = thuc_lanh

    def action_chot_luong(self):
        self.trang_thai = 'da_duyet'