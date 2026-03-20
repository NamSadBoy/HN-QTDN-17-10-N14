{
    'name': 'Quản lý Văn bản',
    'version': '1.0',
    'category': 'Document Management',
    'summary': 'Quản lý hợp đồng, quyết định và hồ sơ đính kèm của nhân viên',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}