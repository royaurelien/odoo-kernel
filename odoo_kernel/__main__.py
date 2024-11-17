import odoo
from ipykernel.kernelapp import IPKernelApp
from odoo_cli.common import Environment

from odoo_kernel.kernel import OdooKernel
from odoo_kernel.utils import Pretty

with Environment() as env:
    local_vars = {
        "openerp": odoo,
        "odoo": odoo,
        "env": env,
        "self": env.user,
        "Pretty": Pretty,
    }
    IPKernelApp.launch_instance(
        kernel_class=OdooKernel,
        user_ns=local_vars,
    )
