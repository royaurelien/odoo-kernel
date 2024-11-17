import odoo
from ipykernel.ipkernel import IPythonKernel


class OdooKernel(IPythonKernel):
    @property
    def banner(self):
        return (
            r"""Odoo %s
Available Odoo variables:
- odoo: Odoo Python module,
- env: Odoo Environment,
- self: administrator user,
- Pretty: a class to pretty print lists and dicts,
  e.g. Pretty(env['res.users'].search_read([], ['name', 'email', 'login']))

/!\ WARNING: USE env.cr.commit() TO APPLY YOUR CHANGES. UNCOMMITTED CHANGES IN AN OPEN SHELL CAN BLOCK YOUR DATABASE !!! /!\
"""
            % odoo.release.version
        )  # NOQA
