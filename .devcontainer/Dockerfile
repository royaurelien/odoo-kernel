FROM odoo:17.0

USER root

RUN apt-get update && apt-get install -y --no-install-recommends git ssh

RUN python3 -m pip install \
    manifestoo \
    inotify \
    pre-commit \
    coverage \
    websocket-client \
    pytest-odoo \
    jupyter \
    git+https://github.com/royaurelien/odoo-cli.git@main

RUN mkdir /workspace
RUN chown odoo:odoo /workspace -R
RUN git config --global --add safe.directory /workspace

RUN mkdir -p /var/lib/odoo
RUN chown odoo:odoo /var/lib/odoo -R

USER odoo

